from caloriecalculator import calorie_calculator, bmi_calculator
from filehandler import find_user, create_user, modify_user
from datetime import datetime
from flask import Flask
from flask import render_template
# render template für Verbindung zu html Seiten
from flask import request
# für das Formular
from forms import CalorieForm

# Ich habe sie Formulare SignUpForm und CalorieForm in forms.py genannt

app = Flask(__name__)
app.config["SECRET_KEY"] = "kerrystieger"
# braucht es um alles laufen zu lassen?

local_file_name = "users.json"
# Hier sagen wir, wie die Datei heisst, wo alles gespeichert wird.
# Sobald die erste Berechnung gemacht wird, wird die Datei , im gleichen Ordner wie main.py ist erstellt
# Bei weiteren Berechnungen wird sie immer aktualisiert

@app.route("/home")
def home():
    return render_template("index.html", sunny=True, author="Kerry")
# nach dem Schrägstich ist das, was ich im Link eingeben muss, damit die Seite erscheint


# GET: Data verlangen
# POST: Data eingeben/hinzufügen
@app.route("/nutrition", methods=["GET", "POST"])
def nutrition():
    form = CalorieForm(request.form)
    # Falls es ein POST request ist. Im HTML file wird dann definiert, dass das POST aus py geschickt wird
    if request.method == 'POST' and form.validate():
        # Jeder Input vom Formular einholen
        # form validate - form bezieht sich auf Calorie Form. Da haben wir Widgets definiert mit min und max
        # form validate überprüft ob sich der Wert zwischen min und max befindet
        # falls nicht retourniert form validate "False" und IF wird gar nicht erst ausgeführt
        # stattdessen wird ELSE ausgeführt und der Error wird angezeigt
        weight = request.form.get("weight")
        height = request.form.get("height")
        age = request.form.get("age")
        gender = request.form.get("gender")
        activity = request.form.get("activity")
        goal = request.form.get("goal")
        # Die Werte an die Hauptfunktion übergeben und die Berechnung duchführen
        result = calorie_calculator(weight, height, age, gender, activity, goal)

        # Die E-Mail vom Nutzer holen
        email = request.form.get("email")
        # Den BMI Wert berechnen
        bmi = bmi_calculator(weight, height)
        # Den Gewichtsstatus anhand vom BMI zuordnen
        if bmi <= 18.5:
            status = "underweight"
        elif bmi <= 24.99:
            status = "normal weight"
        elif bmi <= 29.99:
            status = "overweight"
        else:
            status = "obese"

        # Hier überprüfen wir, ob der Nutzer bereits exisitiert
        # user wird sein,w as auch immer diese Funktion zurückgibt. Also entweder der User oder False
        # dann wird unten ab Zeile 74 gesagt was gemacht wird.
        user = find_user(local_file_name, email)
        # ein Dictionary erstellen um Daten zu speichern mit Datum im mm/dd/yyyy Format
        bmi_dict = {
            "value": bmi,
            "date": datetime.today().strftime('%m/%d/%Y')
        }

        # Falls der Nutzer nicht gefunden wurde (False)
        if (user == False):
            # Einen neuen Nutzer erstellen (create)
            user = create_user(local_file_name, email, bmi_dict)
        # Falls der user schon exisitiert (else)
        else:
            # Heutiger BMI Wert zu den anderen bereits verzeichnenten hinzufügen
            user["bmi"].append(bmi_dict)
            # User im lokalen File modifizieren
            modify_user(local_file_name, user)

        # Variablen angeben, die das Diagramm braucht für die Darstellung
        chart_data = {
            "values": [],
            "labels": []
        }
        # Für jeden BMI Eintrag: Den Wert und das Datum in die Variablen für das Diagramm eingeben
        for bmi in user["bmi"]:
            chart_data["values"].append(bmi["value"])
            chart_data["labels"].append(bmi["date"])

        # Die nötigen Daten weiter geben zum "rendern"
        return render_template("nutrition-results.html", result=result, status=status, goal=goal, chart_data=chart_data)
    # Falls das eine POST request ist und das eingereichte Formular nicht gültig ist
    elif request.method == 'POST':
        # Zeige die Error Meldung
        print(form.errors)
        # Error als wahr (true) anzeigen und  resultate rendern
        return render_template("nutrition-results.html", error=True)
    # Wenn das eine GET Anforderung ist mit keiner Einreichung
    return render_template("nutrition.html", form=form)

# form = form, Form kommt von forms.py wo wir in geschwungenen Klammern sachen genannt haben form.username.label


if __name__ == "__main__":
    app.run(debug=True, port=5000)
