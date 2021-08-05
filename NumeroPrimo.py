a = int(input("Insira um número: "))
divisao = 0

for x in range(1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        divisao += 1

if divisao == 2:
    print("Número {} é primo".format(a))
else:
    print("Número {} não é primo".format(a))
