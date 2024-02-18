import psycopg2

class ConexaoPostgreSQL:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def conectar(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            print("Conexão bem-sucedida!")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def desconectar(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            self.connection = None  
            self.cursor = None      
            print("Desconexão bem-sucedida!")
        except Exception as e:
            print(f"Erro ao desconectar do banco de dados: {e}")

