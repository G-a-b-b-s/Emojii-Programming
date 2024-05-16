grammar Grammar; 

start : stmt+EOF;


IDENTIFIER  :'<input latin uppercase>' [ A - Za - z]+[A - za - z0 - 9 ] * '<input latin uppercase>';
NUMBER : '<input latin uppercase>'[0-9]+('.'[0-9]+)?'<input latin uppercase>';
STRING : '<writing hand>' ~('\n')* '<writing hand>';
WS: [ \t\r\n]+ -> skip;
PLUS        : '<plus>';
MINUS       : '<minus>';
MULTIPLY    : '<multiply>';
DIVIDE      : '<divide>';
EQUAL       : '<heavy equals sign>';

MOD         : '%';
LPAR        : '<leftwards pushing hand>';
RPAR        : '<rightwards pushing hand>';
LBRACE      : '{';
RBRACE      : '}';
LSQB        : '<leftwards hand>';
RSQB        : '<tightwards hand>';
COMMA       : '<paperclip>';
COLON       : '<linked paperclips>';
SEMI        : '<pushpin>';
QUOTE       : '<clapper board>';

OR          : '<woman detective>';
AND         : '<women holding hands>';

COMMENT     : '<cloud>' .*? '<cloud>' -> skip;
PRINT       : '<printer>';
NOT         : '<red exclamation mark>';
IF          : '<red question mark>';
ELSE        : '<red exclamation mark> <red exclamation mark>';
ELIF        : '<red question mark> <red exclamation mark>';
FOR         : '<wrapped gift>';
IN          : '<open mailbox with lowered flag>';
RANGE       : '<snow-capped mountain>';
ENUMERATE   : '<radio>';
WHILE       : '<tornado>';
SWITCH      : '<clipboard>';
CASE        : '<check mark button>';
BREAK       : '<vertical traffic light>';
CONTINUE    : '<person getting massage>';
RETURN      : '<boomerang>';
DEF         : '<light bulb>';
TRUE        : '<thumbs up>';
FALSE       : '<thumbs down>';
TRY         : '<crystal ball>';
CATCH       : '<fishing pole>';
EXCEPT      : 'EXCEPT';
FINALLY     : '<hourglass done>';
RAISE       : '<sunrise>';
CONST       : '<skull>';
IMPORT      : '<globe showing Americas>';
FROM        : '<articulated lorry>';
LAMBDA      : '<rainbow>';
NONE        : '<wastebasket>';
ECOMPLEMENT : '<wavy dash>';
DECL        : 'decl';
TYPE : 'int' | 'string' | 'char' | 'bool' | 'float' | 'void'; 
ARROW       : '->';
AS          : 'as';
BOOLEAN: TRUE | FALSE;

CONDITION_OP : '<dragon>' | '<leopard>' | '<mouse>' | '<chipmunk>' | '==' | '!=';


// Statements within line
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
print_stmt: PRINT LPAR exp RPAR;
multiple_assignment_stmt: assignment_stmt (COMMA assignment_stmt)?;
raise_stmt: RAISE exception_expr;

exception_expr: exception_name | exception_name exp;
exception_name: IDENTIFIER;
// Compound statements
compound_stmt: if_stmt | while_stmt | for_stmt | function_def;
if_stmt: IF conditionalOperation COLON WS func_body (ELIF conditionalOperation COLON WS func_body)* (ELSE conditionalOperation COLON WS func_body)?;
while_stmt: WHILE LPAR conditionalOperation RPAR COLON WS loop_stmt;
for_stmt: FOR IDENTIFIER IN RANGE LPAR NUMBER RPAR COLON WS loop_stmt;
function_def: DEF IDENTIFIER LPAR parameters? RPAR COLON WS func_body;

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
printOperation: STRING COMMA exp ;
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
