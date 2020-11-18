import os
import unittest
from pathlib import Path

from rgenerator.generator import Parser, Method, Argument


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(os.path.dirname(__file__))

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
