def contador_letras(lista): return [len(x) for x in lista]


lista_Animais = ["Cachorro", "Gato", "Gorila"]
print(contador_letras(lista_Animais))


def soma(a, b): return a + b
def subtracao(c, d): return c - d


print(soma(10, 30))
print(subtracao(5, 3))


calculadora = {
    "soma": lambda a, b: a + b,
    "subtracao": lambda a, b: a - b,
    "divisao": lambda a, b: a / b,
    "multiplicacao": lambda a, b: a * b
}

# Ler: "soma recebe DA calculadora o que está em 'soma' " OU soma = lambda a,b : a + b
soma = calculadora["soma"]
subtracao = calculadora["subtracao"]
divisao = calculadora["divisao"]
multiplicacao = calculadora["multiplicacao"]

print(("A soma é {}" .format(soma(10, 3))))
print(("A subtracao é {}" .format(subtracao(10, 3))))
print(("A divisao é {}" .format(divisao(10, 3))))
print(("A multiplicação é {}" .format(multiplicacao(10, 3))))