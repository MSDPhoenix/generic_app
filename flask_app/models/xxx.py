from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL 
from flask_app.models import user
import re
from flask_app import app
from flask_bcrypt import Bcrypt


db = "xxx"

class Xxx:
    def __init__(self,data):
        self.id = data["id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.aaa = data["aaa"]
        self.bbb = data["bbb"]
        self.ccc = data["ccc"]
        self.ddd = data["ddd"]
        self.eee = data["eee"]
        self.fff = data["fff"]
        self.user_id = data["user_id"]
        self.user = None
    
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM xxxs
                JOIN users 
                ON users.id=xxxs.user_id;
                """
        result = connectToMySQL(db).query_db(query)
        xxxs = []
        for row in result:
            this_xxx = cls(row)
            this_xxx.user = user.User(row)
            xxxs.append(this_xxx)
        return xxxs

    @classmethod
    def get_by_id(cls,xxx_id):
        data = {"xxx_id" : xxx_id}
        query = """
                SELECT * FROM xxxs 
                JOIN users
                ON users.id=xxxs.user_id
                WHERE xxxs.id = %(xxx_id)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        xxx = cls(result[0])
        xxx.user = user.User(result[0])
        return xxx
        
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO xxxs (aaa,bbb,ccc,eee,user_id)
                VALUES (%(aaa)s,%(bbb)s,%(ccc)s,%(eee)s,%(user_id)s)
                """
        new_id = connectToMySQL(db).query_db(query,data)
        return new_id

    @classmethod
    def update(cls,data):
        query = """
                UPDATE xxxs
                SET aaa=%(aaa)s,bbb=%(bbb)s,ccc=%(ccc)s,eee=%(eee)s
                WHERE id=%(xxx_id)s;
                """
        connectToMySQL(db).query_db(query,data)

    @classmethod
    def delete(cls,xxx_id):
        data = {"xxx_id" : xxx_id}
        query = """
                DELETE FROM xxxs WHERE id=%(xxx_id)s;"
                """
        connectToMySQL(db).query_db(query,data)

    @staticmethod
    def validate(data):
        is_valid = True

        return is_valid

