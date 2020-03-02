BEGIN;
​
DROP TABLE IF EXISTS ingredients;
​
CREATE TABLE ingredients (
    id INT(5) NOT NULL AUTO_INCREMENT,
    ingredient_name VARCHAR(30) NOT NULL,
    ingredient_type VARCHAR(10) NOT NULL,
    PRIMARY KEY(id)
);

DROP TABLE IF EXISTS recipes;
​
CREATE TABLE recipes (
    id INT(5) NOT NULL AUTO_INCREMENT,
    recipe_name VARCHAR(50) NOT NULL,
    recipe_method VARCHAR(10000) NOT NULL,
    PRIMARY KEY(id)
);

DROP TABLE IF EXISTS recipe_ingredients;
​
CREATE TABLE recipe_ingredients (
    id INT(5) NOT NULL AUTO_INCREMENT,
    recipe_id INT(5) NOT NULL,
    ingredient_id INT(5) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(recipe_id) REFERENCES recipes(id),
    FOREIGN KEY(ingredient_id) REFERENCES ingredients(id)
);
​
COMMIT;