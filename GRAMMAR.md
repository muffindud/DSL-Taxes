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
    <percentage> -> <digit><digit>.<integer> % | <digit><digit> % | <digit> % | 100 % | 0 %
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

### Code example:
```
tax_bracket "moldova"
    range 0..1000 -> 0.07
    range 1001..3000 -> 0.08
    range 3001..5000 -> 0.1
    range 5001..max -> 0.12

tax_bracket "romania"
    range 0..500 -> 7 %
    range 501..1000 -> 0.09
    range 1001..max -> 11.23 %

tax_compute "Alex"
    bracket = "moldova"
    income = 1170

tax_compute "Ion"
    bracket = "moldova"
    income = 3053
    
    deductions
        donation_deduction = 150

tax_compute "Alan"
    bracket = "romania"
    income = 782

    deductions
        standart_deduction = 72
```

### Output:
```
Alex : 93.6
Ion : ...
Alan : ...
```