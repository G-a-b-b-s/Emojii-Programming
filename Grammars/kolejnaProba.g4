grammar kolejnaProba;
IDENTIFIER  : [A-Za-z]+[A-Za-z0-9_]*;
NUMBER : [0-9]+('.'[0-9]+)?;
STRING : '"' (~["])* '"';
WS: [ \t\r\n]+ -> skip;

PLUS        : ':heavy_plus_sign:';
MINUS       : ':heavy_minus_sign:';
MULTIPLY    : ':heavy_multiplication_x:';
DIVIDE      : ':heavy_division_sign:';
EQUAL       : ':heavy_equals_sign:';
GREATER     : ':dragon:';
SMALLER     : ':mouse2:';
EGREATER    : ':leopard:';
ESMALLER    : ':chipmunk:';
LPAR        : ':last_quarter_moon_with_face:';
RPAR        : ':first_quarter_moon_with_face:';
LSQB        : ':leftwards_hand:';
RSQB        : ':rightwards_hand:';
COMMA       : ':paperclip:';
COLON       : ':paperclips:';
SEMI        : ':pushpin:';
//QUOTE       : ':clapper:';

OR          : ':female_detective:';
AND         : ':two_women_holding_hands:';
PERCENT     : ':champagne:';
COMMENT     : '/*' .*? '*/' -> skip;
PRINT       : ':printer:';
NOT         : ':heavy_exclamation_mark:';
IF          : ':question:';
ELSE        : ':heavy_exclamation_mark::heavy_exclamation_mark:';
ELIF       : ':question::heavy_exclamation_mark:';
FOR         : ':gift:';
IN          : ':mailbox_with_no_mail:';
RANGE       : ':mountain_snow:';
ENUMERATE   : ':radio:';
WHILE       : ':tornado:';
SWITCH      : ':clipboard:';
CASE        : ':white_check_mark:';
BREAK       : ':vertical_traffic_light:';
CONTINUE    : ':massage:';
RETURN      : ':boomerang:';
DEF         : ':bulb:';
TRUE        : ':thumbsup:';
FALSE       : ':thumbsdown:';
TRY         : ':crystal_ball:';
EXCEPT      : ':fishing_pole_and_fish:';
FINALLY     : ':hourglass:';
RAISE       : ':sunrise:';

CONST       : ':skull:';
IMPORT      : ':earth_americas:';
FROM        : ':articulated_lorry:';
LAMBDA      : ':rainbow:';
NONE        : ':wastebasket:';
ECOMPLEMENT : '〰';
ARROW       : '->';
DECL        : 'decl';
TYPE : 'int' | 'string' | 'char' | 'bool' | 'float' | 'void';

AS          : 'as';
BOOLEAN: TRUE | FALSE;

CONDITION_OP : '>' | '>=' | '<' | '<=' | '==' | '!=';


start : stmt+EOF;
stmt: (simple_stmt | compound_stmt);
simple_stmt: assignment_stmt | import_stmt |try_stmt | declare_stmt | print_stmt | multiple_assignment_stmt | exp | exp COLON;

assignment_stmt: IDENTIFIER EQUAL exp;

declare_stmt: DECL single_declaration (COMMA single_declaration)*;

single_declaration: IDENTIFIER (EQUAL exp)?;

//declare_stmt: DECL (IDENTIFIER | multiple_assignment_stmt) (COMMA (multiple_assignment_stmt | IDENTIFIER))*;
import_stmt: IMPORT module_name;
from_stmt: FROM module_name IMPORT import_list;
module_name: IDENTIFIER (COMMA IDENTIFIER)*;
import_list: import_name (COLON import_name)*;
import_name: IDENTIFIER (AS IDENTIFIER)?;
try_stmt: TRY COLON stmt except_clause ;
except_clause: EXCEPT IDENTIFIER COLON stmt ;
print_stmt: PRINT LPAR exp RPAR WS?;
multiple_assignment_stmt: assignment_stmt (COMMA assignment_stmt)?;
raise_stmt: RAISE exception_expr;

exception_expr: exception_name | exception_name exp;
exception_name: IDENTIFIER;
// Compound statements
compound_stmt: if_stmt | while_stmt | for_stmt | function_def;
if_stmt: IF conditionalOperation COLON WS func_body (ELIF conditionalOperation COLON WS func_body)* (ELSE conditionalOperation COLON WS func_body)?;
while_stmt: WHILE LPAR conditionalOperation RPAR COLON WS loop_stmt;
for_stmt: FOR IDENTIFIER IN RANGE LPAR NUMBER RPAR COLON WS loop_stmt;
function_def: DEF IDENTIFIER LPAR parameters? RPAR COLON func_body;

parameters: typed_par (COMMA typed_par)*;
typed_par: IDENTIFIER;


// Fillings for compound statements
loop_stmt: (stmt | flow_stmt);
func_body: (loop_stmt | return_stmt);
flow_stmt: (BREAK | CONTINUE) WS;
return_stmt: RETURN (explist)? WS;
explist: exp (COMMA exp);



exp: value
      | arithmeticOperation
      | conditionalOperation
      | printOperation
      ;
arithmeticOperation: term
    | arithmeticOperation PLUS term
    | arithmeticOperation MINUS term
    ;

term: factor
    | term MULTIPLY factor
    | term DIVIDE factor
    ;

factor: value
      | '(' exp ')'
      ;
printOperation: STRING COMMA exp;
conditionalOperation: logicalTerm
            | conditionalOperation CONDITION_OP logicalTerm;

logicalTerm: logicalFactor
            | logicalTerm OR logicalFactor
            ;

logicalFactor: logicalPrimary
             | logicalFactor AND logicalPrimary
             ;

logicalPrimary: value
              | LPAR conditionalOperation RPAR
              | NOT logicalPrimary
              ;
value: IDENTIFIER
       | NUMBER
       | BOOLEAN
       | STRING
       ;