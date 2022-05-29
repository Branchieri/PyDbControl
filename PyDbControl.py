from ast import In, arg
from asyncio.windows_events import NULL
from distutils.log import info
from lib2to3.pgen2.token import EQUAL
from types import NoneType
import mysql.connector

class Banco_De_Dados():
    def __init__(self):
        pass

    def Criar_Banco_De_Dados(self, nome):
        cursor.execute(f"CREATE DATABASE {nome}")
        print('Banco de dados criado')

    def Conectar_Banco_De_Dados(self, host, user, password, database):
        try:
            global data_base
            global cursor
            data_base = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            cursor = data_base.cursor()
            
        except mysql.connector.Error as erro:
            print(f"Falha ao conectar ao banco de dados\n {erro}")

        finally:
            if data_base.is_connected():
                print('Conectado com Sucesso')
            else:
                print("Verifique os dados e tente novamente")
    
    def Desconectar_Banco_De_Dados(self):
        if data_base.is_connected():
            data_base.close()
            print('MySQL desconectado')

    def Cursor_Banco_De_Dados():
        global cursor
        cursor = data_base.cursor()
    
    
    def Criar_Tabela_Produtos_No_Banco_De_Dados(self, nome):
        cursor.execute(f"CREATE TABLE {nome} (id INT(5), nome VARCHAR(255), preço FLOAT(10,2), quantidade INT(15))")
        print('Tabela Produtos criada com sucesso')

    def Excluir_Tabela_Do_Banco_De_Dados(self, nome):
        cursor.execute(f"DROP TABLE {nome}")
        print('Tabela excluida com sucesso')
        
    def Inserir_Valores_Na_Tabela_Banco_De_Dados(self, id, nome, preço, quantidade):
        
        try:

            cursor.execute(f"SELECT * FROM Produtos")
            Busca_Nome_Estoque = []
            Informações_Colunas = dict()        
            for coluna in cursor.fetchall():
                Informações_Colunas['Id'] = coluna[0]
                Busca_Nome_Estoque.append(Informações_Colunas['Id'])
                Informações_Colunas['Nome'] = coluna[1]
                Informações_Colunas['Preço'] = coluna[2]
                Informações_Colunas['Quantidade'] = coluna[3]
                #print(Busca_Nome_Estoque)
            if id in Informações_Colunas.values():    
                print(f'Informações do produto {nome} atualizadas com sucesso')
                Soma_Quantidade = quantidade + Informações_Colunas['Quantidade']
                Novo_Nome = nome
                Novo_Preço = preço
                Executa = f'''UPDATE produtos set quantidade = '{Soma_Quantidade}', preço = '{Novo_Preço}', nome = '{Novo_Nome}' WHERE id = '{id}' '''
                cursor.execute(Executa)
                data_base.commit()
            else:
                nome = nome.upper()
                print(f'Produto {nome} adicionado com sucesso')
                Executa = f"INSERT INTO produtos (id, nome, preço, quantidade) VALUES (%s, %s, %s, %s)"
                Valores = (id, nome, preço, quantidade)
                cursor.execute(Executa, Valores)
                data_base.commit()                            
        except mysql.connector.Error as erro:
                print(f'Ocorreu um erro {erro}')

        finally:
            print('Rotina Finalizada')

    def Excluir_valor_por_id(self, Id):
        cursor.execute(f"DELETE FROM Produtos WHERE id = {Id}")
        data_base.commit()
        print(f'Produto excluido com sucesso')




