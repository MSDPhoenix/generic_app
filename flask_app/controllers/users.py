from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.xxx import Xxx
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

@app.route("/autopopulate/")
def autopopulate():
    metadata1 = [
        {
            "first_name" : "Mickey",
            "last_name" : "Mouse",
            "email" : "mm@mm.mm",
            "password" : bcrypt.generate_password_hash("mmmmmmmm")
        },
        {
            "first_name" : "Minnie",
            "last_name" : "Mouse",
            "email" : "mm2@mm.mm",
            "password" : bcrypt.generate_password_hash("mmmmmmmm")
        },
        {
            "first_name" : "Secret",
            "last_name" : "Squirrel",
            "email" : "ss@ss.ss",
            "password" : bcrypt.generate_password_hash("ssssssss")
        },
        {
            "first_name" : "Daffy",
            "last_name" : "Duck",
            "email" : "dd@dd.dd",
            "password" : bcrypt.generate_password_hash("dddddddd")
        },
        {
            "first_name" : "Bugs",
            "last_name" : "Bunny",
            "email" : "bb@bb.bb",
            "password" : bcrypt.generate_password_hash("bbbbbbbb")
        },
        {
            "first_name" : "Porky",
            "last_name" : "Pig",
            "email" : "pp@pp.pp",
            "password" : bcrypt.generate_password_hash("pppppppp")
        },
        {
            "first_name" : "Elmer",
            "last_name" : "Fudd",
            "email" : "ef@ef.ef",
            "password" : bcrypt.generate_password_hash("eeeeeeee")
        },
    ]
    metadata2 = [
        {
            "aaa" : "aaa",
            "bbb" : "bbb",
            "ccc" : "ccc",
            "eee" : "eee",
            "user_id" : 2,
        },
        {
            "aaa" : "fff",
            "bbb" : "ggg",
            "ccc" : "hhh",
            "eee" : "iii",
            "user_id" : 2,
        },
        {
            "aaa" : "jjj",
            "bbb" : "kkk",
            "ccc" : "lll",
            "eee" : "mmm",
            "user_id" : 2,
        },
        {
            "aaa" : "nnn",
            "bbb" : "ooo",
            "ccc" : "ppp",
            "eee" : "qqq",
            "user_id" : 3,
        },
        {
            "aaa" : "rrr",
            "bbb" : "sss",
            "ccc" : "ttt",
            "eee" : "uuu",
            "user_id" : 3,
        },
        {
            "aaa" : "vvv",
            "bbb" : "www",
            "ccc" : "xxx",
            "eee" : "yyy",
            "user_id" : 4,
        },
        {
            "aaa" : "zzz",
            "bbb" : "111",
            "ccc" : "222",
            "eee" : "333",
            "user_id" : 5,
        },
        {
            "aaa" : "444",
            "bbb" : "555",
            "ccc" : "666",
            "eee" : "777",
            "user_id" : 3,
        },
        {
            "aaa" : "888",
            "bbb" : "999",
            "ccc" : "000",
            "eee" : "???",
            "user_id" : 6,
        },
    ]
    metadata3 = [
        {"user_id" : 1,"xxx_id" : 1},
        {"user_id" : 1,"xxx_id" : 2},
        {"user_id" : 1,"xxx_id" : 3},
        {"user_id" : 1,"xxx_id" : 4},
        {"user_id" : 2,"xxx_id" : 6},
        {"user_id" : 2,"xxx_id" : 5},
        {"user_id" : 2,"xxx_id" : 3},
        {"user_id" : 2,"xxx_id" : 4},
        {"user_id" : 3,"xxx_id" : 1},
        {"user_id" : 3,"xxx_id" : 5},
        {"user_id" : 3,"xxx_id" : 3},
        {"user_id" : 4,"xxx_id" : 4},
        {"user_id" : 4,"xxx_id" : 1},
        {"user_id" : 4,"xxx_id" : 2},
        {"user_id" : 5,"xxx_id" : 3},
        {"user_id" : 5,"xxx_id" : 4},
        {"user_id" : 6,"xxx_id" : 5},
        {"user_id" : 6,"xxx_id" : 6},
    ]
    for data in metadata1:
        User.save(data)
    for data in metadata2:
        Xxx.save(data)
    for data in metadata3:
        User.add_to_many_to_many(data)


    return redirect("/dashboard/")


