def calorie_calculator(we, he, ag, ge, ac, go):
    # Enter your weight in kg:
    weight = int(we)
    # Enter your height in cm:
    height = int(he)
    # Enter your age in years:
    age = int(ag)
    # Enter your gender (female/male):
    gender = ge
    # How active are you on a scale from 1 to 5?
    activity = int(ac)
    # What is your goal (lose/maintain/build)?
    goal = go

    # BMR: basial metabolic rate
    # PMRW: performance metabolic rate work (daily business) + BMR
    # SPTO: sport performance turn over (sport). PAL (physical activity level) berücksichtigen

    if (gender == "female"):
        bmr = (655 + (9.6 * weight) + (1.8 * height) - (4.7 * age))
    elif (gender == "male"):
        bmr = (66 + (13.7 * weight) + (5 * height) - (6.8 * age))

    # daily PAL Faktor bei Aktivitäten 3 bis 5 gleich (1.6) aber sport PAL anderst 2.4-2.6
    if (activity == 1):
        pmrw = ((1.2 - 1) * bmr) + bmr
        spto = 0
    elif (activity == 2):
        pmrw = ((1.4 - 1) * bmr)
        spto = ((((2.4 - 1) * bmr) * 2) / 24) * 2
    elif (activity == 3) or (activity == 4) or (activity == 5):
        pmrw = ((1.6 - 1) * bmr)
        if (activity == 3):
            spto = ((((2.4 - 1) * bmr) * 2) / 24) * 4
        elif (activity == 4):
            spto = ((((2.5 - 1) * bmr) * 2) / 24) * 5
        elif (activity == 5):
            spto = ((((2.6 - 1) * bmr) * 2) / 24) * 6

    pmrw_bmr = bmr + pmrw
    spto_bmr = bmr + spto

    # lose = Kaloriendefizit von 25%
    # maintain = Grundumsatz
    # build = Kalorienüberschuss von 20%

    if (goal == "lose"):
        factor = 0.75
    elif (goal == "maintain"):
        factor = 1
    elif (goal == "build"):
        factor = 1.2

    if (activity == 1):
        result = (pmrw) * factor
    elif (activity == 2):
        result = (((5 * pmrw_bmr) + (2 * spto_bmr)) / 7) * factor
    elif (activity == 3):
        result = (((3 * pmrw_bmr) + (4 * spto_bmr)) / 7) * factor
    elif (activity == 4):
        result = (((2 * pmrw_bmr) + (5 * spto_bmr)) / 7) * factor
    elif (activity == 5):
        result = (((1 * pmrw_bmr) + (6 * spto_bmr)) / 7) * factor

    # Das Resultat der Kalorienberechnung wird als vollständige Nummer (int) ausgeegeben
    return int(result)


def bmi_calculator(we, he):
    weight = int(we)
    height = int(he)

    # pow = Power. Ist in Python für hochgestellte nummern. Also Grösse/100 hoch 2
    result = weight / pow((height / 100), 2)

    # Die BMI Berechnung wird "returned"
    #round, 1 = es wird nach dem Komma auf eine Stelle gerundet
    return round(result, 1)

