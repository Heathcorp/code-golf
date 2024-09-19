f(0,1,0):-!.
f(X,A,B):-Y is X-1,f(Y,B,C),A is B+C,writeln(C).
:-f(31,_,_).
