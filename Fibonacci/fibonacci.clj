(loop[a 1 b 0](println b)(if(< a 1e6)(recur(+ a b)a)a))
