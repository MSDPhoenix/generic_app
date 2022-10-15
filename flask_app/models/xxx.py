from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash
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
        self.user = None
    
    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_by_id(cls,data):
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

