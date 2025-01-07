from sqlmodel import Field, SQLModel, create_engine  # Classes e funções do SQLModel para definir modelos e interagir com o banco de dados
from .model import*

# Nome do arquivo SQLite onde os dados serão armazenados
sqlite_file_name = 'database.db'  # Nome do arquivo para o banco de dados SQLite
sqlite_url = f'sqlite:///{sqlite_file_name}'  # URL do banco de dados no formato SQLite

# Criação do mecanismo de conexão com o banco de dados
engine = create_engine(sqlite_url, echo=False)  # Constrói um mecanismo para interagir com o banco de dados. O parâmetro `echo=True` exibe as instruções SQL geradas no console.

def create_db_and_tables():  
    SQLModel.metadata.create_all(engine)

# Código principal para criar as tabelas no banco de dados
if __name__ == '__main__':  # Verifica se o script está sendo executado diretamente (não importado)
    SQLModel.metadata.create_all(engine)  # Cria todas as tabelas definidas pelos modelos SQLModel no banco de dados
