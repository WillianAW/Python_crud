import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='vendas',
)

cursor = connection.cursor()



sql = "DELETE FROM vendas.produtos WHERE idProdutos = '1'"

cursor.execute(sql)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, 'Registro deletado')