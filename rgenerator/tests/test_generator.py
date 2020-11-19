import hashlib
import os
import unittest
from pathlib import Path

from rgenerator.generator import Parser, Method, Argument, References, Generator


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(os.path.dirname(__file__))

    def test_parse(self):
        path = self.root / "../../documents/adq-master"

        parser = Parser()
        ref = parser.parse(path)
        print(ref)

    def test_parse_head(self):
        path = self.root / "DESCRIPTION"

        parser = Parser()
        ref = parser._parse_head(path)

        self.assertEqual(ref.version, "0.0.0.9000")
        self.assertEqual(ref.name, "AdequacyPatch")
        self.assertEqual(len(ref.description), 798)

    def test_methods_dot_pos(self):
        path = self.root / "dot-pos.Rd"

        expected = Method(
            name='.pos',
            title="Computes the positive part of a numeric.",
            description="The positive part is defined as follows:\n.pos(x) = x if x >= 0\n.pos(x) = 0 otherwise",
            details="",
            examples=".pos(3)  # 3\n.pos(-5)  # 5",
            value="(numeric) the positive part of x",
            usage=".pos(x)",
            arguments=[Argument(name="x", description="(numeric)")]
        )

        parser = Parser()
        method = parser._parse_method(path)

        self.assertEqual(expected, method)

    def test_methods_adq_patch(self):
        path = self.root / "adq_patch.Rd"

        parser = Parser()
        method = parser._parse_method(path)

        self.assertEqual(method.name, "adq_patch")
        self.assertEqual(method.examples, "sim_opts = antaresRead")
        self.assertEqual(len(method.arguments), 6)
        self.assertEqual(method.details, "This function does not solve anything itself")


class TestTemplate(unittest.TestCase):
    def test_generate(self):
        ref = References(
            name="A",
            title="B",
            version="C",
            description="D",
            license="E",
            imports=["F, G"],
            api=[
                Method(
                    name="H",
                    title="I",
                    description="J",
                    details="L",
                    examples="M",
                    value="N",
                    usage="O",
                    arguments=[
                        Argument(name="P", description="Q"),
                        Argument(name="PP", description="QQ")
                    ]
                ),
                Method(
                    name="HH",
                    title="II",
                    description="JJ",
                    details="LL",
                    examples="MM",
                    value="NN",
                    usage="OO",
                    arguments=[
                        Argument(name="PPP", description="QQQ"),
                        Argument(name="PPPP", description="QQQQ")
                    ]
                )
            ]
        )

        content = Generator().generate(ref)
        self.assertEqual("a66e279337a7b12ccdbba2521cedfab95029e6d2f886ccc49911fe9103589bba", hashlib.sha256(content.encode()).hexdigest())