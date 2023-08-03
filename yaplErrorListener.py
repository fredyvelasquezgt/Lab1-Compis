from antlr4 import *
from antlr4.error.ErrorListener import *

class YaplErrorListener(ErrorListener):

    ANSI_RESET = "\u001B[0m"
    ANSI_RED = "\u001B[31m"

    def display_error(self, line, column, message):
        print("\n" + self.ANSI_RED)
        print("----------------------------- ERROR -----------------------------")
        print(f"Error: position {line}:{column} {message}")
        print("-----------------------------------------------------------------")
        print("\n" + self.ANSI_RESET)

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.display_error(line, column, msg)
