Projekt-Idee:
Das Projekt wird ein Kalorienrechner. Der Nutzer kann sämtliche Daten eingeben und erhält dann einen Vorschlag zurück.
Dem Nutzer wird auch der BMI-Wert angezeigt.
ie Daten, die der Nutzer eingibt werden gespeichert. Wenn der Nutzer auf die Seite zurückkehrt und eine weitere Berechnung startet,
überprüft das System, ob er bereits hier war und gibt ihm dann neben der neuen Berechnung auch ein Diagramm zurück.
Das Diagramm zeigt den Verlauf von seinem BMI-Wert (mit Datum).

Der Nutzer wird für das Diagramm nach der E-Mail Adresse gefragt. Mit dieser wird der Nutzer jeweils identiziert.
Wenn jemand mit dieser E-Mail Adresse etwas sucht, wird das .json file durchsucht, ob dieser Nutzer schon exisistiert.
Falls ja, werden die alten Daten aufgerufen und angezeigt. Im Hintergrund werden die alten mit den neuen ergänzt
und der Nutzer wird überschrieben.
Falls noch kein Nutzer besteht, wird ein Neuer automatisch angelegt.

So sieht der Nutzer wie sich sein BMI-Wert verändert hat und wie viele Kalorien zu
seinem jetzigen Gewicht und Ziel passen.