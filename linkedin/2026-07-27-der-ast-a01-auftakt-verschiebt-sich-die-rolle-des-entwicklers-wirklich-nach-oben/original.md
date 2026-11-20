---
title: "(1) Der Ast, auf dem wir sitzen"
subtitle: "Auftakt: Verschiebt sich die Rolle des Entwicklers wirklich nach oben?"
author: "Benjamin Lam"
date: 2026-07-27
source: "LinkedIn"
role: "series"
series: "Der Ast, auf dem wir sitzen"
series_part: 1
original_url: "https://www.linkedin.com/pulse/der-ast-auf-dem-wir-sitzen-benjamin-lam-x3c5f/"
---

# Der Ast, auf dem wir sitzen

## Auftakt: Verschiebt sich die Rolle des Entwicklers wirklich nach oben?

Ich habe KI lange vor allem als Befreiungsschlag betrachtet.

Als Möglichkeit, Routine abzugeben, Wissen zugänglicher zu machen und mit weniger Aufwand mehr gestalten zu können. Einzelne Entwicklerinnen und Entwickler können heute Dinge umsetzen, für die früher ein größeres Team, mehr Zeit oder ein höheres Budget nötig gewesen wäre.

Daran hat sich für mich nichts Grundsätzliches geändert. Diese Serie beginnt trotzdem dort, wo dieses Versprechen komplizierter wird.

Was passiert, wenn wir mit KI nicht nur einzelne Aufgaben erleichtern, sondern ganze Rollen und Arbeitssysteme verändern? Wer gewinnt tatsächlich Zeit? Wer erhält mehr Entscheidungsspielraum? Welche Fähigkeiten bauen wir aus – und welche verlieren wir, weil wir sie nicht mehr ausüben?

Und vor allem:

Wer verfügt am Ende über die Produktivität, die wir gemeinsam erzeugen?

Es geht nicht darum, KI kleinerzureden. Es geht darum, genauer hinzusehen, bevor persönliche Entlastung zur neuen Leistungserwartung wird, Unterstützung in Kontrolle übergeht oder Verantwortung bei Menschen bleibt, während Entscheidungen längst an anderer Stelle getroffen werden.

Der Ast, auf dem wir sitzen, ist nicht die alte Arbeitswelt.

Es ist unsere Fähigkeit, zu verstehen, zu entscheiden, zu widersprechen und den Wert der eigenen Arbeit zu behaupten.

---

Im vergangenen Jahr habe ich häufig über die Verschiebung der Entwicklerrolle geschrieben.

Weniger Code schreiben. Mehr Systeme entwerfen. Weniger Ausführung. Mehr Architektur.

Die Maschine übernimmt die Routine – und der Mensch gewinnt Zeit für die wichtigen Entscheidungen.

Ich habe diese Entwicklung nicht nur beschrieben. Ich habe sie für wahrscheinlich gehalten.

Inzwischen frage ich mich, ob darin eine allzu beruhigende Erzählung steckt.

Die klassische Aufstiegserzählung der Automatisierung lautet:

Was die Maschine übernimmt, muss der Mensch nicht mehr tun. Also steigt der Mensch eine Ebene höher.

Die Maschine rechnet, der Mensch interpretiert. Die Maschine produziert, der Mensch gestaltet. Die Maschine schreibt Code, der Entwickler wird zum Architekten.

Das klingt folgerichtig.

Es setzt allerdings voraus, dass mit der Ausführung nicht auch Teile der Entscheidung verschwinden.

## Weniger schreiben heißt nicht automatisch mehr entscheiden

Code ist nie nur die Übersetzung einer vollständig geklärten Entscheidung.

Im Code werden Entscheidungen konkret:

Wie werden Daten strukturiert? Welche Abhängigkeiten akzeptieren wir? Wo wird validiert? Wie werden Fehler behandelt? Welche Zustände sind erlaubt? Was wird protokolliert? Welche Sicherheitsannahmen gelten? Was passiert, wenn ein externer Dienst ausfällt?

Ein Teil davon wird vor der Implementierung ausdrücklich festgelegt. Vieles entsteht aber erst während der Arbeit: beim Schreiben, Testen, Verwerfen und erneuten Nachdenken. Gute Entwicklung besteht nicht nur darin, eine vorhandene Lösung einzutippen. Sie besteht auch darin, während der Umsetzung zu erkennen, dass die ursprüngliche Vorstellung unvollständig war.

Wenn eine KI Code erzeugt, verschwinden diese Entscheidungen nicht.

Sie erscheinen nur früher als Ergebnis.

Ein Modell schlägt eine Bibliothek vor. Es wählt ein Datenmodell, setzt ein bekanntes Muster ein und ergänzt Fehlerbehandlung. Innerhalb weniger Sekunden liegt etwas vor, das plausibel aussieht und häufig sogar funktioniert.

Damit ist aber nicht nur Schreibarbeit erledigt worden.

Es wurden technische Entscheidungen getroffen – oder zumindest vorbereitet –, ohne dass sie vorher als Entscheidungen sichtbar waren.

## Sichtbare und eingebettete Entscheidungen

Wir sprechen dabei von zwei unterschiedlichen Arten von Entscheidungen.

Die sichtbaren Entscheidungen werden ausdrücklich getroffen:

Eine neue E-Mail-Adresse muss bestätigt werden. Änderungen werden protokolliert. Bestimmte Daten dürfen nur für festgelegte Zwecke verwendet werden. Ein externer Dienst braucht einen definierten Ausfallweg.

Daneben stehen eingebettete Entscheidungen. Sie entstehen durch die Wahl einer Bibliothek, eines Datenmodells, eines Standardmusters oder einer bestimmten Fehlerbehandlung. Sie wirken genauso real, erscheinen aber häufig erst als Bestandteil einer bereits erzeugten Lösung.

Natürlich entscheidet ein Mensch noch, ob er den Vorschlag übernimmt.

Aber diese Entscheidung lautet zunächst nur:

Annehmen, verändern oder verwerfen.

Um die darin enthaltenen technischen Festlegungen bewusst beurteilen zu können, muss er sie zuerst als Entscheidungen erkennen.

Eine grobe Freigabe kann Dutzende feinere Entscheidungen verdecken.

Wer zwischen drei Vorschlägen auswählt, hat deshalb noch keine Architektur entworfen.

Und wer das Ergebnis am Ende freigibt, hatte nicht zwangsläufig Kontrolle über den Weg dorthin.

## Architektur beginnt vor dem Prompt

Nehmen wir eine scheinbar einfache Aufgabe:

> Baue einen Endpunkt, über den Kundinnen und Kunden ihre Kontaktdaten ändern können.

Eine KI kann dafür schnell einen Controller, eine Validierung und den Datenbankzugriff erzeugen.

Die eigentliche Architektur liegt jedoch nicht in diesen Dateien.

Sie liegt in den Fragen davor:

Dürfen alle Kontaktdaten auf demselben Weg geändert werden? Muss eine neue E-Mail-Adresse bestätigt werden? Was geschieht mit laufenden Bestellungen? Welche Änderungen werden protokolliert? Wer darf die Historie einsehen? Wie werden parallele Änderungen behandelt? Welche Systeme müssen informiert werden? Was passiert bei einem Teilausfall?

Wer diese Grenzen bestimmt, trifft Architekturentscheidungen. Wer lediglich prüft, ob der erzeugte Code kompiliert, testbar aussieht und die offensichtliche Anforderung erfüllt, arbeitet nicht automatisch auf einer höheren Ebene. Er übernimmt die Endkontrolle einer Lösung, deren Voraussetzungen nur teilweise geklärt wurden.

Der Unterschied liegt deshalb nicht darin, ob ein Mensch den Code selbst geschrieben hat.

Der Unterschied liegt darin, ob er die entscheidenden Fragen vorgegeben hat.

Architektur beginnt nicht dort, wo weniger getippt wird. Architektur beginnt dort, wo jemand Ziele, Grenzen, Abhängigkeiten und Folgen sichtbar macht, bevor sie sich unbemerkt im Ergebnis festsetzen.

## Das Schreiben von Code verschwindet nicht. Es wandert.

Gleichzeitig wird Code für Menschen zugänglich, die bisher keine Software entwickeln konnten.

Produktverantwortliche bauen Prototypen. Fachabteilungen automatisieren Abläufe. Selbstständige erstellen interne Werkzeuge. Designerinnen und Designer entwickeln interaktive Anwendungen. Kleine Teams testen Ideen, ohne zuerst ein vollständiges Entwicklungsteam zusammenzustellen.

Das ist kein Verfall professioneller Entwicklung. Es ist in vielen Fällen eine reale Öffnung.

Probleme können dort bearbeitet werden, wo sie entstehen. Ideen müssen nicht mehr so früh durch das Nadelöhr knapper Entwicklungskapazitäten. Ein Prototyp kann in Stunden zeigen, ob eine Vorstellung überhaupt trägt.

Dabei sind die neuen Entwicklerinnen und Entwickler keineswegs nur technische Laien. Eine Fachexpertin kann mit KI einen Ablauf entwerfen, dessen Regeln, Ausnahmen und praktische Folgen sie besser versteht als ein generalistisches Entwicklungsteam. Gerade darin liegt ein Teil des Potenzials.

Die Fachabteilung weiß, welche Ausnahme im Alltag entscheidend ist. Sie kennt die Bedeutung einer falschen Zuordnung, einer versäumten Frist oder eines nicht dokumentierten Zwischenschritts. Ein Entwicklungsteam kann technisch sauber arbeiten und trotzdem an der Wirklichkeit des Prozesses vorbeibauen.

Das Risiko beginnt deshalb nicht mit fehlender Fachkenntnis. Es beginnt dort, wo fachliche Autorität als Ersatz für technisches Risikobewusstsein behandelt wird – oder umgekehrt technische Routine die tatsächliche Fachlogik übergeht.

Beide Wissensformen sind notwendig.

Fachkenntnis beantwortet, was der Prozess in der Realität leisten muss.

Technische Systemkenntnis beantwortet, unter welchen Bedingungen er zuverlässig, sicher und dauerhaft betrieben werden kann.

KI kann diese Wissensformen näher zusammenbringen. Sie kann aber auch den Eindruck erzeugen, eine davon genüge.

## Ein Prototyp ist noch kein Betrieb

Etwas erzeugen zu können bedeutet noch nicht, es dauerhaft betreiben zu können.

Ein funktionierender Prototyp beantwortet noch keine Fragen zu Wartung, Datenschutz, Zugriffsrechten, Skalierung, Fehlerfällen oder organisatorischer Verantwortung.

Das ist keine Abwertung des Prototyps.

Ein Prototyp hat eine andere Aufgabe. Er soll eine Annahme sichtbar machen, einen Ablauf testen oder eine Idee erfahrbar machen. Problematisch wird es, wenn seine bloße Funktionsfähigkeit als Beleg für betriebliche Reife gelesen wird.

Je einfacher die Erzeugung wird, desto wichtiger wird deshalb die Grenze zwischen:

> Es funktioniert gerade.

und:

> Wir verstehen, warum es funktioniert, unter welchen Bedingungen es versagt und wer dann handeln kann.

Das Codeschreiben wandert also tatsächlich. Es wandert in Fachbereiche, in Plattformen, in Modelle und zu Menschen, die technische Ergebnisse erzeugen können, ohne den gesamten technischen Lebenszyklus verantworten zu wollen.

Ob die Rolle des Entwicklers dadurch nach oben wandert, entscheidet sich daran, ob sein Einfluss ebenfalls wächst.

Oder ob er erst wieder ins Spiel kommt, wenn aus dem schnellen Prototyp ein dauerhaftes System werden soll.

## Vom Entwickler zum Reparaturbetrieb

Die weniger angenehme Variante der Zukunft sieht nicht so aus, dass Entwicklerinnen und Entwickler vollständig verschwinden.

Sie sieht so aus, dass sie später hinzukommen.

Wenn der erzeugte Code nicht mehr weiterkommt. Wenn sich Abhängigkeiten widersprechen. Wenn Sicherheitsfragen auftauchen. Wenn Daten verloren gehen. Wenn der ursprüngliche Prompt nicht erklärt, warum eine bestimmte Struktur gewählt wurde. Wenn eine Lösung gewachsen ist, ohne dass jemand ihre Gesamtform bestimmt hat.

Dann wird aus dem Entwickler nicht der Architekt.

Dann wird er zum Reparaturbetrieb.

Er prüft, erklärt und stabilisiert Entscheidungen, die bereits in das System eingebaut wurden. Er trägt Verantwortung für ein Ergebnis, dessen Entstehung er nicht vollständig begleitet hat. Und er muss unter Zeitdruck nachvollziehen, welche Annahmen Menschen, Werkzeuge und Modelle vorher getroffen haben.

Auch das ist qualifizierte Arbeit.

Aber es ist keine automatische Aufwertung.

Verantwortung ohne entsprechenden Einfluss ist kein beruflicher Aufstieg.

Sie ist eine Belastung.

## Es gibt die andere Entwicklung ebenfalls

KI kann Entwicklerinnen und Entwickler tatsächlich stärker in Richtung Architektur verschieben.

Dort, wo sie repetitive Umsetzung abnimmt und Zeit für Zusammenhänge schafft.

Dort, wo Anforderungen vor der Generierung präzisiert werden.

Dort, wo technische Entscheidungen dokumentiert werden.

Dort, wo ein Mensch nicht nur den Output, sondern auch Datenflüsse, Risiken, Abhängigkeiten und Betriebsfolgen kontrolliert.

Dort, wo Tests nicht lediglich bestätigen, dass der generierte Code das Erwartete tut, sondern auch prüfen, ob die Erwartung selbst vollständig war.

In einem solchen Arbeitsprozess ist KI kein Ersatz für Architektur.

Sie schafft Kapazität für Architektur.

Der Unterschied ist nicht das verwendete Werkzeug.

Der Unterschied ist die Organisation der Arbeit.

Ein Team, das bisher unter Zeitdruck schlechte Entscheidungen getroffen hat, trifft mit KI schneller schlechte Entscheidungen.

Ein Team, das Ziele, Grenzen und Verantwortung sauber klärt, kann mit KI mehr davon umsetzen, ohne jeden Schritt manuell auszuführen.

KI hebt eine Rolle nicht von selbst an.

Sie verstärkt die Struktur, in der sie eingesetzt wird.

## Woher kommen die künftigen Architekten?

Dabei bleibt ein weiterer Widerspruch.

Architekturverständnis entsteht nicht ausschließlich durch abstraktes Nachdenken.

Es entsteht auch durch Ausführung. Durch Fehler, die erst beim Implementieren sichtbar werden. Durch Systeme, die unter realen Bedingungen anders reagieren als auf dem Papier. Durch schlecht gewählte Abhängigkeiten. Durch Datenmodelle, die später nicht mehr tragen. Durch Wartung, Migrationen und Entscheidungen, deren Folgen erst Jahre später erkennbar werden.

Wer Architektur verantwortet, braucht Erfahrung mit dem Material, aus dem Systeme bestehen.

Wenn Nachwuchskräfte immer seltener selbst entwickeln, Fehler suchen und Lösungen von Grund auf aufbauen, entsteht eine Lücke.

Wir können die ausführende Arbeit nicht vollständig automatisieren und gleichzeitig voraussetzen, dass Menschen auf magische Weise das Urteilsvermögen entwickeln, diese Arbeit auf einer höheren Ebene zu kontrollieren.

Das bedeutet nicht, dass jede Zeile weiterhin von Hand geschrieben werden muss.

Es bedeutet, dass Lernen nicht mit Produktion verwechselt werden darf.

Eine Aufgabe kann für die Produktion überflüssig geworden sein und für den Kompetenzaufbau trotzdem unverzichtbar bleiben.

## Die eigentliche Verschiebung

Vielleicht verschiebt sich die Entwicklerrolle also tatsächlich.

Aber nicht auf einer einzigen, gemeinsamen Treppe nach oben.

Einige Entwicklerinnen und Entwickler werden mehr gestalten. Sie übersetzen zwischen Fachlichkeit, Technik, Recht und Betrieb. Sie bestimmen Grenzen, koordinieren Systeme und übernehmen Verantwortung, weil sie auch die nötige Kontrolle besitzen.

Andere werden generierte Ergebnisse prüfen, korrigieren und absichern.

Wieder andere erleben, dass Teile ihrer bisherigen Arbeit in Fachbereiche und Plattformen wandern, während sie erst bei Problemen zurückgerufen werden.

Und einige Menschen werden Software erzeugen, ohne sich jemals als Entwickler zu verstehen.

Die Entwicklung ist kein einfacher Aufstieg.

Sie ist eine Neuverteilung von Ausführung, Entscheidung, Kontrolle und Verantwortung.

Darum reicht es nicht, festzustellen, dass künftig weniger Code von Hand geschrieben wird.

Wir müssen genauer fragen:

Wer bestimmt die Bedingungen, unter denen der Code entsteht? Wer erkennt die darin eingebetteten Entscheidungen? Wer kann sie beurteilen und korrigieren? Und wer muss am Ende für ihre Folgen einstehen?

---

Ich bin gerade dabei, dieses Thema weiter zu vertiefen.

Dabei möchte ich mein eigenes Bauchgefühl von der praktischen Wirklichkeit trennen.

Ich werde dafür Forschung zu Produktivität und Qualität ebenso betrachten wie konkrete Entwicklungsabläufe, Code-Reviews, Wartungsprobleme und Erfahrungen aus Unternehmen. Mich interessieren die Perspektiven von Entwicklerinnen und Entwicklern, technischen Leitungen, Fachabteilungen und Menschen, die heute mit KI Software erzeugen, ohne aus einer klassischen Entwicklerrolle zu kommen.

Entscheidend sind für mich gerade die Fälle, in denen die einfache Erzählung vom Aufstieg zum Architekten nicht trägt.

Aber ebenso die Gegenbeispiele, in denen KI tatsächlich mehr Gestaltung ermöglicht, Fachlichkeit und Technik näher zusammenbringt und Menschen von unnötiger Ausführung befreit.

Feedback ist deshalb ausdrücklich erwünscht.

Nicht nur Zustimmung, sondern ebenso Gegenbeispiele, Korrekturen und Beobachtungen aus dem Arbeitsalltag.

Gewinnt ihr durch KI tatsächlich mehr architektonischen und fachlichen Gestaltungsspielraum – oder verbringt ihr zunehmend Zeit damit, Entscheidungen zu prüfen, zu erklären und zu reparieren, die bereits im generierten Ergebnis stecken?
