import shutil  # biblioteca que permite mover amigos


def escreverArquivos(texto):

    # Open é um built-in do python que cria e abre arquivos. o W permite que eu escreva no arquivo
    # Caso o arquivo já exista e seja necessário apenas atualiza-lo, usa-se o A
    # Caso seja necessário criar arquivo em uma parte específica do pc, coloca-se o diretório / nomearquivo ou cria-se uma variável com o diretorio(mais organizado)

    diretorio = "C:/Users/Vinicius Alves/Desktop/teste.txt"
    arquivo = open(diretorio, "w")
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivos(texto):
    arquivo = open("teste.txt", "a")
    arquivo.write(texto)
    arquivo.close()


def ler_arquivos(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')  # R vem de Read, ler
    texto = arquivo.read()
    print(texto)


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, "C:\Users\Vinicius Alves\Desktop\Bootcamp\Workspace\Python")


def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo)


if __name__ == "__main__":
    escreverArquivos("Primeira linha\n")
    atualizar_arquivos("Segunda linha\n")
    atualizar_arquivos("terceira linha\n")
    ler_arquivos("teste.txt")
