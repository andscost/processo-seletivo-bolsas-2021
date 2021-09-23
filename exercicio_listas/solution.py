def subtracao_de_listas(lista1, lista2):
    resposta = []

    for elemento in lista1:
        if elemento not in lista2:
            resposta.append(elemento)

    return resposta

def subtracao_de_listas_com_erros(lista1, lista2):
    resposta = []
    for i in range(0,len(lista1)):
        if lista1[i] != lista2[i]:
            resposta.append(lista1[i])
    return resposta

