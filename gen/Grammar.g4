grammar Grammar; 

start : stmt+ EOF;

IDENTIFIER  : [A-Za-z]+[A-Za-z0-9_]*;
NUMBER : [0-9]+('.'[0-9]+)?;
STRING : '"' (~["])* '"';
WS: [ \t\r\n]+ -> skip;
PLUS        : '+';
MINUS       : '-';
MULTIPLY    : '*';
DIVIDE      : '/';
EQUAL       : '=';

MOD         : '%';
LPAR        : '(';
RPAR        : ')';
LBRACE      : '{';
RBRACE      : '}';
LSQB        : '[';
RSQB        : ']';
COMMA       : ',';
COLON       : ':';
SEMI        : ';';
QUOTE       : '"';

OR          : 'or';
AND         : 'and';

COMMENT     : '/*' .*? '*/' -> skip;
PRINT       : 'print';
NOT         : 'not';
IF          : 'if';
ELSE        : 'else';
ELIF        : 'elif';
FOR         : 'for';
IN          : 'in';
RANGE       : 'range';
ENUMERATE   : 'enumerate';
WHILE       : 'while';
SWITCH      : 'switch';
CASE        : 'case';
BREAK       : 'break';
CONTINUE    : 'continue';
RETURN      : 'return';
DEF         : 'def';
TRUE        : 'true';
FALSE       : 'false';
TRY         : 'try';
EXCEPT      : 'EXCEPT';
FINALLY     : 'finally';
RAISE       : 'raise';
CONST       : 'const';
IMPORT      : 'import';
FROM        : 'from';
LAMBDA      : 'lambda';
NONE        : 'none';
ECOMPLEMENT : '~';
DECL        : 'decl';
TYPE : 'int' | 'string' | 'char' | 'bool' | 'float' | 'void'; 
ARROW       : '->';
AS          : 'as';
BOOLEAN: TRUE | FALSE;

CONDITION_OP : '>' | '>=' | '<' | '<=' | '==' | '!=';


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
