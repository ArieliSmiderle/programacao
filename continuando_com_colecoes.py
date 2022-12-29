#para juntar duas listas e tirar números repetidos
#usuarios_data_science = [15, 23, 43, 56]
#usuarios_machine_learning = [13, 23, 56, 42]
#assistiram = usuarios_data_science.copy()
#assistiram.extend(usuarios_machine_learning)
#for usuario in set(assistiram):
#    print(usuario)
 
#ou

#para juntar dois conjuntos e tirar números repetidos
#usuarios_data_science = {15, 23, 43, 56}
#usuarios_machine_learning = {13, 23, 56, 42}
#print(usuarios_data_science | usuarios_machine_learning)

#para ver quem fez os dois cursos

#usuarios_data_science = {15, 23, 43, 56}
#usuarios_machine_learning = {13, 23, 56, 42}
#print(usuarios_data_science & usuarios_machine_learning)

#para quem fez só data science

#usuarios_data_science = {15, 23, 43, 56}
#usuarios_machine_learning = {13, 23, 56, 42}
#fez_ds_as_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
#print(23 in fez_ds_as_nao_fez_ml)

#só fez um dos dois cursos

#usuarios_data_science = {15, 23, 43, 56}
#usuarios_machine_learning = {13, 23, 56, 42}
#print(usuarios_data_science ^ usuarios_machine_learning)

#modificar o conjunto em tempo real

#usuarios = {1, 5, 76, 34, 52, 13, 17}
#usuarios.add(765)
#print(len(usuarios))
#usuarios = frozenset(usuarios)
#print(usuarios)

#textos

#meu_texto = "Bem vindo meu nome é guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
#print(set(meu_texto.split()))

#aparicoes = {
#    "Guilherme" : 1,
#    "cachorro" : 2,
#    "nome" : 2,
#    "vindo" : 1
#}
#aparicoes = ["palavra {}".format(chave) for chave in aparicoes.keys()]
#print(aparicoes)

from collections import Counter
meu_texto = "Bem vindo meu nome é guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
aparicoes = Counter(meu_texto.split())
print(aparicoes)

#from collections import defaultdict
#class Conta:
#    def __init__(self):
#        print("criando uma conta")
#contas = defaultdict(Conta)
#print(contas[15])
#print(contas[17])