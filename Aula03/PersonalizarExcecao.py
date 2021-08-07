class Error(Exception):
    pass

# Toda classe de excecção deve terminar com error. Deve exitir uma classe error herdando de exception e a classe customizada DEVE herdar de Error(mesmo que error esteja vazia)
class InputError(Error):  
    def __init__(self, message):
        self.message = message
        #print (message)

while True:  # Executa eternamente um while
    try:
        x = int(input("Entre com um numero de 0 a 10: "))
        
        if x > 10:
            raise InputError ("O número inserido foi maior que 10") #Raise força uma exceção(Mesma coisa que chamar uma exceção)
        
        elif x <0:
            raise InputError ("O número inserido foi menor que 0")	
        
        print("Você inseriu o número: {}".format(x))
        break
    except ValueError:
        print("Valor errado, deve-se digitar apenas números")
    except InputError as ex:
        print(ex)
