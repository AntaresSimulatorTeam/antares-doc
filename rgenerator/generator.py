import re
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Argument:
    name: str
    description: str


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


@dataclass
class References:
    name: str
    title: str
    version: str
    description: str
    license: str
    imports: List[str]
    api: List[Method]


class Parser:
    def parse(self, path_r: Path) -> References:
        pass

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

        content = path_method.read_text()

        attributes = {att: find(att, content)
                      for att in ["name", "title", "description", "details",
                                  "examples", "value", "usage"]}
        method = Method(**attributes, arguments=args(content))

        return method