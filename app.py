import os
from flask import Flask, render_template, url_for, session, request, redirect, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/index")
def index():
    recipes = mongo.db.recipe.find()
    return render_template("index.html", recipes=recipes)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Check if username is available
        existing_user = mongo.db.users.find_one({"email": request.form.get('email').lower()})
        if existing_user:
            session["alert"] = "alert alert-danger"
            flash('Email already exists. Please try again!')
            return redirect(url_for('register'))

        if request.form.get('password') == request.form.get('repeat-password'):
            register = {
                "name": request.form.get("name").lower(),
                "email": request.form.get("email").lower(),
                "password": generate_password_hash(request.form.get("password"))
            }
            mongo.db.users.insert_one(register)
            # session cookie
            session["user"] = request.form.get('email')
            session["alert"] = "alert alert-success"
            flash('You have successfully registered!')
        else:
            session["alert"] = "alert alert-danger"
            flash('The passwords you entered do not match. Please try again!')
            return redirect(url_for('register'))

    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) # remove this at the end