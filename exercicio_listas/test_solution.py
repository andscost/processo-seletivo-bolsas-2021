import pytest
from solution import subtracao_de_listas_com_erros

# testes função com erros --------------------------------------------------------------------------------

def test_exemplo():
    lista1 = [2, 7, 3.1, 'banana']
    lista2 = [2, 'banana', 'carro']
    assert subtracao_de_listas_com_erros(lista1,lista2) == [7, 3.1]

def test_diferente_lista():
    parametro1 = "teste"
    parametro2 = 42
    with pytest.raises(TypeError):
        subtracao_de_listas_com_erros(parametro1,parametro2) 
    
def test_tamanhos_de_listas_diferente():
    lista1  = [2,4,5]
    lista2 = [1]
    assert subtracao_de_listas_com_erros(lista1,lista2) == lista1

# testes relacionados aos parametros -------------------------

def test_listas_iguais():
    lista1 = [1,2,3,4]
    assert subtracao_de_listas_com_erros(lista1,lista1) == []

def test_inverter_ordem_parametros():
    lista1 = lista1 = [2, 7, 3.1, 'banana']
    lista2 = [2, 'banana', 'carro']
    assert subtracao_de_listas_com_erros(lista2,lista1) == ['carro']

def test_lista_vazia():
    assert subtracao_de_listas_com_erros([],[]) == []

def test_listas_grandes():
    lista1 = []
    for i in range(0,1000): lista1.append(i)
    assert subtracao_de_listas_com_erros(lista1,[]) == lista1

def test_int_e_str(): # estou supondo que por ser de tipos diferentes nao sao a mesma coisa
    lista1 = [1]
    lista2 = ['1']
    assert subtracao_de_listas_com_erros(lista1,lista2) == [1]
