import pytest
from database import ConexaoPostgreSQL,ConsultaEletronicos


@pytest.fixture
def conexao_postgresql():
    
    conexao = ConexaoPostgreSQL(
        host="127.0.0.1",
        port=5432,
        database="postgres",
        user="postgres",
        password="app_password"
    )
    conexao.conectar()
    yield conexao  
    conexao.desconectar()

def test_conexao_bem_sucedida(conexao_postgresql):
    assert conexao_postgresql.connection is not None
    assert conexao_postgresql.cursor is not None

@pytest.fixture
def consulta_eletronicos(conexao_postgresql):
    return ConsultaEletronicos(conexao_postgresql)

# Teste para verificar se a consulta retorna resultados esperados
def test_consulta_eletronicos(consulta_eletronicos):
    # Insira dados de teste na tabela eletronicos antes de executar este teste
    # Certifique-se de ajustar os dados conforme a sua tabela

    # Executa a consulta
    resultados = consulta_eletronicos.buscar_itens()

    # Verifica se pelo menos um resultado foi retornado
    assert len(resultados) > 0

    # Verifica se os resultados têm a estrutura esperada (nome, marca, modelo, preco)
    for item in resultados:
        assert len(item) == 4
        assert isinstance(item[0], str)
        assert isinstance(item[1], str)
        assert isinstance(item[2], str)


def test_desconexao_bem_sucedida(conexao_postgresql):
    conexao_postgresql.desconectar()
    print(conexao_postgresql.connection)
    assert conexao_postgresql.connection is None
    assert conexao_postgresql.cursor is None
