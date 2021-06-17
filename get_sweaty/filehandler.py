from datetime import datetime
import json

# datetime ist ein Modul in Python für das Verwalten von Daten und muss zuerst importiert werden
# datetime wird gebraucht für jeden neuen Nutzer und jede weitere BMI Berechnung bei bestehenden Nutzen
# das wird gebraucht für das Datum, welches im Diagramm angezeigt wird

# import json ist ein eingebautes Modul in Python welches die JSON als dictionary gliedert
# damit kann es auch als dictionary von python gelesen werden
# kann python dictionary auch als json string gliedern, damit es im json file geschrieben werden kann

# ALLGEMEIN: Dieses File enthält functionen, die gelesen, geschrieben, abgerufen werden von dem .json file (der DB).
# das .json file enthält die vorgängigen Berechnungen und E-Mail Adressen der User

# hier sind nur die Funktionen, die gemacht werden müssen. Sie sind nicht miteinander verknüpft
# das wird in main.py geregelt Siehe ab Zeile 64 in main.py

# Function um Datei zu lesen. Dieses File ist erst eine LIST (kein Dictionary). Startet und endet mit []
# read_file: brauchen wir um users.json zu "lesen" und den Content zu "returnen"
# um users.json zu ändern/bearbeiten, müssen wir sie zuerst lesen (read), dann ändern (modify) und dann speichern (save)
def read_file(filename):
    # Die Datei mit dem Dateinamen in der Function/Argument versuchen zu öffnen
    try:
        # mit with open wird die "Verbindung" zum json file hergestellt, geöffnet und gelesen (als string)
        with open(filename) as file:
            try:
                # Die Daten in der Datei speichern
                # Konvertiert string welches von json file returned wird in ein python dictionary
                # "Gegenteil" von Zeile 51
                file_as_list = json.load(file)
            # Falls die Datei exisitiert aber leer ist, soll eine leere Liste eröffnet werden
            except:
                file_as_list = []
    # Falls die Datei NICHT gefunden wird, soll eine leere Liste eröffnet werden
    except FileNotFoundError:
        file_as_list = []

    # Die Daten sollen "returned" werden.
    return file_as_list


# Funktion um einen neuen Eintrag zu machen
# Die Datei wird gelesen, ein Dictionary wird erstellt und die Datei wird gespeichert
def write_entry(filename, dictionary):
    # Zuerst lesen wir die Datei mit file name welches als Argument erfasst wurde
    file_as_list = read_file(filename)
    # Das Dictionary hinzufügen, welches als Argument dictionary erfasst wurde
    file_as_list.append(dictionary)

    # Die Datei speichern
    # w steht für write --> wir wollen ja in diesem file etwas schreiben, nicht nur lesen
    # lesen wäre r - aber wird nicht angegeben sondern nur open() geschrieben
    with open(filename, "w") as file:
        # json.dump = convertiert file_as_list in json string, damit es in file erfasst werden kann
        # "Gegenteil" von Zeile 27
        # default (vorgabe) =str - wir geben vor, dass die werte im dictionary oder list string sein müssen
        # Die Daten sind daten von datetime, welche im json file nicht geschrieben werden können
        #wir verwandeln diese Daten in ein String, damit sie im json file geschrieben werden könne
        json.dump(file_as_list, file, default=str)


# Funktion überprüft ob der Nutzer mit angegebener Email in der Datei existiert
# Falls der Nutzer gefunden wird, wird der nutzer zurückgegeben. Falls nicht wird False "returned"
def find_user(filename, email):
    # Die Datei lesen
    file_as_list = read_file(filename)

    # Für jeden Nutzer in der Datei, machen wir folgendes...
    # For loop wird gestartet. Da es ein For Loop ist braucht es kein else
    # beim else würde es sonst beim ersten user der nicht passt ein false ausgeben aber wir wollen ja weitersuchen
    for user in file_as_list:
        # Falls der Nutzer die gleiche E-Mail Adresse hat wie der Wert in dem Argument
        if user["email"] == email:
            # Return den übereinstimmenden Nutzer
            return user

    # Falls kein Nutzer gefunden wurde,
    return False


# Diese Funktion wird gebraucht, wenn die Funktion find_user false ist
# Mit dieser Funktion erstellen wir einen neuen Nutzer und eröffnen ihn in der Datei
def create_user(filename, email, bmi):
    # Das Datum holen, an dem der Eintrag gemacht wird
    created_at = datetime.now()
    # Den Nutzer mit den Daten aus dem ARgument eröffnen/erstellen
    user = {
        "email": email,
        "bmi": [bmi],
        "createdAt": created_at
    }
    # In unserer Datei erfasesn wir den neuen Nutzer
    write_entry(filename, user)

    # Sobald das erledigt wurde, soll uns der User "returned" werden
    return user


# Funktion wird gebraucht, wenn find_user einen Nutzer findet und diesen als Dictionary "returned"
# Dann wird die neue BMI Berechnung zu seinem Dictionary hinzugefügt
# Funktion sucht den existierenden Nutzer und ersetzt ihn mit dem modifizierten Nutzer (alte + neue Daten)
def modify_user(filename, user_modified):
    # Die Datei wird gelesen
    file_as_list = read_file(filename)

    # Für jeden Nutzer der gespeichert ist, machen wir...
    for index, user in enumerate(file_as_list):
        # Wenn die Email die gleiche ist wie ein "gesuchter" Nutzer...
        if user["email"] == user_modified["email"]:
            # Ändern wir die ursprüngliche Datei und ersetzen die alten mit den neuen Daten
            file_as_list[index] = user_modified

    # Die Datei wird mit den neuen Daten gespeichert
    with open(filename, "w") as file:
        json.dump(file_as_list, file, default=str)
