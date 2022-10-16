from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register/",methods=["POST"])
def register():
    if not User.validate(request.form):
        session["first_name"] = request.form["first_name"]
        session["last_name"] = request.form["last_name"]
        session["email"] = request.form["email"]
        session["password"] = request.form["password"]
        session["confirm_password"] = request.form["confirm_password"]
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        **request.form,
        "password" : pw_hash
    }
    session["user_id"] = User.save(data)
    return redirect("/dashboard/")

@app.route("/login/",methods=["POST"])
def login():
    user = User.get_by_email(request.form["email"])
    password_correct = bcrypt.check_password_hash(
                            user.password,
                            request.form["password"]
                            )
    if not user or not  password_correct:
        flash("invalid email/password","login")
        return redirect("/")
    # session.clear()
    session["user_id"] = user.id  
    return redirect("/dashboard/")

@app.route("/logout/")
def logout():
    session.clear()
    return redirect("/")




