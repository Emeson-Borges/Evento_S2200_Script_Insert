import psycopg2

# Conexão com o banco de dados
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

# Criação do objeto cursor
cursor = conn.cursor()

# Execução da consulta
cursor.execute("SELECT * FROM esocial.historico WHERE evento='S2200' AND status='P'")
# Recuperação dos resultados da consulta
results = cursor.fetchall()

# Geração do script de insert
#for result in results:
#    insert_query = f"INSERT INTO esocial.historico (idevento, evento, status, criado_por, alterado_por, message, protocolo, cnpj, nr_recibo, ) VALUES ('{result[0]}', '{result[1]}', '{result[2]}', '{result[3]}', '{result[4]}', '{result[5]}', '{result[6]}', '{result[7]}', '{result[8]}', '{result[9]}', '{result[10]}', '{result[11]}');"
#    print(insert_query)



# Geração do script de insert
with open('script_insert.txt', 'w') as f:
    for result in results:
        insert_query = f"INSERT INTO esocial.historico (idevento, evento, status, criado_por, alterado_por, message, protocolo, cnpj, nr_recibo) VALUES ('{result[1]}', '{result[2]}', '{result[3]}', '{result[4]}', '{result[5]}', '{result[8]}', '{result[9]}', '{result[10]}', '{result[11]}');"
        f.write(insert_query + '\n')
        print(insert_query)



# Fechamento do cursor e da conexão
cursor.close()
conn.close()
