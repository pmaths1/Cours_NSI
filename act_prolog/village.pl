/* fichier village.pl   */

homme(pierre).
homme(paul).
homme(amaury).
homme(pedro).
homme(matthieu).
homme(martin).
homme(henri).
homme(alain).
homme(antoine).
homme(hector).
homme(yves).
homme(thierry).
homme(nicolas).
homme(hugues).
homme(antonin).
homme(sylvain).




femme(martine).
femme(sophie).
femme(agnes).
femme(charlotte).
femme(aida).
femme(marie).
femme(lucie).
femme(louise).
femme(manon).
femme(lea).
femme(gaelle).
femme(sylvie).
femme(henriette).
femme(muriel).


enfant(louise,paul).
enfant(louise,marie).
enfant(henri,paul).
enfant(henri,marie).
enfant(manon,paul).
enfant(manon,marie).
enfant(alain,matthieu).
enfant(alain,lucie).
enfant(antoine,matthieu).
enfant(antoine,lucie).
enfant(lea,matthieu).
enfant(lea,lucie).
enfant(hector,martin).
enfant(hector,sophie).
enfant(pierre,louise).
enfant(pierre,alain).
enfant(sylvie,manon).
enfant(sylvie,antoine).
enfant(henriette,manon).
enfant(henriette,antoine).

:- op(500,xfx,parent_de).
X parent_de Y :- enfant(Y,X).
parent(X,Y) :- enfant(Y,X).
pere(X,Y) :- enfant(Y,X),homme(Y).
mere(X,Y) :- enfant(Y,X),femme(Y).
fille(X,Y) :- enfant(Y,X), femme(Y).
garcon(X,Y) :- enfant(Y,X), homme(Y).

fraterie(X,Y) :- enfant(X,Z), enfant(Y,Z), X\==Y.

cousin(X,Y) :- parent(X,Z), parent(Y,T), fraterie(Z,T).

grand_pere(X,Y) :- pere(X,Z),parent(Z,Y).

ancetre(X,X).
ancetre(X,Y) :- parent(X,Z), ancetre(Z,Y).
