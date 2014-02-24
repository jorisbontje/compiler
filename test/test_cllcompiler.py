import ast
import glob
import os
import unittest

from helpers import load_ast, load_asm
import cllcompiler

class TestCompiler(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def check_compile_ast_returns_asm(self, name):
        ast = load_ast(name)
        asm_should = load_asm(name)
        stmts = cllcompiler.compile_stmt(ast)
        asm_is = cllcompiler.assemble(stmts)
        self.assertEqual(asm_is, asm_should)

    def test_01_expression(self):
        self.check_compile_ast_returns_asm("expr")

    def test_02_array(self):
        self.check_compile_ast_returns_asm("array")

    def test_03_mktx(self):
        self.check_compile_ast_returns_asm("mktx")

    def test_04_namecoin(self):
        self.check_compile_ast_returns_asm("namecoin")

    def test_05_while(self):
        self.check_compile_ast_returns_asm("while")

    def test_06_contract_storage(self):
        self.check_compile_ast_returns_asm("contract_storage")

if __name__ == '__main__':
    unittest.main()
