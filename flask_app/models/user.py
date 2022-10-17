from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash,session
import re
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models import xxx

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
        self.many_to_many = []        

    def get_xxxs(self):
        data = {"user_id":self.id}
        query = """
                SELECT * FROM xxxs
                JOIN users
                ON xxxs.user_id=users.id
                WHERE users.id=%(user_id)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        for row in result:
            this_xxx = xxx.Xxx(row)
            self.xxxs.append(this_xxx)

    def get_many_to_many(self):
        data = {"user_id":self.id}
        query = """
                SELECT * FROM xxxs
                JOIN user_has_xxx
                ON user_has_xxx.xxx_id=xxxs.id
                WHERE user_has_xxx.user_id=%(user_id)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        for row in result:
            this_xxx = xxx.Xxx(row)
            self.many_to_many.append(this_xxx)

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM users;
                """
        result = connectToMySQL(db).query_db(query)
        users = []
        for row in result:
            this_user = cls(row)
            this_user.get_xxxs()
            this_user.get_many_to_many()
            users.append(this_user)
        return users 

    @classmethod
    def get_by_id(cls,user_id):
        data = {"user_id":user_id}
        query = """
                SELECT * FROM users WHERE id = %(user_id)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        if len(result) == 0:
            return False
        user = cls(result[0])
        user.get_xxxs()
        user.get_many_to_many()
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
        user.get_xxxs()
        user.get_many_to_many()
        return user

    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO users (first_name,last_name,email,password)
                VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                """
        return connectToMySQL(db).query_db(query,data)


    @classmethod
    def update(cls,data):
        print("\n\tCode for 'Update User' function is not writtten.\n")
        

    @classmethod
    def delete(cls,data): 
        print("\n\tCode for 'Delete User' function is not writtten.\n")
        
    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["first_name"]) < 1:
            flash("First name required","validate")
            is_valid = False
        elif len(data["first_name"]) < 2:
            flash("First name must be at least two letters","validate")
            is_valid = False
        elif not data["first_name"].isalpha():
            flash("First name must contain letters only","validate")
            is_valid = False
        
        if len(data["last_name"]) < 1:
            flash("Last name required","validate")
            is_valid = False
        elif len(data["last_name"]) < 2:
            flash("Last name must be at least two letters","validate")
            is_valid = False
        elif not data["last_name"].isalpha():
            flash("Last name must contain letters only","validate")
            is_valid = False
        
        if len(data["email"]) < 1:
            flash("Email required","validate")
            is_valid = False
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Must use valid email format","validate")
            is_valid = False
        elif User.get_by_email(data["email"]):
            print("\tA")
            flash("Email already registered","validate")
            is_valid = False

        if len(data["password"]) < 1:
            flash("Password required","validate")
            is_valid = False
        elif len(data["password"]) < 8:
            flash("Password must be at least 8 characters","validate")
            is_valid = False
        elif data["password"] != data["confirm_password"]:
            flash("Password does not match Confirm Password","validate")
            is_valid = False

        return is_valid

    @staticmethod
    def add_to_many_to_many(data):
        query = """
                INSERT INTO user_has_xxx
                (user_id,xxx_id)
                VALUES 
                (%(user_id)s,%(xxx_id)s);
                """
        connectToMySQL(db).query_db(query,data)

    @staticmethod
    def remove_from_many_to_many(xxx_id):
        data = {
            "xxx_id" : xxx_id,
            "user_id" : session["user_id"],
            }
        query = """
                DELETE FROM user_has_xxx
                WHERE user_id=%(user_id)s
                AND xxx_id=%(xxx_id)s;
                """
        connectToMySQL(db).query_db(query,data)

