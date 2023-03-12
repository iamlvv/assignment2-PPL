// Le Van Vy. MSSV: 2010805
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  decllist EOF ;
decllist: declaration decllist | declaration;
declaration: vardec | funcdec;
typ: atomictype | arraytype | AUTO;

// readInteger: 'readInteger' LP RP SEMICOLON;
// readFloat: 'readFloat' LP RP SEMICOLON;
// readBoolean: 'readBoolean' LP RP SEMICOLON;
// readString: 'readString' LP RP SEMICOLON;
// printInteger: 'printInteger' LP (IDENTIFIER | INTLIT) RP SEMICOLON;
// printFloat: 'printFloat' LP (IDENTIFIER | FLOATLIT) RP SEMICOLON;
// printBoolean: 'printBoolean' LP (IDENTIFIER | BOOLLIT) RP SEMICOLON;
// printString: 'printString' LP (IDENTIFIER | STRINGLIT) RP SEMICOLON;
// superexpr: 'super' LP exprlist RP SEMICOLON;
// preventDefault: 'preventDefault' LP RP SEMICOLON;

//Variable declaration:
vardec: ((idlist COLON typ) | subvardec) SEMICOLON;
subvardec: IDENTIFIER COMMA subvardec COMMA expr | expand;
expand: IDENTIFIER COLON typ ASSIGNOP expr;
idlist: IDENTIFIER COMMA idlist | IDENTIFIER;
exprlist: expr COMMA exprlist | expr | ;


//Function declaration:
funcdec: IDENTIFIER COLON FUNCTION (typ | VOID) LP parameterlist RP (INHERIT IDENTIFIER)? (blockstate | emptycurl);
emptycurl: LC RC;
parameter: (INHERIT)? (OUT)? IDENTIFIER COLON typ;
parameterlist: parameter (COMMA) parameterlist | parameter | ;

blockstate: LC (blockstatemin) RC;
blockstatemin: (statement | vardec) blockstatemin | ;
//Statement:
statement:
	assignstate
	| ifstate
	| whilestate
	| forstate
	| breakstate
	| continuestate
	| returnstate
	| funcall
	| blockstate
	| dowhilestate
	;

lhs: scalarvar | exprindex;

scalarvar: IDENTIFIER;

assignstate: lhs ASSIGNOP expr SEMICOLON;
ifstate: IF LP expr RP statement (ELSE statement)?;
whilestate: WHILE LP expr RP statement;
dowhilestate: DO blockstate WHILE LP expr RP SEMICOLON;
forstate: FOR LP lhs ASSIGNOP expr COMMA expr COMMA expr RP statement;
breakstate: BREAK SEMICOLON;
continuestate: CONTINUE SEMICOLON;
returnstate: RETURN (expr | ) SEMICOLON;


funcall: (IDENTIFIER)  LP exprlist RP SEMICOLON;


SL_COMMENT: '//' ((~'\n')* ('\n' | EOF)) -> skip ;

ML_COMMENT: '/*' .*? '*/' -> skip ;

arraytype: ARRAY LS dimensions RS OF atomictype;

dimensions: INTLIT COMMA dimensions | INTLIT;

atomictype: INTEGER | BOOLEAN | FLOAT | STRING;

literal: INTLIT | BOOLLIT | STRINGLIT | FLOATLIT | arraylit;

//Expressions:

expr: expr1 (STRINGOP) expr1 | expr1;
expr1: expr2 (GTOP | LTOP | GTEOP | LTEOP | EQOP | NEOP) expr2 | expr2;
expr2: expr2 (ANDOP | OROP) expr3 | expr3;
expr3: expr3 (ADDOP | SUBOP) expr4 | expr4;
expr4: expr4 (MULOP | DIVOP | MODOP) expr5 | expr5;
expr5: (NOTOP) expr5 | expr6;
expr6: (SUBOP) expr6 | expr7;
expr7: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT 
| IDENTIFIER | exprindex | (IDENTIFIER LP exprlist RP) | (LP expr RP) | arraylit;
exprindex: IDENTIFIER LS exprlist RS;


//Special functions


//Alphabet characters:
fragment A: ('a' | 'A');

fragment B: ('b' | 'B');

fragment C: ('c' | 'C');

fragment D: ('d' | 'D');

fragment E: ('e' | 'E');

fragment F: ('f' | 'F');

fragment G: ('g' | 'G');

fragment H: ('h' | 'H');

fragment I: ('i' | 'I');

fragment J: ('j' | 'J');

fragment K: ('k' | 'K');

fragment L: ('l' | 'L');

fragment M: ('m' | 'M');

fragment N: ('n' | 'N');

fragment O: ('o' | 'O');

fragment P: ('p' | 'P');

fragment Q: ('q' | 'Q');

fragment R: ('r' | 'R');

fragment S: ('s' | 'S');

fragment T: ('t' | 'T');

fragment U: ('u' | 'U');

fragment V: ('v' | 'V');

fragment W: ('w' | 'W');

fragment X: ('x' | 'X');

fragment Y: ('y' | 'Y');

fragment Z: ('z' | 'Z');



//Operators
ASSIGNOP: '=';
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
EQOP: '==';
NEOP: '!=';
GTOP: '>';
LTOP: '<';
GTEOP: '>=';
LTEOP: '<=';
ANDOP: '&&';
OROP: '||';
STRINGOP: '::';
NOTOP: '!';

//Separators:
LP: '(';
RP: ')';
LC: '{';
RC: '}';
LS: '[';
RS: ']';
SEMICOLON: ';';
COMMA: ',';
DOT: '.';
COLON: ':';


//Identifiers:


//Literals:
INTLIT: [0] | [1-9] [0-9]* ([_] [0-9]+)* {self.text = self.text.replace("_", "")};
BOOLLIT: 'true' | 'false';
FLOATLIT: INTLIT ([.] [0-9]*)? ([eE]('+'|'-')? [0-9]+)? {self.text = self.text.replace("_", "")} | ([.] [0-9]* [eE] [-+]? [0-9]+);
//FLOATLIT: [0-9]+[.]?[0-9]*[eE]?('+' | '-')?[.]?[0-9]+ ;
//STRINGLIT: '"' (~["] | '""')* '"' {self.text = self.text.replace(""", "\"")};
// STRINGLIT
//    : '"' (ESC | SAFECODEPOINT)* '"' {self.text = self.text[1:-1]}
//    ;
STRINGLIT
 : '"' ( '\\' [btnfr"'\\] | ~[\r\n\\"] )* '"' {self.text = self.text[1:-1]}
 ;
fragment ESC
   : '\\' (["\\/bfnrt])
   ;

fragment SAFECODEPOINT
   : ~ ["\\\u0000-\u001F]
   ;
   


//ARRAYLIT: [{] INTLIT ([,] INTLIT)* [}] | [{] FLOATLIT ([,] FLOATLIT)* [}] | [{] BOOLLIT ([,] BOOLLIT)* [}] | [{] STRINGLIT ([,] STRINGLIT)* [}] | [{] [}];
arraylit: '{' (exprlist | emptycurl) '}';
//BOOLEAN_TYPE: ;
//Keywords:
AUTO: A U T O;
BREAK: B R E A K;
BOOLEAN: B O O L E A N;
CONTINUE: C O N T I N U E;
ELSE: E L S E;
FLOAT: F L O A T;
FOR: F O R;
FUNCTION: F U N C T I O N;
IF: I F;
INHERIT: I N H E R I T;
INTEGER: I N T E G E R;
OUT: O U T;
RETURN: R E T U R N;
STRING: S T R I N G;
VOID: V O I D;
WHILE: W H I L E;
TRUE: T R U E;
FALSE: F A L S E;
DO: D O;
OF: O F;
ARRAY: A R R A Y;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
WS : [ \t\r\b\f\n]+ -> skip ; // skip spaces, tabs, newlines

fragment STRINGCHAR: ~["\\\n\r] | EscapeSequence;

fragment EscapeSequence: '\\' [btnfr"'\\];


// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;
UNCLOSE_STRING:
	'"' STRINGCHAR* {
	raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE:
	'"' STRINGCHAR* '\\' ~[btnfr"'\\] {
	raise IllegalEscape(self.text[1:])
};
ERROR_CHAR: . {raise ErrorToken(self.text)};
