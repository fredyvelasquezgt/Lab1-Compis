
from antlr4 import *
from symbolTable import SymbolTable
from build.yaplParser import yaplParser
from build.yaplVisitor import yaplVisitor

class YaplWalker(yaplVisitor):
    def __init__(self):
        self.symbolTable = SymbolTable()

    def get_symbol_table(self):
        return self.symbolTable

    def visit_node(self, node, node_type):
        self.symbolTable.add(node_type, node)

    def visitProg(self, ctx:yaplParser.ProgContext):
        return self.visitChildren(ctx)

    def visitClass_def(self, ctx:yaplParser.Class_defContext):
        self.visit_node(ctx.CLASS(), "CLASS")
        
        if len(ctx.TYPE_ID()) == 1:
            self.visit_node(ctx.TYPE_ID()[0], "TYPE_ID")

        return self.visitChildren(ctx)

    def visitFeature(self, ctx:yaplParser.FeatureContext):
        self.visit_node(ctx.OBJECT_ID(), "OBJECT_ID")

        if len(ctx.TYPE_ID()) == 1:
            self.visit_node(ctx.TYPE_ID()[0], "TYPE_ID")

        return self.visitChildren(ctx)

    def visitFormal(self, ctx:yaplParser.FormalContext):
        self.visit_node(ctx.OBJECT_ID(), "OBJECT_ID")

        if len(ctx.TYPE_ID()) == 1:
            self.visit_node(ctx.TYPE_ID()[0], "TYPE_ID")

        return self.visitChildren(ctx)

    def visitExpr(self, ctx:yaplParser.ExprContext):
        self.visit_node(ctx.OBJECT_ID()[0], "OBJECT_ID")

        if len(ctx.TYPE_ID()) == 1:
            self.visit_node(ctx.TYPE_ID()[0], "TYPE_ID")

        keywords = ["IF", "THEN", "ELSE", "FI", "WHILE", "LOOP", "POOL", "LET", "IN",
                    "NEW", "ISVOID", "NOT", "INT", "STRING", "TRUE", "FALSE", "SELF"]

        for keyword in keywords:
            if hasattr(ctx, keyword):
                self.visit_node(getattr(ctx, keyword)(), keyword)

        return self.visitChildren(ctx)

del yaplParser
