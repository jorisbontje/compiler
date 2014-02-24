import ast
import glob
import os
import unittest

from helpers import load_cll, load_ast
import cllparser

class TestParser(unittest.TestCase):

    def check_parse_cll_returns_ast(self, name):
        cll_lines = load_cll(name)
        ast_should = load_ast(name)
        ast_is = cllparser.parse_lines(cll_lines)
        self.assertEqual(ast_is, ast_should)

    def test_empty(self):
        self.check_parse_cll_returns_ast("empty")

    def test_expression(self):
        self.check_parse_cll_returns_ast("expr")

    def test_array(self):
        self.check_parse_cll_returns_ast("array")

    def test_mktx(self):
        self.check_parse_cll_returns_ast("mktx")

    def test_namecoin(self):
        self.check_parse_cll_returns_ast("namecoin")

    def test_while(self):
        self.check_parse_cll_returns_ast("while")

    def test_contract_storage(self):
        self.check_parse_cll_returns_ast("contract_storage")

if __name__ == '__main__':
    unittest.main()
