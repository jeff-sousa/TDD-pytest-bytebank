from codigo.bitebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_24(self):
        # Given - Contexto
        entrada = '13/03/2000' 
        esperado = 24
        # When - Ação
        funcionario_teste = Funcionario('nome teste', entrada, 1111) 
        resultado = funcionario_teste.idade()
        # Then - desfecho
        assert resultado == esperado 

    def test_quando_nome_recebe_jefferson_sousa_deve_retornar_sousa(self):
        # Given
        entrada = " Jefferson sousa "
        esperado = 'sousa'

        # When
        funcionario_teste = Funcionario(entrada, '11/11/2000', 1111)
        resultado = funcionario_teste.sobrenome()

        # Then
        assert resultado == esperado


    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # when
        resultado = funcionario_teste.salario

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario('jeff', '11/11/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception): 

            entrada_salario = 100000

            funcionario_teste = Funcionario('jeff', '11/11/2000', entrada_salario)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado
