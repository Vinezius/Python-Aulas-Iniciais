
Lista = [1, 3, 5, 7]
lista_Animal = ["Cachorro", "gato", "vaca", "cavalo"]
animal = input("Insira o nome de um animal: ")

lista_Animal.sort()  # Ordena a lista
Lista.sort()

# Tuplas são imutáveis, enquanto listas podem ser alteradas. Tuplas usam parenteses e listas colchetes.
tupla = (1, 10, 12, 14)

print(len(tupla))  # Retorna a quantidade de elementos da lista ou tupla.

lista_Animal.reverse()  # Ordena inversamente a lista

print(lista_Animal[2])  # buscando posição específica na lista

for x in Lista:  # correr printando as informações da lista
    print(x)
print("O valor da soma dos números da lista é:" + str(sum(Lista)))
print("O maior número da lista é: " + str(max(Lista)))


if animal in lista_Animal:  # verificando se existe um determinado valor numa lista
    print("Esse animal já está na lista")
else:
    print("Não existe esse animal na lista. Deseja adiciona-lo? S para sim N para não.: ")
    escolha = input()

if escolha == "s" or escolha == "S":
    print("O animal foi adicionado a lista.")
    lista_Animal.append(animal)
    print("Lista atualizada: " + str(lista_Animal))

else:
    print("O animal não foi adicionado à lista.")

tupla_Animal = tuple(lista_Animal)  # Converte uma lista para uma tupla
