
class Calculadora():

    # Quando os objetos não serão iniciados na classe não existe necessidade de um método init

    def __init__(self):
        #o init não pode ficar vazio, portanto usa-se o pass que não faz nada
        pass

    def Soma(self, a, b):  # Em python, os pârametros são chamados definições, por isso Def (Caso tenha retorno se transforma em Função normalmente)
        return a + b

    def subtracao(self, a, b):  # Não existe necessidade de passar valores por parâmetro para todos as definições. Utilizando o self após a instanciação é suficiente
        return a - b

    def divisao(self, a, b):
        return a/b

    def multiplicacao(self, a, b):
        return a * b


calculadora = Calculadora()
print(calculadora.Soma(5, 2))
print(calculadora.subtracao(3, 4))
print(calculadora.divisao(8, 7))
print(calculadora.multiplicacao(10, 2))
