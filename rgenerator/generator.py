import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


@dataclass
class Argument:
    name: str
    description: str

    def to_mk(self):
        return f"- `{self.name}`:  {self.description}\n"


@dataclass
class Method:
    name: str
    title: str
    description: str
    details: str
    examples: str
    value: str
    usage: str
    arguments: List[Argument]

    def to_mk(self):
        details = "*Details:*" + self.details if self.details else ""
        description = self.description if self.description != self.title else ""
        args = "\n".join([a.to_mk() for a in self.arguments])
        return f"""
### `{self.name}`
**{self.title}**\n
{description}\n
{details}
 **Usage:**
```
{self.usage}
```
**Arguments**\n
{args}

**Value**\n
{self.value}

**Examples**
```
{self.examples}
```
"""


@dataclass
class References:
    name: str
    title: str
    version: str
    description: str
    license: str
    imports: List[str]
    api: List[Method]

    def to_mk(self):
        imports = ', '.join([f"`{i}`" for i in self.imports])
        api = '\n'.join([i.to_mk() for i in self.api])
        return f"""
# {self.name}
## References
**Title:** {self.title}\n
**Description:** {self.description}\n
**Version:** {self.version}\n
**License:** {self.license}\n
**Imports:** {imports}\n
{api}
"""


class Parser:
    def parse(self, path_r: Path) -> References:
        ref = self._parse_head(path_r / "DESCRIPTION")
        ref.api = [self._parse_method(p) for p in (path_r / "man").iterdir()]
        return ref

    def _parse_head(self, path_head: Path) -> References:
        content = path_head.read_text()
        content = re.sub(r"\n\s+", " ", content)

        data = dict()
        for line in content.split("\n"):
            r = re.search(r"^(\w*):\s(.*)$", line)
            if r:
                data[r.group(1)] = r.group(2)

        return References(
            name=data["Package"],
            title=data["Title"],
            version=data["Version"],
            description=data["Description"],
            license=data["License"],
            imports=data["Imports"].split(', '),
            api=[]
        )

    def _parse_method(self, path_method: Path) -> Method:
        def find(token: str, data: str) -> str:
            res = re.findall(r"\\" + re.escape(token) + r"{([^}]*)}", data)
            return res[0].strip() if len(res) else ""

        def args(data: str) -> List[Argument]:
            items = [item.replace('\n', ' ').split('}{') for item in re.findall(r"\\item{(.+\}\{[^}]+)}", data)]
            return [Argument(name=n, description=d) for n, d in items]

        def examples(data: str) -> str:
            return find("examples", data).replace("\\dontrun{\n", "")

        content = path_method.read_text()
        return Method(name=find("name", content),
                      title=find("title", content),
                      description=find("description", content),
                      details=find("details", content),
                      examples=examples(content),
                      value=find("value", content),
                      usage=find("usage", content),
                      arguments=args(content))


class Generator:
    def __init__(self, parser: Parser):
        self.parser = parser

    def _get_vignette(self, path: Path) -> str:
        content = path.read_text()
        # Get vignette name
        name = re.search(r"^\s*---\s+title: \"(.+)\"", content).group(1)

        # Replace header
        content = re.sub(r"^---[\w\W\n]*---\s*", f"## {name}\n", content)

        # Remove include and setup code block
        content = re.sub(r"```{r, include = FALSE}[^`]*```\s*", "", content)
        content = re.sub(r"```{r setup}[^`]*```\s*", "", content)

        # Replace code bloc
        content = re.sub(r"```{r.*}", "```r", content)

        # downgrade all chapter level
        content = content.replace("\n#", "\n##")

        return content

    def generate(self, path_r: Path) -> str:
        content = self.parser.parse(path_r).to_mk()
        for vi in (path_r / "vignettes").iterdir():
            if vi.suffix == '.Rmd':
                content += self._get_vignette(vi) + "\n"
        return content


def main(path_r: Path, out: Path):
    content = Generator(parser=Parser()).generate(path_r)

    (out / f"{path_r.name}.md").write_text(content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--package", dest="path_r", help="Path to R package")
    parser.add_argument("-o", "--output", dest="out", help="Path to the output directory")

    args = parser.parse_args()
    main(Path(args.path_r), Path(args.out))
