class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 5

    def Power(self):
        if self.ligada == True:
            self.ligada = False
            print("A tv tá desligada")
        else:
            self.ligada = True
            print("A tv tá ligada")

    def aumentaCanal(self):
        if self.ligada:
            self.canal += 1
            print("Aumentando o canal")

    def diminuiCanal(self):
        if self.ligada:
            self.canal -= 1
            print("Diminuindo o canal")


if __name__ == "__main__": #Faz com que o arquivo so execute caso quem esteja chamando seja o Main. Aumenta a segurança.
    televisao = Televisao()
    print(televisao.ligada)
    televisao.Power()
    televisao.Power()

    print(televisao.canal)
    televisao.aumentaCanal()
    televisao.aumentaCanal()
    televisao.aumentaCanal()
    print("A tv está no canal {}".format(televisao.canal))

    televisao.diminuiCanal()
    televisao.diminuiCanal()
    print("A tv está no canal {}".format(televisao.canal))
