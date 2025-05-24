import psycopg2

try:
    conn = psycopg2.connect(
        dbname='sis_db',
        user='postgres',
        password='root',
        host='localhost',
        port='5432'
    )
    print("✅ Conectado com sucesso ao banco de dados.")
    conn.close()
except Exception as e:
    print("❌ Erro ao conectar:", e)
