from sqlalchemy import create_engine
import json
from base_log import LoggerHand

log = LoggerHand(__name__, f"logs/{__name__}.log")


class DBClient:
    def __init__(self):
        with open('credentials/db_credentials.json', 'r') as file:
            db_credentials: dict = json.load(file)
        self.db_name = db_credentials.get('dbname')
        self.user = db_credentials.get('user')
        self.password = db_credentials.get('password')

    def __str__(self):
        return f"db_name: {self.db_name}, user: {self.user}"

    def create_sql_alchemy_engine(self):
        db_engine = create_engine(f"postgresql://{self.user}:{self.password}@localhost/{self.db_name}")
        log.logger.debug(f"SQL alchemy engine for DB: {self} has been created")
        return db_engine
