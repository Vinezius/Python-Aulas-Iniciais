# biblioteca que permite trabalhar com o dia
from datetime import date, time, datetime, timedelta

def utilizandoDate():
    dataAtual = date.today() #Classe que me permite salvar o dia atual
    print(dataAtual.strftime("%d/%m/%Y")) # strftime permite alterar como será mostrado o dia; definido como dia mês e ano pro mim

    print(dataAtual.strftime("%A, dia %d/%m/%Y"))

def utilizandoTime():
    horaAtual = time(hour = 20, minute = 53, second =30)
    print(horaAtual)


def utilizandoDateTime():
    dataAtual = datetime.now()
    print(dataAtual.strftime("%d/%m/%Y %H:%M:%S"))  # printa o dia e o horario
    # printa nessa ordem : dia da semana, mês, dia do mês horário e ano
    print(dataAtual.strftime("%c"))
    # Printa só o ano. Pode ser tambem day, minute, date, etc
    print(dataAtual.year)

    # Configurando uma tupla para traduzir os dias da semana e outra para traduzir o mês
    tuplaDia = ('Segunda', "Terça", "Quarta",
                "Quinta", "Sexta", "Sábado", "Domingo")
    tuplaMes = ("Janeiro", "Feveiro", "Março", "Abril", "Maio", "Junho",
                "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
    
    # utilizando a tupla para printar o dia da semana em portugues
    print(tuplaDia[dataAtual.weekday()])
    print(tuplaMes[dataAtual.month])

    # Convertendo uma string para um datetime
    dataString = "01/01/2021"
    dataConvertida = datetime.strptime(dataString, ("%d/%m/%Y"))

    # Utilizando o timedelta para realizar soma e subtração de datas
    novaData = dataConvertida - timedelta(days= 365)
    print (novaData)



if __name__ == '__main__':
    utilizandoDate()
    utilizandoTime()
    utilizandoDateTime()
