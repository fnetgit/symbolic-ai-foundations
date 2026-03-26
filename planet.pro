% Dadas as distâncias do sol aos planetas do Sistema solar em milhões de milhas:
% Escreva o programa: distancia_planetas(P1, P2, D) que encontra a distância
% entre dois planetas quaisquer

distancia_sol(mercurio, 36).
distancia_sol(venus, 67).
distancia_sol(terra, 93).
distancia_sol(marte, 141).
distancia_sol(jupiter, 484).
distancia_sol(saturno, 886).
distancia_sol(urano, 1790).
distancia_sol(netuno, 2800).

distancia_planetas(P1, P2, D) :-
    distancia_sol(P1, D1),
    distancia_sol(P2, D2),
    D is abs(D1 - D2).