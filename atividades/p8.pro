% Monte uma base de dados sobre as mulheres de uma
% família e suas relações de descendências
% - Deve-se poder consultar se 1 pessoa descende direta
% ou indiretamente de outra.

mulher(ana).
mulher(bia).
mulher(clara).
mulher(deb).

mae(ana,bia).
mae(bia,clara).
mae(clara, deb).

desc_direta(X, Y) :-
    mae(Y, X).

neta(X, Y) :-
    mae(Y, Z),
    desc_direta(X, Z).

descendente(X, Y) :-
    desc_direta(X, Y).

descendente(X, Y) :-
    mae(Y, Z),
    descendente(X, Z).

