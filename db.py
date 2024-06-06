import os
from dotenv import load_dotenv
import psycopg2 as psql
load_dotenv()

class Database:
    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database=os.getenv("db_name"),
            user=os.getenv("db_user"),
            password=os.getenv("db_password"),
            host=os.getenv("db_host"),
            port=os.getenv("db_port")
        )

        cursor = db.cursor()
        cursor.execute(query)
        data = ["update", "insert", "delete", "alter"]   # select
        if query_type in data:
            db.commit()
            if query_type == "update":
                return "updated data"

            elif query_type == "insert":
                return "inserted data"

            elif query_type == "delete":
                return "deleted data"

            elif query_type == "alter":
                return "alter data"

        else:
            return cursor.fetchall()