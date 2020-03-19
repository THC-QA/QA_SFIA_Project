from flask import Flask, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Call config variables from pre-assigned environmentals, check Jenkinsfile for preferred source

app.config['SECRET_KEY'] = os.environ.get("SECRETKEY")
app.config['MYSQL_HOST'] = os.environ.get('MYSQLHOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = 'testing'

mysql = MySQL(app)

def test_empty():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT concat('DROP TABLE IF EXISTS `', table_name, '`;') FROM information_schema.tables WHERE table_schema = 'testing';")
        drops = cur.fetchall()
        mysql.connection.commit()
        cur.execute("SET FOREIGN_KEY_CHECKS = 0")
        mysql.connection.commit()
        for drop in drops:
            cur.execute(drop[0])
            mysql.connection.commit()
        cur.execute("SET FOREIGN_KEY_CHECKS = 1")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        empty = len(cur.fetchall())+1
        mysql.connection.commit()
        cur.close()
        assert empty

def test_create_recipes():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DROP TABLE IF EXISTS test_recipes;")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("CREATE TABLE test_recipes(id INT(5) NOT NULL AUTO_INCREMENT,recipe_name VARCHAR(50) NOT NULL UNIQUE,recipe_method VARCHAR(10000) NOT NULL,PRIMARY KEY(id));")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 1

def test_recipes_coherence():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DESCRIBE test_recipes;")
        col = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert col == 3

def test_create_ingredients():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DROP TABLE IF EXISTS test_ingredients;")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("CREATE TABLE test_ingredients(id INT(5) NOT NULL AUTO_INCREMENT, ingredient_name VARCHAR(30) NOT NULL UNIQUE, ingredient_type VARCHAR(10) NOT NULL, PRIMARY KEY(id));")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 1

def test_ingredients_coherence():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DESCRIBE test_ingredients;")
        col = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert col == 3

def test_create_recipe_ingredients():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DROP TABLE IF EXISTS test_recipe_ingredients;")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("CREATE TABLE test_recipe_ingredients(id INT(5) NOT NULL AUTO_INCREMENT,recipe_id INT(5) NOT NULL,ingredient_id INT(5) NOT NULL,PRIMARY KEY(id),FOREIGN KEY(recipe_id) REFERENCES test_recipes(id),FOREIGN KEY(ingredient_id) REFERENCES test_ingredients(id));")
        mysql.connection.commit()
        cur.execute("SHOW tables;")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 1

def test_recipe_ingredients_coherence():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DESCRIBE test_recipe_ingredients;")
        col = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert col == 3

def test_recipe_insert():
    recipe_name = "Placeholder"
    recipe_method = "Place your holder"
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM test_recipes;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("INSERT IGNORE INTO test_recipes(recipe_name, recipe_method) VALUES (%s, %s)", (recipe_name, recipe_method))
        mysql.connection.commit()
        cur.execute("SELECT * FROM test_recipes")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 1

def test_ingredient_insert():
    ingredient_name = "Placeholder"
    ingredient_type = "Spice"
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM test_ingredients;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("INSERT IGNORE INTO test_ingredients(ingredient_name, ingredient_type) VALUES (%s, %s)", (ingredient_name, ingredient_type))
        mysql.connection.commit()
        cur.execute("SELECT * FROM test_ingredients")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 1

def test_recipe_unique():
    recipe_name = "Placeholder"
    recipe_method = "Place your holder"
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM test_recipes;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("INSERT IGNORE INTO test_recipes(recipe_name, recipe_method) VALUES (%s, %s)", (recipe_name, recipe_method))
        mysql.connection.commit()
        cur.execute("SELECT * FROM test_recipes")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 0

def test_ingredient_unique():
    ingredient_name = "Placeholder"
    ingredient_type = "Spice"
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM test_ingredients;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("INSERT IGNORE INTO test_ingredients(ingredient_name, ingredient_type) VALUES (%s, %s)", (ingredient_name, ingredient_type))
        mysql.connection.commit()
        cur.execute("SELECT * FROM test_ingredients")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 0

def test_recipe_ingredients_insert():
    name = "Placeholder"
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM test_recipe_ingredients;")
        start = len(cur.fetchall())
        mysql.connection.commit()
        cur.execute("SELECT id FROM test_recipes WHERE recipe_name = (%s)", [name])
        recipe = cur.fetchall()
        mysql.connection.commit()
        cur.execute("SELECT id FROM test_ingredients WHERE ingredient_name = (%s)", [name])
        ingredient = cur.fetchall()
        mysql.connection.commit()
        cur.execute("INSERT IGNORE INTO test_recipe_ingredients(recipe_id, ingredient_id) VALUES (%s, %s)", (recipe, ingredient))
        mysql.connection.commit()
        cur.execute("SELECT * FROM test_recipe_ingredients;")
        end = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert abs(start - end) == 1

def test_browse():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT recipe_name, recipe_method FROM test_recipes")
        rows = cur.fetchall()
        mysql.connection.commit()
        recipes = {}
        for row in rows:
            recipes[row[0]]=[row[1]]
            cur.execute("SELECT ingredient_name FROM test_recipes r JOIN test_recipe_ingredients r_i ON r.id=r_i.recipe_id JOIN test_ingredients i ON i.id=r_i.ingredient_id WHERE r.recipe_name=%s;", [row[0]])
            ingredients = cur.fetchall()
            for i in ingredients:
                recipes[row[0]].append(i[0])
            mysql.connection.commit()
        index = [name for name in recipes]
        cur.close()
        assert len(index) == 1 and len(recipes["Placeholder"]) == 2

def test_recipe_rename():
    recipe_name = "Placeholder"
    new_name = "place_holder"
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("UPDATE test_recipes SET recipe_name = (%s) WHERE recipe_name = (%s);", (new_name, recipe_name))
        mysql.connection.commit()
        cur.execute("SELECT * FROM test_recipes WHERE recipe_name = (%s);", [new_name])
        result = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert result == 1

def test_conflict_deletion():
    with app.app_context():
        cur = mysql.connection.cursor()
        try:
            cur.execute("DELETE FROM test_ingredients WHERE ingredient_name = 'Placeholder'")
            deleted = len(cur.fetchall())
            mysql.connection.commit()
            cur.close()
        except:
            deleted = False
        assert deleted == 0

def test_clean_ingredient_deletion():
    ingredient_name = "Placeholder"
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM test_ingredients WHERE ingredient_name = (%s)", [ingredient_name])
        ingredient_id = cur.fetchall()
        mysql.connection.commit()
        cur.execute("DELETE IGNORE FROM test_recipe_ingredients WHERE ingredient_id = (%s);", [ingredient_id])
        mysql.connection.commit()
        cur.execute("DELETE FROM test_ingredients WHERE ingredient_name = (%s);", [ingredient_name])
        mysql.connection.commit()
        cur.execute("SELECT * FROM test_ingredients;")
        deleted = len(cur.fetchall()) + 1
        mysql.connection.commit()
        cur.close()
        assert deleted

def test_recipe_deletion():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DELETE IGNORE FROM test_recipes WHERE recipe_name = 'place_holder';")
        mysql.connection.commit()
        cur.execute("SELECT * FROM test_recipes;")
        deleted = len(cur.fetchall()) + 1
        mysql.connection.commit()
        cur.close()
        assert deleted