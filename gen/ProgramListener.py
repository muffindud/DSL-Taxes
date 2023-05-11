# Generated from C:/Users/corne/Documents/TaxIt\Program.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProgramParser import ProgramParser
else:
    from ProgramParser import ProgramParser

# This class defines a complete listener for a parse tree produced by ProgramParser.
class ProgramListener(ParseTreeListener):

    # Enter a parse tree produced by ProgramParser#program.
    def enterProgram(self, ctx:ProgramParser.ProgramContext):
        pass

    # Exit a parse tree produced by ProgramParser#program.
    def exitProgram(self, ctx:ProgramParser.ProgramContext):
        pass


    # Enter a parse tree produced by ProgramParser#tax_bracket.
    def enterTax_bracket(self, ctx:ProgramParser.Tax_bracketContext):
        pass

    # Exit a parse tree produced by ProgramParser#tax_bracket.
    def exitTax_bracket(self, ctx:ProgramParser.Tax_bracketContext):
        pass


    # Enter a parse tree produced by ProgramParser#range.
    def enterRange(self, ctx:ProgramParser.RangeContext):
        pass

    # Exit a parse tree produced by ProgramParser#range.
    def exitRange(self, ctx:ProgramParser.RangeContext):
        pass


    # Enter a parse tree produced by ProgramParser#tax_compute.
    def enterTax_compute(self, ctx:ProgramParser.Tax_computeContext):
        pass

    # Exit a parse tree produced by ProgramParser#tax_compute.
    def exitTax_compute(self, ctx:ProgramParser.Tax_computeContext):
        pass


    # Enter a parse tree produced by ProgramParser#deductions.
    def enterDeductions(self, ctx:ProgramParser.DeductionsContext):
        pass

    # Exit a parse tree produced by ProgramParser#deductions.
    def exitDeductions(self, ctx:ProgramParser.DeductionsContext):
        pass


    # Enter a parse tree produced by ProgramParser#donation_deductions.
    def enterDonation_deductions(self, ctx:ProgramParser.Donation_deductionsContext):
        pass

    # Exit a parse tree produced by ProgramParser#donation_deductions.
    def exitDonation_deductions(self, ctx:ProgramParser.Donation_deductionsContext):
        pass


    # Enter a parse tree produced by ProgramParser#standard_deductions.
    def enterStandard_deductions(self, ctx:ProgramParser.Standard_deductionsContext):
        pass

    # Exit a parse tree produced by ProgramParser#standard_deductions.
    def exitStandard_deductions(self, ctx:ProgramParser.Standard_deductionsContext):
        pass



del ProgramParser