
lista = [1, 10]
arquivo = open("teste.txt","r")

# Qual será a tentativa a ser realizada
try:
    texto = arquivo.read()
    divisao = 10/1
    numero = lista[1]
except ZeroDivisionError:  # Definindo a exceção
    print("Não é possivel realizar uma divisao por 0")
except IndexError:
    print("Erro ao acessar um indice invalado da lista")

# BaseException é a excessão base. Qualquer exceção que der irá cair nela(excluindo as que eu definir) Sempre colocar ele por último pois o codigo é lido linha a linha
except BaseException as ex:
    print("Erro desconhecido. Erro: {}".format(ex))

# O else faz com que caso não ocorra nenhum erro o código continue. Interessante colocar quando o código não pode de forma alguma continuar pós erro
else:
    print("Executa quando não ocorre exceção")

finally: #Executa caso ocorra erro ou não
    print("Sempre executa.")
    print("Fechando o arquivo")
    arquivo.close()