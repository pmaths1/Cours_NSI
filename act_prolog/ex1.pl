somme(0,0).
somme(N,Sp) :- NN is N-1, somme(NN,S), Sp is S+N.

fact(0,1):-!.
fact(N,Pp):- NN is N-1, fact(NN,P), Pp is P*N, asserta((fact(N,Pp):-!)).


syr(U0,0,U0):-!.
syr(U0,N,R):- N>0,
        NN is N-1,
        syr(U0,NN,PP),
        PP mod 2 =:= 1,
        R is 3*PP+1.
syr(U0,N,R):- N>0,
              NN is N-1,
              syr(U0,NN,PP),
              PP mod 2 =:= 0,
              R is PP/2.


vol(1,N,X):- X is N.
vol(U0,N,X) :-  U0>1,
        U0 mod 2 =:= 1,
        U1 is 3*U0+1,
        NN is N+1,
        vol(U1,NN,X).


vol(U0,N,X) :-  U0>1,
        U0 mod 2 =:= 0,
        U1 is U0/2,
        NN is N+1,
        vol(U1,NN,X).

hauteur(1,H,X):- 1 > H, X is 1.
hauteur(1,H,X):- H > 1, X is H.

hauteur(U0,H,X) :-
        syr(U0,1,R),
        U0 > H,
        hauteur(R,U0,X).

hauteur(U0,H,X) :-
        syr(U0,1,R),
        U0 < H,
        hauteur(R,H,X).

fibo(U0,_,0,X):- X is U0.
fibo(_,U1,1,X):- X is U1.

fibo(U,V,N,X):- N>1,
              NN is N-1,
              VP is U+V,
              fibo(V,VP,NN,X).
