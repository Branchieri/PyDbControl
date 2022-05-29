# PyDbControl
 • Controla Funçoes básicas de armazenamento de arquivos em banco de dados MySQL
 
 • Planejo futuramente implementar funções novas, mais avançadas, conforme for aprendendo.

 • Sinta-se livre para ajudar, sério.
 
# Instalação
 • Clone o repositório pro seu pc

 • Digite pip install mysql-connector-python no terminal para instalar o conector

 • Certifique-se de ter o MySQL instalado no seu pc -> https://www.mysql.com/downloads/

# Funções
Os nomes são bem auto-explicativos 

 • Conectar_Banco_De_Dados() 
   -> Faz a conexão com o servidor local MySQL

 • Desconectar_Banco_De_Dados()
   -> Desliga a conexão com o servidor

 • Cursor_Banco_De_Dados()
   -> Retorna o cursor, usado para manipular a base de dados usando as demais funções do objeto

 • Criar_Banco_De_Dados()
   -> Cria uma base de dados no servidor local

 • Criar_Tabela_Produtos_No_Banco_De_Dados()
   -> Cria uma tabela simples de produtos, contendo id, nome do produto, preço do produto e quantidade em estoque

 • Excluir_Tabela_Do_Banco_De_Dados()
   -> Deleta uma tabela por completo, tendo como parâmetro o nome da tabela existente

 • Inserir_Produtos_Na_Tabela()
   -> Insere produto na tabela, tendo como parâmetros o id, nome, preço e quantidade em estoque
   -> Se o produto já existir, todos os valores do produto são atualizados conforme os parâmetros

 • Excluir_Produto_Por_Id()
   -> Exclui um produto na tabela à partir de um id específico



 
  