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
            INSERT INTO tb_requisitos (descricao, nivel, valor, situacao)
            VALUES (%s, %s, %s, "pendente");
            """, (descricao, nivel, valor))
    
    conexao.commit()
    cursor.close()


def excluir_descricao(cod_requisitos:int) -> bool:
    try:
        conexao, cursor = conectar()

        cursor.execute("""
        DELETE FROM tb_requisitos
        WHERE cod_requisito = %s
                       
        """,
        [cod_requisitos])
        conexao.commit()

        conexao.close()

        return True
    
    except Exception as erro:
        print(erro)
        return False
    


    
def update(cod_requisitos, situacao):
    conexao, cursor = conectar()

    cursor.execute("""
                    UPDATE tb_requisitos SET situacao = %s WHERE cod_requisito = %s;
            """, (situacao, cod_requisitos ))
    conexao.commit()

    conexao.close()


    