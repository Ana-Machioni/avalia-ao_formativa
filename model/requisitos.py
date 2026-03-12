from database.conexao import conectar

def recuperar_requisitos():
    conexao, cursor = conectar()

    cursor.execute("SELECT * FROM tb_requisitos")

    requisitos = cursor.fetchall()

    conexao.close()

    return requisitos

def inserir_dados(descricao, nivel, valor):
    conexao, cursor = conectar()

    cursor.execute("""
            INSERT INTO tb_requisitos (DESCRICAO, NIVEL, VALOR)
            VALUES (%s, %s, %s);
            """, [descricao, nivel, valor])
    
    conexao.commit()
    cursor.close()
    