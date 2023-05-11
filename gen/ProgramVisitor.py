# Generated from C:/Users/corne/Documents/TaxIt\Program.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProgramParser import ProgramParser
else:
    from ProgramParser import ProgramParser

# This class defines a complete generic visitor for a parse tree produced by ProgramParser.

class ProgramVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ProgramParser#program.
    def visitProgram(self, ctx:ProgramParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramParser#tax_bracket.
    def visitTax_bracket(self, ctx:ProgramParser.Tax_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramParser#range.
    def visitRange(self, ctx:ProgramParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramParser#tax_compute.
    def visitTax_compute(self, ctx:ProgramParser.Tax_computeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramParser#deductions.
    def visitDeductions(self, ctx:ProgramParser.DeductionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramParser#donation_deductions.
    def visitDonation_deductions(self, ctx:ProgramParser.Donation_deductionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProgramParser#standard_deductions.
    def visitStandard_deductions(self, ctx:ProgramParser.Standard_deductionsContext):
        return self.visitChildren(ctx)



del ProgramParser