# Generated from C:/Users/martyna/PycharmProjects/teoriaKompilatorow/Emojii-Programming/Grammars/graamPROBA.g4 by ANTLR 4.13.1
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
        4,1,62,361,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        22,1,22,1,22,3,22,235,8,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,5,
        23,244,8,23,10,23,12,23,247,9,23,1,24,1,24,1,25,1,25,3,25,253,8,
        25,1,26,1,26,3,26,257,8,26,1,27,1,27,1,27,1,28,1,28,3,28,264,8,28,
        1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,3,30,276,8,30,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,287,8,31,10,31,
        12,31,290,9,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,5,32,
        301,8,32,10,32,12,32,304,9,32,1,33,1,33,1,33,1,33,1,33,3,33,311,
        8,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,5,35,323,
        8,35,10,35,12,35,326,9,35,1,36,1,36,1,36,1,36,1,36,1,36,5,36,334,
        8,36,10,36,12,36,337,9,36,1,37,1,37,1,37,1,37,1,37,1,37,5,37,345,
        8,37,10,37,12,37,348,9,37,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,
        357,8,38,1,39,1,39,1,39,0,5,62,64,70,72,74,40,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,0,2,1,0,41,42,2,0,3,5,61,61,359,0,
        81,1,0,0,0,2,89,1,0,0,0,4,101,1,0,0,0,6,103,1,0,0,0,8,107,1,0,0,
        0,10,116,1,0,0,0,12,121,1,0,0,0,14,124,1,0,0,0,16,129,1,0,0,0,18,
        137,1,0,0,0,20,145,1,0,0,0,22,150,1,0,0,0,24,155,1,0,0,0,26,160,
        1,0,0,0,28,165,1,0,0,0,30,170,1,0,0,0,32,177,1,0,0,0,34,179,1,0,
        0,0,36,185,1,0,0,0,38,187,1,0,0,0,40,211,1,0,0,0,42,219,1,0,0,0,
        44,230,1,0,0,0,46,240,1,0,0,0,48,248,1,0,0,0,50,252,1,0,0,0,52,256,
        1,0,0,0,54,258,1,0,0,0,56,261,1,0,0,0,58,267,1,0,0,0,60,275,1,0,
        0,0,62,277,1,0,0,0,64,291,1,0,0,0,66,310,1,0,0,0,68,312,1,0,0,0,
        70,316,1,0,0,0,72,327,1,0,0,0,74,338,1,0,0,0,76,356,1,0,0,0,78,358,
        1,0,0,0,80,82,3,2,1,0,81,80,1,0,0,0,82,83,1,0,0,0,83,81,1,0,0,0,
        83,84,1,0,0,0,84,85,1,0,0,0,85,86,5,0,0,1,86,1,1,0,0,0,87,90,3,4,
        2,0,88,90,3,36,18,0,89,87,1,0,0,0,89,88,1,0,0,0,90,3,1,0,0,0,91,
        102,3,6,3,0,92,102,3,12,6,0,93,102,3,22,11,0,94,102,3,8,4,0,95,102,
        3,26,13,0,96,102,3,28,14,0,97,102,3,60,30,0,98,99,3,60,30,0,99,100,
        5,22,0,0,100,102,1,0,0,0,101,91,1,0,0,0,101,92,1,0,0,0,101,93,1,
        0,0,0,101,94,1,0,0,0,101,95,1,0,0,0,101,96,1,0,0,0,101,97,1,0,0,
        0,101,98,1,0,0,0,102,5,1,0,0,0,103,104,5,3,0,0,104,105,5,11,0,0,
        105,106,3,60,30,0,106,7,1,0,0,0,107,108,5,58,0,0,108,113,3,10,5,
        0,109,110,5,21,0,0,110,112,3,10,5,0,111,109,1,0,0,0,112,115,1,0,
        0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,9,1,0,0,0,115,113,1,0,0,
        0,116,119,5,3,0,0,117,118,5,11,0,0,118,120,3,60,30,0,119,117,1,0,
        0,0,119,120,1,0,0,0,120,11,1,0,0,0,121,122,5,52,0,0,122,123,3,16,
        8,0,123,13,1,0,0,0,124,125,5,53,0,0,125,126,3,16,8,0,126,127,5,52,
        0,0,127,128,3,18,9,0,128,15,1,0,0,0,129,134,5,3,0,0,130,131,5,21,
        0,0,131,133,5,3,0,0,132,130,1,0,0,0,133,136,1,0,0,0,134,132,1,0,
        0,0,134,135,1,0,0,0,135,17,1,0,0,0,136,134,1,0,0,0,137,142,3,20,
        10,0,138,139,5,22,0,0,139,141,3,20,10,0,140,138,1,0,0,0,141,144,
        1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,19,1,0,0,0,144,142,1,
        0,0,0,145,148,5,3,0,0,146,147,5,60,0,0,147,149,5,3,0,0,148,146,1,
        0,0,0,148,149,1,0,0,0,149,21,1,0,0,0,150,151,5,47,0,0,151,152,5,
        22,0,0,152,153,3,2,1,0,153,154,3,24,12,0,154,23,1,0,0,0,155,156,
        5,48,0,0,156,157,5,3,0,0,157,158,5,22,0,0,158,159,3,2,1,0,159,25,
        1,0,0,0,160,161,5,29,0,0,161,162,5,17,0,0,162,163,3,60,30,0,163,
        164,5,18,0,0,164,27,1,0,0,0,165,168,3,6,3,0,166,167,5,21,0,0,167,
        169,3,6,3,0,168,166,1,0,0,0,168,169,1,0,0,0,169,29,1,0,0,0,170,171,
        5,50,0,0,171,172,3,32,16,0,172,31,1,0,0,0,173,178,3,34,17,0,174,
        175,3,34,17,0,175,176,3,60,30,0,176,178,1,0,0,0,177,173,1,0,0,0,
        177,174,1,0,0,0,178,33,1,0,0,0,179,180,5,3,0,0,180,35,1,0,0,0,181,
        186,3,38,19,0,182,186,3,40,20,0,183,186,3,42,21,0,184,186,3,44,22,
        0,185,181,1,0,0,0,185,182,1,0,0,0,185,183,1,0,0,0,185,184,1,0,0,
        0,186,37,1,0,0,0,187,188,5,31,0,0,188,189,3,70,35,0,189,190,5,22,
        0,0,190,191,5,6,0,0,191,200,3,52,26,0,192,193,5,33,0,0,193,194,3,
        70,35,0,194,195,5,22,0,0,195,196,5,6,0,0,196,197,3,52,26,0,197,199,
        1,0,0,0,198,192,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,
        1,0,0,0,201,209,1,0,0,0,202,200,1,0,0,0,203,204,5,32,0,0,204,205,
        3,70,35,0,205,206,5,22,0,0,206,207,5,6,0,0,207,208,3,52,26,0,208,
        210,1,0,0,0,209,203,1,0,0,0,209,210,1,0,0,0,210,39,1,0,0,0,211,212,
        5,38,0,0,212,213,5,17,0,0,213,214,3,70,35,0,214,215,5,18,0,0,215,
        216,5,22,0,0,216,217,5,6,0,0,217,218,3,50,25,0,218,41,1,0,0,0,219,
        220,5,34,0,0,220,221,5,3,0,0,221,222,5,35,0,0,222,223,5,36,0,0,223,
        224,5,17,0,0,224,225,5,4,0,0,225,226,5,18,0,0,226,227,5,22,0,0,227,
        228,5,6,0,0,228,229,3,50,25,0,229,43,1,0,0,0,230,231,5,44,0,0,231,
        232,5,3,0,0,232,234,5,17,0,0,233,235,3,46,23,0,234,233,1,0,0,0,234,
        235,1,0,0,0,235,236,1,0,0,0,236,237,5,18,0,0,237,238,5,22,0,0,238,
        239,3,52,26,0,239,45,1,0,0,0,240,245,3,48,24,0,241,242,5,21,0,0,
        242,244,3,48,24,0,243,241,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,
        0,245,246,1,0,0,0,246,47,1,0,0,0,247,245,1,0,0,0,248,249,5,3,0,0,
        249,49,1,0,0,0,250,253,3,2,1,0,251,253,3,54,27,0,252,250,1,0,0,0,
        252,251,1,0,0,0,253,51,1,0,0,0,254,257,3,50,25,0,255,257,3,56,28,
        0,256,254,1,0,0,0,256,255,1,0,0,0,257,53,1,0,0,0,258,259,7,0,0,0,
        259,260,5,6,0,0,260,55,1,0,0,0,261,263,5,43,0,0,262,264,3,58,29,
        0,263,262,1,0,0,0,263,264,1,0,0,0,264,265,1,0,0,0,265,266,5,6,0,
        0,266,57,1,0,0,0,267,268,3,60,30,0,268,269,5,21,0,0,269,270,3,60,
        30,0,270,59,1,0,0,0,271,276,3,78,39,0,272,276,3,62,31,0,273,276,
        3,70,35,0,274,276,3,68,34,0,275,271,1,0,0,0,275,272,1,0,0,0,275,
        273,1,0,0,0,275,274,1,0,0,0,276,61,1,0,0,0,277,278,6,31,-1,0,278,
        279,3,64,32,0,279,288,1,0,0,0,280,281,10,2,0,0,281,282,5,7,0,0,282,
        287,3,64,32,0,283,284,10,1,0,0,284,285,5,8,0,0,285,287,3,64,32,0,
        286,280,1,0,0,0,286,283,1,0,0,0,287,290,1,0,0,0,288,286,1,0,0,0,
        288,289,1,0,0,0,289,63,1,0,0,0,290,288,1,0,0,0,291,292,6,32,-1,0,
        292,293,3,66,33,0,293,302,1,0,0,0,294,295,10,2,0,0,295,296,5,9,0,
        0,296,301,3,66,33,0,297,298,10,1,0,0,298,299,5,10,0,0,299,301,3,
        66,33,0,300,294,1,0,0,0,300,297,1,0,0,0,301,304,1,0,0,0,302,300,
        1,0,0,0,302,303,1,0,0,0,303,65,1,0,0,0,304,302,1,0,0,0,305,311,3,
        78,39,0,306,307,5,1,0,0,307,308,3,60,30,0,308,309,5,2,0,0,309,311,
        1,0,0,0,310,305,1,0,0,0,310,306,1,0,0,0,311,67,1,0,0,0,312,313,5,
        5,0,0,313,314,5,21,0,0,314,315,3,60,30,0,315,69,1,0,0,0,316,317,
        6,35,-1,0,317,318,3,72,36,0,318,324,1,0,0,0,319,320,10,1,0,0,320,
        321,5,62,0,0,321,323,3,72,36,0,322,319,1,0,0,0,323,326,1,0,0,0,324,
        322,1,0,0,0,324,325,1,0,0,0,325,71,1,0,0,0,326,324,1,0,0,0,327,328,
        6,36,-1,0,328,329,3,74,37,0,329,335,1,0,0,0,330,331,10,1,0,0,331,
        332,5,25,0,0,332,334,3,74,37,0,333,330,1,0,0,0,334,337,1,0,0,0,335,
        333,1,0,0,0,335,336,1,0,0,0,336,73,1,0,0,0,337,335,1,0,0,0,338,339,
        6,37,-1,0,339,340,3,76,38,0,340,346,1,0,0,0,341,342,10,1,0,0,342,
        343,5,26,0,0,343,345,3,76,38,0,344,341,1,0,0,0,345,348,1,0,0,0,346,
        344,1,0,0,0,346,347,1,0,0,0,347,75,1,0,0,0,348,346,1,0,0,0,349,357,
        3,78,39,0,350,351,5,17,0,0,351,352,3,70,35,0,352,353,5,18,0,0,353,
        357,1,0,0,0,354,355,5,30,0,0,355,357,3,76,38,0,356,349,1,0,0,0,356,
        350,1,0,0,0,356,354,1,0,0,0,357,77,1,0,0,0,358,359,7,1,0,0,359,79,
        1,0,0,0,28,83,89,101,113,119,134,142,148,168,177,185,200,209,234,
        245,252,256,263,275,286,288,300,302,310,324,335,346,356
    ]

class graamPROBAParser ( Parser ):

    grammarFileName = "graamPROBA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\u00E2\\u017E\\u2022'", 
                     "'\\u00E2\\u017E\\u2013'", "'\\u00E2\\u015B\\u2013\\u010F\\u00B8\\u0179'", 
                     "'\\u00E2\\u017E\\u2014'", "'\\u0111\\u017A\\u017A\\u00B0'", 
                     "'\\u0111\\u017A\\uFFFD\\u2030'", "'\\u0111\\u017A\\uFFFD\\uFFFD'", 
                     "'\\u0111\\u017A\\uFFFD\\u2020'", "'\\u0111\\u017A\\uFFFD\\u017C\\u010F\\u00B8\\u0179'", 
                     "'%'", "'\\u0111\\u017A\\u00AB\\u00B7'", "'\\u0111\\u017A\\u00AB\\u00B8'", 
                     "'\\u0111\\u017A\\u00AB\\u02DB'", "'\\u0111\\u017A\\u00AB\\u00B1'", 
                     "'\\u0111\\u017A\\u201C\\u017D'", "'\\u0111\\u017A\\u2013\\u2021\\u010F\\u00B8\\u0179'", 
                     "'\\u0111\\u017A\\u201C\\u015A'", "'\\u0111\\u017A\\u017D\\u00AC'", 
                     "'\\u0111\\u017A\\u2022\\u00B5\\u010F\\u00B8\\u0179\\u00E2\\u20AC\\u0164\\u00E2\\u2122\\u20AC\\u010F\\u00B8\\u0179'", 
                     "'\\u0111\\u017A\\u2018\\u00AD'", "'\\u0111\\u017A\\u0164\\u013E'", 
                     "<INVALID>", "'\\u0111\\u017A\\u2013\\u00A8\\u010F\\u00B8\\u0179'", 
                     "'\\u00E2\\u0165\\u2014'", "'\\u00E2\\u0165\\u201C'", 
                     "'\\u00E2\\u0165\\u2014\\u00E2\\u0165\\u2014'", "'\\u00E2\\u0165\\u201C\\u00E2\\u0165\\u2014'", 
                     "'\\u0111\\u017A\\u017D\\uFFFD'", "'\\u0111\\u017A\\u201C\\u00AD'", 
                     "'\\u0111\\u017A\\u0179\\u201D\\u010F\\u00B8\\u0179'", 
                     "'\\u0111\\u017A\\u201C\\u00BB'", "'\\u0111\\u017A\\u015A\\u015E\\u010F\\u00B8\\u0179'", 
                     "'\\u0111\\u017A\\u201C\\u2039'", "'\\u00E2\\u015B\\u2026'", 
                     "'\\u0111\\u017A\\u0161\\u00A6'", "'\\u0111\\u017A\\u2019\\u2020'", 
                     "'\\u0111\\u017A\\u015E\\uFFFD'", "'\\u0111\\u017A\\u2019\\u02C7'", 
                     "'\\u0111\\u017A\\u2018\\u0164'", "'\\u0111\\u017A\\u2018\\u017D'", 
                     "'\\u0111\\u017A\\u201D\\u00AE'", "'\\u0111\\u017A\\u017D\\u0141'", 
                     "'\\u00E2\\u015A\\u203A'", "'\\u0111\\u017A\\u015A\\u2026'", 
                     "'\\u0111\\u017A\\u2019\\u20AC'", "'\\u0111\\u017A\\u015A\\u017D'", 
                     "'\\u0111\\u017A\\u0161\\u203A'", "'\\u0111\\u017A\\u015A\\uFFFD'", 
                     "'\\u0111\\u017A\\u2014\\u2018\\u010F\\u00B8\\u0179'", 
                     "'\\u0103\\u20AC\\u00B0'", "'->'", "'decl'", "<INVALID>", 
                     "'as'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "NUMBER", "STRING", "WS", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "EQUAL", "GREATER", "SMALLER", "EGREATER", 
                      "ESMALLER", "MOD", "LPAR", "RPAR", "LSQB", "RSQB", 
                      "COMMA", "COLON", "SEMI", "QUOTE", "OR", "AND", "PERCENT", 
                      "COMMENT", "PRINT", "NOT", "IF", "ELSE", "ELIF", "FOR", 
                      "IN", "RANGE", "ENUMERATE", "WHILE", "SWITCH", "CASE", 
                      "BREAK", "CONTINUE", "RETURN", "DEF", "TRUE", "FALSE", 
                      "TRY", "EXCEPT", "FINALLY", "RAISE", "CONST", "IMPORT", 
                      "FROM", "LAMBDA", "NONE", "ECOMPLEMENT", "ARROW", 
                      "DECL", "TYPE", "AS", "BOOLEAN", "CONDITION_OP" ]

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
    T__0=1
    T__1=2
    IDENTIFIER=3
    NUMBER=4
    STRING=5
    WS=6
    PLUS=7
    MINUS=8
    MULTIPLY=9
    DIVIDE=10
    EQUAL=11
    GREATER=12
    SMALLER=13
    EGREATER=14
    ESMALLER=15
    MOD=16
    LPAR=17
    RPAR=18
    LSQB=19
    RSQB=20
    COMMA=21
    COLON=22
    SEMI=23
    QUOTE=24
    OR=25
    AND=26
    PERCENT=27
    COMMENT=28
    PRINT=29
    NOT=30
    IF=31
    ELSE=32
    ELIF=33
    FOR=34
    IN=35
    RANGE=36
    ENUMERATE=37
    WHILE=38
    SWITCH=39
    CASE=40
    BREAK=41
    CONTINUE=42
    RETURN=43
    DEF=44
    TRUE=45
    FALSE=46
    TRY=47
    EXCEPT=48
    FINALLY=49
    RAISE=50
    CONST=51
    IMPORT=52
    FROM=53
    LAMBDA=54
    NONE=55
    ECOMPLEMENT=56
    ARROW=57
    DECL=58
    TYPE=59
    AS=60
    BOOLEAN=61
    CONDITION_OP=62

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
            return self.getToken(graamPROBAParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(graamPROBAParser.StmtContext)
            else:
                return self.getTypedRuleContext(graamPROBAParser.StmtContext,i)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_start

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

        localctx = graamPROBAParser.StartContext(self, self._ctx, self.state)
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2598735610483179578) != 0)):
                    break

            self.state = 85
            self.match(graamPROBAParser.EOF)
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
            return self.getTypedRuleContext(graamPROBAParser.Simple_stmtContext,0)


        def compound_stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.Compound_stmtContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_stmt

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

        localctx = graamPROBAParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 5, 17, 29, 30, 47, 52, 58, 61]:
                self.state = 87
                self.simple_stmt()
                pass
            elif token in [31, 34, 38, 44]:
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
            return self.getTypedRuleContext(graamPROBAParser.Assignment_stmtContext,0)


        def import_stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.Import_stmtContext,0)


        def try_stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.Try_stmtContext,0)


        def declare_stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.Declare_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.Print_stmtContext,0)


        def multiple_assignment_stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.Multiple_assignment_stmtContext,0)


        def exp(self):
            return self.getTypedRuleContext(graamPROBAParser.ExpContext,0)


        def COLON(self):
            return self.getToken(graamPROBAParser.COLON, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_simple_stmt

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

        localctx = graamPROBAParser.Simple_stmtContext(self, self._ctx, self.state)
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
                self.match(graamPROBAParser.COLON)
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
            return self.getToken(graamPROBAParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(graamPROBAParser.EQUAL, 0)

        def exp(self):
            return self.getTypedRuleContext(graamPROBAParser.ExpContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_assignment_stmt

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

        localctx = graamPROBAParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(graamPROBAParser.IDENTIFIER)
            self.state = 104
            self.match(graamPROBAParser.EQUAL)
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
            return self.getToken(graamPROBAParser.DECL, 0)

        def single_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(graamPROBAParser.Single_declarationContext)
            else:
                return self.getTypedRuleContext(graamPROBAParser.Single_declarationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(graamPROBAParser.COMMA)
            else:
                return self.getToken(graamPROBAParser.COMMA, i)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_declare_stmt

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

        localctx = graamPROBAParser.Declare_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declare_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(graamPROBAParser.DECL)
            self.state = 108
            self.single_declaration()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 109
                self.match(graamPROBAParser.COMMA)
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
            return self.getToken(graamPROBAParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(graamPROBAParser.EQUAL, 0)

        def exp(self):
            return self.getTypedRuleContext(graamPROBAParser.ExpContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_single_declaration

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

        localctx = graamPROBAParser.Single_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_single_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(graamPROBAParser.IDENTIFIER)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 117
                self.match(graamPROBAParser.EQUAL)
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
            return self.getToken(graamPROBAParser.IMPORT, 0)

        def module_name(self):
            return self.getTypedRuleContext(graamPROBAParser.Module_nameContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_import_stmt

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

        localctx = graamPROBAParser.Import_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_import_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(graamPROBAParser.IMPORT)
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
            return self.getToken(graamPROBAParser.FROM, 0)

        def module_name(self):
            return self.getTypedRuleContext(graamPROBAParser.Module_nameContext,0)


        def IMPORT(self):
            return self.getToken(graamPROBAParser.IMPORT, 0)

        def import_list(self):
            return self.getTypedRuleContext(graamPROBAParser.Import_listContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_from_stmt

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

        localctx = graamPROBAParser.From_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_from_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(graamPROBAParser.FROM)
            self.state = 125
            self.module_name()
            self.state = 126
            self.match(graamPROBAParser.IMPORT)
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
                return self.getTokens(graamPROBAParser.IDENTIFIER)
            else:
                return self.getToken(graamPROBAParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(graamPROBAParser.COMMA)
            else:
                return self.getToken(graamPROBAParser.COMMA, i)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_module_name

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

        localctx = graamPROBAParser.Module_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_module_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(graamPROBAParser.IDENTIFIER)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 130
                self.match(graamPROBAParser.COMMA)
                self.state = 131
                self.match(graamPROBAParser.IDENTIFIER)
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
                return self.getTypedRuleContexts(graamPROBAParser.Import_nameContext)
            else:
                return self.getTypedRuleContext(graamPROBAParser.Import_nameContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(graamPROBAParser.COLON)
            else:
                return self.getToken(graamPROBAParser.COLON, i)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_import_list

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

        localctx = graamPROBAParser.Import_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_import_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.import_name()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 138
                self.match(graamPROBAParser.COLON)
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
                return self.getTokens(graamPROBAParser.IDENTIFIER)
            else:
                return self.getToken(graamPROBAParser.IDENTIFIER, i)

        def AS(self):
            return self.getToken(graamPROBAParser.AS, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_import_name

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

        localctx = graamPROBAParser.Import_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_import_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(graamPROBAParser.IDENTIFIER)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==60:
                self.state = 146
                self.match(graamPROBAParser.AS)
                self.state = 147
                self.match(graamPROBAParser.IDENTIFIER)


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
            return self.getToken(graamPROBAParser.TRY, 0)

        def COLON(self):
            return self.getToken(graamPROBAParser.COLON, 0)

        def stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.StmtContext,0)


        def except_clause(self):
            return self.getTypedRuleContext(graamPROBAParser.Except_clauseContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_try_stmt

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

        localctx = graamPROBAParser.Try_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_try_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(graamPROBAParser.TRY)
            self.state = 151
            self.match(graamPROBAParser.COLON)
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
            return self.getToken(graamPROBAParser.EXCEPT, 0)

        def IDENTIFIER(self):
            return self.getToken(graamPROBAParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(graamPROBAParser.COLON, 0)

        def stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.StmtContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_except_clause

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

        localctx = graamPROBAParser.Except_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_except_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(graamPROBAParser.EXCEPT)
            self.state = 156
            self.match(graamPROBAParser.IDENTIFIER)
            self.state = 157
            self.match(graamPROBAParser.COLON)
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
            return self.getToken(graamPROBAParser.PRINT, 0)

        def LPAR(self):
            return self.getToken(graamPROBAParser.LPAR, 0)

        def exp(self):
            return self.getTypedRuleContext(graamPROBAParser.ExpContext,0)


        def RPAR(self):
            return self.getToken(graamPROBAParser.RPAR, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_print_stmt

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

        localctx = graamPROBAParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(graamPROBAParser.PRINT)
            self.state = 161
            self.match(graamPROBAParser.LPAR)
            self.state = 162
            self.exp()
            self.state = 163
            self.match(graamPROBAParser.RPAR)
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
                return self.getTypedRuleContexts(graamPROBAParser.Assignment_stmtContext)
            else:
                return self.getTypedRuleContext(graamPROBAParser.Assignment_stmtContext,i)


        def COMMA(self):
            return self.getToken(graamPROBAParser.COMMA, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_multiple_assignment_stmt

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

        localctx = graamPROBAParser.Multiple_assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_multiple_assignment_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.assignment_stmt()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 166
                self.match(graamPROBAParser.COMMA)
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
            return self.getToken(graamPROBAParser.RAISE, 0)

        def exception_expr(self):
            return self.getTypedRuleContext(graamPROBAParser.Exception_exprContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_raise_stmt

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

        localctx = graamPROBAParser.Raise_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_raise_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(graamPROBAParser.RAISE)
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
            return self.getTypedRuleContext(graamPROBAParser.Exception_nameContext,0)


        def exp(self):
            return self.getTypedRuleContext(graamPROBAParser.ExpContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_exception_expr

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

        localctx = graamPROBAParser.Exception_exprContext(self, self._ctx, self.state)
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
            return self.getToken(graamPROBAParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_exception_name

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

        localctx = graamPROBAParser.Exception_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exception_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(graamPROBAParser.IDENTIFIER)
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
            return self.getTypedRuleContext(graamPROBAParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.While_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.For_stmtContext,0)


        def function_def(self):
            return self.getTypedRuleContext(graamPROBAParser.Function_defContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_compound_stmt

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

        localctx = graamPROBAParser.Compound_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_compound_stmt)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.if_stmt()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.while_stmt()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.for_stmt()
                pass
            elif token in [44]:
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
            return self.getToken(graamPROBAParser.IF, 0)

        def conditionalOperation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(graamPROBAParser.ConditionalOperationContext)
            else:
                return self.getTypedRuleContext(graamPROBAParser.ConditionalOperationContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(graamPROBAParser.COLON)
            else:
                return self.getToken(graamPROBAParser.COLON, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(graamPROBAParser.WS)
            else:
                return self.getToken(graamPROBAParser.WS, i)

        def func_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(graamPROBAParser.Func_bodyContext)
            else:
                return self.getTypedRuleContext(graamPROBAParser.Func_bodyContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(graamPROBAParser.ELIF)
            else:
                return self.getToken(graamPROBAParser.ELIF, i)

        def ELSE(self):
            return self.getToken(graamPROBAParser.ELSE, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_if_stmt

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

        localctx = graamPROBAParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(graamPROBAParser.IF)
            self.state = 188
            self.conditionalOperation(0)
            self.state = 189
            self.match(graamPROBAParser.COLON)
            self.state = 190
            self.match(graamPROBAParser.WS)
            self.state = 191
            self.func_body()
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 192
                    self.match(graamPROBAParser.ELIF)
                    self.state = 193
                    self.conditionalOperation(0)
                    self.state = 194
                    self.match(graamPROBAParser.COLON)
                    self.state = 195
                    self.match(graamPROBAParser.WS)
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
                self.match(graamPROBAParser.ELSE)
                self.state = 204
                self.conditionalOperation(0)
                self.state = 205
                self.match(graamPROBAParser.COLON)
                self.state = 206
                self.match(graamPROBAParser.WS)
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
            return self.getToken(graamPROBAParser.WHILE, 0)

        def LPAR(self):
            return self.getToken(graamPROBAParser.LPAR, 0)

        def conditionalOperation(self):
            return self.getTypedRuleContext(graamPROBAParser.ConditionalOperationContext,0)


        def RPAR(self):
            return self.getToken(graamPROBAParser.RPAR, 0)

        def COLON(self):
            return self.getToken(graamPROBAParser.COLON, 0)

        def WS(self):
            return self.getToken(graamPROBAParser.WS, 0)

        def loop_stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.Loop_stmtContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_while_stmt

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

        localctx = graamPROBAParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(graamPROBAParser.WHILE)
            self.state = 212
            self.match(graamPROBAParser.LPAR)
            self.state = 213
            self.conditionalOperation(0)
            self.state = 214
            self.match(graamPROBAParser.RPAR)
            self.state = 215
            self.match(graamPROBAParser.COLON)
            self.state = 216
            self.match(graamPROBAParser.WS)
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
            return self.getToken(graamPROBAParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(graamPROBAParser.IDENTIFIER, 0)

        def IN(self):
            return self.getToken(graamPROBAParser.IN, 0)

        def RANGE(self):
            return self.getToken(graamPROBAParser.RANGE, 0)

        def LPAR(self):
            return self.getToken(graamPROBAParser.LPAR, 0)

        def NUMBER(self):
            return self.getToken(graamPROBAParser.NUMBER, 0)

        def RPAR(self):
            return self.getToken(graamPROBAParser.RPAR, 0)

        def COLON(self):
            return self.getToken(graamPROBAParser.COLON, 0)

        def WS(self):
            return self.getToken(graamPROBAParser.WS, 0)

        def loop_stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.Loop_stmtContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_for_stmt

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

        localctx = graamPROBAParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(graamPROBAParser.FOR)
            self.state = 220
            self.match(graamPROBAParser.IDENTIFIER)
            self.state = 221
            self.match(graamPROBAParser.IN)
            self.state = 222
            self.match(graamPROBAParser.RANGE)
            self.state = 223
            self.match(graamPROBAParser.LPAR)
            self.state = 224
            self.match(graamPROBAParser.NUMBER)
            self.state = 225
            self.match(graamPROBAParser.RPAR)
            self.state = 226
            self.match(graamPROBAParser.COLON)
            self.state = 227
            self.match(graamPROBAParser.WS)
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
            return self.getToken(graamPROBAParser.DEF, 0)

        def IDENTIFIER(self):
            return self.getToken(graamPROBAParser.IDENTIFIER, 0)

        def LPAR(self):
            return self.getToken(graamPROBAParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(graamPROBAParser.RPAR, 0)

        def COLON(self):
            return self.getToken(graamPROBAParser.COLON, 0)

        def func_body(self):
            return self.getTypedRuleContext(graamPROBAParser.Func_bodyContext,0)


        def parameters(self):
            return self.getTypedRuleContext(graamPROBAParser.ParametersContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_function_def

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

        localctx = graamPROBAParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(graamPROBAParser.DEF)
            self.state = 231
            self.match(graamPROBAParser.IDENTIFIER)
            self.state = 232
            self.match(graamPROBAParser.LPAR)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 233
                self.parameters()


            self.state = 236
            self.match(graamPROBAParser.RPAR)
            self.state = 237
            self.match(graamPROBAParser.COLON)
            self.state = 238
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
                return self.getTypedRuleContexts(graamPROBAParser.Typed_parContext)
            else:
                return self.getTypedRuleContext(graamPROBAParser.Typed_parContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(graamPROBAParser.COMMA)
            else:
                return self.getToken(graamPROBAParser.COMMA, i)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_parameters

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

        localctx = graamPROBAParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.typed_par()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 241
                self.match(graamPROBAParser.COMMA)
                self.state = 242
                self.typed_par()
                self.state = 247
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
            return self.getToken(graamPROBAParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_typed_par

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

        localctx = graamPROBAParser.Typed_parContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typed_par)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(graamPROBAParser.IDENTIFIER)
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
            return self.getTypedRuleContext(graamPROBAParser.StmtContext,0)


        def flow_stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.Flow_stmtContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_loop_stmt

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

        localctx = graamPROBAParser.Loop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_loop_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 5, 17, 29, 30, 31, 34, 38, 44, 47, 52, 58, 61]:
                self.state = 250
                self.stmt()
                pass
            elif token in [41, 42]:
                self.state = 251
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
            return self.getTypedRuleContext(graamPROBAParser.Loop_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(graamPROBAParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_func_body

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

        localctx = graamPROBAParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 5, 17, 29, 30, 31, 34, 38, 41, 42, 44, 47, 52, 58, 61]:
                self.state = 254
                self.loop_stmt()
                pass
            elif token in [43]:
                self.state = 255
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
            return self.getToken(graamPROBAParser.WS, 0)

        def BREAK(self):
            return self.getToken(graamPROBAParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(graamPROBAParser.CONTINUE, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_flow_stmt

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

        localctx = graamPROBAParser.Flow_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_flow_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            _la = self._input.LA(1)
            if not(_la==41 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 259
            self.match(graamPROBAParser.WS)
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
            return self.getToken(graamPROBAParser.RETURN, 0)

        def WS(self):
            return self.getToken(graamPROBAParser.WS, 0)

        def explist(self):
            return self.getTypedRuleContext(graamPROBAParser.ExplistContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_return_stmt

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

        localctx = graamPROBAParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(graamPROBAParser.RETURN)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2305843010287566906) != 0):
                self.state = 262
                self.explist()


            self.state = 265
            self.match(graamPROBAParser.WS)
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
                return self.getTypedRuleContexts(graamPROBAParser.ExpContext)
            else:
                return self.getTypedRuleContext(graamPROBAParser.ExpContext,i)


        def COMMA(self):
            return self.getToken(graamPROBAParser.COMMA, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_explist

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

        localctx = graamPROBAParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_explist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.exp()

            self.state = 268
            self.match(graamPROBAParser.COMMA)
            self.state = 269
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
            return self.getTypedRuleContext(graamPROBAParser.ValueContext,0)


        def arithmeticOperation(self):
            return self.getTypedRuleContext(graamPROBAParser.ArithmeticOperationContext,0)


        def conditionalOperation(self):
            return self.getTypedRuleContext(graamPROBAParser.ConditionalOperationContext,0)


        def printOperation(self):
            return self.getTypedRuleContext(graamPROBAParser.PrintOperationContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_exp

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

        localctx = graamPROBAParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp)
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.arithmeticOperation(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.conditionalOperation(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 274
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
            return self.getTypedRuleContext(graamPROBAParser.TermContext,0)


        def arithmeticOperation(self):
            return self.getTypedRuleContext(graamPROBAParser.ArithmeticOperationContext,0)


        def PLUS(self):
            return self.getToken(graamPROBAParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(graamPROBAParser.MINUS, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_arithmeticOperation

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
        localctx = graamPROBAParser.ArithmeticOperationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_arithmeticOperation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 288
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 286
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = graamPROBAParser.ArithmeticOperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticOperation)
                        self.state = 280
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 281
                        self.match(graamPROBAParser.PLUS)
                        self.state = 282
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = graamPROBAParser.ArithmeticOperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmeticOperation)
                        self.state = 283
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 284
                        self.match(graamPROBAParser.MINUS)
                        self.state = 285
                        self.term(0)
                        pass

             
                self.state = 290
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
            return self.getTypedRuleContext(graamPROBAParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(graamPROBAParser.TermContext,0)


        def MULTIPLY(self):
            return self.getToken(graamPROBAParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(graamPROBAParser.DIVIDE, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_term

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
        localctx = graamPROBAParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 300
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = graamPROBAParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 294
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 295
                        self.match(graamPROBAParser.MULTIPLY)
                        self.state = 296
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = graamPROBAParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 297
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 298
                        self.match(graamPROBAParser.DIVIDE)
                        self.state = 299
                        self.factor()
                        pass

             
                self.state = 304
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
            return self.getTypedRuleContext(graamPROBAParser.ValueContext,0)


        def exp(self):
            return self.getTypedRuleContext(graamPROBAParser.ExpContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_factor

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

        localctx = graamPROBAParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_factor)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 61]:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.value()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.match(graamPROBAParser.T__0)
                self.state = 307
                self.exp()
                self.state = 308
                self.match(graamPROBAParser.T__1)
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
            return self.getToken(graamPROBAParser.STRING, 0)

        def COMMA(self):
            return self.getToken(graamPROBAParser.COMMA, 0)

        def exp(self):
            return self.getTypedRuleContext(graamPROBAParser.ExpContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_printOperation

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

        localctx = graamPROBAParser.PrintOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_printOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(graamPROBAParser.STRING)
            self.state = 313
            self.match(graamPROBAParser.COMMA)
            self.state = 314
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
            return self.getTypedRuleContext(graamPROBAParser.LogicalTermContext,0)


        def conditionalOperation(self):
            return self.getTypedRuleContext(graamPROBAParser.ConditionalOperationContext,0)


        def CONDITION_OP(self):
            return self.getToken(graamPROBAParser.CONDITION_OP, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_conditionalOperation

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
        localctx = graamPROBAParser.ConditionalOperationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_conditionalOperation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.logicalTerm(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = graamPROBAParser.ConditionalOperationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conditionalOperation)
                    self.state = 319
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 320
                    self.match(graamPROBAParser.CONDITION_OP)
                    self.state = 321
                    self.logicalTerm(0) 
                self.state = 326
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
            return self.getTypedRuleContext(graamPROBAParser.LogicalFactorContext,0)


        def logicalTerm(self):
            return self.getTypedRuleContext(graamPROBAParser.LogicalTermContext,0)


        def OR(self):
            return self.getToken(graamPROBAParser.OR, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_logicalTerm

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
        localctx = graamPROBAParser.LogicalTermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_logicalTerm, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.logicalFactor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = graamPROBAParser.LogicalTermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalTerm)
                    self.state = 330
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 331
                    self.match(graamPROBAParser.OR)
                    self.state = 332
                    self.logicalFactor(0) 
                self.state = 337
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
            return self.getTypedRuleContext(graamPROBAParser.LogicalPrimaryContext,0)


        def logicalFactor(self):
            return self.getTypedRuleContext(graamPROBAParser.LogicalFactorContext,0)


        def AND(self):
            return self.getToken(graamPROBAParser.AND, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_logicalFactor

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
        localctx = graamPROBAParser.LogicalFactorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_logicalFactor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.logicalPrimary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = graamPROBAParser.LogicalFactorContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalFactor)
                    self.state = 341
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 342
                    self.match(graamPROBAParser.AND)
                    self.state = 343
                    self.logicalPrimary() 
                self.state = 348
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
            return self.getTypedRuleContext(graamPROBAParser.ValueContext,0)


        def LPAR(self):
            return self.getToken(graamPROBAParser.LPAR, 0)

        def conditionalOperation(self):
            return self.getTypedRuleContext(graamPROBAParser.ConditionalOperationContext,0)


        def RPAR(self):
            return self.getToken(graamPROBAParser.RPAR, 0)

        def NOT(self):
            return self.getToken(graamPROBAParser.NOT, 0)

        def logicalPrimary(self):
            return self.getTypedRuleContext(graamPROBAParser.LogicalPrimaryContext,0)


        def getRuleIndex(self):
            return graamPROBAParser.RULE_logicalPrimary

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

        localctx = graamPROBAParser.LogicalPrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_logicalPrimary)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 61]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.value()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.match(graamPROBAParser.LPAR)
                self.state = 351
                self.conditionalOperation(0)
                self.state = 352
                self.match(graamPROBAParser.RPAR)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                self.match(graamPROBAParser.NOT)
                self.state = 355
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
            return self.getToken(graamPROBAParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(graamPROBAParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(graamPROBAParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(graamPROBAParser.STRING, 0)

        def getRuleIndex(self):
            return graamPROBAParser.RULE_value

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

        localctx = graamPROBAParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2305843009213694008) != 0)):
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
         




