BEGIN;

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Scotch Bonnet", "Chilli");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Birds Eye", "Chilli");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Serrano", "Chilli");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Thai Red", "Chilli");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Red Onion", "Vegetable");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Garlic Bulb", "Vegetable");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Cherry Tomato", "Vegetable");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Romano Pepper", "Vegetable");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Mango", "Fruit");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Pineapple", "Fruit");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Lime", "Fruit");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Coriander", "Herb");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Apple Cider Vinegar", "Liquid");

INSERT IGNORE INTO ingredients (ingredient_name, ingredient_type)
VALUES ("Orange/Mango Juice", "Liquid");

INSERT IGNORE INTO recipes (recipe_name, recipe_method)
VALUES ("Scotch Sunrise", "4 Scotch Bonnets, 4 Birds Eye, 8 Serrano, 11 Thai Red, 1 Red Onion, 1 Romano Peppr, 1/2 bulb of Garlic, 15 Cherry Tomatoes, 1 Mango, 1 small sweet Pineapple, 1 bunch Coriander, 1 bottle Raw Apple Cider Vinegar, juice and zest of 2 limes, Orange/Mango fresh juice. Roast all the fruit and veg excepting coriander @ 200*C for 30 mins, blend with liquid and coriander. Simmer for 20 minutes, then blend again. Bottle in a sterilised jar or bottle.");

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Scotch Bonnet"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Birds Eye"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Serrano"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Thai Red"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Red Onion"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Garlic Bulb"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Cherry Tomato"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Romano Pepper"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Mango"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Pineapple"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Lime"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Coriander"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Apple Cider Vinegar"));

INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id)
VALUES ((SELECT id FROM recipes WHERE recipe_name = "Scotch Sunrise"), (SELECT id FROM ingredients WHERE ingredient_name = "Orange/Mango Juice"));

COMMIT;