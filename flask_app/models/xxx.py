from flask import flash,session
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
        self.many_to_many = []
        self.logged_in_user_in_many_to_many = False

    def get_many_to_many(self):
        data = {"xxx_id" : self.id}
        query = """
                SELECT * FROM users
                JOIN user_has_xxx
                ON users.id=user_has_xxx.user_id
                WHERE user_has_xxx.xxx_id=%(xxx_id)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        for row in result:
            this_user=user.User(row)
            self.many_to_many.append(this_user)
    
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
            this_xxx.get_many_to_many()
            for one_user in this_xxx.many_to_many:
                if one_user.id == session["user_id"]:
                    this_xxx.logged_in_user_in_many_to_many = True
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
        if len(result) == 0:
            return False
        xxx = cls(result[0])
        xxx.user = user.User(result[0])
        xxx.get_many_to_many()
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
        # data1 = {"xxx_id" : xxx_id}
        # query1 = """
        #         DELETE FROM user_has_xxx 
        #         WHERE xxx_id=%(xxx_id)s
        #         """
        # connectToMySQL(db).query_db(query1,data1)
        data2 = {"xxx_id" : xxx_id}
        query2 = """
                DELETE FROM xxxs 
                WHERE id=%(xxx_id)s;
                """
        connectToMySQL(db).query_db(query2,data2)


    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["aaa"]) < 1:
            flash("Name is required","xxx")
            is_valid = False
        elif len(data["aaa"]) < 3:
            flash("Name must be at least 3 letters","xxx")
            is_valid = False
        if len(data["bbb"]) < 1:
            flash("Description required","xxx")
            is_valid = False
        elif len(data["bbb"]) < 3:
            flash("Description must be at least 3 letters","xxx")
            is_valid = False
        if len(data["ccc"]) < 1:
            flash("Instructions required","xxx")
            is_valid = False
        elif len(data["ccc"]) < 3:
            flash("Instructions must be at least 3 letters","xxx")
            is_valid = False
        # if len(data["date_made"]) < 1:
        #     flash("Date cooked/made is required","xxx")
        #     is_valid = False
        if "eee" not in data:
            flash("\"Under 30 minutes?\" is required","xxx")
            is_valid = False

        return is_valid
