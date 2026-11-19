Stellen wir uns für einen Moment vor, ChatGPT, Claude und Codex wären keine KI-Systeme.

Sondern externe Auftragnehmer.

Man gibt ihnen einen Job, stellt die notwendigen Unterlagen zusammen, sie verschwinden damit für eine Weile in ihrem Büro und kommen anschließend mit einem Ergebnis zurück.

So weit, so normal.

Schwierig wird es erst, wenn nach einigen Monaten der Auftragnehmer wechselt.

Der neue Kollege sitzt am Tisch, schaut mich erwartungsvoll an und fragt:

„Was wurde bisher entschieden?“

Und ich sage:

„Moment.“

Dann öffne ich den Chat des alten Auftragnehmers.

Dort steht irgendwo, warum wir Datei A verwendet und Datei B verworfen haben. Dort steht, welche Variante wir ausprobiert haben. Dort steht, was nicht funktioniert hat. Dort stehen Rückfragen, Zwischenergebnisse, Entscheidungen und womöglich genau der eine Satz, der erklärt, warum das Projekt heute so aussieht, wie es aussieht.

Ich besitze zwar noch meinen Code.

Aber einen Teil meiner Arbeit besitzt der Chat.

Das ist ungefähr der Punkt, an dem die **Independent Workbench** entstanden ist.

Die Idee ist zunächst erstaunlich unspektakulär:

Ich möchte KI-Systeme benutzen können, ohne ihnen mein Projektgedächtnis zu schenken.

Also habe ich angefangen, dieses Gedächtnis aus dem Chat herauszuholen.

Aufträge, Quellen, Ergebnisse und Entscheidungen sollten bei mir liegen. Die KI sollte nur noch das bekommen, was sie für einen konkreten Job braucht – und danach wieder verschwinden können.

Die Workbench soll deshalb wie mein eigenes Projektbüro funktionieren. Dort liegen Auftrag, Quellen, Ergebnisse und Entscheidungen. Eine KI bekommt für einen konkreten Job nur die Unterlagen, die sie tatsächlich braucht. Sie erledigt die Arbeit. Das Ergebnis kommt zurück. Und irgendwann kann ein anderer Anbieter denselben Job übernehmen, ohne dass vorher eine digitale Ausgrabung in alten Chats notwendig ist.

Das klingt vernünftig.

Es klingt sogar so vernünftig, dass man sehr schnell glauben könnte, das Problem sei damit gelöst.

Das war es nicht.

### Wir haben bereits ein Büro. Nur noch keinen echten Auftragnehmer.

Die gute Nachricht zuerst:

Das Projekt funktioniert.

Zumindest in der Bedeutung von „funktioniert“, die man bei einem Pre-Alpha-Projekt verwenden sollte.

Es gibt eine portable Kernanwendung. Quellen, Aufgaben, Ergebnisse und Prüfbelege haben maschinenlesbare Formate. Es gibt Regeln für Berechtigungen und Datenklassen. Tests laufen. Eine lokale Demo nimmt eine vorbereitete PHP-Datei, erstellt daraus einen Auftrag, lässt einen Fake-Reviewer arbeiten, überprüft dessen Befund und legt anschließend sechs nachvollziehbare Dateien ab.

Vereinfacht gesagt: Die Workbench kann heute bereits einen kleinen Auftrag vorbereiten, kontrolliert ausführen lassen und das Ergebnis nachvollziehbar ablegen.

Das ist nicht nichts.

Aber es ist ungefähr so, als hätte man ein Restaurant eingerichtet, die Küche getestet, den Bon-Drucker angeschlossen und mit den Mitarbeitern einmal den Freitagabend durchgespielt.

Nur Gäste waren noch keine da.

Die derzeitige Workbench ist eine Generalprobe.

Das Büro steht.

Die Formulare liegen bereit.

Die Ablage funktioniert.

Ein Testdarsteller hat bereits einen Auftrag erledigt.

Was noch fehlt, ist der Moment, in dem tatsächlich Claude, OpenAI, Codex oder irgendein anderer externer Dienst auf der anderen Seite der Tür steht.

Bis hierhin hatte ich also vor allem geprüft, ob meine Workbench das tut, was ich programmiert hatte.

Das tat sie.

Also habe ich den Blick gewechselt.

Statt weiterzubauen, habe ich die Idee mehreren Kritikern zum Fraß vorgeworfen. Sie sollten nicht bestätigen, dass die Architektur plausibel klingt.

Sie sollten nach den Stellen suchen, an denen ich mir selbst etwas vormache.

Nicht:

Findet ihr die Idee gut?

Sondern:

Wo bricht sie?

Einige Einwände konnte ich ziemlich schnell abhaken.

Andere blieben liegen.

Einer davon betraf ausgerechnet den Teil, bei dem ich mich bis dahin ziemlich sicher gefühlt hatte:

die Kontrolle darüber, welche Daten das System verlassen.

### Mein Pförtner ist gewissenhaft. Leider schaut er in den falschen Teil des Pakets.

Eine zentrale Idee der Workbench lautet:

Nicht jede Information darf automatisch an irgendeine Cloud-KI geschickt werden.

Also bekommt jede Quelle eine Klassifikation.

Öffentlich.

Cloud erlaubt.

Nur lokal.

Und bevor etwas das eigene System verlässt, kontrolliert die Workbench diese Angaben.

Sehr ordentlich.

Leider gibt es ein Problem.

Eine der Review-Fragen war nämlich ziemlich banal:

**Prüfen wir eigentlich wirklich, was das Haus verlässt?**

Im aktuellen Modell prüft der Pförtner im Wesentlichen den Lieferschein.

Auf dem steht:

Im Karton befinden sich drei freigegebene Dateien.

Stempel drauf.

Tor auf.

Nur wissen wir damit noch nicht sicher, ob im Karton tatsächlich genau diese drei Dateien liegen.

Ein Programm könnte theoretisch ein korrekt freigegebenes Kontextpaket prüfen – und anschließend andere Bytes an den Anbieter übertragen.

Der Prüfbericht wäre sauber.

Der Datenabfluss möglicherweise nicht.

Man könnte nun sagen:

Dann schauen wir eben direkt vor dem Versand noch einmal in den Karton.

Nur reicht auch das nicht.

Wenn zwischen Prüfung und Übertragung noch etwas verändert werden kann, prüfen wir Zustand A und verschicken womöglich Zustand B.

Das ist keine philosophische Spitzfindigkeit. Es ist einer der echten Blocker vor dem ersten Cloud-Runner.

Die Lösung ist entsprechend wenig glamourös:

Der Karton muss versiegelt werden.

Aus den freigegebenen Daten muss ein unveränderliches Sendepaket entstehen. Davon wird ein digitaler Fingerabdruck erzeugt. Und anschließend muss überprüfbar sein, dass exakt dieses Paket tatsächlich übertragen wurde.

Nicht:

„Wir glauben, dass wir diese Dateien geschickt haben.“

Sondern:

„Das hier waren die Bytes, die das Haus verlassen haben.“

Erst dann kontrolliert der Pförtner tatsächlich den Karton.

### Und dann kommt der Agent und sagt: „Ich hole mir nur noch schnell etwas aus dem Keller.“

Bei einem klassischen KI-Aufruf wäre die Sache damit fast erledigt:

Paket rein.

Antwort raus.

Nur ist ein Coding Agent kein Briefkasten.

Er arbeitet während eines Auftrags weiter, liest, probiert aus, benutzt Werkzeuge und stellt manchmal erst unterwegs fest, dass ihm etwas fehlt.

Und irgendwann sagt er möglicherweise:

„Für diese Aufgabe brauche ich übrigens noch config.production.secret.irgendwas.“

Wenn der Agent in diesem Moment freien Zugriff auf das gesamte Projekt hat, können wir uns das sorgfältig zusammengestellte Kontextpaket auch an den Kühlschrank hängen.

Dann wurde zwar am Anfang geprüft, welche Unterlagen erlaubt sind.

Anschließend darf der Auftragnehmer aber selbst durch die Aktenschränke laufen.

Die Workbench braucht deshalb langfristig eine ziemlich klare Regel:

Entweder der Agent arbeitet ausschließlich mit seinem versiegelten Paket.

Oder jeder zusätzliche Zugriff läuft erneut durch die kontrollierte Tür.

Und diese Tür muss im Zweifel auch sagen können:

Nein.

Diese Schublade bleibt zu.

### Leider kann Software nicht erkennen, dass jemand „streng vertraulich“ als „öffentlich“ markiert hat.

Selbst wenn diese technische Kontrolle irgendwann perfekt funktioniert, bleibt allerdings eine zweite Frage:

**Wer entscheidet eigentlich, was überhaupt hinausdarf?**

Damit kommen wir zu einem Problem, das sich nicht wegprogrammieren lässt.

Menschen.

Die Workbench kann Regeln hervorragend durchsetzen.

Wenn dort steht:

local-only

kann sie verhindern, dass eine Datei an einen Cloud-Anbieter geschickt wird.

Was sie nicht wissen kann:

Ob local-only überhaupt die richtige Entscheidung war.

Wenn jemand eine vertrauliche Datei versehentlich als öffentlich klassifiziert, führt die Maschine eine falsche Anweisung vollkommen korrekt aus.

Das ist eine dieser Stellen, an denen Technik gerne beeindruckend aussieht und Organisation trotzdem notwendig bleibt.

Man kann sichere Standardwerte verwenden.

Man kann unbekannte Daten zunächst grundsätzlich lokal halten.

Man kann eine Vorschau anzeigen.

Bei besonders kritischen Informationen kann ein zweiter Mensch die Freigabe prüfen.

Aber irgendwann muss jemand sagen:

„Ja. Diese Information darf raus.“

Die Workbench kann Verantwortung sichtbar machen.

Sie kann sie nicht abschaffen.

### Ein Beleg ist übrigens noch kein Beweis

Einer der Bausteine, die zunächst sehr beruhigend wirken, ist der Receipt.

Zu jedem Lauf soll die Workbench später einen solchen Receipt erzeugen.

Im Grunde einen Kassenzettel:

Welcher Anbieter?

Welcher Auftrag?

Welche Quellen?

Welches Ergebnis?

Wann?

Mit welchen digitalen Fingerabdrücken?

Das ist enorm nützlich.

Aber auch hier lauert eine hübsche Selbsttäuschung.

Wenn meine eigene Software hinterher einen Zettel ausdruckt, auf dem steht:

Ich habe exakt diese Daten übertragen.

dann weiß ich zunächst nur eines:

Meine Software behauptet, exakt diese Daten übertragen zu haben.

Der Receipt wird erst wirklich interessant, wenn er dort entsteht, wo die Daten tatsächlich das System verlassen.

Also wieder am Tor.

Damit taucht langsam ein Muster auf.

Je genauer ich hinschaue, desto weniger geht es bei diesem Projekt eigentlich um KI.

Es geht um **Kontrolle von Übergaben**.

Wer bekommt was?

Wer durfte das entscheiden?

Was wurde tatsächlich übergeben?

Was kam zurück?

Was wurde davon angenommen?

Und lässt sich das später noch nachvollziehen?

An diesem Punkt wechselten die Reviews erneut die Perspektive.

Denn selbst wenn ich sauber kontrollieren kann, was einen Anbieter erreicht, bleibt noch eines meiner ursprünglichen Versprechen übrig:

**Ich wollte diesen Anbieter ja gerade austauschbar machen.**

### Jetzt wechseln wir einfach von Claude zu OpenAI.

Austauschbarkeit war von Anfang an eines der großen Versprechen der Workbench.

Die Idee dahinter klingt technisch angenehm sauber:

Zwischen Workbench und KI sitzt ein sogenannter Runner. Er übersetzt den Auftrag für den jeweiligen Anbieter.

Soll Claude raus und OpenAI rein, tauschen wir eben den Runner.

Zumindest auf dem Papier.

Denn auch das ist im Moment noch ein Satz.

Kein Beweis.

Heute existiert davon ein Fake Runner.

Der macht genau das, was er machen soll.

Was ungefähr so überraschend ist wie die Erkenntnis, dass mein selbst geschriebener Testkunde die Hausordnung vorbildlich befolgt.

Interessant wird es erst mit zwei echten, ausreichend unabhängigen Wegen.

Dann bekommt Runner A einen Auftrag.

Runner B bekommt fachlich denselben Auftrag.

Beide Ergebnisse landen wieder lokal.

Und anschließend wird nicht geprüft, ob beide dasselbe geschrieben haben.

Das wäre Unsinn.

Zwei gute Berater können zu unterschiedlichen Einschätzungen kommen.

Entscheidend ist etwas anderes:

Erfüllen beide dieselben fachlichen Mindestanforderungen?

Kann ich mit beiden Resultaten weiterarbeiten?

Und bleibt mein bisheriger Projektstand erhalten, wenn ich einen der Anbieter aus dem System werfe?

Das wäre echte Austauschbarkeit.

Nicht:

Jede KI antwortet gleich.

Sondern:

Keine KI besitzt mein Projekt.

Bis hierhin hatten wir immer dieselbe Frage gestellt:

**Wie muss die Workbench gebaut sein, damit ihre Versprechen halten?**

Dann kam aus den Reviews eine unangenehmere Frage.

Eine, die nicht einen Baustein angreift, sondern das ganze Projekt:

**Warum braucht es die Workbench überhaupt?**

### Vielleicht ist aber auch Markdown die bessere Software.

Denn der härteste Konkurrent der Independent Workbench ist womöglich kein Startup.

Kein amerikanischer Plattformanbieter.

Keine neue Agenten-IDE.

Ein Ordner.

Man kann nämlich bereits heute einen Auftrag in eine Markdown-Datei schreiben.

Die freigegebenen Quellen danebenlegen.

Alles an Claude oder ChatGPT übergeben.

Die Antwort speichern.

Eine Entscheidung darunter schreiben.

Git commit.

Fertig.

Für seltene und wenig riskante Aufgaben ist das möglicherweise vollkommen ausreichend.

Das ist für mich inzwischen eine der wichtigsten Prüfungen des gesamten Projekts.

Die Workbench darf nicht deshalb existieren, weil man eine Workbench bauen kann.

Sie muss etwas besser machen.

Zum Beispiel:

Datenfreigaben zuverlässig durchsetzen.

Einen unterbrochenen Auftrag später wieder aufnehmen.

Den Anbieter wechseln.

Prüfungen strukturieren.

Oder nach Monaten noch erklären können, warum eine Entscheidung getroffen wurde.

Wenn Nutzer irgendwann sagen:

„Schönes System. Ich kopiere die drei Dateien trotzdem schnell in ChatGPT.“

dann haben sie vermutlich recht.

Das wäre kein Onboarding-Problem.

Das wäre ein Produkturteil.

### Es könnte auch sein, dass wir eine perfekte Bürokratie bauen.

Selbst wenn die Workbench gegenüber einem Ordner objektiv Vorteile hat, könnte sie an etwas viel Banalerem scheitern:

Niemand möchte sie benutzen.

Aufgabenverträge.

Kontextpakete.

Freigaben.

Receipts.

Prüfungen.

Entscheidungen.

Für einen wichtigen Auftrag klingt das vernünftig.

Für:

„Kannst du bitte in diesen 20 Zeilen PHP nachsehen, warum die Variable leer ist?“

klingt es irgendwann nach ISO-Zertifizierung für einen Toaster.

Auch das gehört zu den Risiken.

Ein System, das Menschen kontrollierte Arbeitsabläufe ermöglichen soll, kann so viel Kontrolle verlangen, dass Menschen es umgehen.

Dann gewinnt wieder der Chat.

Nicht weil er sicherer ist.

Sondern weil er schneller ist.

Die Workbench braucht deshalb wahrscheinlich nicht **einen** Prozess.

Sie braucht ein Verhältnis zwischen Risiko und Aufwand.

Kleine Aufgabe?

Kleine Leitplanke.

Kritischer Auftrag mit vertraulichen Daten und langfristigen Auswirkungen?

Der ganze Papierkrieg.

Oder zumindest dessen digitale Variante.

### Kontrolle hat noch eine zweite, viel langweiligere Seite.

Bisher ging es darum, was das System verlassen darf.

Aber wenn das Projektgedächtnis tatsächlich bei mir bleiben soll, muss ich auch fragen, ob es dort morgen noch existiert.

Festplatten gehen kaputt.

USB-Laufwerke verschwinden.

Verzeichnisse werden gelöscht.

Konfigurationen zeigen auf Datenträger, die gerade überhaupt nicht angeschlossen sind.

Wenn das große Versprechen lautet:

Dein Projektgedächtnis bleibt bei dir.

wäre es ausgesprochen unglücklich, dieses Projektgedächtnis erfolgreich vor OpenAI, Anthropic und Microsoft zu schützen und anschließend durch eine sterbende SSD zu verlieren.

Deshalb gehört zu Anbieterunabhängigkeit irgendwann auch eine ziemlich langweilige Übung:

Backup machen.

Auf einen anderen Rechner gehen.

Restore durchführen.

Und prüfen, ob das Projekt dort ohne ursprünglichen Anbieter wieder vollständig verständlich ist.

Langweilige Tests sind manchmal die interessantesten.

### Was haben die Kritiker also kaputtgemacht?

Erstaunlich wenig.

Oder ziemlich viel.

Je nachdem, was man vorher behauptet hat.

Die Grundidee wurde nicht widerlegt.

Cloud-Nutzung widerspricht lokaler Kontrolle nicht automatisch.

Ein Agent darf während eines Auftrags ein eigenes Arbeitsgedächtnis haben.

Ein lokales KI-Modell ist keine Voraussetzung.

Zwei verschiedene Anbieter müssen nicht dieselben Antworten produzieren.

Und dass die aktuelle Oberfläche eine Python-Kommandozeile ist, ist bei einem frühen Entwickler-MVP kein Weltuntergang.

Kaputtgegangen ist etwas anderes:

die Versuchung, aus einer funktionierenden Architektur zu früh ein bewiesenes Produktversprechen zu machen.

Heute kann die Independent Workbench nicht seriös behaupten:

Wir verhindern Datenabfluss.

Oder:

Beliebige KI-Anbieter sind austauschbar.

Oder:

Das System erfüllt Compliance-Anforderungen.

Was sie heute sagen kann, ist kleiner.

Aber meiner Meinung nach interessanter:

Wir haben eine lokale Generalprobe gebaut.

Jetzt können wir die Behauptungen einzeln testen.

### Der nächste Test ist deshalb erfreulich unspektakulär

Aus den Reviews ist deshalb keine Liste mit zwanzig neuen Features entstanden.

Eher das Gegenteil.

Der nächste Schritt ist kleiner geworden.

Kein Multi-Agent-System.

Keine Vektordatenbank.

Keine riesige Weboberfläche.

Kein lokales 400-Milliarden-Parameter-Modell unter meinem Schreibtisch.

Ein echtes Repository.

Ein echter lesender Auftrag.

Ein exakt definiertes Sendepaket.

Zwei echte oder zumindest ausreichend unabhängige Runner.

Fachliche Mindestkriterien.

Lokale Speicherung.

Dann ziehen wir einem Anbieter den Stecker.

Können wir trotzdem weiterarbeiten?

Danach exportieren wir das Projekt.

Stellen es auf einem zweiten System wieder her.

Und irgendwann geben wir es echten Nutzern.

Nicht um zu zählen, wie viele JSON-Dateien die Workbench erzeugt.

Sondern um herauszufinden, ob sie weniger Wissen verlieren.

Ob sie Aufgaben leichter wieder aufnehmen.

Ob sie Fehler vermeiden.

Und vor allem:

Ob sie die Workbench tatsächlich benutzen.

### Vielleicht ist das eigentliche Produkt gar nicht die Workbench

Ich hatte die Reviews ursprünglich angestoßen, um herauszufinden, ob wir wirklich Anbieterunabhängigkeit gebaut hatten – oder nur eine Architektur, die danach aussieht.

Übrig geblieben ist eine andere Frage als die, mit der ich angefangen habe.

Nicht:

**Kann ich eine Software bauen, mit der sich unterschiedliche KI-Systeme ansteuern lassen?**

Natürlich kann man das.

Die interessantere Frage lautet:

**Kann ich KI wie einen externen Auftragnehmer behandeln, ohne gleichzeitig mein Projektgedächtnis, meine Entscheidungen und meine Kontrolle an diesen Auftragnehmer auszulagern?**

Und noch unangenehmer:

**Kann ich diese Kontrolle zurückholen, ohne dabei so viel Bürokratie zu erzeugen, dass niemand das System freiwillig benutzt?**

Genau das ist im Moment die eigentliche Produktthese der Independent Workbench.

Vielleicht stellt sich am Ende heraus, dass dafür ein paar Markdown-Dateien und Git reichen.

Vielleicht braucht es eine Workbench.

Vielleicht entsteht etwas dazwischen.

Aber immerhin können wir jetzt unterscheiden, was wir wissen und was wir lediglich hoffen.

Der Pförtner steht jedenfalls schon am Tor.

Ich dachte nur anfangs, seine Aufgabe bestünde darin, Lieferscheine zu kontrollieren.

Inzwischen sieht es eher so aus, als müssten wir herausfinden, wie man das ganze Büro organisiert.

## Quellen und Arbeitsnotizen

Die Fußnoten sitzen vor allem an den **Entstehungspunkten der Gedanken**, nicht als nachträgliche „Beweisstempel“ für jede Meinung. Das passt besser zum Charakter des Artikels als Entwicklernotiz und Arbeitsstand.

### Fußnoten

### 1. Local-first als Hintergrund der Produktidee

Martin Kleppmann, Adam Wiggins, Peter van Hardenberg und Mark McGranaghan beschreiben mit „Local-first Software“ ein Modell, bei dem die lokale Kopie maßgeblich bleibt und Nutzer Kontrolle und langfristigen Zugriff auf ihre Daten behalten, ohne Cloud-Funktionen grundsätzlich auszuschließen.

Das Papier war für die Überlegung relevant, Projektgedächtnis und Provider voneinander zu trennen.

**Quelle:** Ink & Switch, *Local-first software: You own your data, in spite of the cloud*, 2019. [Local-first software – Ink & Switch](https://www.inkandswitch.com/essay/local-first/)

---

### 2. Aktueller Stand der Independent Workbench

Die Projekt-README dokumentiert die lokale M0-Demo: Eine PHP-Datei wird gelesen und gehasht, ein deterministischer Fake Reviewer ausgeführt, dessen Befund überprüft und sechs nachvollziehbare JSON-Artefakte erzeugt.

Das Projekt bezeichnet dies ausdrücklich als lokalen Contract Flow und nicht als Nachweis für Provider Switching.

**Quelle:** Independent Workbench, Projekt-README und M0-Dokumentation.

---

### 3. Adversarial Reviews als Arbeitsmethode

Im Repository existiert ein eigener Review-Auftrag, der unter anderem Fail-closed-Verhalten, Egress-Klassifikation, Berechtigungen, Time-of-check/Time-of-use-Probleme, Secrets und technisch nicht überprüfbare Behauptungen gezielt angreifen soll.

Daraus entstanden unter anderem die dokumentierten Claude- und Copilot-Reviews.

**Quelle:** Independent Workbench, `adversarial-project-review.prompt.md` sowie die dokumentierten Adversarial Reviews.

---

### 4. Egress-Klassen der Workbench

Im eigentlichen Datenmodell sind die Klassen genauer als im vereinfachten Bild des Artikels:

- `public`
- `cloud-approved`
- `cloud-redacted`
- `local-only`

Unbekannte Klassifikationen werden standardmäßig nicht abgeschwächt, sondern bleiben `local-only`; der Preflight weist solche Quellen für externe Runner zurück.

**Quelle:** Independent Workbench, Datenmodell, Schemas und Preflight-Tests.

---

### 5. Der „Pförtner kontrolliert den Lieferschein“

Diese Überlegung stammt unmittelbar aus der Architektur- und Reviewarbeit.

Das aktuelle Architekturdokument hält fest, dass der Preflight deklarierte Metadaten validiert. Vor dem ersten externen Adapter soll die Freigabe deshalb an die exakten Bytes gebunden werden, die der Adapter tatsächlich senden kann.

Dynamische Reads müssen entweder verhindert oder kontrolliert und aufgezeichnet werden. Ein Receipt allein gilt dort ausdrücklich nicht als Beweis dafür, dass keine anderen Bytes versendet werden konnten.

**Quelle:** Independent Workbench, `WORKBENCH_ARCHITECTURE.md`.

---

### 6. Digitaler Fingerabdruck / Hash

NIST beschreibt kryptografische Hashfunktionen als Verfahren zur Erzeugung eines Message Digest, mit dem erkannt werden kann, ob eine Nachricht seit der Erzeugung des Digest verändert wurde.

Der Hash ist hier deshalb Teil der Überlegung zur Integrität eines freigegebenen Sendepakets; er ersetzt für sich allein keine kontrollierte Übertragungsgrenze.

**Quelle:** NIST, *FIPS 180-4 – Secure Hash Standard*. [Secure Hash Standard – NIST](https://www.nist.gov/publications/secure-hash-standard)

---

### 7. Coding Agents arbeiten iterativ und mit Werkzeugen

OpenAI beschreibt Coding Agents als Systeme, die Repositorys prüfen, Befehle ausführen und mit Entwicklungswerkzeugen interagieren können.

Für Codex werden deshalb Sandboxing, geschützte Pfade, Freigaben und kontrollierter Netzwerkzugriff als technische Grenzen eingesetzt.

Diese Arbeitsweise ist der Hintergrund für das Bild vom Agenten, der während eines Auftrags „noch einmal in den Keller“ möchte.

**Quelle:** OpenAI, *Running Codex safely at OpenAI*, 8. Mai 2026. [Running Codex safely at OpenAI – OpenAI](https://openai.com/index/running-codex-safely/)

---

### 8. Least Privilege und erneute Freigabe

OWASP empfiehlt für KI-Agenten, nur die für einen konkreten Auftrag notwendigen Tools und Ressourcen freizugeben, Rechte auf einzelne Ressourcen zu begrenzen und für sensible Aktionen explizite Autorisierung vorzusehen.

Das ist der Sicherheitsgedanke hinter der „kontrollierten Tür“ für nachträglich angeforderte Zugriffe.

**Quelle:** OWASP Cheat Sheet Series, *AI Agent Security*. [AI Agent Security – OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html)

---

### 9. Austauschbarkeit ist noch nicht bewiesen

Die Workbench enthält derzeit einen deterministischen Fake Runner.

Das Repository und das Adversarial Review halten ausdrücklich fest, dass der tatsächliche Weg von einem realen Provider zu einem anderen noch nicht demonstriert wurde und der aktuelle M0-Durchstich kein Provider Switching beweist.

**Quelle:** Independent Workbench, README und Adversarial Reviews.

---

### 10. Lokale Kontrolle bringt Backup-Verantwortung mit sich

Ink & Switch weist bei Local-first Software darauf hin, dass Datenhoheit auch Verantwortung für Backups und Schutz vor Datenverlust bedeutet.

Die allgemeine Resilienz-Perspektive wird durch NISTs Contingency-Planning-Leitfaden ergänzt, der Recovery-Strategien sowie Tests und Übungen als Bestandteil eines belastbaren Wiederherstellungskonzepts behandelt.

**Quellen:** Ink & Switch, *Local-first software: You own your data, in spite of the cloud*. [Local-first software – Ink & Switch](https://www.inkandswitch.com/essay/local-first/)

NIST, *Contingency Planning Guide for Federal Information Systems (SP 800-34 Rev. 1)*.