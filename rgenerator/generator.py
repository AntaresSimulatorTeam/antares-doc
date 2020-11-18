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
    example: str
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