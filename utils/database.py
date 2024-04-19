import psycopg2 as db
from main import config
import random


class Database:
    def __init__(self):
        self.conn = db.connect(
            database=config.DB_NAME,
            password=config.DB_PASS,
            user=config.DB_USER,
            host=config.DB_HOST
        )
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.conn.commit()
        user_table = """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        chat_id BIGINT NOT NULL,
        full_name VARCHAR(55),
        phone_number VARCHAR(13),
        location_name VARCHAR(55))
        """

        photos = """
        CREATE TABLE IF NOT EXISTS photos (
        id SERIAL PRIMARY KEY,
        chat_id BIGINT,
        photo_id VARCHAR(250),
        status BOOLEAN DEFAULT false)
        """

        likes = """
        CREATE TABLE IF NOT EXISTS likes (
        id SERIAL PRIMARY KEY,
        chat_id BIGINT,
        photo_id INT references photos(id),
        is_like BOOLEAN DEFAULT false)
        """

        self.cursor.execute(user_table)
        self.cursor.execute(photos)
        self.cursor.execute(likes)

        self.conn.commit()

    def get_user_by_chat_id(self, chat_id):
        query = f"SELECT * FROM users WHERE chat_id = {chat_id}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def get_user_photo_by_chat_id(self, chat_id):
        query = f"SELECT * FROM photos WHERE chat_id = {chat_id} AND status = true"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def get_random_photo(self, chat_id):
        query = f"SELECT * FROM photos WHERE status = true"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        random_photo = random.choice(result)
        return random_photo

    def check_user_like(self, chat_id, photo_id):
        query = f"SELECT * FROM likes WHERE chat_id = {chat_id} and photo_id = {photo_id}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def get_photo_likes(self, photo_id):
        query_like = f"SELECT COUNT(*) FROM likes WHERE photo_id = {photo_id} AND is_like = true"
        query_dislike = f"SELECT COUNT(*) FROM likes WHERE photo_id = {photo_id} AND is_like = false"
        self.cursor.execute(query_like)
        likes = self.cursor.fetchall()
        self.cursor.execute(query_dislike)
        dislikes = self.cursor.fetchall()
        return likes, dislikes

    def add_user(self, data: dict):
        chat_id = data["chat_id"]
        full_name = data["full_name"]
        phone_number = data["phone_number"]
        location = data["location"]
        query = f"""INSERT INTO users (chat_id, full_name, phone_number, location_name)
        VALUES ({chat_id}, '{full_name}', '{phone_number}', '{location}')"""
        self.cursor.execute(query)
        self.conn.commit()
        return True

    def add_photo(self, data: dict):
        chat_id = data["chat_id"]
        photo_id = data["photo_id"]

        query = f"""INSERT INTO photos (chat_id, photo_id, status)
           VALUES ({chat_id}, '{photo_id}', true)"""
        self.cursor.execute(query)
        self.conn.commit()
        return True

    def user_like(self, chat_id, photo_id, is_like):
        query = f"""INSERT INTO likes (chat_id, photo_id, is_like)
           VALUES ({chat_id}, '{photo_id}', {is_like})"""
        self.cursor.execute(query)
        self.conn.commit()
        return True

    def user_delete_like(self, chat_id, photo_id):
        query = f"""DELETE FROM likes WHERE chat_id = {chat_id} AND photo_id = {photo_id}"""
        self.cursor.execute(query)
        self.conn.commit()
        return True