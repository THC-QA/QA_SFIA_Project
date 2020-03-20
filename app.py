from flask import Flask, render_template, request, flash, redirect
from flask_mysqldb import MySQL
import os
from forms import *
# IMPORTS
app = Flask(__name__)

# Call config variables from pre-assigned environmentals, check Jenkinsfile for preferred source

app.config['SECRET_KEY'] = os.environ.get("SECRETKEY")
app.config['MYSQL_HOST'] = os.environ.get('MYSQLHOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

mysql = MySQL(app)

@app.route('/')
def home():
    """This function calls the homepage, passing a LIMIT 3 random selection fo recipes and ingredients to Jinja"""
    cur = mysql.connection.cursor()
    cur.execute("SELECT ingredient_name, ingredient_type FROM ingredients ORDER BY RAND() LIMIT 3;")
    rand_i = cur.fetchall()
    mysql.connection.commit()
    cur.execute("SELECT recipe_name, recipe_method FROM recipes ORDER BY RAND() LIMIT 3;")
    rand_r = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('home.html', title = 'Home', recipes = rand_r, ingredients = rand_i) # posts = dummyData

@app.route('/history')
def history():
    """This function calls the 'history' page, largely flavour text"""
    return render_template('history.html', title = 'History of the Chilli')

@app.route('/about')
def about():
    """This function calls the 'about' page, largely flavour text"""
    return render_template('about.html', title = 'About')

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    """This function calls the submit page, handling the form feedback and passing to one of three tables, two WTForms are used, and one HTML"""
    r_form = recipe_form()
    i_form = ingredient_form()
    cur = mysql.connection.cursor()
    cur.execute("SELECT recipe_name FROM recipes")
    r_names = cur.fetchall()
    mysql.connection.commit()
    cur.execute("SELECT ingredient_name FROM ingredients")
    i_names = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    if request.method == "POST":
        if r_form.validate_on_submit():
            recipe_name = r_form.recipe_name.data
            recipe_method = r_form.recipe_method.data
            flash("Thank you for your submission of {} sauce.".format(r_form.recipe_name.data))
            cur = mysql.connection.cursor()
            cur.execute("INSERT IGNORE INTO recipes(recipe_name, recipe_method) VALUES (%s, %s)", (recipe_name, recipe_method))
            mysql.connection.commit()
            cur.close()
            return redirect("/browse")
        elif i_form.validate_on_submit():
            flash("Thank you for your submission of {} ingredient.".format(i_form.ingredient_name.data))
            ingredient_name = i_form.ingredient_name.data
            ingredient_type = i_form.ingredient_type.data
            cur = mysql.connection.cursor()
            cur.execute("INSERT IGNORE INTO ingredients(ingredient_name, ingredient_type) VALUES (%s, %s)", (ingredient_name, ingredient_type))
            mysql.connection.commit()
            cur.close()
            return redirect("/browse")
        else:
            details = request.form
            recipe = details["recipe_name"]
            ingredient = details["ingredient_name"]
            flash("Thank you.")
            cur = mysql.connection.cursor()
            cur.execute("SELECT id FROM recipes WHERE recipe_name = (%s)", [recipe])
            recipe = cur.fetchall()
            mysql.connection.commit()
            cur.execute("SELECT id FROM ingredients WHERE ingredient_name = (%s)", [ingredient])
            ingredient = cur.fetchall()
            mysql.connection.commit()
            cur.execute("INSERT IGNORE INTO recipe_ingredients(recipe_id, ingredient_id) VALUES (%s, %s)", (recipe, ingredient))
            mysql.connection.commit()
            cur.close()
            return redirect("/browse")

    return render_template('submit.html', title = 'Submit', recipe_form = r_form, ingredient_form = i_form, recipes = r_names, ingredients = i_names)

@app.route('/browse')
def browse():
    """This function calls the browse page, displaying the linked information of all recipes using a joining table"""
    cur = mysql.connection.cursor()
    cur.execute("SELECT recipe_name, recipe_method FROM recipes")
    rows = cur.fetchall()
    mysql.connection.commit()
    recipes = {}
    for row in rows:
        recipes[row[0]]=[row[1]]
        cur.execute("SELECT ingredient_name FROM recipes r JOIN recipe_ingredients r_i ON r.id=r_i.recipe_id JOIN ingredients i ON i.id=r_i.ingredient_id WHERE r.recipe_name=%s;", [row[0]])
        ingredients = cur.fetchall()
        for i in ingredients:
            recipes[row[0]].append(i[0])
        mysql.connection.commit()
    index = [name for name in recipes]
    cur.close()
    return render_template('browse.html', title = 'Browse All', recipes = recipes, index = index)

# @app.route('/search')
# def search():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT ingredient_name FROM ingredients WHERE ingredient_type = "Chilli")
#     chillies = cur.fetchall()
#     mysql.connection.commit()
#     cur.close()

# @app.route('/admin', methods = ["GET", "POST"])
# def admin():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT recipe_name FROM recipes")
#     r_names = cur.fetchall()
#     mysql.connection.commit()
#     cur.execute("SELECT ingredient_name FROM ingredients")
#     i_names = cur.fetchall()
#     mysql.connection.commit()
#     cur.close()
#     u_form = update_form(r_names, i_names)
#     return render_template('admin.html', title = "ADMIN", update_form = u_form)

@app.route('/mvp', methods = ["GET", "POST"])
def minimum():
    """This function calls the MVP page, fulfilling the minimum viability of the brief without requiring a user function, form details passed to one of two tables for three processes"""
    cur = mysql.connection.cursor()
    cur.execute("SELECT recipe_name FROM recipes")
    r_names = cur.fetchall()
    mysql.connection.commit()
    cur.execute("SELECT ingredient_name FROM ingredients")
    i_names = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    if request.method == "POST":
        details = request.form
        if "new_name" in details:
            recipe_name = details["recipe_name"]
            new_name = details["new_name"]
            cur = mysql.connection.cursor()
            cur.execute("UPDATE recipes SET recipe_name = (%s) WHERE recipe_name = (%s);", (new_name, recipe_name))
        elif "ingredient_name" in details:
            ingredient_name = details["ingredient_name"]
            cur = mysql.connection.cursor()
            cur.execute("SELECT id FROM ingredients WHERE ingredient_name = (%s)", [ingredient_name])
            ingredient_id = cur.fetchall()
            mysql.connection.commit()
            cur.execute("DELETE IGNORE FROM recipe_ingredients WHERE ingredient_id = (%s);", [ingredient_id])
            mysql.connection.commit()
            cur.execute("DELETE FROM ingredients WHERE ingredient_name = (%s);", [ingredient_name])
        else:
            recipe_name = details["recipe_name"]
            cur = mysql.connection.cursor()
            cur.execute("SELECT id FROM recipes WHERE recipe_name = (%s)", [recipe_name])
            recipe_id = cur.fetchall()
            mysql.connection.commit()
            cur.execute("DELETE IGNORE FROM recipe_ingredients WHERE recipe_id = (%s);", [recipe_id])
            mysql.connection.commit()
            cur.execute("DELETE FROM recipes WHERE recipe_name = (%s);", [recipe_name])
        mysql.connection.commit()
        cur.close()
        return redirect("/browse")
    return render_template('mvp.html', title = "MINIMUM VIABILITY", recipes = r_names, ingredients = i_names)

if __name__ == '__main__':
    app.run('0.0.0.0', debug = True)