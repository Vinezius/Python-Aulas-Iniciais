
print("Meu primeiro Programa em Python!")

# Quando for receber um input de um usuario, é obrigatorio declarar o tipo de variavel a ser recebida
a = int(input("Entre com o valor: "))
b = int(input("Entre com o segundo valor: "))
soma = a + b
subtracao = a-b

# Mostrar qual o tipo da variável(type)
print(type(soma))

# MANEIRA NAO IDEAL: Como concatenar variaveis diferentes no mesmo print (transformando a variavel para string usando str)
print("soma: " + str(soma) + "\nsubtração: " + str(subtracao))

# MANEIRA IDEAL: Como concatenar variaveis diferentes no mesmo print (transformando a variavel usando .format(variável) Pode ser usado com varias variáveis ao mesmo tempo)
print("Soma: {}" .format(soma))

# É possível usar o format de outra forma, dando "Apelidos" as variaveis
print("Soma: {soma}. \nSubtração {sub}".format(soma=soma, sub=subtracao))


# IF, Else e Elif(else if) não utilizam chaves, no lugar utilizam dois pontos
if a > b:
    print("A é maior que B")
elif a == b:
    print("Os números são iguais")
else:
    print("B é maior que A")


# For e range
# Range seleciona os valores até o range definido. Exemplo range(100) irá pegar os números de 0 até 99. (range definido -1)
# Para definir um valor inicial utiliza-se dentro do range uma vírgula. Exemplo range(1,100) irá correr do 1 até o 99. (range definido-1)
for x in range(100):  # x é variável
    print(x)  # irá printar do 0 até o 99


# para somar +1 ao número utiliza-se +=1. (Exemplo num+=1)
# em java e em C utiliza-se o variável++. (Exemplo num++)


# While funciona basicamente igual as outras linguagens
while a <= 10:
    print("aaaaa")
    a += 1


# Listas utilizam colchetes. Exemplo lista = [1,2,3,4,5]
# É possível ter tipos de variáveis diferentes na mesma lista. Exemplo lista2 = [1,2,3,4,"cachorro"] porém não é recomendado
# Como padrão, o python também começa as contagens de listas pelo 0, logo, na Lista 2 o cachorro está na quarta posição.
    Lista = [1, 2, 3, 4, 5]

# esse método sum soma os valores presentes numa lista automáticamente
print(sum(Lista))

print(max(Lista))  # esse método max apresenta o maior valor da lista automaticamente

print(Lista * 3)  # Copia a lista N vezes na hora de printar. pode ser usado para criar uma nova lista. Exemplo novaLista = Lista*3

print(Lista[2])  # busca valor específico na lista

Lista.append(5)  # append adiciona novos registros à lista.

Lista.pop()  # Retira a o ultimo registro da lista. Pode ter uma posicição específica. Exemplo Lista.pop(1)

Lista.remove()  # Remove um registro passando parâmetro. Exemplo Listta.remove("Lobo")

print(len(Lista))  # Retorna a quantidade de elementos da lista ou tupla.

tupla_Lista = tuple(Lista)  # Converte uma lista em tupla

Lista_numerica = list(tupla_Lista)  # Converte uma tupla em lista
