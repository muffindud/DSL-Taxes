### Iteration No. 1.0 of Team 17's Tax Computation DSL
```
V_n = {
    <program>, <tax_bracket>, <range>, <tax_compute>, <deductions>, <donation_deductions>, <standart_deductions>, <space>, <text>, <real>, <percent>, <newline>
}

V_t = {
     tax_bracket, range, max, tax_compute, income, deductions, donations, standart, [a - z], [A - Z], [0 - 9], %, :, +, -, =, '\n', '\r'
}

S = {
    <program> 
}

P = {
    <program> --> <tax_bracket>+ <tax_compute>+
    <tax_bracket> --> tax_bracket <space> <text> <newline>+ <ranges>+
    <range> --> <space>? range <space> (<real> | max) <space>? -> <space>? (<real> | <percent>) <newline>+
    <tax_compute> --> tax_compute <space> <text> <newline>+ <space> bracket <space>? = <space>? <text> <newline>+ <space>? income <space>? = <space>? <real> <newline>* <deductions>?
    <deductions> --> <newline>+ <space>? deductions <newline>+ (<donation_deductions> | <standard_deductions> | <donation_deductions> <standard_deductions> | <standard_deductions> <donation_deductions>)
    <donation_deductions> --> <space>? donation_deduction <space>? = <space>? <real> <newline>?
    <standard_deductions> --> <space>? standard_deduction <space>? = <space>? <real> <newline>?

    <space> --> [ ]+
    <text> --> " ([a-zA-Z] | [ ] | [0-9] | : | + | - | =)+ "
    <real> --> [0-9]+ . [0-9]+ | [0-9]+
    <percent> --> ([0-9] | [0-9][0-9] | [0-9][0-9].[0-9]+ | 100) <space> %
    <newline> --> <space>? ('\r' '\n' | '\n' | '\r')+
}
```
TODO: Expresion support
### Code example:
```
tax_bracket "moldova:mdl"
    range 1000 -> 0.07
    range 3000 -> 0.08
    range 5000 -> 0.1
    range max -> 0.12

tax_bracket "romania:eur"
    range 500 -> 7 %
    range 1000 -> 0.09
    range max -> 11.2 %

tax_compute "Alex"
    bracket = "moldova:mdl"
    income = 1170

tax_compute "Ion"
    bracket = "moldova:mdl"
    income = 3053

    deductions
        donation_deduction = 150

tax_compute "Alan"
    bracket = "romania:eur"
    income = 782

    deductions
        standard_deduction = 72
```

### Output:
```
Alex : 93.6
Ion : ...
Alan : ...
```