from codigo.bytebank import Funcionario
import pytest
from pytest import mark
class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        #Given-Contexto
        entrada = "13/03/2000"
        esperado = 23
        funcionario_teste = Funcionario("Teste", entrada, 1111)

        #When-Ação
        resultado = funcionario_teste.idade()

        #Then-Desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_apenas_Carvalho(self):
        #Given-Contexto
        entrada = "Lucas Carvalho"
        esperado = "Carvalho"
        lucas = Funcionario(entrada, "11/11/2000", 1111)


        #When-Ação
        resultado = lucas.sobrenome()

        #Then-Desfecho
        assert resultado == esperado  

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        #Given-Contexto
        entrada_salario = 100000
        entrada_nome = "Paulo Bragança"
        esperado = 90000
        socio = Funcionario(entrada_nome, "11/11/2000", entrada_salario)

        #When-Ação
        socio.decrescimo_salario()
        resultado = socio.salario

        #Then-Desfecho
        assert resultado == esperado


    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        #Given-Contexto
        entrada = 1000
        esperado = 100
        funcionario_teste = Funcionario("teste", "11/11/2000", entrada)

        #When-Ação
        resultado = funcionario_teste.calcular_bonus()

        #Then-Desfecho
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        #Given-Contexto
        with pytest.raises(Exception):
            entrada = 100000000
            funcionario_teste = Funcionario("Teste", "11/11/2000", entrada)
            
            #When-Ação
            resultado = funcionario_teste.calcular_bonus()
        
            #Then-Desfecho
            assert resultado 
    

            