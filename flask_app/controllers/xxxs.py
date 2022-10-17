from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.xxx import Xxx

def validation_failed(data):
    session["aaa"] = data["aaa"]
    session["bbb"] = data["bbb"]
    session["ccc"] = data["ccc"]
    session["eee"] = data["eee"]

def validation_succeeded():
    if "aaa" in session:
        session.pop("aaa")
    if "bbb" in session:
        session.pop("bbb")
    if "ccc" in session:
        session.pop("ccc")
    if "ddd" in session:
        session.pop("ddd")
    if "eee" in session:
        session.pop("eee")

@app.route("/dashboard/")
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    all_users = User.get_all()
    if len(all_users) == 1:
        return redirect("/autopopulate/")
    return render_template(
        "dashboard.html",
        user = User.get_by_id(session["user_id"]),
        xxxs = Xxx.get_all()
        )

@app.route("/view_one/<int:xxx_id>/")
def view_one(xxx_id):
    if "user_id" not in session:
        return redirect("/") 
    return render_template(
        "view_one.html", 
        user = User.get_by_id(session["user_id"]),
        xxx = Xxx.get_by_id(xxx_id)
        )

@app.route("/add_form/")
def add_form():
    if "user_id" not in session:
        return redirect("/")
    return render_template("add_form.html")

@app.route("/edit_form/<int:xxx_id>/")
def edit_form(xxx_id):
    if "user_id" not in session:
        return redirect("/")
    return render_template(
        "edit_form.html",
        user=User.get_by_id(session["user_id"]),
        xxx=Xxx.get_by_id(xxx_id)
        )

@app.route("/save_xxx/",methods=["POST"])
def save_xxx():
    if "user_id" not in session:
        return redirect("/")
    if not Xxx.validate(request.form):
        validation_failed(request.form)
        return redirect("/add_form/")
    validation_succeeded()
    data = {
        **request.form,
        "user_id" : session["user_id"],
    }
    Xxx.save(data)
    return redirect("/dashboard/")

@app.route("/update_xxx/",methods=["POST"])
def update_xxx():
    if "user_id" not in session:
        return redirect("/")
    if not Xxx.validate(request.form):
        validation_failed(request.form)
        return redirect(f"/edit_form/{request.form['xxx_id']}/")
    validation_succeeded()
    Xxx.update(request.form)
    return redirect("/dashboard/")

@app.route("/delete_xxx/<int:xxx_id>/")
def delete_xxx(xxx_id):
    if "user_id" not in session:
        return redirect("/")
    xxx = Xxx.get_by_id(xxx_id)
    if not xxx or xxx.user_id != session["user_id"]:
        session.clear()
        return redirect("https://www.churchofjesuschrist.org/?lang=eng")
    Xxx.delete(xxx_id)
    print("\n\tE\n")
    print(f"{xxx.aaa} deleted\n")
    return redirect("/dashboard/")
