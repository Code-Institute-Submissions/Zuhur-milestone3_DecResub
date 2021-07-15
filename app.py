import os
from flask import Flask, render_template, url_for, session, request, redirect, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
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
            session["name"] = request.form.get('name')
            session["alert"] = "alert alert-success"
            flash('You have successfully registered!')
            return redirect(url_for('allrecipes'))
        else:
            session["alert"] = "alert alert-danger"
            flash('The passwords you entered do not match. Please try again!')
            return redirect(url_for('register'))

    return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # Check if user exists
        check_user = mongo.db.users.find_one({"email": request.form.get('email').lower()})
        # if user exists check if password matches 
        if check_user:
            if check_password_hash(check_user["password"], request.form.get("password")):
                session["user"] = request.form.get("email").lower()
                session["name"] = mongo.db.users.find_one({"email": session["user"]})["name"]
                session["alert"] = "alert alert-success"
                flash("You have been logged in!")
                return redirect(url_for("allrecipes"))
            else:
                session["alert"] = "alert alert-danger"
                flash("Incorrect Username/Password. Try again.")
                return redirect(url_for("login"))
        else:
            session["alert"] = "alert alert-danger"
            flash("Incorrect Username/Password. Try again.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove users session
    session['alert'] = "alert alert-danger"
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for('login'))


@app.route("/profile")
def profile(name):
    return render_template('profile.html', name=name)
    
    
@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    if request.method == "POST":
        if "recipe_image" in request.files:
            recipe_image = request.files['recipe_image']
            if bool(recipe_image):
                mongo.save_file(recipe_image.filename, recipe_image)

            ingredients = {
                "recipe_name": request.form.get('recipe_name').capitalize(),
                "prep_time": request.form.get('prep_time') + ' ' + request.form.get('prep_unit'),
                "cook_time": request.form.get('cook_time') + ' ' + request.form.get('cook_unit'),
                "serves": request.form.get('serves'),
                "ingredients": request.form.get('ingredients').replace('\r', '').split('\n'),
                "instructions": request.form.get('instructions').replace('\r', '').split('\n'),
                "author": session["user"],
                "recipe_image": recipe_image.filename,
                "is_private": bool(request.form.get('is_private')),
                "created": datetime.now().strftime("%m-%d-%Y")
            }
            mongo.db.recipe.insert(ingredients)
            session['alert'] = "alert alert-success"
            flash("You have successully created a recipe!") 
            return redirect(url_for('allrecipes'))
    
    return render_template("create_recipe.html")

@app.route("/allrecipes")
def allrecipes():
    if session["user"]:
        recipes = list(mongo.db.recipe.find())
        return render_template('allrecipes.html', recipes=recipes)
    
    return redirect('login')


@app.route('/img_file/<filename>')
def img_file(filename):
    return mongo.send_file(filename)


@app.route("/viewrecipe/<recipe_id>")
def viewrecipe(recipe_id):
    show_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    print(show_recipe)
    return render_template('viewrecipe.html', show_recipe = show_recipe)

@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})

    if request.method == "POST":
        recipe_image = request.files['recipe_image']
        print(recipe_image.filename)
        if recipe_image.filename != "":
            mongo.save_file(recipe_image.filename, recipe_image)
            mongo.db.recipe.update({"_id": ObjectId(recipe_id)}, {"recipe_image": recipe_image.filename})

            new_recipe = {
                "recipe_name": request.form.get('recipe_name').capitalize(),
                "prep_time": request.form.get('prep_time') + ' ' + request.form.get('prep_unit'),
                "cook_time": request.form.get('cook_time') + ' ' + request.form.get('cook_unit'),
                "serves": request.form.get('serves'),
                "ingredients": request.form.get('ingredients').replace('\r', '').split('\n'),
                "instructions": request.form.get('instructions').replace('\r', '').split('\n'),
                "author": session["user"],
                "recipe_image": recipe_image.filename,
                "is_private": bool(request.form.get('is_private')),
            }
            mongo.db.recipe.update({"_id": ObjectId(recipe_id)}, { "$set": new_recipe })
            session["alert"] = "alert alert-success"
            flash("Recipe successfully updated")

    
        return redirect(url_for('allrecipes'))


    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)}) 
    return render_template("edit_recipe.html", recipe=recipe)

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("allrecipes"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) # remove this at the end