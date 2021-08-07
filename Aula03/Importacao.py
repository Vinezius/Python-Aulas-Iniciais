import requests

def retornaCep(cep):
    response = requests.get("https://viacep.com.br/ws/{}/json/".format(cep)) #Puxa as informações do site(requisição de api)
    
    print(response.status_code) #Retorna 200 quando da certo
    print(response.json()) #Printa as informações como um arquivo json(dicionario/dict)

    dadosCep = response.json()
    print (dadosCep["logradouro"])
    print (dadosCep["bairro"])
    return dadosCep

def retornaSite(url):
    response = requests.get(url)
    return response.text

def retornaPokemon(pokemon):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(pokemon))
    dadosPokemon = response.json()
    return dadosPokemon

if __name__ == '__main__':
    response = retornaSite("https://globallab.org/en/#.YQ7Rk1PPyUk")
    print (response)
    #retornaCep("83215290")
    # dadosPokemon = retornaPokemon("pikachu")
    # print (dadosPokemon["sprites"]["front_shiny"])