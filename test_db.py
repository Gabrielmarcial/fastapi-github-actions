import pytest
from database import ConexaoPostgreSQL


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

def test_desconexao_bem_sucedida(conexao_postgresql):
    conexao_postgresql.desconectar()
    print(conexao_postgresql.connection)
    assert conexao_postgresql.connection is None
    assert conexao_postgresql.cursor is None


