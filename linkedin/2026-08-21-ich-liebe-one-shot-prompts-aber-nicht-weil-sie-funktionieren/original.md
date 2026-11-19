# Ich liebe One-Shot-Prompts. Aber nicht, weil sie funktionieren.

Ich liebe One-Shot-Prompts.

Diese etwas größenwahnsinnigen Dokumente, in denen man versucht, einer KI auf einmal zu erklären, was sie bauen soll, wie sie es bauen soll, was sie auf gar keinen Fall tun darf und woran sie am Ende bitte selbst erkennt, dass sie fertig ist.

Am besten endet das Ganze noch mit einer kleinen Verständnisfrage.

*Hast du das verstanden? Kannst du das so umsetzen?*

Worauf ein LLM ungefähr antwortet:

> Ja. Das ist ein hervorragend strukturiertes und durchdachtes Konzept, das die funktionalen Anforderungen, technischen Leitplanken und Qualitätskriterien klar miteinander verbindet.

Natürlich ist es das.

Ich habe es schließlich zusammen mit einem LLM geschrieben.

Ich liebe diese One-Shots allerdings nicht, weil nach ausreichend Vorarbeit in einem Rutsch die perfekte Anwendung hinten herausfällt.

Das passiert nicht.

Oder zumindest nicht bei mir.

Was hinten herausfällt, ist inzwischen erstaunlich oft passabel. Mit jeder neuen Modellgeneration gibt es weniger von diesen Startschwierigkeiten, bei denen man nach zwei Minuten feststellt, dass die Anwendung zwar einen Login hat, aber leider keine Benutzer, oder dass der Button „Speichern“ philosophisch gemeint war.

Die Sachen funktionieren.

Und genau das macht sie interessant.

Denn meistens funktionieren sie ein bisschen anders, als die Anwendung, die ich beim Absenden des Prompts bereits ziemlich deutlich in meinem Kopf gesehen habe.

## Eine ziemlich lange Nachricht bei Stiller Post

Mein letzter Versuch war unspektakulär.

Ich wollte eine Erweiterung für VS Code bauen.

Eine kleine Schreibwerkstatt.

Keine neue Textverarbeitung, kein KI-Wunderland mit animierten Assistenten und vermutlich auch kein SaaS-Abo für 19,90 Euro im Monat.

Die Idee war eher banal: Wenn ich einen längeren Artikel schreibe, entstehen dabei verschiedene Fassungen, Recherchefragen, Claims, Quellen, redaktionelle Reviews, Stilprüfungen und irgendwann eine Zielfassung.

Das liegt normalerweise irgendwo zwischen Editor, Chatfenstern und meinem Kopf herum.

Also wollte ich dafür eine Werkbank.

Dateibasiert. Lokal. Überschaubar. KI als Werkzeug, nicht als Autor. Nichts still überschreiben. Keine erfundenen Quellen. Ein paar klare Zustände. Ein paar Checks. Fertig.

Das war jedenfalls die Idee.

Dann beginnt bei mir inzwischen ein etwas fragwürdiger Prozess.

Ich erkläre einem LLM, was ich vorhabe.

Das LLM formuliert daraus etwas Präziseres.

Ich korrigiere.

Es strukturiert.

Ich ergänze.

Es entdeckt eine Lücke.

Ich schließe die Lücke.

Es baut daraus Anforderungen.

Irgendwann liegt vor mir ein umfangreiches Dokument, bei dem beide Beteiligten der Meinung sind, dass jetzt wirklich alles drinsteht.

Eine Art Stille Post, nur dass jeder Teilnehmer sehr gute Grammatik hat und die Nachricht nach jeder Station professioneller aussieht.

Gefühlt komme ich meinem Ziel bei jedem Pingpong näher.

Tatsächlich entsteht bei jedem Schritt zunächst die statistisch wahrscheinlichste Interpretation meiner Intention.

Das ist nicht dasselbe.

Zu meiner Schande muss ich außerdem gestehen, dass ich diese Spezifikation anschließend nicht immer gründlich lese.

Dafür habe ich sie doch schreiben lassen.

Ein Satz, den man sich vielleicht irgendwo aufhängen sollte.

Nicht unbedingt als Best Practice.

Also: One-Shot an Codex.

Einfach mal machen.

Und ich hole mir einen Kaffee.

## Während ich Kaffee koche, werden Entscheidungen getroffen

Das ist der Teil, den ich an One-Shots mag.

Nicht der Kaffee.

Der ist nur organisatorisch günstig.

Während ich in der Küche stehe, entsteht auf meinem Rechner etwas, für das ein menschlicher Entwickler eine ganze Reihe kleiner und größerer Entscheidungen treffen müsste.

Wie speichere ich den Projektzustand?

Was leite ich aus vorhandenen Dateien ab und was muss explizit gespeichert werden?

Wie verhindere ich, dass bestehende Texte überschrieben werden?

Wie bilde ich verschiedene Fassungen ab?

Welche Teile der Anwendung funktionieren auch ohne Sprachmodell?

Wie integriere ich die VS-Code-API?

Welche Tests sind für den MVP sinnvoll?

Was passiert, wenn kein Modell verfügbar ist?

Was passiert bei beschädigtem JSON?

Wie sieht ein Dateiname aus, wenn es ihn schon gibt?

Keiner dieser Punkte ist spektakulär.

Das ist ja das Gemeine an Softwareentwicklung.

Ein beträchtlicher Teil besteht aus Entscheidungen, die einzeln so klein wirken, dass niemand dafür eine Strategiesitzung einberufen würde.

Zusammen sind sie die Anwendung.

Das nachträglich rekonstruierte Worklog meines Experiments kommt für einen kompetenten menschlichen Entwickler auf ungefähr **17 bis 25 Stunden Arbeit**.

Zweieinhalb bis vier normale Arbeitstage.

Anforderungen verstehen. Architektur festlegen. Extension scaffolden. Kernmodell bauen. Dateizugriffe anbinden. KI-Abstraktion entwickeln. Prompts schreiben. Commands bauen. Tree View. Checks. Statusleiste. Tests. Fehlersuche. Smoke-Test. Dokumentation.

17 bis 25 Stunden.

Während ich einen Kaffee koche.

Na gut.

Ganz so schnell war es nicht.

Fünf Minuten? Zehn? Mehr?

Ich habe nicht auf die Uhr gesehen.

Was vermutlich ebenfalls keine Best Practice ist.

Kurz frage ich mich noch, wie viel Wasser und Energie der Rechnerverbund für diese kleine Demonstration meiner Produktivität gerade in Wärme verwandelt. Dann fällt mir auf, dass ich eigentlich einen Artikel über Softwareentwicklung schreibe und nicht über die Ökobilanz meines Kaffees.

Ich schweife ab.

Weiter als der Drift in meiner IDE.

## Ach ja. Die Spezifikation.

Irgendwann während des Laufs fällt mir ein Satz ein, den ich nicht hineingeschrieben habe.

Wir befinden uns im Jahr 2026.

Das klingt als Anforderung zunächst ungefähr so sinnvoll wie „Bitte berücksichtigen, dass Wasser nass ist“.

Bei KI-gestützter Entwicklung kann es trotzdem relevant werden.

Auf welchem Wissensstand arbeitet das Modell gerade?

Kennt es die aktuelle API?

Verwendet es ein Muster, das 2023 hervorragend gewesen wäre?

Hat es die nötigen Informationen nachgeschlagen?

Hat es zumindest in die aktuellen Typdefinitionen geschaut?

Oder baut es gerade mit großer Überzeugung etwas, das vor drei Jahren plausibel war?

Ich überlege kurz, den Lauf abzubrechen.

Dann sehe ich, dass bereits Tests geschrieben werden.

Test Last.

Also gleich durch.

Ich entscheide mich gegen den Abbruch.

Vielleicht hat sich der Agent ja zwischendurch eingestempelt und dabei zufällig aufs Datum geschaut.

Ach ja.

Specs lesen.

Specs lesen Last.

Auch ein schönes Vorgehensmodell.

## Und dann funktioniert das Ding

Das wäre jetzt die ideale Stelle für die übliche Geschichte.

KI baut irgendetwas Absurdes.

Alles bricht zusammen.

Der erfahrene Entwickler lächelt milde, öffnet seinen Editor und erklärt der Welt, warum wir Menschen doch noch gebraucht werden.

Leider ist genau das nicht passiert.

Die Extension kompiliert.

Der Typecheck läuft durch.

13 von 13 Unit-Tests sind grün.

Der komplette Schreibworkflow lässt sich in einem Headless-Smoke-Test vom Anlegen des Projekts bis zu einer zweiten Zielfassung durchspielen.

Sogar der Offline-Pfad funktioniert vollständig ohne KI-Aufruf.

Quellen werden nicht einfach erfunden.

Ausgangstexte werden nicht still überschrieben.

Reviews und Rewrite sind grundsätzlich getrennt.

Versionen werden angelegt.

Das Ding ist für einen One-Shot erstaunlich ordentlich.

Das anschließende MVP-Review kommt trotzdem zu einem recht deutlichen Urteil:

**REWORK BEFORE REAL ARTICLE.**

Und ab da wurde das Experiment für mich interessant.

## Es hat verstanden, was ich geschrieben habe

Einer der zentralen Gedanken meiner Schreibwerkstatt war Orientierung.

Wenn ich einen Artikel über mehrere Schleifen bearbeite, möchte ich nicht am nächsten Morgen erst rekonstruieren müssen, wo ich eigentlich war.

Welche Fassung ist aktuell?

In welcher Phase befinde ich mich?

Was fehlt?

Was sollte ich als Nächstes tun?

Die Anwendung speichert deshalb unter anderem eine aktuelle Arbeitsphase und ein aktives Dokument.

So weit, so gut.

Im ersten linearen Durchlauf funktioniert das auch.

Idee.

Draft.

Recherche.

Review.

Revision.

Zielfassung.

Alles sauber.

Dann macht man etwas ausgesprochen Menschliches.

Man geht zurück.

Nach der bereits vorhandenen Zielfassung erzeugt man noch einen neuen Draft.

Im Projektzustand steht anschließend korrekt:

Aktuelle Phase: Draft.

Aktives Dokument: `first-draft-2.md`.

Nur die Oberfläche sieht das anders.

Sie zeigt weiterhin:

**Zielfassung.**

Und der neue aktive Draft taucht in der Sidebar nicht einmal auf.

Das ist kein spektakulärer Programmierfehler.

Eigentlich ist es ein ziemlich vernünftiger Fehler.

Die Anwendung hat zwei plausible Vorstellungen von „Wo stehe ich?“ bekommen.

Die eine lautet:

Wo arbeitet der Benutzer gerade?

Die andere lautet:

Wie weit ist dieses Projekt jemals gekommen?

Für meinen Kopf war völlig klar, welche davon die Sidebar beantworten sollte.

Für den Code offenbar nicht.

Und wenn ich meine Spezifikation rückwärts lese, wird die Sache unangenehm.

Denn dort war diese Klarheit offenbar nicht so klar, wie sie in meinem Kopf gewesen war.

## Noch schöner wird es beim Nicht-Überschreiben

Eine andere Forderung war mir besonders wichtig:

Die KI soll meine Artefakte nicht einfach überschreiben.

Wenn bereits ein Editorial Review existiert und ich einen neuen anfordere, soll die alte Fassung erhalten bleiben.

Also macht die Extension genau das.

Sie erzeugt:

`editorial-review.md`

und später:

`editorial-review-2.md`

Perfekt.

Anforderung erfüllt.

Nur verwendet der nächste Rewrite anschließend wieder den ersten Review.

Dasselbe passiert beim Style Review.

Der neue Review wird korrekt erzeugt.

Er bleibt erhalten.

Er wird nur von der Anwendung weitgehend ignoriert.

Ich musste darüber länger nachdenken, weil es ein wunderbares kleines Beispiel für das Problem ist.

Ich hatte gesagt:

**Nicht überschreiben.**

Was ich gemeint hatte, war:

**Nicht überschreiben – und sorge dafür, dass die jeweils neue bewusste Entscheidung anschließend als aktuelle Fassung im weiteren Prozess verwendet wird.**

Der zweite Teil war für mich selbstverständlich.

Für die Spezifikation offenbar nicht.

Für den Code schon gar nicht.

Code hat eine unangenehme Eigenschaft.

Er respektiert Selbstverständlichkeiten nur, wenn man sie implementiert.

## Das ist kein Argument gegen Specs

Man könnte daraus jetzt die gemütliche Schlussfolgerung ziehen, dass Spezifikationen eben nichts bringen und wir einfach wieder anfangen sollten, Software nach Gefühl zu bauen.

Wäre praktisch.

Dann müsste ich meine eigenen Specs auch nicht mehr lesen.

Aber das wäre die falsche Lehre.

Ohne die Spezifikation wäre dieses Experiment vermutlich wesentlich chaotischer verlaufen.

Sie hat Grenzen gesetzt.

Sie hat Architekturentscheidungen vorbereitet.

Sie hat festgelegt, was nicht gebaut werden soll.

Sie hat dafür gesorgt, dass das Ergebnis testbar war.

Sie hat aus einer Idee etwas gemacht, das ein Agent überhaupt in einem zusammenhängenden Lauf bearbeiten konnte.

Die Spezifikation war wertvoll.

Sie war nur nicht meine Intention.

Sie war ein Artefakt meiner Intention.

Das klingt nach Wortklauberei, bis man Software daraus baut.

Dann wird der Unterschied ausführbar.

## Vielleicht ist das der eigentliche Nutzen des One-Shots

Ich habe lange gedacht, der interessante Vergleich bei KI-gestützter Entwicklung sei Geschwindigkeit.

Der Mensch braucht vielleicht drei Tage.

Der Agent braucht Minuten.

Beeindruckend.

Stimmt wahrscheinlich sogar als Größenordnung.

Aber inzwischen finde ich einen anderen Vergleich spannender.

Ein Mensch verteilt seine Annahmen über Zeit.

Er beginnt mit dem Scaffold.

Baut einen Teil.

Probiert ihn aus.

Stellt eine Rückfrage.

Ändert etwas.

Sieht einen Widerspruch.

Liest die Anforderung noch einmal.

Flucht eventuell.

Trinkt Kaffee.

Spricht mit jemandem.

Entscheidet weiter.

Viele Missverständnisse haben Gelegenheit, sichtbar zu werden, bevor das ganze System vor einem steht.

Ein One-Shot komprimiert diese Strecke.

Das ist sein Vorteil.

Und möglicherweise gleichzeitig sein interessantestes Risiko.

Die Entscheidungen verschwinden nicht.

Sie werden nur schneller getroffen.

Aus Anforderungen werden Architekturentscheidungen.

Aus Lücken werden Annahmen.

Aus Annahmen wird Code.

Und weil das Ergebnis inzwischen erstaunlich häufig funktioniert, gibt es immer weniger Stellen, an denen man zwangsläufig innehält.

Das kaputte Programm zwingt mich zur Prüfung.

Das plausible Programm lädt mich zum Weiterklicken ein.

Das ist angenehmer.

Und genau deshalb gefährlicher.

## Also lese ich das Worklog

Deshalb interessieren mich die Logs inzwischen fast mehr als der erste Build.

Ich lasse den One-Shot laufen und mache danach etwas, das ein wenig nach Unfalluntersuchung klingt, obwohl nichts explodiert ist.

Debriefing.

Welche Entscheidungen wurden getroffen?

Welche Annahmen waren dafür nötig?

Wo gab es Alternativen?

Welche APIs wurden verwendet?

Welche Fehler traten auf?

Was wurde getestet?

Was nicht?

Welche Teile waren aus der Anforderung eindeutig?

Welche nur plausibel?

Und wie hätte ein Mensch denselben Weg zurückgelegt?

Das Worklog meines kleinen VS-Code-Experiments ist deshalb kein Triumphbericht darüber, wie viele Entwicklerstunden KI eingespart hat.

Im Gegenteil.

Es macht erst einmal sichtbar, **wie viel Arbeit überhaupt in diesen paar Minuten verschwunden ist**.

17 bis 25 Stunden menschlicher Workflow stecken in einem Ergebnis, das auf meinem Bildschirm einfach irgendwann fertig war.

Das ist enorm.

Aber die interessantere Zahl steht dort gar nicht.

Wie viele Entscheidungen davon hätte ich genauso getroffen?

## Die gefährlichste KI-Floskel ist vielleicht gar keine Floskel

Damit komme ich zurück zu diesem Satz vom Anfang.

*Das ist ein hervorragend strukturiertes und durchdachtes Konzept.*

Ich mache mich gern darüber lustig.

LLMs halten bemerkenswert viele Dinge für hervorragend strukturiert.

Vermutlich wäre selbst meine Einkaufsliste ein solides Fundament für einen skalierbaren, modularen Beschaffungsworkflow.

Aber vielleicht steckt in dieser Floskel inzwischen ein Problem, das weniger mit Höflichkeit zu tun hat.

Wir fragen:

**Hast du das verstanden?**

Und meinen:

**Hast du in deinem internen Modell exakt dieselbe Vorstellung aufgebaut, die ich gerade in meinem Kopf habe?**

Darauf kann die Maschine nicht ernsthaft mit Ja antworten.

Eigentlich kann es ein Mensch auch nur begrenzt.

Sie kann prüfen, ob Anforderungen widersprüchlich wirken.

Sie kann Lücken benennen.

Sie kann das Konzept zusammenfassen.

Sie kann Rückfragen stellen.

Sie kann daraus eine sehr plausible Interpretation bauen.

Aber sie kann meine Intention nicht gegen das Original in meinem Kopf diffen.

Ich leider auch nicht besonders gut.

Sonst hätte ich die fehlenden Sätze vermutlich vorher aufgeschrieben.

## Vielleicht brauche ich deshalb gar nicht den perfekten One-Shot

Das ist momentan der Punkt, an dem ich bei dem Experiment lande.

Nicht: One-Shots ersetzen Softwareentwicklung.

Auch nicht: One-Shots funktionieren nicht.

Beides wäre mir inzwischen zu einfach.

Mich interessiert etwas anderes.

Ein One-Shot ist für mich eine ziemlich brutale Form der Gegenprobe.

Ich nehme das, was ich für eine ausreichende Beschreibung meiner Absicht halte.

Ich lasse daraus ohne viele Zwischenkorrekturen ein System bauen.

Und danach kann ich mir ansehen, was meine Beschreibung tatsächlich bedeutet hat, sobald jemand – oder etwas – Entscheidungen daraus machen musste.

Das Ergebnis ist Code.

Aber fast interessanter ist die Differenz.

Hier dachte ich, etwas sei selbstverständlich.

War es nicht.

Hier hielt ich zwei Begriffe für identisch.

Waren sie nicht.

Hier hatte die KI eine plausible Interpretation.

Nur nicht meine.

Hier fehlte Kontext.

Hier war die Anforderung gut.

Hier war sie lediglich ausführlich.

Und manchmal stelle ich beim Debriefing fest, dass die Entscheidung der KI gar nicht schlechter ist.

Nur anders.

Was für das Ego etwas unpraktischer ist.

## Der Kaffee ist inzwischen kalt

Meine Schreibwerkstatt bekommt also einen zweiten Sprint.

Die aktuelle Arbeitsfassung muss zu einer eindeutigen Wahrheit werden.

Neue Reviews müssen nicht nur erhalten bleiben, sondern anschließend auch wirklich verwendet werden.

Die Sidebar braucht einen klareren nächsten Schritt.

Keine Revolution.

Keine grundlegende neue Architektur.

Ein paar präzise Korrekturen an Stellen, an denen aus meiner Intention eine andere plausible Bedeutung geworden ist.

Und vermutlich werde ich auch den nächsten größeren Schritt wieder als One-Shot losschicken.

Nicht weil ich inzwischen glaube, dass beim zweiten Versuch die perfekte Anwendung herauskommt.

Sondern weil ich langsam glaube, dass der eigentliche Wert dieser Läufe woanders liegt.

Sie zeigen mir sehr schnell, was ich gesagt habe.

Und mit etwas Abstand auch, was ich eigentlich meinte.

Vielleicht ist das im Moment sogar die interessantere Frage bei Spec-Driven Development mit KI:

**Wie gut kann eine Maschine unsere Spezifikation umsetzen?**

Oder:

**Was erfahren wir über unsere Spezifikation, wenn sie es tatsächlich tut?**