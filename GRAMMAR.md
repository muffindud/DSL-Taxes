### Iteration No. 0 of Team 17's Tax Computation DSL
```
V_n = {
    <program>, <newtaxbracket>, <newrange>, <text>, <character>, <real>, <integer>, <rate>, <percentage>, <letter>, <symbol>, <digit>, <newline>, <newtaxcompute>, <deductions>, <charity>, <standart>
}

V_t = {
    tax_bracket, range, tax_compute, amount, deductions, charity_deduction, standart_deduction, a..z, A..Z, 0..9, max, ., -, <, >, =, %, ", \, /, @, #, !, ?, +, *, $, NEWLINE, IDENTATION 
}

S = {
    <program> 
}

P = {
    <program > -> <newtaxbracket> NEWLINE <newline> <newtaxcompute>
    <newtaxbracket> -> tax_bracket "<text>" NEWLINE <newline> <newrange> | tax_bracket "<text>" NEWLINE <newline> <newrange> <newbracket>
    <newline> -> NEWLINE | NEWLINE <newline> | ε
    <text> -> <character> | <character><text> | ε
    <character> -> <letter> | <symbol> | <digit>
    <real> -> <integer>.<integer> | <integer> | max
    <integer> -> <digit><integer> | <digit>
    <rate> -> 0.<integer> | 1 | 0
    <percentage> -> <digit><digit>.<integer> % | 100 % | 0 %
    <letter> -> a | A | b | B | ... | z | Z
    <symbol> -> . | ! | ? | , | : | ; | - | < | > | @ | # | % | \ | / | + | * | $
    <digit> -> 0 | 1 | 2 | ... | 9
    <newrange> -> IDENTATION range <real>..<real> -> <percentage> NEWLINE <newline> | IDENTATION range <real>..<real> -> <rate> NEWLINE <newline> | IDENTATION range <real>..<real> -> <percentage> NEWLINE <newline> <newrange> | IDENTATION range <real>..<real> -> <rate> NEWLINE <newline> <newrange>
    <newtaxcompute> -> tax_compute "<text>" NEWLINE <newline> IDENTATION bracket = "<text>" NEWLINE <newline> IDENTATION income = <real> <newline> | tax_compute "<text>" NEWLINE <newline> IDENTATION bracket = "<text>" NEWLINE <newline> IDENTATION income = <real> NEWLINE <newline> | ε
    <deductions> -> IDENTATION deductions NEWLINE <newline> <charity> <standart> | IDENTATION deductions NEWLINE <newline> <charity> | IDENTATION deductions NEWLINE <newline> <standart> | ε
    <charity> -> INDENTATION INDENTATION charity_deduction = <float> NEWLINE <newline> 
    <standart> -> INDENTATION INDENTATION standart_deduction = <float> NEWLINE <newline>
}
```