
import sys
from antlr4 import *
from build.yaplLexer import yaplLexer
from build.yaplParser import yaplParser
from yaplWalker import yaplWalker
from yaplErrorListener import yaplErrorListener


def process_yapl_file(file_path):
    input_stream = FileStream(file_path)

    lexer = yaplLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(yaplErrorListener())

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("Tokens:")
    for token in token_stream.tokens:
        print(token)

    parser = yaplParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(yaplErrorListener())

    parse_tree = parser.prog()
    print("\nParse Tree:")
    # print(parse_tree.toStringTree(parser.ruleNames))

    symbol_walker = yaplWalker()
    symbol_walker.initSymbolTable()
    symbol_walker.visit(parse_tree)

    print("\nSymbol Table:")
    for record in symbol_walker.symbolTable.records:
        print("Symbol", record.toString())
        # print(record.id)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python your_script_name.py <input_file>")
    else:
        input_file = sys.argv[1]
        process_yapl_file(input_file)
