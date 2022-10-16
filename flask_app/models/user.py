from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app import app
from flask_bcrypt import Bcrypt

db = "xxx"
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.xxxs = []

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM users;
                """
        result = connectToMySQL(db).query_db(query)
        users = []
        for row in result:
            this_user = cls(row)
            users.append(this_user)
        return users 

    @classmethod
    def get_by_id(cls,user_id):
        data = {"user_id":user_id}
        query = """
                SELECT * FROM users WHERE id = %(user_id)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        user = cls(result[0])
        return user

    @classmethod
    def get_by_email(cls,email):
        data = {"email":email}
        query = """
                SELECT * FROM users WHERE email=%(email)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        if len(result) == 0:
            return False
        user = cls(result[0])
        return user

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO users (first_name,last_name,email,password)
                VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                """
        connectToMySQL(db).query_db(query,data)

    @classmethod
    def update(cls,data):
        print("\n\tCode for 'Update User' function is not writtten.\n")
        

    @classmethod
    def delete(cls,data): 
        print("\n\tCode for 'Delete User' function is not writtten.\n")
        

    @staticmethod
    def validate(data):
        is_valid = True

        return is_valid