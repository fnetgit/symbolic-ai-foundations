% Implemente um programa em Prolog (base de
% conhecimento e regras) para determinar se uma pessoa
% é irmã de outra, sabendo o seguinte:
% uma pessoa X é irmã de uma pessoa Y se X é mulher e X
% e Y possuem os mesmos pais

mulher(ana).
mulher(maria).
mulher(joana).
mulher(isis).
mulher(bia).
mulher(lia).

homem(joao).
homem(gabriel).
homem(luca).

pais(joao, ana, maria).
pais(joao, ana, isis).
pais(gabriel, maria, bia).
pais(joao, joana, lia).
pais(joao, joana, luca).

irma(X, Y) :-
    mulher(X),
    pais(P, M, X),
    pais(P, M, Y),
    X \= Y.