# Generated from C:/Users/martyna/PycharmProjects/teoriaKompilatorow/Emojii-Programming/Grammars/Grammar.g4 by ANTLR 4.13.1
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
        4,1,57,362,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        1,0,4,0,82,8,0,11,0,12,0,83,1,0,1,0,1,1,1,1,3,1,90,8,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,102,8,2,1,3,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,5,4,112,8,4,10,4,12,4,115,9,4,1,5,1,5,1,5,3,5,120,8,5,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,133,8,8,10,8,12,
        8,136,9,8,1,9,1,9,1,9,5,9,141,8,9,10,9,12,9,144,9,9,1,10,1,10,1,
        10,3,10,149,8,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,3,14,169,8,14,1,15,1,
        15,1,15,1,16,1,16,1,16,1,16,3,16,178,8,16,1,17,1,17,1,18,1,18,1,
        18,1,18,3,18,186,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,5,19,199,8,19,10,19,12,19,202,9,19,1,19,1,19,1,19,1,
        19,1,19,1,19,3,19,210,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,
        22,1,22,1,22,3,22,235,8,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,
        23,5,23,245,8,23,10,23,12,23,248,9,23,1,24,1,24,1,25,1,25,3,25,254,
        8,25,1,26,1,26,3,26,258,8,26,1,27,1,27,1,27,1,28,1,28,3,28,265,8,
        28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,3,30,277,8,
        30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,288,8,31,10,
        31,12,31,291,9,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,5,
        32,302,8,32,10,32,12,32,305,9,32,1,33,1,33,1,33,1,33,1,33,3,33,312,
        8,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,5,35,324,
        8,35,10,35,12,35,327,9,35,1,36,1,36,1,36,1,36,1,36,1,36,5,36,335,
        8,36,10,36,12,36,338,9,36,1,37,1,37,1,37,1,37,1,37,1,37,5,37,346,
        8,37,10,37,12,37,349,9,37,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,
        358,8,38,1,39,1,39,1,39,0,5,62,64,70,72,74,40,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,0,2,1,0,36,37,2,0,1,3,56,56,360,0,
        81,1,0,0,0,2,89,1,0,0,0,4,101,1,0,0,0,6,103,1,0,0,0,8,107,1,0,0,
        0,10,116,1,0,0,0,12,121,1,0,0,0,14,124,1,0,0,0,16,129,1,0,0,0,18,
        137,1,0,0,0,20,145,1,0,0,0,22,150,1,0,0,0,24,155,1,0,0,0,26,160,
        1,0,0,0,28,165,1,0,0,0,30,170,1,0,0,0,32,177,1,0,0,0,34,179,1,0,
        0,0,36,185,1,0,0,0,38,187,1,0,0,0,40,211,1,0,0,0,42,219,1,0,0,0,
        44,230,1,0,0,0,46,241,1,0,0,0,48,249,1,0,0,0,50,253,1,0,0,0,52,257,
        1,0,0,0,54,259,1,0,0,0,56,262,1,0,0,0,58,268,1,0,0,0,60,276,1,0,
        0,0,62,278,1,0,0,0,64,292,1,0,0,0,66,311,1,0,0,0,68,313,1,0,0,0,
        70,317,1,0,0,0,72,328,1,0,0,0,74,339,1,0,0,0,76,357,1,0,0,0,78,359,
        1,0,0,0,80,82,3,2,1,0,81,80,1,0,0,0,82,83,1,0,0,0,83,81,1,0,0,0,
        83,84,1,0,0,0,84,85,1,0,0,0,85,86,5,0,0,1,86,1,1,0,0,0,87,90,3,4,
        2,0,88,90,3,36,18,0,89,87,1,0,0,0,89,88,1,0,0,0,90,3,1,0,0,0,91,
        102,3,6,3,0,92,102,3,12,6,0,93,102,3,22,11,0,94,102,3,8,4,0,95,102,
        3,26,13,0,96,102,3,28,14,0,97,102,3,60,30,0,98,99,3,60,30,0,99,100,
        5,18,0,0,100,102,1,0,0,0,101,91,1,0,0,0,101,92,1,0,0,0,101,93,1,
        0,0,0,101,94,1,0,0,0,101,95,1,0,0,0,101,96,1,0,0,0,101,97,1,0,0,
        0,101,98,1,0,0,0,102,5,1,0,0,0,103,104,5,1,0,0,104,105,5,9,0,0,105,
        106,3,60,30,0,106,7,1,0,0,0,107,108,5,52,0,0,108,113,3,10,5,0,109,
        110,5,17,0,0,110,112,3,10,5,0,111,109,1,0,0,0,112,115,1,0,0,0,113,
        111,1,0,0,0,113,114,1,0,0,0,114,9,1,0,0,0,115,113,1,0,0,0,116,119,
        5,1,0,0,117,118,5,9,0,0,118,120,3,60,30,0,119,117,1,0,0,0,119,120,
        1,0,0,0,120,11,1,0,0,0,121,122,5,47,0,0,122,123,3,16,8,0,123,13,
        1,0,0,0,124,125,5,48,0,0,125,126,3,16,8,0,126,127,5,47,0,0,127,128,
        3,18,9,0,128,15,1,0,0,0,129,134,5,1,0,0,130,131,5,17,0,0,131,133,
        5,1,0,0,132,130,1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,
        1,0,0,0,135,17,1,0,0,0,136,134,1,0,0,0,137,142,3,20,10,0,138,139,
        5,18,0,0,139,141,3,20,10,0,140,138,1,0,0,0,141,144,1,0,0,0,142,140,
        1,0,0,0,142,143,1,0,0,0,143,19,1,0,0,0,144,142,1,0,0,0,145,148,5,
        1,0,0,146,147,5,55,0,0,147,149,5,1,0,0,148,146,1,0,0,0,148,149,1,
        0,0,0,149,21,1,0,0,0,150,151,5,42,0,0,151,152,5,18,0,0,152,153,3,
        2,1,0,153,154,3,24,12,0,154,23,1,0,0,0,155,156,5,43,0,0,156,157,
        5,1,0,0,157,158,5,18,0,0,158,159,3,2,1,0,159,25,1,0,0,0,160,161,
        5,24,0,0,161,162,5,11,0,0,162,163,3,60,30,0,163,164,5,12,0,0,164,
        27,1,0,0,0,165,168,3,6,3,0,166,167,5,17,0,0,167,169,3,6,3,0,168,
        166,1,0,0,0,168,169,1,0,0,0,169,29,1,0,0,0,170,171,5,45,0,0,171,
        172,3,32,16,0,172,31,1,0,0,0,173,178,3,34,17,0,174,175,3,34,17,0,
        175,176,3,60,30,0,176,178,1,0,0,0,177,173,1,0,0,0,177,174,1,0,0,
        0,178,33,1,0,0,0,179,180,5,1,0,0,180,35,1,0,0,0,181,186,3,38,19,
        0,182,186,3,40,20,0,183,186,3,42,21,0,184,186,3,44,22,0,185,181,
        1,0,0,0,185,182,1,0,0,0,185,183,1,0,0,0,185,184,1,0,0,0,186,37,1,
        0,0,0,187,188,5,26,0,0,188,189,3,70,35,0,189,190,5,18,0,0,190,191,
        5,4,0,0,191,200,3,52,26,0,192,193,5,28,0,0,193,194,3,70,35,0,194,
        195,5,18,0,0,195,196,5,4,0,0,196,197,3,52,26,0,197,199,1,0,0,0,198,
        192,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,
        209,1,0,0,0,202,200,1,0,0,0,203,204,5,27,0,0,204,205,3,70,35,0,205,
        206,5,18,0,0,206,207,5,4,0,0,207,208,3,52,26,0,208,210,1,0,0,0,209,
        203,1,0,0,0,209,210,1,0,0,0,210,39,1,0,0,0,211,212,5,33,0,0,212,
        213,5,11,0,0,213,214,3,70,35,0,214,215,5,12,0,0,215,216,5,18,0,0,
        216,217,5,4,0,0,217,218,3,50,25,0,218,41,1,0,0,0,219,220,5,29,0,
        0,220,221,5,1,0,0,221,222,5,30,0,0,222,223,5,31,0,0,223,224,5,11,
        0,0,224,225,5,2,0,0,225,226,5,12,0,0,226,227,5,18,0,0,227,228,5,
        4,0,0,228,229,3,50,25,0,229,43,1,0,0,0,230,231,5,39,0,0,231,232,
        5,1,0,0,232,234,5,11,0,0,233,235,3,46,23,0,234,233,1,0,0,0,234,235,
        1,0,0,0,235,236,1,0,0,0,236,237,5,12,0,0,237,238,5,18,0,0,238,239,
        5,4,0,0,239,240,3,52,26,0,240,45,1,0,0,0,241,246,3,48,24,0,242,243,
        5,17,0,0,243,245,3,48,24,0,244,242,1,0,0,0,245,248,1,0,0,0,246,244,
        1,0,0,0,246,247,1,0,0,0,247,47,1,0,0,0,248,246,1,0,0,0,249,250,5,
        1,0,0,250,49,1,0,0,0,251,254,3,2,1,0,252,254,3,54,27,0,253,251,1,
        0,0,0,253,252,1,0,0,0,254,51,1,0,0,0,255,258,3,50,25,0,256,258,3,
        56,28,0,257,255,1,0,0,0,257,256,1,0,0,0,258,53,1,0,0,0,259,260,7,
        0,0,0,260,261,5,4,0,0,261,55,1,0,0,0,262,264,5,38,0,0,263,265,3,
        58,29,0,264,263,1,0,0,0,264,265,1,0,0,0,265,266,1,0,0,0,266,267,
        5,4,0,0,267,57,1,0,0,0,268,269,3,60,30,0,269,270,5,17,0,0,270,271,
        3,60,30,0,271,59,1,0,0,0,272,277,3,78,39,0,273,277,3,62,31,0,274,
        277,3,70,35,0,275,277,3,68,34,0,276,272,1,0,0,0,276,273,1,0,0,0,
        276,274,1,0,0,0,276,275,1,0,0,0,277,61,1,0,0,0,278,279,6,31,-1,0,
        279,280,3,64,32,0,280,289,1,0,0,0,281,282,10,2,0,0,282,283,5,5,0,
        0,283,288,3,64,32,0,284,285,10,1,0,0,285,286,5,6,0,0,286,288,3,64,
        32,0,287,281,1,0,0,0,287,284,1,0,0,0,288,291,1,0,0,0,289,287,1,0,
        0,0,289,290,1,0,0,0,290,63,1,0,0,0,291,289,1,0,0,0,292,293,6,32,
        -1,0,293,294,3,66,33,0,294,303,1,0,0,0,295,296,10,2,0,0,296,297,
        5,7,0,0,297,302,3,66,33,0,298,299,10,1,0,0,299,300,5,8,0,0,300,302,
        3,66,33,0,301,295,1,0,0,0,301,298,1,0,0,0,302,305,1,0,0,0,303,301,
        1,0,0,0,303,304,1,0,0,0,304,65,1,0,0,0,305,303,1,0,0,0,306,312,3,
        78,39,0,307,308,5,11,0,0,308,309,3,60,30,0,309,310,5,12,0,0,310,
        312,1,0,0,0,311,306,1,0,0,0,311,307,1,0,0,0,312,67,1,0,0,0,313,314,
        5,3,0,0,314,315,5,17,0,0,315,316,3,60,30,0,316,69,1,0,0,0,317,318,
        6,35,-1,0,318,319,3,72,36,0,319,325,1,0,0,0,320,321,10,1,0,0,321,
        322,5,57,0,0,322,324,3,72,36,0,323,320,1,0,0,0,324,327,1,0,0,0,325,
        323,1,0,0,0,325,326,1,0,0,0,326,71,1,0,0,0,327,325,1,0,0,0,328,329,
        6,36,-1,0,329,330,3,74,37,0,330,336,1,0,0,0,331,332,10,1,0,0,332,
        333,5,21,0,0,333,335,3,74,37,0,334,331,1,0,0,0,335,338,1,0,0,0,336,
        334,1,0,0,0,336,337,1,0,0,0,337,73,1,0,0,0,338,336,1,0,0,0,339,340,
        6,37,-1,0,340,341,3,76,38,0,341,347,1,0,0,0,342,343,10,1,0,0,343,
        344,5,22,0,0,344,346,3,76,38,0,345,342,1,0,0,0,346,349,1,0,0,0,347,
        345,1,0,0,0,347,348,1,0,0,0,348,75,1,0,0,0,349,347,1,0,0,0,350,358,
        3,78,39,0,351,352,5,11,0,0,352,353,3,70,35,0,353,354,5,12,0,0,354,
        358,1,0,0,0,355,356,5,25,0,0,356,358,3,76,38,0,357,350,1,0,0,0,357,
        351,1,0,0,0,357,355,1,0,0,0,358,77,1,0,0,0,359,360,7,1,0,0,360,79,
        1,0,0,0,28,83,89,101,113,119,134,142,148,168,177,185,200,209,234,
        246,253,257,264,276,287,289,301,303,311,325,336,347,357
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'='", "'%'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "':'", 
                     "';'", "'\"'", "'or'", "'and'", "<INVALID>", "'print'", 
                     "'not'", "'if'", "'else'", "'elif'", "'for'", "'in'", 
                     "'range'", "'enumerate'", "'while'", "'switch'", "'case'", 
                     "'break'", "'continue'", "'return'", "'def'", "'true'", 
                     "'false'", "'try'", "'EXCEPT'", "'finally'", "'raise'", 
                     "'const'", "'import'", "'from'", "'lambda'", "'none'", 
                     "'~'", "'decl'", "<INVALID>", "'->'", "'as'" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "NUMBER", "STRING", "WS", 
                      "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "EQUAL", "MOD", 
                      "LPAR", "RPAR", "LBRACE", "RBRACE", "LSQB", "RSQB", 
                      "COMMA", "COLON", "SEMI", "QUOTE", "OR", "AND", "COMMENT", 
                      "PRINT", "NOT", "IF", "ELSE", "ELIF", "FOR", "IN", 
                      "RANGE", "ENUMERATE", "WHILE", "SWITCH", "CASE", "BREAK", 
                      "CONTINUE", "RETURN", "DEF", "TRUE", "FALSE", "TRY", 
                      "EXCEPT", "FINALLY", "RAISE", "CONST", "IMPORT", "FROM", 
                      "LAMBDA", "NONE", "ECOMPLEMENT", "DECL", "TYPE", "ARROW", 
                      "AS", "BOOLEAN", "CONDITION_OP" ]

    RULE_start = 0
    RULE_stmt = 1
    RULE_simple_stmt = 2
    RULE_assignment_stmt = 3
    RULE_declare_stmt = 4
    RULE_single_declaration = 5
    RULE_import_stmt = 6
    RULE_from_stmt = 7
    RULE_module_name = 8
    RULE_import_list = 9
    RULE_import_name = 10
    RULE_try_stmt = 11
    RULE_except_clause = 12
    RULE_print_stmt = 13
    RULE_multiple_assignment_stmt = 14
    RULE_raise_stmt = 15
    RULE_exception_expr = 16
    RULE_exception_name = 17
    RULE_compound_stmt = 18
    RULE_if_stmt = 19
    RULE_while_stmt = 20
    RULE_for_stmt = 21
    RULE_function_def = 22
    RULE_parameters = 23
    RULE_typed_par = 24
    RULE_loop_stmt = 25
    RULE_func_body = 26
    RULE_flow_stmt = 27
    RULE_return_stmt = 28
    RULE_explist = 29
    RULE_exp = 30
    RULE_arithmeticOperation = 31
    RULE_term = 32
    RULE_factor = 33
    RULE_printOperation = 34
    RULE_conditionalOperation = 35
    RULE_logicalTerm = 36
    RULE_logicalFactor = 37
    RULE_logicalPrimary = 38
    RULE_value = 39

    ruleNames =  [ "start", "stmt", "simple_stmt", "assignment_stmt", "declare_stmt", 
                   "single_declaration", "import_stmt", "from_stmt", "module_name", 
                   "import_list", "import_name", "try_stmt", "except_clause", 
                   "print_stmt", "multiple_assignment_stmt", "raise_stmt", 
                   "exception_expr", "exception_name", "compound_stmt", 
                   "if_stmt", "while_stmt", "for_stmt", "function_def", 
                   "parameters", "typed_par", "loop_stmt", "func_body", 
                   "flow_stmt", "return_stmt", "explist", "exp", "arithmeticOperation", 
                   "term", "factor", "printOperation", "conditionalOperation", 
                   "logicalTerm", "logicalFactor", "logicalPrimary", "value" ]

    EOF = Token.EOF
    IDENTIFIER=1
    NUMBER=2
    STRING=3
    WS=4
    PLUS=5
    MINUS=6
    MULTIPLY=7
    DIVIDE=8
    EQUAL=9
    MOD=10
    LPAR=11
    RPAR=12
    LBRACE=13
    RBRACE=14
    LSQB=15
    RSQB=16
    COMMA=17
    COLON=18
    SEMI=19
    QUOTE=20
    OR=21
    AND=22
    COMMENT=23
    PRINT=24
    NOT=25
    IF=26
    ELSE=27
    ELIF=28
    FOR=29
    IN=30
    RANGE=31
    ENUMERATE=32
    WHILE=33
    SWITCH=34
    CASE=35
    BREAK=36
    CONTINUE=37
    RETURN=38
    DEF=39
    TRUE=40
    FALSE=41
    TRY=42
    EXCEPT=43
    FINALLY=44
    RAISE=45
    CONST=46
    IMPORT=47
    FROM=48
    LAMBDA=49
    NONE=50
    ECOMPLEMENT=51
    DECL=52
    TYPE=53
    ARROW=54
    AS=55
    BOOLEAN=56
    CONDITION_OP=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StmtContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = GrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.stmt()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 76706888200226830) != 0)):
                    break

            self.state = 85
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Simple_stmtContext,0)


        def compound_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Compound_stmtContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = GrammarParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 11, 24, 25, 42, 47, 52, 56]:
                self.state = 87
                self.simple_stmt()
                pass
            elif token in [26, 29, 33, 39]:
                self.state = 88
                self.compound_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Assignment_stmtContext,0)


        def import_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Import_stmtContext,0)


        def try_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Try_stmtContext,0)


        def declare_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Declare_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Print_stmtContext,0)


        def multiple_assignment_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Multiple_assignment_stmtContext,0)


        def exp(self):
            return self.getTypedRuleContext(GrammarParser.ExpContext,0)


        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_simple_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_stmt" ):
                listener.enterSimple_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_stmt" ):
                listener.exitSimple_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_stmt" ):
                return visitor.visitSimple_stmt(self)
            else:
                return visitor.visitChildren(self)




    def simple_stmt(self):

        localctx = GrammarParser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simple_stmt)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.assignment_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.import_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.try_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.declare_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 95
                self.print_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 96
                self.multiple_assignment_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 97
                self.exp()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 98
                self.exp()
                self.state = 99
                self.match(GrammarParser.COLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(GrammarParser.EQUAL, 0)

        def exp(self):
            return self.getTypedRuleContext(GrammarParser.ExpContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_assignment_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_stmt" ):
                listener.enterAssignment_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_stmt" ):
                listener.exitAssignment_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = GrammarParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(GrammarParser.IDENTIFIER)
            self.state = 104
            self.match(GrammarParser.EQUAL)
            self.state = 105
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECL(self):
            return self.getToken(GrammarParser.DECL, 0)

        def single_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Single_declarationContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Single_declarationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_declare_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare_stmt" ):
                listener.enterDeclare_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare_stmt" ):
                listener.exitDeclare_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_stmt" ):
                return visitor.visitDeclare_stmt(self)
            else:
                return visitor.visitChildren(self)




    def declare_stmt(self):

        localctx = GrammarParser.Declare_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declare_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(GrammarParser.DECL)
            self.state = 108
            self.single_declaration()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 109
                self.match(GrammarParser.COMMA)
                self.state = 110
                self.single_declaration()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(GrammarParser.EQUAL, 0)

        def exp(self):
            return self.getTypedRuleContext(GrammarParser.ExpContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_single_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_declaration" ):
                listener.enterSingle_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_declaration" ):
                listener.exitSingle_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_declaration" ):
                return visitor.visitSingle_declaration(self)
            else:
                return visitor.visitChildren(self)




    def single_declaration(self):

        localctx = GrammarParser.Single_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_single_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(GrammarParser.IDENTIFIER)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 117
                self.match(GrammarParser.EQUAL)
                self.state = 118
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(GrammarParser.IMPORT, 0)

        def module_name(self):
            return self.getTypedRuleContext(GrammarParser.Module_nameContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_import_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_stmt" ):
                listener.enterImport_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_stmt" ):
                listener.exitImport_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_stmt" ):
                return visitor.visitImport_stmt(self)
            else:
                return visitor.visitChildren(self)




    def import_stmt(self):

        localctx = GrammarParser.Import_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_import_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(GrammarParser.IMPORT)
            self.state = 122
            self.module_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class From_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(GrammarParser.FROM, 0)

        def module_name(self):
            return self.getTypedRuleContext(GrammarParser.Module_nameContext,0)


        def IMPORT(self):
            return self.getToken(GrammarParser.IMPORT, 0)

        def import_list(self):
            return self.getTypedRuleContext(GrammarParser.Import_listContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_from_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom_stmt" ):
                listener.enterFrom_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom_stmt" ):
                listener.exitFrom_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFrom_stmt" ):
                return visitor.visitFrom_stmt(self)
            else:
                return visitor.visitChildren(self)




    def from_stmt(self):

        localctx = GrammarParser.From_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_from_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(GrammarParser.FROM)
            self.state = 125
            self.module_name()
            self.state = 126
            self.match(GrammarParser.IMPORT)
            self.state = 127
            self.import_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Module_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.IDENTIFIER)
            else:
                return self.getToken(GrammarParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_module_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule_name" ):
                listener.enterModule_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule_name" ):
                listener.exitModule_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule_name" ):
                return visitor.visitModule_name(self)
            else:
                return visitor.visitChildren(self)




    def module_name(self):

        localctx = GrammarParser.Module_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_module_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(GrammarParser.IDENTIFIER)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 130
                self.match(GrammarParser.COMMA)
                self.state = 131
                self.match(GrammarParser.IDENTIFIER)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Import_nameContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Import_nameContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COLON)
            else:
                return self.getToken(GrammarParser.COLON, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_import_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_list" ):
                listener.enterImport_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_list" ):
                listener.exitImport_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_list" ):
                return visitor.visitImport_list(self)
            else:
                return visitor.visitChildren(self)




    def import_list(self):

        localctx = GrammarParser.Import_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_import_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.import_name()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 138
                self.match(GrammarParser.COLON)
                self.state = 139
                self.import_name()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.IDENTIFIER)
            else:
                return self.getToken(GrammarParser.IDENTIFIER, i)

        def AS(self):
            return self.getToken(GrammarParser.AS, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_import_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_name" ):
                listener.enterImport_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_name" ):
                listener.exitImport_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_name" ):
                return visitor.visitImport_name(self)
            else:
                return visitor.visitChildren(self)




    def import_name(self):

        localctx = GrammarParser.Import_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_import_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(GrammarParser.IDENTIFIER)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 146
                self.match(GrammarParser.AS)
                self.state = 147
                self.match(GrammarParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Try_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(GrammarParser.TRY, 0)

        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def stmt(self):
            return self.getTypedRuleContext(GrammarParser.StmtContext,0)


        def except_clause(self):
            return self.getTypedRuleContext(GrammarParser.Except_clauseContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_try_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTry_stmt" ):
                listener.enterTry_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTry_stmt" ):
                listener.exitTry_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTry_stmt" ):
                return visitor.visitTry_stmt(self)
            else:
                return visitor.visitChildren(self)




    def try_stmt(self):

        localctx = GrammarParser.Try_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_try_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(GrammarParser.TRY)
            self.state = 151
            self.match(GrammarParser.COLON)
            self.state = 152
            self.stmt()
            self.state = 153
            self.except_clause()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Except_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCEPT(self):
            return self.getToken(GrammarParser.EXCEPT, 0)

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def stmt(self):
            return self.getTypedRuleContext(GrammarParser.StmtContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_except_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExcept_clause" ):
                listener.enterExcept_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExcept_clause" ):
                listener.exitExcept_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExcept_clause" ):
                return visitor.visitExcept_clause(self)
            else:
                return visitor.visitChildren(self)




    def except_clause(self):

        localctx = GrammarParser.Except_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_except_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(GrammarParser.EXCEPT)
            self.state = 156
            self.match(GrammarParser.IDENTIFIER)
            self.state = 157
            self.match(GrammarParser.COLON)
            self.state = 158
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(GrammarParser.PRINT, 0)

        def LPAR(self):
            return self.getToken(GrammarParser.LPAR, 0)

        def exp(self):
            return self.getTypedRuleContext(GrammarParser.ExpContext,0)


        def RPAR(self):
            return self.getToken(GrammarParser.RPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stmt" ):
                return visitor.visitPrint_stmt(self)
            else:
                return visitor.visitChildren(self)




    def print_stmt(self):

        localctx = GrammarParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(GrammarParser.PRINT)
            self.state = 161
            self.match(GrammarParser.LPAR)
            self.state = 162
            self.exp()
            self.state = 163
            self.match(GrammarParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiple_assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Assignment_stmtContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Assignment_stmtContext,i)


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_multiple_assignment_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiple_assignment_stmt" ):
                listener.enterMultiple_assignment_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiple_assignment_stmt" ):
                listener.exitMultiple_assignment_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiple_assignment_stmt" ):
                return visitor.visitMultiple_assignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def multiple_assignment_stmt(self):

        localctx = GrammarParser.Multiple_assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_multiple_assignment_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.assignment_stmt()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 166
                self.match(GrammarParser.COMMA)
                self.state = 167
                self.assignment_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Raise_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RAISE(self):
            return self.getToken(GrammarParser.RAISE, 0)

        def exception_expr(self):
            return self.getTypedRuleContext(GrammarParser.Exception_exprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_raise_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaise_stmt" ):
                listener.enterRaise_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaise_stmt" ):
                listener.exitRaise_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaise_stmt" ):
                return visitor.visitRaise_stmt(self)
            else:
                return visitor.visitChildren(self)




    def raise_stmt(self):

        localctx = GrammarParser.Raise_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_raise_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(GrammarParser.RAISE)
            self.state = 171
            self.exception_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exception_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exception_name(self):
            return self.getTypedRuleContext(GrammarParser.Exception_nameContext,0)


        def exp(self):
            return self.getTypedRuleContext(GrammarParser.ExpContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_exception_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterException_expr" ):
                listener.enterException_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitException_expr" ):
                listener.exitException_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitException_expr" ):
                return visitor.visitException_expr(self)
            else:
                return visitor.visitChildren(self)




    def exception_expr(self):

        localctx = GrammarParser.Exception_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exception_expr)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.exception_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.exception_name()
                self.state = 175
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exception_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_exception_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterException_name" ):
                listener.enterException_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitException_name" ):
                listener.exitException_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitException_name" ):
                return visitor.visitException_name(self)
            else:
                return visitor.visitChildren(self)




    def exception_name(self):

        localctx = GrammarParser.Exception_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exception_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(GrammarParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(GrammarParser.While_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(GrammarParser.For_stmtContext,0)


        def function_def(self):
            return self.getTypedRuleContext(GrammarParser.Function_defContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_compound_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_stmt" ):
                listener.enterCompound_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_stmt" ):
                listener.exitCompound_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_stmt" ):
                return visitor.visitCompound_stmt(self)
            else:
                return visitor.visitChildren(self)




    def compound_stmt(self):

        localctx = GrammarParser.Compound_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_compound_stmt)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.if_stmt()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.while_stmt()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.for_stmt()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
                self.function_def()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GrammarParser.IF, 0)

        def conditionalOperation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ConditionalOperationContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ConditionalOperationContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COLON)
            else:
                return self.getToken(GrammarParser.COLON, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.WS)
            else:
                return self.getToken(GrammarParser.WS, i)

        def func_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Func_bodyContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Func_bodyContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.ELIF)
            else:
                return self.getToken(GrammarParser.ELIF, i)

        def ELSE(self):
            return self.getToken(GrammarParser.ELSE, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = GrammarParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(GrammarParser.IF)
            self.state = 188
            self.conditionalOperation(0)
            self.state = 189
            self.match(GrammarParser.COLON)
            self.state = 190
            self.match(GrammarParser.WS)
            self.state = 191
            self.func_body()
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 192
                    self.match(GrammarParser.ELIF)
                    self.state = 193
                    self.conditionalOperation(0)
                    self.state = 194
                    self.match(GrammarParser.COLON)
                    self.state = 195
                    self.match(GrammarParser.WS)
                    self.state = 196
                    self.func_body() 
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 203
                self.match(GrammarParser.ELSE)
                self.state = 204
                self.conditionalOperation(0)
                self.state = 205
                self.match(GrammarParser.COLON)
                self.state = 206
                self.match(GrammarParser.WS)
                self.state = 207
                self.func_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(GrammarParser.WHILE, 0)

        def LPAR(self):
            return self.getToken(GrammarParser.LPAR, 0)

        def conditionalOperation(self):
            return self.getTypedRuleContext(GrammarParser.ConditionalOperationContext,0)


        def RPAR(self):
            return self.getToken(GrammarParser.RPAR, 0)

        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def WS(self):
            return self.getToken(GrammarParser.WS, 0)

        def loop_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Loop_stmtContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = GrammarParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(GrammarParser.WHILE)
            self.state = 212
            self.match(GrammarParser.LPAR)
            self.state = 213
            self.conditionalOperation(0)
            self.state = 214
            self.match(GrammarParser.RPAR)
            self.state = 215
            self.match(GrammarParser.COLON)
            self.state = 216
            self.match(GrammarParser.WS)
            self.state = 217
            self.loop_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GrammarParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def IN(self):
            return self.getToken(GrammarParser.IN, 0)

        def RANGE(self):
            return self.getToken(GrammarParser.RANGE, 0)

        def LPAR(self):
            return self.getToken(GrammarParser.LPAR, 0)

        def NUMBER(self):
            return self.getToken(GrammarParser.NUMBER, 0)

        def RPAR(self):
            return self.getToken(GrammarParser.RPAR, 0)

        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def WS(self):
            return self.getToken(GrammarParser.WS, 0)

        def loop_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Loop_stmtContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = GrammarParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(GrammarParser.FOR)
            self.state = 220
            self.match(GrammarParser.IDENTIFIER)
            self.state = 221
            self.match(GrammarParser.IN)
            self.state = 222
            self.match(GrammarParser.RANGE)
            self.state = 223
            self.match(GrammarParser.LPAR)
            self.state = 224
            self.match(GrammarParser.NUMBER)
            self.state = 225
            self.match(GrammarParser.RPAR)
            self.state = 226
            self.match(GrammarParser.COLON)
            self.state = 227
            self.match(GrammarParser.WS)
            self.state = 228
            self.loop_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(GrammarParser.DEF, 0)

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def LPAR(self):
            return self.getToken(GrammarParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(GrammarParser.RPAR, 0)

        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def WS(self):
            return self.getToken(GrammarParser.WS, 0)

        def func_body(self):
            return self.getTypedRuleContext(GrammarParser.Func_bodyContext,0)


        def parameters(self):
            return self.getTypedRuleContext(GrammarParser.ParametersContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_function_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_def" ):
                listener.enterFunction_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_def" ):
                listener.exitFunction_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_def" ):
                return visitor.visitFunction_def(self)
            else:
                return visitor.visitChildren(self)




    def function_def(self):

        localctx = GrammarParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(GrammarParser.DEF)
            self.state = 231
            self.match(GrammarParser.IDENTIFIER)
            self.state = 232
            self.match(GrammarParser.LPAR)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 233
                self.parameters()


            self.state = 236
            self.match(GrammarParser.RPAR)
            self.state = 237
            self.match(GrammarParser.COLON)
            self.state = 238
            self.match(GrammarParser.WS)
            self.state = 239
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typed_par(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Typed_parContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Typed_parContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = GrammarParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.typed_par()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 242
                self.match(GrammarParser.COMMA)
                self.state = 243
                self.typed_par()
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typed_parContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_typed_par

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyped_par" ):
                listener.enterTyped_par(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyped_par" ):
                listener.exitTyped_par(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyped_par" ):
                return visitor.visitTyped_par(self)
            else:
                return visitor.visitChildren(self)




    def typed_par(self):

        localctx = GrammarParser.Typed_parContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typed_par)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(GrammarParser.StmtContext,0)


        def flow_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Flow_stmtContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_loop_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_stmt" ):
                listener.enterLoop_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_stmt" ):
                listener.exitLoop_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_stmt" ):
                return visitor.visitLoop_stmt(self)
            else:
                return visitor.visitChildren(self)




    def loop_stmt(self):

        localctx = GrammarParser.Loop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_loop_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 11, 24, 25, 26, 29, 33, 39, 42, 47, 52, 56]:
                self.state = 251
                self.stmt()
                pass
            elif token in [36, 37]:
                self.state = 252
                self.flow_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loop_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Loop_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(GrammarParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_func_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_body" ):
                listener.enterFunc_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_body" ):
                listener.exitFunc_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = GrammarParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 11, 24, 25, 26, 29, 33, 36, 37, 39, 42, 47, 52, 56]:
                self.state = 255
                self.loop_stmt()
                pass
            elif token in [38]:
                self.state = 256
                self.return_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Flow_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self):
            return self.getToken(GrammarParser.WS, 0)

        def BREAK(self):
            return self.getToken(GrammarParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(GrammarParser.CONTINUE, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_flow_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlow_stmt" ):
                listener.enterFlow_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlow_stmt" ):
                listener.exitFlow_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlow_stmt" ):
                return visitor.visitFlow_stmt(self)
            else:
                return visitor.visitChildren(self)




    def flow_stmt(self):

        localctx = GrammarParser.Flow_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_flow_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            _la = self._input.LA(1)
            if not(_la==36 or _la==37):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 260
            self.match(GrammarParser.WS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(GrammarParser.RETURN, 0)

        def WS(self):
            return self.getToken(GrammarParser.WS, 0)

        def explist(self):
            return self.getTypedRuleContext(GrammarParser.ExplistContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = GrammarParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(GrammarParser.RETURN)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594071484430) != 0):
                self.state = 263
                self.explist()


            self.state = 266
            self.match(GrammarParser.WS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpContext,i)


        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_explist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplist" ):
                listener.enterExplist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplist" ):
                listener.exitExplist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = GrammarParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_explist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.exp()

            self.state = 269
            self.match(GrammarParser.COMMA)
            self.state = 270
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(GrammarParser.ValueContext,0)


        def arithmeticOperation(self):
            return self.getTypedRuleContext(GrammarParser.ArithmeticOperationContext,0)


        def conditionalOperation(self):
            return self.getTypedRuleContext(GrammarParser.ConditionalOperationContext,0)


        def printOperation(self):
            return self.getTypedRuleContext(GrammarParser.PrintOperationContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = GrammarParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.arithmeticOperation(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 274
                self.conditionalOperation(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 275
                self.printOperation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(GrammarParser.TermContext,0)


        def arithmeticOperation(self):
            return self.getTypedRuleContext(GrammarParser.ArithmeticOperationContext,0)


        def PLUS(self):
            return self.getToken(GrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GrammarParser.MINUS, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_arithmeticOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticOperation" ):
                listener.enterArithmeticOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticOperation" ):
                listener.exitArithmeticOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticOperation" ):
                return visitor.visitArithmeticOperation(self)
            else:
                return visitor.visitChildren(self)



    def arithmeticOperation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ArithmeticOperationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_arithmeticOperation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 289
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 287
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.ArithmeticOperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticOperation)
                        self.state = 281
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 282
                        self.match(GrammarParser.PLUS)
                        self.state = 283
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.ArithmeticOperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticOperation)
                        self.state = 284
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 285
                        self.match(GrammarParser.MINUS)
                        self.state = 286
                        self.term(0)
                        pass

             
                self.state = 291
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(GrammarParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(GrammarParser.TermContext,0)


        def MULTIPLY(self):
            return self.getToken(GrammarParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(GrammarParser.DIVIDE, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 301
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 295
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 296
                        self.match(GrammarParser.MULTIPLY)
                        self.state = 297
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 298
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 299
                        self.match(GrammarParser.DIVIDE)
                        self.state = 300
                        self.factor()
                        pass

             
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(GrammarParser.ValueContext,0)


        def LPAR(self):
            return self.getToken(GrammarParser.LPAR, 0)

        def exp(self):
            return self.getTypedRuleContext(GrammarParser.ExpContext,0)


        def RPAR(self):
            return self.getToken(GrammarParser.RPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = GrammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_factor)
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.value()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.match(GrammarParser.LPAR)
                self.state = 308
                self.exp()
                self.state = 309
                self.match(GrammarParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def COMMA(self):
            return self.getToken(GrammarParser.COMMA, 0)

        def exp(self):
            return self.getTypedRuleContext(GrammarParser.ExpContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_printOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintOperation" ):
                listener.enterPrintOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintOperation" ):
                listener.exitPrintOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintOperation" ):
                return visitor.visitPrintOperation(self)
            else:
                return visitor.visitChildren(self)




    def printOperation(self):

        localctx = GrammarParser.PrintOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_printOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(GrammarParser.STRING)
            self.state = 314
            self.match(GrammarParser.COMMA)
            self.state = 315
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalTerm(self):
            return self.getTypedRuleContext(GrammarParser.LogicalTermContext,0)


        def conditionalOperation(self):
            return self.getTypedRuleContext(GrammarParser.ConditionalOperationContext,0)


        def CONDITION_OP(self):
            return self.getToken(GrammarParser.CONDITION_OP, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_conditionalOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalOperation" ):
                listener.enterConditionalOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalOperation" ):
                listener.exitConditionalOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalOperation" ):
                return visitor.visitConditionalOperation(self)
            else:
                return visitor.visitChildren(self)



    def conditionalOperation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ConditionalOperationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_conditionalOperation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.logicalTerm(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ConditionalOperationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conditionalOperation)
                    self.state = 320
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 321
                    self.match(GrammarParser.CONDITION_OP)
                    self.state = 322
                    self.logicalTerm(0) 
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicalTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalFactor(self):
            return self.getTypedRuleContext(GrammarParser.LogicalFactorContext,0)


        def logicalTerm(self):
            return self.getTypedRuleContext(GrammarParser.LogicalTermContext,0)


        def OR(self):
            return self.getToken(GrammarParser.OR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_logicalTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalTerm" ):
                listener.enterLogicalTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalTerm" ):
                listener.exitLogicalTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalTerm" ):
                return visitor.visitLogicalTerm(self)
            else:
                return visitor.visitChildren(self)



    def logicalTerm(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.LogicalTermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_logicalTerm, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.logicalFactor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.LogicalTermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalTerm)
                    self.state = 331
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 332
                    self.match(GrammarParser.OR)
                    self.state = 333
                    self.logicalFactor(0) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicalFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalPrimary(self):
            return self.getTypedRuleContext(GrammarParser.LogicalPrimaryContext,0)


        def logicalFactor(self):
            return self.getTypedRuleContext(GrammarParser.LogicalFactorContext,0)


        def AND(self):
            return self.getToken(GrammarParser.AND, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_logicalFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalFactor" ):
                listener.enterLogicalFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalFactor" ):
                listener.exitLogicalFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalFactor" ):
                return visitor.visitLogicalFactor(self)
            else:
                return visitor.visitChildren(self)



    def logicalFactor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.LogicalFactorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_logicalFactor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.logicalPrimary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.LogicalFactorContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalFactor)
                    self.state = 342
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 343
                    self.match(GrammarParser.AND)
                    self.state = 344
                    self.logicalPrimary() 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicalPrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(GrammarParser.ValueContext,0)


        def LPAR(self):
            return self.getToken(GrammarParser.LPAR, 0)

        def conditionalOperation(self):
            return self.getTypedRuleContext(GrammarParser.ConditionalOperationContext,0)


        def RPAR(self):
            return self.getToken(GrammarParser.RPAR, 0)

        def NOT(self):
            return self.getToken(GrammarParser.NOT, 0)

        def logicalPrimary(self):
            return self.getTypedRuleContext(GrammarParser.LogicalPrimaryContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_logicalPrimary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalPrimary" ):
                listener.enterLogicalPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalPrimary" ):
                listener.exitLogicalPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalPrimary" ):
                return visitor.visitLogicalPrimary(self)
            else:
                return visitor.visitChildren(self)




    def logicalPrimary(self):

        localctx = GrammarParser.LogicalPrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_logicalPrimary)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.value()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.match(GrammarParser.LPAR)
                self.state = 352
                self.conditionalOperation(0)
                self.state = 353
                self.match(GrammarParser.RPAR)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 355
                self.match(GrammarParser.NOT)
                self.state = 356
                self.logicalPrimary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GrammarParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(GrammarParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(GrammarParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(GrammarParser.STRING, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = GrammarParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594037927950) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.arithmeticOperation_sempred
        self._predicates[32] = self.term_sempred
        self._predicates[35] = self.conditionalOperation_sempred
        self._predicates[36] = self.logicalTerm_sempred
        self._predicates[37] = self.logicalFactor_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmeticOperation_sempred(self, localctx:ArithmeticOperationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def conditionalOperation_sempred(self, localctx:ConditionalOperationContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def logicalTerm_sempred(self, localctx:LogicalTermContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

    def logicalFactor_sempred(self, localctx:LogicalFactorContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




