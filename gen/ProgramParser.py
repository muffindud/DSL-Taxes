# Generated from C:/Users/corne/Documents/TaxIt\Program.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,157,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,0,4,0,21,8,0,11,0,12,0,22,1,1,1,
        1,1,1,1,1,4,1,29,8,1,11,1,12,1,30,1,1,4,1,34,8,1,11,1,12,1,35,1,
        2,3,2,39,8,2,1,2,1,2,1,2,1,2,3,2,45,8,2,1,2,1,2,3,2,49,8,2,1,2,1,
        2,4,2,53,8,2,11,2,12,2,54,1,3,1,3,1,3,1,3,4,3,61,8,3,11,3,12,3,62,
        1,3,3,3,66,8,3,1,3,1,3,3,3,70,8,3,1,3,1,3,3,3,74,8,3,1,3,1,3,4,3,
        78,8,3,11,3,12,3,79,1,3,3,3,83,8,3,1,3,1,3,3,3,87,8,3,1,3,1,3,3,
        3,91,8,3,1,3,1,3,5,3,95,8,3,10,3,12,3,98,9,3,1,3,3,3,101,8,3,1,4,
        4,4,104,8,4,11,4,12,4,105,1,4,3,4,109,8,4,1,4,1,4,4,4,113,8,4,11,
        4,12,4,114,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,125,8,4,1,5,3,5,128,
        8,5,1,5,1,5,3,5,132,8,5,1,5,1,5,3,5,136,8,5,1,5,1,5,3,5,140,8,5,
        1,6,3,6,143,8,6,1,6,1,6,3,6,147,8,6,1,6,1,6,3,6,151,8,6,1,6,1,6,
        3,6,155,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,2,2,0,3,3,14,14,1,0,14,15,
        181,0,15,1,0,0,0,2,24,1,0,0,0,4,38,1,0,0,0,6,56,1,0,0,0,8,103,1,
        0,0,0,10,127,1,0,0,0,12,142,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,
        16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,19,21,3,
        6,3,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,
        1,1,0,0,0,24,25,5,1,0,0,25,26,5,12,0,0,26,28,5,13,0,0,27,29,5,16,
        0,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,33,
        1,0,0,0,32,34,3,4,2,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,
        35,36,1,0,0,0,36,3,1,0,0,0,37,39,5,12,0,0,38,37,1,0,0,0,38,39,1,
        0,0,0,39,40,1,0,0,0,40,41,5,2,0,0,41,42,5,12,0,0,42,44,7,0,0,0,43,
        45,5,12,0,0,44,43,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,48,5,4,
        0,0,47,49,5,12,0,0,48,47,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,
        52,7,1,0,0,51,53,5,16,0,0,52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,
        0,0,54,55,1,0,0,0,55,5,1,0,0,0,56,57,5,5,0,0,57,58,5,12,0,0,58,60,
        5,13,0,0,59,61,5,16,0,0,60,59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,
        0,62,63,1,0,0,0,63,65,1,0,0,0,64,66,5,12,0,0,65,64,1,0,0,0,65,66,
        1,0,0,0,66,67,1,0,0,0,67,69,5,6,0,0,68,70,5,12,0,0,69,68,1,0,0,0,
        69,70,1,0,0,0,70,71,1,0,0,0,71,73,5,7,0,0,72,74,5,12,0,0,73,72,1,
        0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,77,5,13,0,0,76,78,5,16,0,0,
        77,76,1,0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,
        0,0,0,81,83,5,12,0,0,82,81,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,
        86,5,8,0,0,85,87,5,12,0,0,86,85,1,0,0,0,86,87,1,0,0,0,87,88,1,0,
        0,0,88,90,5,7,0,0,89,91,5,12,0,0,90,89,1,0,0,0,90,91,1,0,0,0,91,
        92,1,0,0,0,92,96,5,14,0,0,93,95,5,16,0,0,94,93,1,0,0,0,95,98,1,0,
        0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,99,
        101,3,8,4,0,100,99,1,0,0,0,100,101,1,0,0,0,101,7,1,0,0,0,102,104,
        5,16,0,0,103,102,1,0,0,0,104,105,1,0,0,0,105,103,1,0,0,0,105,106,
        1,0,0,0,106,108,1,0,0,0,107,109,5,12,0,0,108,107,1,0,0,0,108,109,
        1,0,0,0,109,110,1,0,0,0,110,112,5,9,0,0,111,113,5,16,0,0,112,111,
        1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,124,
        1,0,0,0,116,125,3,10,5,0,117,125,3,12,6,0,118,119,3,10,5,0,119,120,
        3,12,6,0,120,125,1,0,0,0,121,122,3,12,6,0,122,123,3,10,5,0,123,125,
        1,0,0,0,124,116,1,0,0,0,124,117,1,0,0,0,124,118,1,0,0,0,124,121,
        1,0,0,0,125,9,1,0,0,0,126,128,5,12,0,0,127,126,1,0,0,0,127,128,1,
        0,0,0,128,129,1,0,0,0,129,131,5,10,0,0,130,132,5,12,0,0,131,130,
        1,0,0,0,131,132,1,0,0,0,132,133,1,0,0,0,133,135,5,7,0,0,134,136,
        5,12,0,0,135,134,1,0,0,0,135,136,1,0,0,0,136,137,1,0,0,0,137,139,
        5,14,0,0,138,140,5,16,0,0,139,138,1,0,0,0,139,140,1,0,0,0,140,11,
        1,0,0,0,141,143,5,12,0,0,142,141,1,0,0,0,142,143,1,0,0,0,143,144,
        1,0,0,0,144,146,5,11,0,0,145,147,5,12,0,0,146,145,1,0,0,0,146,147,
        1,0,0,0,147,148,1,0,0,0,148,150,5,7,0,0,149,151,5,12,0,0,150,149,
        1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,154,5,14,0,0,153,155,
        5,16,0,0,154,153,1,0,0,0,154,155,1,0,0,0,155,13,1,0,0,0,30,17,22,
        30,35,38,44,48,54,62,65,69,73,79,82,86,90,96,100,105,108,114,124,
        127,131,135,139,142,146,150,154
    ]

class ProgramParser ( Parser ):

    grammarFileName = "Program.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'tax_bracket'", "'range'", "'max'", "'->'", 
                     "'tax_compute'", "'bracket'", "'='", "'income'", "'deductions'", 
                     "'donations'", "'standart'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SPACE", "TEXT", "REAL", "PERCENT", "NEWLINE" ]

    RULE_program = 0
    RULE_tax_bracket = 1
    RULE_range = 2
    RULE_tax_compute = 3
    RULE_deductions = 4
    RULE_donation_deductions = 5
    RULE_standart_deductions = 6

    ruleNames =  [ "program", "tax_bracket", "range", "tax_compute", "deductions", 
                   "donation_deductions", "standart_deductions" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    SPACE=12
    TEXT=13
    REAL=14
    PERCENT=15
    NEWLINE=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tax_bracket(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.Tax_bracketContext)
            else:
                return self.getTypedRuleContext(ProgramParser.Tax_bracketContext,i)


        def tax_compute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.Tax_computeContext)
            else:
                return self.getTypedRuleContext(ProgramParser.Tax_computeContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ProgramParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.tax_bracket()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                self.tax_compute()
                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tax_bracketContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self):
            return self.getToken(ProgramParser.SPACE, 0)

        def TEXT(self):
            return self.getToken(ProgramParser.TEXT, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.NEWLINE)
            else:
                return self.getToken(ProgramParser.NEWLINE, i)

        def range_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.RangeContext)
            else:
                return self.getTypedRuleContext(ProgramParser.RangeContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_tax_bracket

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTax_bracket" ):
                listener.enterTax_bracket(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTax_bracket" ):
                listener.exitTax_bracket(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTax_bracket" ):
                return visitor.visitTax_bracket(self)
            else:
                return visitor.visitChildren(self)




    def tax_bracket(self):

        localctx = ProgramParser.Tax_bracketContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tax_bracket)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(ProgramParser.T__0)
            self.state = 25
            self.match(ProgramParser.SPACE)
            self.state = 26
            self.match(ProgramParser.TEXT)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.match(ProgramParser.NEWLINE)
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.range_()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==12):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.SPACE)
            else:
                return self.getToken(ProgramParser.SPACE, i)

        def REAL(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.REAL)
            else:
                return self.getToken(ProgramParser.REAL, i)

        def PERCENT(self):
            return self.getToken(ProgramParser.PERCENT, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.NEWLINE)
            else:
                return self.getToken(ProgramParser.NEWLINE, i)

        def getRuleIndex(self):
            return ProgramParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange" ):
                return visitor.visitRange(self)
            else:
                return visitor.visitChildren(self)




    def range_(self):

        localctx = ProgramParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_range)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 37
                self.match(ProgramParser.SPACE)


            self.state = 40
            self.match(ProgramParser.T__1)
            self.state = 41
            self.match(ProgramParser.SPACE)
            self.state = 42
            _la = self._input.LA(1)
            if not(_la==3 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 43
                self.match(ProgramParser.SPACE)


            self.state = 46
            self.match(ProgramParser.T__3)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 47
                self.match(ProgramParser.SPACE)


            self.state = 50
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.match(ProgramParser.NEWLINE)
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tax_computeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.SPACE)
            else:
                return self.getToken(ProgramParser.SPACE, i)

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.TEXT)
            else:
                return self.getToken(ProgramParser.TEXT, i)

        def REAL(self):
            return self.getToken(ProgramParser.REAL, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.NEWLINE)
            else:
                return self.getToken(ProgramParser.NEWLINE, i)

        def deductions(self):
            return self.getTypedRuleContext(ProgramParser.DeductionsContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_tax_compute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTax_compute" ):
                listener.enterTax_compute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTax_compute" ):
                listener.exitTax_compute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTax_compute" ):
                return visitor.visitTax_compute(self)
            else:
                return visitor.visitChildren(self)




    def tax_compute(self):

        localctx = ProgramParser.Tax_computeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tax_compute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(ProgramParser.T__4)
            self.state = 57
            self.match(ProgramParser.SPACE)
            self.state = 58
            self.match(ProgramParser.TEXT)
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.match(ProgramParser.NEWLINE)
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 64
                self.match(ProgramParser.SPACE)


            self.state = 67
            self.match(ProgramParser.T__5)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 68
                self.match(ProgramParser.SPACE)


            self.state = 71
            self.match(ProgramParser.T__6)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 72
                self.match(ProgramParser.SPACE)


            self.state = 75
            self.match(ProgramParser.TEXT)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.match(ProgramParser.NEWLINE)
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 81
                self.match(ProgramParser.SPACE)


            self.state = 84
            self.match(ProgramParser.T__7)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 85
                self.match(ProgramParser.SPACE)


            self.state = 88
            self.match(ProgramParser.T__6)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 89
                self.match(ProgramParser.SPACE)


            self.state = 92
            self.match(ProgramParser.REAL)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 93
                    self.match(ProgramParser.NEWLINE) 
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 99
                self.deductions()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeductionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def donation_deductions(self):
            return self.getTypedRuleContext(ProgramParser.Donation_deductionsContext,0)


        def standart_deductions(self):
            return self.getTypedRuleContext(ProgramParser.Standart_deductionsContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.NEWLINE)
            else:
                return self.getToken(ProgramParser.NEWLINE, i)

        def SPACE(self):
            return self.getToken(ProgramParser.SPACE, 0)

        def getRuleIndex(self):
            return ProgramParser.RULE_deductions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeductions" ):
                listener.enterDeductions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeductions" ):
                listener.exitDeductions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeductions" ):
                return visitor.visitDeductions(self)
            else:
                return visitor.visitChildren(self)




    def deductions(self):

        localctx = ProgramParser.DeductionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_deductions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.match(ProgramParser.NEWLINE)
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 107
                self.match(ProgramParser.SPACE)


            self.state = 110
            self.match(ProgramParser.T__8)
            self.state = 112 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 111
                self.match(ProgramParser.NEWLINE)
                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 116
                self.donation_deductions()
                pass

            elif la_ == 2:
                self.state = 117
                self.standart_deductions()
                pass

            elif la_ == 3:
                self.state = 118
                self.donation_deductions()
                self.state = 119
                self.standart_deductions()
                pass

            elif la_ == 4:
                self.state = 121
                self.standart_deductions()
                self.state = 122
                self.donation_deductions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Donation_deductionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REAL(self):
            return self.getToken(ProgramParser.REAL, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.SPACE)
            else:
                return self.getToken(ProgramParser.SPACE, i)

        def NEWLINE(self):
            return self.getToken(ProgramParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ProgramParser.RULE_donation_deductions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDonation_deductions" ):
                listener.enterDonation_deductions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDonation_deductions" ):
                listener.exitDonation_deductions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDonation_deductions" ):
                return visitor.visitDonation_deductions(self)
            else:
                return visitor.visitChildren(self)




    def donation_deductions(self):

        localctx = ProgramParser.Donation_deductionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_donation_deductions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 126
                self.match(ProgramParser.SPACE)


            self.state = 129
            self.match(ProgramParser.T__9)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 130
                self.match(ProgramParser.SPACE)


            self.state = 133
            self.match(ProgramParser.T__6)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 134
                self.match(ProgramParser.SPACE)


            self.state = 137
            self.match(ProgramParser.REAL)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 138
                self.match(ProgramParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Standart_deductionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REAL(self):
            return self.getToken(ProgramParser.REAL, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.SPACE)
            else:
                return self.getToken(ProgramParser.SPACE, i)

        def NEWLINE(self):
            return self.getToken(ProgramParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ProgramParser.RULE_standart_deductions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStandart_deductions" ):
                listener.enterStandart_deductions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStandart_deductions" ):
                listener.exitStandart_deductions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStandart_deductions" ):
                return visitor.visitStandart_deductions(self)
            else:
                return visitor.visitChildren(self)




    def standart_deductions(self):

        localctx = ProgramParser.Standart_deductionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_standart_deductions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 141
                self.match(ProgramParser.SPACE)


            self.state = 144
            self.match(ProgramParser.T__10)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 145
                self.match(ProgramParser.SPACE)


            self.state = 148
            self.match(ProgramParser.T__6)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 149
                self.match(ProgramParser.SPACE)


            self.state = 152
            self.match(ProgramParser.REAL)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 153
                self.match(ProgramParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





