idades = [15, 87, 32, 65, 56, 32, 49, 37]

idades_menor_para_maior = sorted(idades)
print(idades_menor_para_maior)

idades_maior_para_menor = sorted(idades, reverse=True)
print(idades_maior_para_menor)

#ou

idades_maior_para_menor2 = list(reversed(sorted(idades)))
print(idades_maior_para_menor2)

for indice, idade in enumerate(idades):
    print(indice, "-", idade)

#usuarios

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]
for nome, _, _ in usuarios:
    print(nome)