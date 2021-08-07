from Televisao import Televisao
from Calculadora import Calculadora
from Contador_Letras import contador_Letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.Power()
    print(televisao.ligada)

    calculadora = Calculadora(5,10)
    print(calculadora.Soma())
    print(calculadora.subtracao())
    lista = ["Cachorro","Gato","Gorila"]
    print(contador_Letras(lista))   