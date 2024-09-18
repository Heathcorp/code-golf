c(1,0):-!.
c(N,D):-mod(N,2)=:=0,!,is(X,N/2),c(X,T),is(D,T+1).
c(N,D):-is(X,N*3+1),c(X,T),is(D,T+1).
c(G):-c(G,X),writeln(X).
:-foreach(between(1,1000,G),c(G)).
