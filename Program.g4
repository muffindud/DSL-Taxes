grammar Program;


program:
    tax_bracket+ tax_compute+;

tax_bracket:
    'tax_bracket' SPACE TEXT NEWLINE+ range+;

range:
    SPACE? 'range' SPACE (REAL | 'max') SPACE? '->' SPACE? (REAL | PERCENT) NEWLINE+;

tax_compute:
    'tax_compute' SPACE TEXT NEWLINE+
    SPACE? 'bracket' SPACE? '=' SPACE? TEXT NEWLINE+
    SPACE? 'income' SPACE? '=' SPACE? REAL NEWLINE*
    deductions?;

deductions:
    NEWLINE+ SPACE? 'deductions' NEWLINE+ (
        donation_deductions |
        standart_deductions |
        donation_deductions standart_deductions |
        standart_deductions donation_deductions);

donation_deductions:
    SPACE? 'donations' SPACE? '=' SPACE? REAL NEWLINE?;

standart_deductions:
    SPACE? 'standart' SPACE? '=' SPACE? REAL NEWLINE?;


SPACE: [ ]+;
TEXT: '"' ([a-zA-Z] | [ ] | [0-9] | ':' | '+' | '-' | '=')+ '"';
REAL: [0-9]+'.'[0-9]+ | [0-9]+;
PERCENT: ([0-9] | [0-9][0-9] | [0-9][0-9].[0-9]+ | '100') SPACE '%';
NEWLINE: SPACE? ('\r' '\n' | '\n' | '\r')+;
