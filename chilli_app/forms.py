from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length
class recipe_form(FlaskForm):
    recipe_name = StringField('Recipe Name',
        validators = [
            DataRequired(),
            Length(min=4, max=50)
            ]
        )
    recipe_method = TextAreaField('Recipe Instructions',
        validators = [
            DataRequired(),
            Length(min=10, max=10000)
            ]
        )
    submit = SubmitField("Post Recipe")
class ingredient_form(FlaskForm):
    ingredient_name = StringField("Ingredient Name",
        validators = [
            DataRequired(),
            Length(min=4, max=50)
            ]
        )
    ingredient_type = SelectField(u"Ingredient Type",
        choices = [
            ("Chilli", "Chilli"),
            ("Vegetable", "Vegetable"),
            ("Fruit", "Fruit"),
            ("Herb", "Herb"),
            ("Spice", "Spice"),
            ("Liquid", "Liquid")
        ])
    submit = SubmitField("Post Ingredient")
class update_form(FlaskForm):
    # form requires outside assignment of dynamic values for the select fields, but can't be done with the binary form choice, so was dropped
    def __init__(self,r_names, i_names):
        self.r_names = r_names
        self.i_names = i_names
    table_selection = SelectField(u"Select a Table",
        choices = [
            ("RECIPES", "recipes"),
            ("INGREDIENTS", "ingredients"),
        ])
    if table_selection == "recipes":
        self.name.choices = self.r_names
        name = SelectField(u"Select a Recipe",)
        new_name = StringField('New Name',
        validators = [
            DataRequired(),
            Length(min=4, max=50)
            ]
        )
    elif table_selection == "ingredients":
        self.name.choices = self.i_names
        name = SelectField(u"Select an Ingredient")
        new_name = StringField("Ingredient Name",
        validators = [
            DataRequired(),
            Length(min=4, max=50)
            ]
        )
    submit = SubmitField("Update Records")