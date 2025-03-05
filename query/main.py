import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
from postgres_connection import PostgresConnection
from postgres_databases import PostgresDatabases
from sql_query_ai import SQLQueryAI
from llm_type import LLMType

#schema path
root = os.path.dirname(os.path.abspath(__file__))
schema_path = os.path.join(root, "schemas", "schema_ecommerce.yaml")

sql_crew = SQLQueryAI(LLMType.OPEN_AI_GPT_4O_MINI)
# Executar o agente com uma consulta de exemplo]

inputs = {
    "database_type": "Postgres",
    "database_name": "ecommerce",
    "yaml_path": schema_path,
    "user_request": "Qual é o nome e o preço dos produtos que custam mais de R$ 100. Eu só quero os 5 primeiros resultados.",
    "json_output": False
}

sql_query = sql_crew.kickoff(inputs)

print("\n🔍 Consulta SQL Gerada:\n")
print(sql_query)

ecommerce_database = PostgresDatabases.ECOMMERCE

conn = PostgresConnection(database_uri=ecommerce_database)
conn.connect()

print(conn.get_current_database())

cursor = conn.cursor
cursor.execute(sql_query)
# Obtendo os resultados
results = cursor.fetchall()

colunas = conn.get_colunas()

df = pd.DataFrame(results, columns=colunas)

if results:
    print(df)
else:
    print("Nenhum resultado encontrado.")