import os
import unittest
from pathlib import Path

from rgenerator.generator import Parser


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