
class Calculadora():

    # Faz com que na hora de instanciar uma classe seja obrigatória a passagem pelo método __init__
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def Soma(self):  # Em python, os pârametros são chamados definições, por isso Def (Caso tenha retorno se transforma em Função normalmente)
        return self.a + self.b

    def subtracao(self):  # Não existe necessidade de passar valores por parâmetro para todos as definições. Utilizando o self após a instanciação é suficiente
        return self.a - self.b

    def divisao(self):
        return self.a / self.b

    def multiplicacao(self):
        return self.a * self.b


if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.Soma())
    print(calculadora.subtracao())
    print(calculadora.divisao())
    print(calculadora.multiplicacao())
