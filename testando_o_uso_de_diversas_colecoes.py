from collections import Counter
texto1 = """Imaginando uma solução com lazy evaluation
Por enquanto, lemos nosso arquivo de registro linha por linha e armazenamos as linhas em uma lista. Estamos, então, iterando sobre nosso arquivo, isto é, repetindo o mesmo procedimento sobre ele para se obter cada linha.

Conseguimos fazer isso porque nosso arquivo aberto no Python é um iterável, um tipo de objeto que possibilita a ação de repetição sobre seus elementos, como listas e strings.

No Python, um objeto é considerado iterável se ele implementa o método __iter__, permitindo, por exemplo, que um loop for seja executado sobre ele.

Sabendo disso e considerando nosso problema com a memória do computador, uma solução hipotética seria ter um iterável que nos permitisse gerar uma URL por vez a cada iteração, à medida do necessário.

Esse tipo de lógica, na computação, tem nome - avaliação preguiçosa, ou, em inglês, lazy evaluation.

A avaliação preguiçosa, como já indica o nome, atrasa o processamento de uma expressão até que o resultado seja de fato necessário. Então como podemos utilizar dessa técnica no Python?
"""
texto2 = """Mapeando contatos com um dicionário
Até agora temos uma lista de contatos em que, ao menos, cada contato tem seu nome e telefone conectados. Entretanto, por enquanto, só conseguimos acessar um contato individualmente pela sua posição na lista, e não pelo seu próprio nome.

O ideal seria mapear o nome de cada contato com seu telefone, evitando outros problemas.

Por exemplo, podemos falar que o contato Yan tem o número de telefone 1234-5678. Assim, quando quisermos saber qual o n de telefone do Yan, basta ir até o seu nome. Dessa forma, não precisamos decorar qual a posição na lista que o telefone se encontra, basta sabermos seu nome de contato.

Veja que, nesse caso, estamos criando uma espécie de dicionário, parecido com os dicionários de língua portuguesa, ou inglesa. Nesses dicionários, temos uma chave que é a palavra que estamos a buscar, que no nosso caso é o nome de contato.

Quando achamos essa palavra, podemos ver o seu significado, isto é, o valor daquela palavra na língua, que no nosso caso, é o número de telefone.

Esse tipo de estrutura é muito utilizado em diversas linguagens de programação (mas normalmente tem outro nome, como array associativo. Com ela, conseguimos ter um comportamento parecido com o de dicionários.

Bem, vamos falar para o Python criar um desses dicionários para a gente. No Python, usamos chaves para construir nossos dicionários. Neste caso, falamos para o Python, que a chave 'Yan' possuí (:) o valor 1234-5678 como seu telefone:
"""
def analisa_frequencia_de_letras(texto):
    aparicoes = (Counter(texto.lower()))
    total_de_caracteres = sum(aparicoes.values())
    proporcoes= [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))
analisa_frequencia_de_letras(texto2)