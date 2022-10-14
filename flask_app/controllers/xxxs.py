from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.xxx import Xxx

@app.route("/dashboard/")
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    return render_template("dashboard.html")

@app.route("/view_one/")
def view_one():
    if "user_id" not in session:
        return redirect("/")
    return render_template("view_one.html")

@app.route("/add_form/")
def add_form():
    if "user_id" not in session:
        return redirect("/")
    return render_template("add_form.html")

@app.route("/edit_form/")
def edit_form():
    if "user_id" not in session:
        return redirect("/")
    return render_template("edit_form.html")

@app.route("/save_xxx/")
def save_xxx():

    return redirect("/.../")

@app.route("/update_xxx/")
def update_xxx():

    return redirect("/.../")

@app.route("/delete_xxx/")
def delete_xxx():
    
    return redirect("/.../")
