# Aufgabe: Neue Rule erstellen

Die Aufgabe ist es, eine Mini-Version von "wohni" anhand von Feedback aus der Sachbearbeitung zu erweitern.

Zunächst ein **kleiner Überblick** über das Repo:

- `antrag.py`: Vereinfachte Darstellung eines Wohngeld-Antrags der von Bürger:innen ausgefüllt und eingereicht wird.
- `nachweise.py`: Verschiedene "Nachweise", die neben dem Antrag eingereicht werden müssen (bspw. ein Mietvertrag).
- `anforderungen.py`: Jede `Anforderung` ist eine Information, die von den Bürger:innen nachgewiesen werden muss, damit der Wohngeld-Antrag bearbeitet werden kann. Eine `Anforderung` hat eine Funktion `ist_erfuellt`, die insbesondere anhand der eingereichten Nachweise prüft, ob sie bereits erfüllt wurde.
- `rules.py`: Je nach Antrag sind nur bestimmte Anforderungen relevant. Bei einem Antrag von einem Rentner muss bspw. ein Rentenbescheid angefordert werden; bei einer 20-jährigen Studentin ergibt das aber keinen Sinn. Jede `Rule` entscheidet anhand des Antrags oder der Nachweise, ob bestimmte Anforderungen relevant sind und fügt sie dementsprechend hinzu.
- `main.py` spielt die Logik von wohni in vereinfachter Form einmal durch:
  1. Ein Antrag inkl. Nachweise wird eingelesen.
  2. Jede `Rule` wird darauf ausgeführt und die resultierenden `Anforderungen` werden gesammelt.
  3. Für jede `Anforderung` wird geprüft, ob sie bereits erfüllt wurde, oder ob sie noch einmal von Antragsteller:in angefragt werden muss.
  4. Alle erfüllten und unerfüllten `Anforderungen` werden ausgegeben. Außerdem werden Hinweise an die Sachbearbeitung angezeigt.

Nun kommen wir zu **deiner Aufgabe**: Jens hat unten ein neues Issue erstellt. Überlege dir, wie das Issue umgesetzt werden kann, und **implementiere dementsprechend eine neue Rule** (und ggf. andere kleinen Änderungen).

### Issue: Hinweis wenn Antragsteller nicht im Mietvertrag steht

Antragsteller ist dann nicht antragsberechtigt. Beispiel: Siehe `wohngeld_antrag_student` in `beispiel_antrag.py`.

Zusätzliches Feedback aus der Sachbearbeitung:

> Grundsätzlich kann nur die Person, den Antrag stellen, die auch den Mietvertrag unterschrieben hat. Der Name des Antragstellers muss also im Mietvertrag stehen.
> 
> Hiervon gibt es aber eine Ausnahme. Es kann auch sein, dass ein Haushaltsmitglied, bspw. der Ehe-/Partner den Mietvertrag unterschrieben hat und auch nur als alleiniger Mieter aufgeführt ist. Hier wird aber vermutet, dass diese Person den Wohngeldantragsteller beauftragt hat, den Antrag zu stellen.
> 
> Der Name der Person im Mietvertrag muss dann aber im Antrag unter Haushaltsmitgliedern zu finden sein. Diese Konstellation kommt relativ häufig vor und bedarf dann auch keiner weiteren Nachfrage.
> 
> Nur wenn weitere Personen im Mietvertrag stehen, die nicht im Antrag als Haushaltsmitglied aufgeführt sind, muss nachgefragt werden. Klassische Fälle hierfür sind WGs oder Bürgschaften.

Eventuell hat der Hinweis zwei "Stufen":

- Obacht Antragsteller steht nicht im Mietvertrag
- Obacht NIEMAND aus dem Haushalt steht im Mietvertrag

## Hinweise zur Umsetzung

Wir gehen davon aus, dass die Aufgabe mit etwas Python-Erfahrung in etwa 90 Minuten umsetzbar ist.

Du darfst als Hilfsmittel alle Werkzeuge nutzen, die du auch im echten Alltag nutzen würdest (inkl. beliebiger LLMs).
# formal_task
