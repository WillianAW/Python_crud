import mysql.connector


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='vendas',
)

cursor = connection.cursor()


# comando = '' =>
# cursor.execute(comando)
# conexao.commit()      # edita o banco de dados
#resultado = cursor.fatchall() #ler o banco de dados


#CREAETE
nomeProduto = 'teste'
valorProduto = 5

sql = f'INSERT INTO vendas.produtos (nome_produtos, valor_produtos) VALUES ("{nomeProduto}",{valorProduto})'
cursor.execute(sql)
connection.commit()

#userId = cursor.lasttrowid

cursor.close()
connection.close()

print('Um novo produto foi adicionado')