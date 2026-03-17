gostadores: dict[str, list[str]] = {
    "joao": ["jose", "ana"],
    "jose": ["pedro", "joao"],
    "ana": ["maria", "pedro", "felipe"],
    "maria": ["jose", "ana", "felipe"],
    "pedro": ["maria", "ana"],
    "felipe": ["pedro", "joao"],
}


def se_gostam(p1: str = "", p2: str = "") -> bool:
    p1 = input("Digite a pessoa 1: ").lower().strip()
    p2 = input("Digite a pessoa 2: ").lower().strip()
    return p1 in gostadores and p2 in gostadores[p1]


def gosta_de_quem(p: str = "") -> list[str] | bool:
    p = input("Diga uma pessoa pra saber de quem ela gosta: ").lower().strip()
    return p in gostadores and gostadores[p]


print(se_gostam())
print()
print(gosta_de_quem())
