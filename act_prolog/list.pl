app(X,[X|_]).
app(X,[_|L]) :- app(X,L).

long([],0).
long([_|L],N) :-  long(L,Ni), N is Ni+1.

concat([],L,L).
concat([X|L1],L2,[X|L3]) :- concat(L1,L2,L3).

retourne([Z],X):- X = [Z].
retourne([U|L],X):- concat(L,U,Y), retoune(Y,X).
