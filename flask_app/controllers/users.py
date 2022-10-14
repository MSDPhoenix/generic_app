from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register/")
def register():
    
    return redirect("/dashboard/")

@app.route("/login/")
def login():
    
    return redirect("/dashboard/")

@app.route("/logout/")
def logout():
    session.clear()
    return redirect("/")




