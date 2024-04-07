import psycopg2 as db
from main import config


class Database:
    def __init__(self):
        self.conn = db.connect(
            database=config.DB_NAME,
            user=config.DB_USER,
            host=config.DB_HOST,
            password=config.DB_PASS
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        users = """
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                chat_id BIGINT,
                full_name VARCHAR(88),
                username VARCHAR(20),
                bio VARCHAR(200),
                create_date TIMESTAMP default now()
            )
        """

        self.cursor.execute(users)
        self.conn.commit()

    def chat_id_cheakc(self, chat_id):
        query = f"SELECT * FROM users WHERE chat_id = {chat_id}"
        self.cursor.execute(query)
        res = self.cursor.fetchone()
        self.cursor.fetchall()
        return res

    def add_users(self, data: dict):
        chat_id = data['chat_id']
        fullname = data['fullname']
        phone_number = data['phone_number']
        location = data['location']
        query = f"INSERT INTO users (chat_id, full_name, phone_number, location) VALUES ({chat_id}, '{fullname}', '{phone_number}', '{location}')"
        self.cursor.execute(query)
        self.conn.commit()
        return True

    def get_users_data(self):
        query = f"SELECT * FROM users"
        self.cursor.execute(query)
        res = self.cursor.fetchone()
        self.cursor.fetchall()
        return res