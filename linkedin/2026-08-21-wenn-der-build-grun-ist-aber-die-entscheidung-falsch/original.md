# Wenn der Build grün ist, aber die Entscheidung falsch

**Coding-Agenten können heute Repositories analysieren, Implementierungen planen, Dateien ändern, Shell-Befehle ausführen, Tests reparieren und Aufgaben parallel bearbeiten. Damit wächst aber auch die Zahl der Entscheidungen, die zwischen Anforderung und fertigem Code getroffen werden, bevor ein Mensch sie überhaupt sieht. Ein kleiner Fehler aus einem One-Shot-Experiment zeigt, warum genau diese Entscheidungen zum neuen Review-Gegenstand werden könnten.**

Der Fehler war unspektakulär.

Eine kleine Anwendung sollte vorhandene Review-Dateien nicht überschreiben. Wenn bereits ein `editorial-review.md` existierte, sollte beim nächsten Durchlauf eine neue Datei entstehen.

Der Coding-Agent setzte die Anforderung sauber um.

Nach dem zweiten Durchlauf lagen zwei Dateien im Projekt:

```text
editorial-review.md
editorial-review-2.md
```

Keine Datei wurde überschrieben. Die Tests waren grün.

Nur verwendete der nächste Verarbeitungsschritt wieder `editorial-review.md`.

Der neuere Review existierte, wurde aber ignoriert.

Im anschließenden Produkttest wurde genau dieses Verhalten als schwerwiegender Fehler eingestuft: Neue Review-Varianten wurden korrekt erzeugt, Tree, Checks und der nächste Rewrite blieben jedoch beim ersten kanonischen Dateinamen.

Das Interessante daran ist nicht der Bug.

Interessant ist, dass auf dem Weg dorthin erstaunlich viel **richtig** war.

Die Anforderung „nicht überschreiben“ wurde erfüllt. Die Implementierung war konsistent. Die vorhandenen Tests bestanden. Die nicht-destruktive Dateierzeugung funktionierte.

Falsch war eine Entscheidung, die ich nie ausdrücklich getroffen hatte.

Was ich geschrieben hatte, war:

> Bestehende Reviews dürfen nicht überschrieben werden.

Was ich gemeint hatte, war zusätzlich:

> Die neu erzeugte Variante wird anschließend zur aktuell relevanten Variante.

Der zweite Satz stand nur nicht da.

## Der Fehler liegt eine Ebene vor dem Code

Das ist ein altes Problem der Softwareentwicklung. Anforderungen sind unvollständig, Begriffe mehrdeutig und Menschen setzen gemeinsames Vorwissen voraus. Entwickler treffen während der Umsetzung ständig kleine Entscheidungen, die in keinem Ticket stehen.

Neu ist nicht, dass solche Lücken existieren.

Neu ist, **wie schnell und wie weit sie heute durch einen Entwicklungsprozess laufen können, bevor wieder ein Mensch eingreift.**

Mein eigener KI-Workflow begann 2022 und 2023 noch mit sehr sichtbarer Handarbeit: Code aus der IDE ins Chatfenster kopieren, Antwort lesen, zurückkopieren, ausprobieren, Fehlermeldung wieder in den Chat tragen.

Später ließ ich im Chat Anforderungen und Spezifikationen ausarbeiten und endete regelmäßig mit dem Satz:

> Erstelle daraus bitte einen Prompt, den ich 1:1 an Codex weitergeben kann.

Ich war die Schnittstelle zwischen den Systemen.

Heute kann ein Coding-Agent einen erheblichen Teil dieser Strecke selbst zurücklegen.

Damit verschwinden die Entscheidungen nicht. Es verschwinden zunächst die Stellen, an denen ich sie zwangsläufig bemerken musste.

## Vom Codevorschlag zur delegierten Aufgabe

Als GitHub Copilot 2021 als Technical Preview startete, war der Aktionsradius noch überschaubar: Das System nutzte den aktuellen Code als Kontext und schlug beim Schreiben einzelne Zeilen oder ganze Funktionen vor. Der Entwickler schrieb, Copilot ergänzte.

Mit ChatGPT kam Ende 2022 der dialogische Schritt hinzu. Code konnte außerhalb der IDE diskutiert und debuggt werden. Der Kontext wurde größer, aber der Mensch musste ihn weitgehend selbst auswählen und zwischen Entwicklungsumgebung und Modell transportieren.

Mit Coding-Agenten verschob sich diese Grenze grundlegend. Aktuelle Agentensysteme können selbst relevante Dateien suchen, mehrere Dateien verändern, Shell-Befehle aufrufen und ihre Arbeit anhand von Test-, Linter- oder Build-Ergebnissen korrigieren. OpenAI beschreibt den Kern von Codex ausdrücklich als „Agent Loop“, der die Interaktion zwischen Benutzer, Modell und Werkzeugen orchestriert.

2026 kommt zunehmend Parallelisierung dazu. Die Codex-App ist darauf ausgelegt, mehrere Agenten in getrennten Threads und isolierten Git-Worktrees parallel an Projekten arbeiten zu lassen. Damit wird nicht nur Codegenerierung parallelisiert, sondern potenziell auch Exploration, Implementierung und Gegenprüfung.

Aus „ergänze diesen Code“ ist damit innerhalb weniger Jahre „bearbeite diese Aufgabe“ geworden.

Das vergrößert nicht nur den Umfang dessen, was die KI erledigen kann.

Es vergrößert auch den Raum, in dem sie selbst Entscheidungen treffen muss.

## Der Agent implementiert nicht nur – er füllt Lücken

Ein aktueller Agentenlauf besteht technisch aus Schleifen. Das Modell bekommt Kontext, entscheidet über den nächsten Schritt, benutzt gegebenenfalls ein Werkzeug, nimmt dessen Ergebnis wieder in den Kontext auf und entscheidet weiter.

Dabei entstehen zwangsläufig Entscheidungen:

Welche Dateien sind relevant?

Welche vorhandene Architektur wird fortgesetzt?

Welche Bibliothek wird verwendet?

Wie wird ein nicht vollständig beschriebener Zustand modelliert?

Welcher Test repräsentiert eine Anforderung?

Und was folgt aus einem fehlgeschlagenen Test?

Das sind nicht zwangsläufig große Architekturentscheidungen. Oft sind es kleine Dinge.

In meinem Beispiel war eine davon:

> Wie finde ich den aktuellen Review?

Eine plausible Antwort lautet:

> Über den kanonischen Pfad `editorial-review.md`.

Eine andere:

> Über die zuletzt erzeugte Variante.

Eine dritte:

> Über eine explizit gespeicherte Referenz auf den aktiven Review.

Alle drei sind technisch denkbar.

Meine Anforderung beantwortete die Frage nicht.

Der Agent musste sie trotzdem beantworten, um Software zu bauen.

## Specs helfen – aber sie verschieben die Prüfung

Es ist deshalb kein Zufall, dass moderne Coding-Werkzeuge wieder stärker mit strukturierten Spezifikationen arbeiten.

GitHubs Spec Kit strukturiert einen Workflow über Spec, Plan, Tasks und Implementierung. Ergänzende Schritte können unklare Anforderungen vor der Planung klären oder später Konflikte und Lücken zwischen `spec.md`, `plan.md` und `tasks.md` suchen.

Kiro erzeugt ebenfalls Requirements, Design und konkrete Tasks. Im normalen Spec-Workflow können diese Artefakte zwischen den Phasen geprüft werden. Beim aktuellen Quick-Spec-Modus beantwortet der Benutzer zunächst Rückfragen; Requirements, Design und Tasks werden anschließend automatisch in einem Durchgang erzeugt, ohne Freigabe zwischen den Phasen. Kiro empfiehlt die Variante entsprechend eher für gut verstandene Aufgaben und explizite Review-Gates bei unbekanntem oder kritischem Terrain.

Das reduziert Mehrdeutigkeit.

Interessant wird es dort, wo derselbe Agent auch die Zwischenartefakte erzeugt.

Aus einer unvollständigen Anforderung kann zunächst eine plausible Requirement werden. Daraus entsteht ein dazu passendes Design, anschließend passende Tasks, Code und schließlich Tests.

Am Ende können sämtliche Artefakte miteinander konsistent sein.

Nur die erste Annahme war falsch.

Specs lösen dieses Problem deshalb nicht automatisch. Sie schaffen zusätzliche Stellen, an denen wir Annahmen prüfen **können** – sofern wir diese Stellen nicht ebenfalls vollständig überspringen.

## Ein Test kann eine falsche Interpretation perfekt bestätigen

Tests bleiben für agentische Entwicklung unverzichtbar. Vielleicht werden sie sogar wichtiger, weil sie dem Agenten ein maschinenlesbares Feedbacksignal geben: Test ausführen, Ergebnis interpretieren, Implementierung korrigieren, erneut testen.

Aber ein Test weiß nicht, was ich gemeint habe.

Er weiß, welche Bedingung er prüfen soll.

Bei meinem Review-Beispiel könnte ein vollkommen korrekter Test feststellen:

```text
Vorhandene Review-Datei bleibt unverändert.
Neue Review-Datei wird zusätzlich erzeugt.
```

Beide Bedingungen sind erfüllt.

Der Test sagt nichts darüber, welche Datei anschließend als aktuell gelten soll.

Eine interessante Parallele liefert die Diskussion um SWE-bench Verified. OpenAI stellte im Februar 2026 die Nutzung des Benchmarks für Frontier-Modellvergleiche ein und verwies unter anderem auf fehlerhafte Tests sowie Aufgaben, bei denen mehrere vernünftige Interpretationen möglich waren, die Tests jedoch nur eine davon akzeptierten.

Das ist kein Beweis für mein konkretes Agentenproblem.

Aber es illustriert denselben grundlegenden Unterschied:

**Aufgabenbeschreibung, tatsächliche Intention und automatisierte Prüfung sind drei verschiedene Dinge.**

Sie können übereinstimmen.

Sie müssen es nicht.

## Grün war auch mein Build

Im getesteten MVP bestanden 13 Unit-Tests. Typecheck und Compile waren erfolgreich. Das später rekonstruierte Worklog schätzte den entsprechenden menschlichen Entwicklungsaufwand auf 17 bis 25 Stunden.

Trotzdem fanden sich im anschließenden Produkttest zwei strukturell ähnliche Fehler.

Neben den ignorierten neuen Reviews gab es eine zweite Mehrdeutigkeit beim Projektstatus.

Nach einer bereits erzeugten Zielfassung wurde wieder an einem neuen Draft gearbeitet. Das Projekt selbst speicherte korrekt:

```text
stage: draft
activeDocument: first-draft-2.md
```

Die Oberfläche zeigte dagegen weiterhin „Zielfassung“.

Auch dafür gibt es zwei plausible Interpretationen von „aktueller Status“:

> Woran arbeitet der Benutzer gerade?

oder:

> Wie weit ist das Projekt bisher maximal gekommen?

Die Implementierung entschied sich für die zweite Variante. Für die Benutzerführung hatte ich die erste gemeint.

Auch hier war der Code nicht zufällig kaputt.

Er beantwortete nur eine offene Frage anders als ich.

Genau diese Fehlerklasse finde ich inzwischen interessanter als einen Build, der einfach rot wird.

## Aktivitätslogs beantworten die falsche Hälfte der Frage

Coding-Agenten liefern schon heute erheblich mehr Nachweise als ein klassisches Chatfenster. Diffs, Terminalausgaben, Tests, Sessions und parallele Arbeitsstränge lassen sich nachvollziehen. Die Codex-App beispielsweise macht Änderungen pro Agent sichtbar und ermöglicht die Prüfung isolierter Worktrees.

Das beantwortet vor allem:

> **Was hat der Agent getan?**

Bei einem längeren Agentenlauf brauche ich zunehmend noch eine zweite Antwort:

> **Warum hat er sich an den offenen Stellen genau dafür entschieden?**

Damit meine ich kein vollständiges Gedankenprotokoll. Ein Log mit 400 Shell-Befehlen wäre als Review-Artefakt beinahe wertlos.

Interessant sind die Stellen, an denen aus einer unvollständigen Vorgabe eine verhaltensrelevante Annahme wurde.

Für das Review-Beispiel könnte ein Eintrag etwa so aussehen:

```text
Entscheidung:
Neue Reviews erhalten bei Namenskollision einen Suffix.

Grundlage:
Anforderung: Bestehende Reviews dürfen nicht überschrieben werden.

Ergänzte Annahme:
Der kanonische Pfad editorial-review.md bleibt die Quelle
für nachfolgende Verarbeitungsschritte.

Validiert:
Bestehende Datei bleibt unverändert.
Neue Variante wird erzeugt.

Nicht validiert:
Welche Review-Variante nach der Erzeugung als aktuell gelten soll.
```

Hätte ich diesen Eintrag vor dem Code-Diff gesehen, wäre der eigentliche Fehler vermutlich sofort aufgefallen.

Nicht weil ich TypeScript besser gelesen hätte.

Sondern weil eine implizite Annahme plötzlich als Entscheidung sichtbar geworden wäre.

## Wie aus dem Log ein Decision Review werden könnte

Praktisch müsste dafür nicht jede Entscheidung protokolliert werden. Sonst entsteht nur ein zweites Logfile, das ebenfalls niemand liest.

Interessant sind Entscheidungen mit **Interpretationsspielraum**: immer dann, wenn eine Spezifikation mehr als eine vernünftige Umsetzung zulässt, der Agent selbst eine Quelle der Wahrheit auswählt, ein Fallback definiert oder eine fachlich relevante Annahme ergänzt.

Ein Agent könnte deshalb vor Abschluss einer größeren Aufgabe zusätzlich einen kurzen Decision Review erzeugen. Fünf Fragen würden für einen ersten Versuch reichen:

1. Welche verhaltensrelevanten Entscheidungen habe ich getroffen, die nicht ausdrücklich vorgegeben waren?
2. Welche plausiblen Alternativen gab es?
3. Worauf habe ich meine Auswahl gestützt?
4. Wie wurde diese Entscheidung überprüft?
5. Welche Annahme sollte ein Mensch vor dem Merge ausdrücklich bestätigen?

Für mein Beispiel hätte schon eine einzige Zeile gereicht:

> **Offen: Welche Review-Datei gilt nach dem Erzeugen einer neuen Variante als aktuell?**

Dafür hätte es keinen weiteren Architekturworkshop gebraucht.

Nur einen Moment, in dem die Maschine ihre eigene plausible Ergänzung wieder als offene Entscheidung an mich zurückgibt.

Ob genau diese fünf Fragen die richtige Form sind, müsste sich in realen Projekten erst zeigen. Ebenso wäre zu prüfen, ob Agenten ihre eigenen relevanten Annahmen zuverlässig genug identifizieren oder ob dafür ein separater Review-Agent bessere Ergebnisse liefert.

Aber damit wird aus der abstrakten Forderung nach „mehr Nachvollziehbarkeit“ zumindest eine überprüfbare Arbeitshypothese.

Man kann sie ausprobieren.

Und man kann messen, welche Fehler dadurch früher auffallen.

## Nicht jeder Tool-Call ist eine Entscheidung

Ein agentischer Entwicklungsprozess kann hunderte Aktionen enthalten, die für einen solchen Review kaum interessant sind.

Eine Datei wurde gelesen, `npm install` ausgeführt, der Typecheck gestartet, ein Import korrigiert und der Test erneut ausgeführt.

Diese Spuren sind für Debugging und Reproduzierbarkeit wertvoll. Sie sind aber nicht automatisch die Entscheidungsspur, die ein menschlicher Reviewer braucht.

Die interessantere Prüffrage lautet:

> **Wo hätte ein anderer vernünftiger Entwickler aufgrund derselben Anforderung eine andere Entscheidung treffen können?**

Dort lohnt sich die zusätzliche Aufmerksamkeit.

Das kann eine Architekturentscheidung sein, die Interpretation eines Begriffs, die Wahl einer Quelle der Wahrheit, eine Berechtigungsentscheidung, ein Fallback oder eben die Frage, welche von mehreren erhaltenen Dateien anschließend als aktuell gilt.

## Der Review-Gegenstand wird größer als der Diff

In klassischer Entwicklung steckt ein Teil dieser Information im Entwickler selbst. Wer zwei Tage an einem Feature gearbeitet hat, erinnert sich meistens zumindest daran, warum ein Zustand auf eine bestimmte Weise modelliert oder eine Alternative verworfen wurde.

Das ist kein besonders zuverlässiges Dokumentationssystem.

Aber die Entscheidungsstrecke hat Zeit gebraucht.

Bei einem Coding-Agenten kann dieselbe Strecke stark komprimiert werden. Werden mehrere Agenten parallel eingesetzt, fällt sogar die zeitliche Reihenfolge teilweise auseinander: Ein Mensch sieht anschließend möglicherweise mehrere fertige Diffs aus isolierten Arbeitssträngen. Die Codex-App unterstützt genau solche parallelen Worktree-Workflows.

Der klassische Code Review wird dadurch nicht überflüssig.

Aber sein Gegenstand könnte größer werden.

Neben

> Was wurde geändert?

treten Fragen wie:

> Welche Anforderungen waren tatsächlich explizit?

> Welche Verhaltensentscheidungen hat der Agent ergänzt?

> Worauf stützte er sie?

> Welche davon wurden nur durch Tests bestätigt, die aus derselben Interpretation entstanden?

> Was wurde überhaupt nicht gegen die ursprüngliche Absicht geprüft?

Das ist keine neue Entwicklungsmethode.

Es ist zunächst nur ein anderer Blick auf den Review.

## Specs reduzieren den Entscheidungsraum. Sie beseitigen ihn nicht.

Die naheliegende Antwort auf all das lautet: Dann müssen wir eben bessere Spezifikationen schreiben.

Ja.

Aber eine Spezifikation ist keine Gedankenübertragung.

Der Wert einer guten Spec liegt nicht darin, dass anschließend keine Entscheidungen mehr getroffen werden müssen. Sie reduziert den Raum, in dem ein Agent selbst ergänzen muss, und gibt dem Reviewer eine bessere Grundlage, diese Ergänzungen zu erkennen.

Wir sollten deshalb vermutlich nicht versuchen, jede mögliche Entscheidung vorab in immer größere Dokumente zu schreiben.

Interessanter ist die Trennung:

**Was war vorgegeben?**

**Was wurde daraus abgeleitet?**

**Was musste angenommen werden?**

**Und was davon wurde tatsächlich geprüft?**

GitHubs Spec Kit behandelt genau diese Art von Unsicherheit inzwischen explizit: `/speckit.clarify` soll unterbestimmte Stellen vor der Planung reduzieren, `/speckit.analyze` sucht später nach Lücken und Widersprüchen zwischen Spec, Plan und Tasks.

Auch das verhindert keine falsche Entscheidung.

Aber es schafft Stellen, an denen sie sichtbar werden kann.

## Das plausible Programm ist schwieriger als das kaputte

Ein kaputtes Programm hat einen großen Vorteil: Es zwingt zur Aufmerksamkeit. Der Build schlägt fehl, ein Test wird rot oder die Anwendung startet nicht. Jemand muss hinsehen.

Ein plausibles Programm ist schwieriger.

Es kompiliert, die Oberfläche sieht vernünftig aus, die Tests passen zur implementierten Interpretation und der Agent meldet seine Aufgabe als erledigt.

Genau dann kann menschlicher Review wichtiger werden als vorher.

Nicht weil der Agent keinen Code schreiben kann.

Sondern weil er inzwischen gut genug ist, eine unvollständige Absicht in eine konsistente, getestete und dennoch falsche Implementierung zu verwandeln.

Der Diff zeigt mir, was der Agent geändert hat.

Die Tests zeigen mir, welche Bedingungen diese Implementierung erfüllt.

Was mir dazwischen noch fehlt, ist eine andere Frage:

**Welche offenen Fragen hat der Agent für mich beantwortet, ohne dass ich sie überhaupt gestellt hatte?**

Genau die möchte ich vor dem Merge sehen.