"""
Problema inicial

Armazenam-se os fatos de que João gosta de Maria, de que João também gosta
de Ana, de que Ana gosta de Pedro, etc. Se o usuário perguntar se João gosta de
Ana, a resposta deve ser “sim”, mas a resposta para a pergunta se Ana gosta de
João deve ser “não”"""

gostadores = {
    "joao": ["jose", "ana"],
    "jose": ["pedro", "joao"],
    "ana": ["maria", "pedro", "felipe"],
    "maria": ["jose", "ana", "felipe"],
    "pedro": ["maria", "ana"],
    "felipe": ["pedro", "joao"],
}


def se_gostam(p1, p2):
    p1 = input("digite a pessoa 1: ").lower().strip()
    p2 = input("digite a pessoa 2: ").lower().strip()
    return p1 in gostadores and p2 in gostadores[p1]


# print(se_gostam("joao", "jose"))
# print(se_gostam("joao", "maria"))
print(se_gostam("", ""))


# implementar depois "de quem PESSOA gosta?"
# "fazer em cpp"
