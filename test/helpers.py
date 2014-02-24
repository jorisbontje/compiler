import ast
import itertools
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def load_cll(cll_file):
    with open(os.path.join(DATA_DIR, cll_file + ".cll"), 'r') as f:
        return f.readlines()

def load_ast(ast_file):
    try:
        with open(os.path.join(DATA_DIR, ast_file + ".ast"), 'r') as f:
            return ast.literal_eval("".join(f.readlines()))
    except SyntaxError as e:
        raise RuntimeError("Error parsing \"%s\": %s" % (ast_file, e))

def load_asm(asm_file):
    with open(os.path.join(DATA_DIR, asm_file + ".asm"), 'r') as f:
        lines = [line.strip().split(" ") for line in f.readlines()]
    codes = list(itertools.chain.from_iterable(lines))
    result = []
    for code in codes:
        if code.isdigit():
            result.append(long(code))
        else:
            result.append(code)
    return result
