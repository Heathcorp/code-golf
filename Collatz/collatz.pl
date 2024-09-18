c(N,D):-N=1,writeln(D);n(N,M),T is D+1,c(M,T).
n(N,M):-M is N/2,integer(M),!;M is N*3+1.
:-between(1,1000,G),\+c(G,0).
