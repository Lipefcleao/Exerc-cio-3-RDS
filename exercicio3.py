import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='database-1-ffcljglsc.cvwnkxcsu9la.eu-north-1.rds.amazonaws.com',
                                         database='ffcljglsc',
                                         user='ffcljglsc',
                                         password='ffcljglsc')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_salario_por_regiao():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """
            SELECT d.UF as Regiao, 
                   SUM(e.Salario) as Total_Salario
            FROM Departamento d
            LEFT JOIN Empregado e ON d.Codigo = e.Departamento_Codigo
            GROUP BY d.UF
            ORDER BY d.UF
        """
        cursor.execute(select_query)
        records = cursor.fetchall()
        print("Total de custo da empresa por região:")
        print("#" * 20)
        for row in records:
            print(f"Região (UF): {row[0]}")
            print(f"Total de Salário: R$ {row[1]:.2f}")
            print("#" * 20)
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Erro ao retornar dados:", error)

get_salario_por_regiao()