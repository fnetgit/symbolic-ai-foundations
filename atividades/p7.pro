% Estenda o programa anterior para considerar o caso de
% irmãos que não sabem que têm os mesmos pais, pois
% foram separados no início de suas vidas

mulher(ana).
mulher(maria).
mulher(joana).
mulher(isis).
mulher(bia).
mulher(lia).

homem(joao).
homem(gabriel).
homem(luca).
homem(jonas).

pais(joao, ana, maria).
pais(joao, ana, isis).
pais(joao, ana, jonas).
pais(gabriel, maria, bia).
pais(joao, joana, lia).
pais(joao, joana, luca).

irmaos_sem_saber(maria, isis).

separados(X, Y) :-
    pais(P, M, X),
    pais(P, M, Y).

irma(X, Y) :-
    mulher(X),
    pais(P, M, X),
    pais(P, M, Y),
    X \= Y.