from db_modul.db_client import DBClient

# Создание движка для работы с базой данных
db_client = DBClient()
db_engine = db_client.create_sql_alchemy_engine()