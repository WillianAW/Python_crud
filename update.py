import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='vendas',
)

cursor = connection.cursor()


sql = f'UPDATE vendas.produtos SET nome_produtos = "new_teste2" , valor_produtos = 10 WHERE idProdutos = "1"'

cursor.execute(sql)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, 'registro alterado')