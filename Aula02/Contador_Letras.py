def contador_Letras(lista_Palavras):
    contador = []

    for x in lista_Palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':
    Lista = ["Cachorro", "Gato"]
    print(contador_Letras(Lista))