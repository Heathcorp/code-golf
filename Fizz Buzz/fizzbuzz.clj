(loop[i 1 j 99](println(str(if(=(mod i 3)0)"Fizz""")(if(=(mod i 5)0)"Buzz""")(if(>(*(mod i 3)(mod i 5))0)i"")))(if(> j 0)(recur(inc i)(dec j))0))
