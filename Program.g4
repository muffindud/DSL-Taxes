grammar Program;


program:
    tax_brackets+ tax_computes+;

tax_brackets:
    'tax_bracket' SPACE TEXT NEWLINE+ ranges+;

ranges:
    INDENT 'range' SPACE REAL '..' (REAL | 'max') SPACE? '->' SPACE? (REAL | PERCENT) NEWLINE+;

tax_computes:
    'tax_compute' SPACE TEXT NEWLINE+
    INDENT 'bracket' SPACE? '=' SPACE? TEXT NEWLINE+
    INDENT 'income' SPACE? '=' SPACE? REAL NEWLINE*
    deductions?;

deductions:
    NEWLINE+ INDENT 'deductions' NEWLINE+ (
        donation_deductions |
        standart_deductions |
        donation_deductions standart_deductions |
        standart_deductions donation_deductions);

donation_deductions:
    DINDENT 'donations' SPACE? '=' SPACE? REAL NEWLINE?;

standart_deductions:
    DINDENT 'standart' SPACE? '=' SPACE? REAL NEWLINE?;

DINDENT: '        ';
INDENT: '    ';
SPACE: [ ]+;
TEXT: '"' ([a-zA-Z] | [ ] | [0-9] | ':' | '+' | '-' | '=')+ '"';
REAL: [0-9]+'.'[0-9]+ | [0-9]+;
PERCENT: ([0-9] | [0-9][0-9] | [0-9][0-9].[0-9]+ | '100') SPACE '%';
NEWLINE: SPACE? ('\r' '\n' | '\n' | '\r')+;
