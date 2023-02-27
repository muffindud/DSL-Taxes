V_n = {
&nbsp;&nbsp;&nbsp;&nbsp;\<program\>, \<newtaxbracket\>, \<newrange\>, \<text\>, \<character\>, \<real\>, \<integer\>, \<rate\>, \<percentage\>, \<letter\>, \<symbol\>, \<digit\>, \<newline\>
}

V_t = {
&nbsp;&nbsp;&nbsp;&nbsp;tax_bracket,&nbsp;&nbsp;&nbsp;&nbsp;range, tax_compute, amount, a..z, A..Z, 0..9, ., -, \<, \>, =, %, ", \\, /, @, #, !, ?, +, \*, $, NEWLINE, IDENTATION
}

S = {
&nbsp;&nbsp;&nbsp;&nbsp;\<program\>
}

P = {
&nbsp;&nbsp;&nbsp;&nbsp;\<program \> -> \<newtaxbracket\>
&nbsp;&nbsp;&nbsp;&nbsp;\<newtaxbracket\> ->tax_bracket "\<text\>"NEWLINE \<newrange\> | tax_bracket  "\<text\>"\<newline\> \<newrange\>\<newbracket\>
&nbsp;&nbsp;&nbsp;&nbsp;\<newline\> -> NEWLINE | NEWLINE\<newline\> | ε
&nbsp;&nbsp;&nbsp;&nbsp;\<text\> -> \<character\> | \<character\>\<text\> | ε
&nbsp;&nbsp;&nbsp;&nbsp;\<character\> -> \<letter\> | \<symbol\> | \<digit\>
&nbsp;&nbsp;&nbsp;&nbsp;\<real\> -> \<integer\>.\<integer\> | \<integer\>
&nbsp;&nbsp;&nbsp;&nbsp;\<integer\> -> \<digit\>\<integer\> | \<digit\> 
&nbsp;&nbsp;&nbsp;&nbsp;\<.rate\> -> 0.\<integer\> | 1 | 0
&nbsp;&nbsp;&nbsp;&nbsp;\<percentage\> -> \<digit\>\<digit\>.\<integer\> % | 100 %
&nbsp;&nbsp;&nbsp;&nbsp;\<letter\> -> a | A | b | B | ... | z | Z
&nbsp;&nbsp;&nbsp;&nbsp;\<symbol\> -> . | ! | ? | , | : | ; | - | \< | \> | @ | # | % | \\ | / | + | \* | $
&nbsp;&nbsp;&nbsp;&nbsp;\<digit\> ->  0 | 1 | 2 | ... | 9  
&nbsp;&nbsp;&nbsp;&nbsp;\<newrange\> -> IDENTATION range \<real\>..\<real\>  -> \<percentage\>NEWLINE | IDENTATION range \<real\>..\<real\>  -> \<rate\>NEWLINE | IDENTATION range \<real\>..\<real\>  -> \<percentage\>NEWLINE IDENTATION\<newrange\> | IDENTATION range \<real\>..\<real\>  -> \<rate\>NEWLINE \<newline\> IDENTATION\<newrange\>
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
}