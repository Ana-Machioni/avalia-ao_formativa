import mysql.connector 

def conectar():
    # conectando no bd
    conexao = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="db_formativa"
    )

    # cursor
    cursor = conexao.cursor(dictionary=True)

    return conexao, cursor