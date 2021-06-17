from flask_wtf import FlaskForm
from wtforms import StringField, StringField, SubmitField, SelectField, validators
# WTForms HTML5 fields for number validation and email
from wtforms.fields.html5 import IntegerField, EmailField
from wtforms.widgets.html5 import NumberInput


class CalorieForm(FlaskForm):
    # Email field
    email = EmailField("Email address: ", [validators.DataRequired(), validators.Email()])
    # Feld wird hier erstellt. "Gedruckt" wird es im HTML Zeile 13
    # Data Required sagt, dass das das Feld einen Input braucht
    # validators Email sagt, dass der Input eine Mail-Adresse sein muss (kein Abstand, emthält @ und endet mit .com o.ä

    # Integer Felder. Falls kein Integer eingegeben wird kommt ein Error
    weight = IntegerField("Enter your weight in KG: ", widget=NumberInput(min=5, max=300, step=1))
    height = IntegerField("Enter your height in CM: ", widget=NumberInput(min=10, max=300, step=1))
    age = IntegerField("Enter your age in years: ", widget=NumberInput(min=1, max=150, step=1))
    # Auswahl Felder. Choices enthält Felder mit den verfügbaren Optionen (value, label)
    gender = SelectField("Enter your gender: ", choices=[("female", "Female"), ("male", "Male")])
    activity = SelectField("How active are you on a scale from 1 to 5?",
                           choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])
    goal = SelectField("What is your goal?",
                       choices=[("lose", "Lose Weight"), ("maintain", "Maintain Weight"), ("build", "Build Weight")])
    submit = SubmitField("Calculate")

