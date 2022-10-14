from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app import app
from flask_bcrypt import Bcrypt

db = "yyyyyyyyyyyy"
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
        self.xxx = []

    @classmethod
    def get_all(self):
        users = []
        return users 

    @classmethod
    def get_by_id(cls,data):
        pass

    @classmethod
    def get_by_email(cls,data):
        pass

    @classmethod
    def save(cls,data):
        pass

    @classmethod
    def update(cls,data):
        pass

    @classmethod
    def delete(cls,data): 
        pass

    @staticmethod
    def validate(data):
        pass