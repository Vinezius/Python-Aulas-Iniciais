
conjunto = {1, 2, 3, 4}  # Conjuntos são definidos pelas chaves.
conjunto2 = {5, 6, 7, 8, 9, 10}
conjuntoA = {1, 2, 3}
conjuntoB = {1, 2, 3, 4, 5}

conjunto.add(5)  # adiciona um objeto ao conjunto
conjunto.discard(2)  # remove um objeto do conjunto

conjuntoUnido = conjunto.union(conjunto2)  # union junta dois conjuntos
print("União: {}" .format(conjuntoUnido))

# Intercecção entre os conjuntos(o que tem de igual nos dois)
conjuntoInterseccao = conjunto.intersection(conjunto2)
print("Intercecção: {}" .format(conjuntoInterseccao))

# Mostra os numeros que SÓ estão presentes no conjunto que está chamando o método
conjuntoDiferenca = conjunto.difference(conjunto2)
print("Diferenca: {}" .format(conjuntoDiferenca))

# Mostra todos os números dos conjunto exceto os repetidos
conjuntoDifSimetrica = conjunto.symmetric_difference(conjunto2)
print("Difsimetrica: {}" .format(conjuntoDifSimetrica))

# Retorna True(boolean) caso o conjunto que esteja chamando o método seja subconjunto(conjunto dentro de outro)
conjunto_subset = conjunto.issubset(conjuntoB)
print("Subset: {}" .format(conjunto_subset))

# Retorna True caso seja o superconjunto.
conjunto_superSet = conjuntoB.issuperset(conjunto)
print("SuperSet: {}" .format(conjunto_superSet))

Lista = ["cachorro", "vaca", "ovelha"]
# Passa as informações de uma lista ou tupla para um conjunto
conjuntoAnimais = set(Lista)
print("Animais: {}" .format(conjuntoAnimais))
