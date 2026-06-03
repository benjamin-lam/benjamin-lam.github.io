---
title: "Was ich aus einer Copilot-Session über Prompt Driven Development gelernt habe"
slug: "was-ich-aus-einer-copilot-session-ueber-prompt-driven-development-gelernt-habe"
source: "LinkedIn"
source_slug: "linkedin"
source_url: "https://de.linkedin.com/pulse/ich-aus-einer-copilot-session-%C3%BCber-prompt-driven-development-lam-tccme"
first_published: "2026-05-22"
archived_at: "2026-06-03"
status: "aktuell"
tags:
  - "ki"
  - "prompting"
  - "copilot"
  - "entwicklung"
  - "arbeitswelt"
  - "kontext"
canonical_url: "https://benjamin-lam.github.io/linkedin/2026-05-22-was-ich-aus-einer-copilot-session-ueber-prompt-driven-development-gelernt-habe/"
description: "Archivierte Veröffentlichung von Benjamin Lam. Erstveröffentlicht am 22.05.2026 auf LinkedIn."
---

# Was ich aus einer Copilot-Session über Prompt Driven Development gelernt habe

## Hinweis zur Erstveröffentlichung

Dieser Artikel erschien zuerst am 22.05.2026 auf LinkedIn.

Original: https://de.linkedin.com/pulse/ich-aus-einer-copilot-session-%C3%BCber-prompt-driven-development-lam-tccme

## Artikel

---
Eigentlich wollte ich nur ein Vorschaubild debuggen.
OpenGraph. Link Share. LinkedIn Preview. Dieses schöne kleine Randthema, das immer genau dann aufpoppt, wenn man dachte: „Die Seite ist fertig.“
Das Bild wurde nicht sauber gezogen. Oder doch. Oder LinkedIn hatte noch einen alten Stand im Cache. Also einmal die übliche Runde: externe Preview-Tools, Meta-Tags prüfen, Cache-Vermutungen, Ergebnis vergleichen.
Und dann kam dieser sehr naheliegende Gedanke:
Warum habe ich dafür eigentlich kein eigenes Tool?
Nicht nur für OpenGraph. Auch für JSON. Base64. URL-Encoding. HTML-Entities. JWTs. Slugs. Structured Data. Markdown. Regex. Timestamp-Konvertierung. All diese kleinen Werkzeuge, die man ständig irgendwo im Netz sucht, obwohl man sie eigentlich lieber selbst kontrolliert hätte.
Und weil wir ja in Zeiten von KI-Automatisierung, Coding Agents und diesem ominösen „Vibe Coding“ leben, war der nächste Gedanke natürlich:
Warum ein Tool bauen, wenn ich gleich eine ganze Tool-Sammlung bekommen kann?
Gesagt. Gepromptet. Gebaut.
Ein paar Prompts später stand eine statische Web-Toolbox für GitHub Pages. Mobile first. Keine Cookies. Kein Tracking. Kein Backend. Keine externen CDNs. Keine externen Fonts. Keine Live-Prüfung fremder URLs im MVP. Dafür eine klare Struktur, Toolseiten, README, Security-Hinweise, Open-Source-Disclaimer und Playwright-Tests als Release-Sicherheitsnetz.
Aber eigentlich ist das Ergebnis gar nicht der spannendste Teil.
Spannender ist der Weg dahin.
Es ist noch gar nicht so lange her, da klangen viele KI-Coding-Versuche ungefähr so:
Dann kam ein bisschen Vibe. Ein bisschen Spezifikation. Ein paar technische Wünsche. Und am Ende etwas, das auf den ersten Blick beeindruckend aussah, aber beim zweiten Blick auseinanderfiel.
Nicht immer, weil der Prompt schlecht war.
Sondern weil die Systeme noch nicht wirklich gut darin waren, Arbeit zu strukturieren, Grenzen zu respektieren, Folgeentscheidungen sauber abzuleiten und den eigenen Output gegen die ursprünglichen Anforderungen zu prüfen.
Heute sieht das anders aus.
Nicht perfekt. Aber deutlich anders.
Die Tool-Liste war relativ banal:
JSON Formatter. HTML Formatter. Base64 Encode/Decode. URL Encode/Decode. JWT Decoder. UTM Builder. Markdown Preview. Regex Tester. OpenGraph Inspector aus eingefügtem HTML. Structured Data Extractor. Inspect-URI-Platzhalter.
Das ist nicht die Revolution.
Die eigentliche Qualität entstand durch die Grenzen:
```text
kein Backend
kein Tracking
keine Cookies
kein LocalStorage
keine externen CDNs
keine externen Fonts
kein npm für die App
kein Build-System
keine Live-Prüfung fremder URLs
kein Crawler
kein Proxy
kein Screenshot-Service
/api/inspect-uri nur vorbereiten
```
Diese Negativ-Anforderungen waren wahrscheinlich wichtiger als die eigentlichen Features.
Denn sie haben den Entscheidungsraum begrenzt.
Die KI musste nicht raten, ob sie „mal eben“ ein Framework hinzufügen soll. Sie musste nicht interpretieren, ob ein Service Worker hilfreich wäre. Sie musste nicht aus einer Toolseite plötzlich eine kleine SaaS machen.
Die Ansage war klar:
Statisch. Sicher. GitHub Pages. Browserbasiert. Kein Overengineering.
Und genau daraus entstand die Architektur.
Was mich an der Session wirklich interessiert hat, war die Beziehung zwischen Anweisung und Umsetzung.
Ein paar Beispiele:
Prompt-Anweisung / Umsetzung durch Copilot / Erkenntnis

- Prompt-Anweisung: „GitHub Pages kompatibel“
  Umsetzung durch Copilot: statische HTML/CSS/JS-Struktur
  Erkenntnis: Plattformwahl prägt Architektur
- Prompt-Anweisung: „kein npm / kein Build-System“
  Umsetzung durch Copilot: keine Frameworks, kein Build-Step
  Erkenntnis: Tooling wurde bewusst klein gehalten
- Prompt-Anweisung: „keine Cookies / kein Tracking“
  Umsetzung durch Copilot: keine Speicherung, keine Analytics
  Erkenntnis: Privacy wurde zur technischen Leitplanke
- Prompt-Anweisung: „keine externen Requests“
  Umsetzung durch Copilot: keine CDNs, keine Fonts, keine externen Libraries
  Erkenntnis: Performance und Datenschutz wurden miterzwungen
- Prompt-Anweisung: „/api/inspect-uri nur vorbereiten“
  Umsetzung durch Copilot: UI-Platzhalter statt gefährlicher Live-Fetch
  Erkenntnis: Zukunft vorbereitet, Risiko vermieden
- Prompt-Anweisung: „kein Crawler, kein Proxy“
  Umsetzung durch Copilot: Scope-&-Limits-Sektion
  Erkenntnis: Nicht-Ziele wurden Teil des Produkts
- Prompt-Anweisung: konkrete Dateiliste
  Umsetzung durch Copilot: alle Toolseiten wurden erstellt
  Erkenntnis: Struktur schlägt Absicht
- Prompt-Anweisung: konkrete Akzeptanzkriterien
  Umsetzung durch Copilot: Review entlang dieser Kriterien
  Erkenntnis: Prüfung wurde schon im Prompt mitgebaut
- Prompt-Anweisung: „Review als Security Reviewer“
  Umsetzung durch Copilot: innerHTML-Audit, Markdown-Bug gefunden
  Erkenntnis: Rollenwechsel verbessert Qualität
- Prompt-Anweisung: „Playwright nur für Tests“
  Umsetzung durch Copilot: npm nur als Testabhängigkeit
  Erkenntnis: Tooling erlaubt, Produktarchitektur geschützt
Das ist für mich der interessante Punkt:
Der erste Prompt hat gebaut.
Der zweite Prompt hat gehärtet.
Das ist vielleicht die wichtigste praktische Erkenntnis aus der Session.
Nach der ersten Umsetzung kam kein „sieht gut aus, merge“. Sondern ein zweiter Auftrag:
Prüfe das Projekt als Senior Frontend Engineer, Security Reviewer und Open-Source-Maintainer.
Und plötzlich wurden andere Dinge sichtbar:
- Fehlt eine LICENSE?
- Gibt es einen SECURITY.md?
- Ist der AI-assisted development Hinweis sauber formuliert?
- Gibt es einen Disclaimer?
- Wird irgendwo innerHTML mit Userdaten verwendet?
- Kann Markdown XSS auslösen?
- Sind alle Tools wirklich vorhanden?
- Sind alle Seiten über Navigation erreichbar?
- Gibt es externe Requests?
- Wird LocalStorage verwendet?
- Ist /api/inspect-uri wirklich nur vorbereitet?
Dabei wurde sogar ein echter Bug gefunden: Im Markdown-Parser gab es ein Problem mit JavaScripts String.replace() und $-Substitutionen. Kein XSS, kein Weltuntergang, aber ein echter Fehler — vermutlich genau einer von denen, die erst auffallen, wenn man das Tool gerade wirklich braucht und sich fragt, warum der Preview plötzlich Unsinn erzählt.
Nicht weil die KI perfekt war. Sondern weil der zweite Prompt einen anderen Blick erzwungen hat.
Bauen und Reviewen sind zwei verschiedene Tätigkeiten. Auch mit KI.
Vielleicht sogar besonders mit KI.
Ich habe nichts gegen Vibes.
Vibes sind gut, um eine Richtung zu setzen.
Aber Vibes ersetzen keine Grenzen.
„Mach mir eine schöne Toolseite“ führt zu irgendwas. „Baue eine statische GitHub-Pages-Toolbox ohne Backend, ohne Tracking, ohne externe Requests, mit genau diesen Toolseiten, diesen Nicht-Zielen, diesen Akzeptanzkriterien und anschließendem Security-Review“ führt zu einem anderen Ergebnis.
Das ist für mich der Unterschied:
Vibe Coding sagt:
Prompt Driven Development sagt:
Für mich war diese Session weniger ein Benchmark der KI.
Es war eher ein Benchmark der Beziehung zwischen Mensch und KI.
Die KI wurde nicht als magischer Entwickler behandelt. Auch nicht als dummer Codegenerator.
Eher als erfahrener Entwickler, der unverhofft in ein Projekt geworfen wird und deshalb sehr klare Rahmenbedingungen braucht:
- Was ist das Ziel?
- Was ist ausdrücklich nicht das Ziel?
- Welche Plattform gilt?
- Welche Risiken sollen vermieden werden?
- Was bedeutet „fertig“?
- Wer prüft das Ergebnis?
- Welche Tests sichern den Stand ab?
Je klarer diese Fragen beantwortet waren, desto besser wurde die Umsetzung.
Und ja, das Ergebnis nähert sich mittlerweile tatsächlich dem an, was man von einem erfahrenen Entwickler erwarten würde, der schnell produktiv werden soll.
Nicht, weil man ihn mit einem Superprompt motiviert. Sondern weil man ihm Kontext, Grenzen und Prüfkriterien gibt.
Erstens: **Nicht-Ziele sind produktiver als man denkt.** „Kein Backend“ hat mehr Architektur entschieden als „baue ein Tool“.
Zweitens: **Akzeptanzkriterien sind Prompts mit Zukunft.** Was am Ende geprüft werden soll, muss am Anfang formuliert werden.
Drittens: **Review ist ein eigener Prompt-Schritt.** Eine KI, die baut, ist nicht automatisch dieselbe KI, die gut prüft.
Viertens: **Tooling muss begrenzt werden.** Playwright für Tests? Ja. Playwright als Produktbestandteil? Nein.
Fünftens: **Ein guter Prompt erzeugt nicht nur Code, sondern Verhalten.** Er legt fest, wie Entscheidungen getroffen werden.
Ich wollte eigentlich nur ein OpenGraph-Problem lösen.
Am Ende hatte ich eine kleine Web-Toolbox und eine deutlich klarere Vorstellung davon, wie sich KI-gestützte Entwicklung gerade verändert.
Der spannende Teil ist nicht, dass eine KI Code schreiben kann.
Der spannende Teil ist, dass sie zunehmend in der Lage ist, innerhalb sauber formulierter Grenzen produktiv zu arbeiten.
Aber genau diese Grenzen entstehen nicht von allein.
Sie sind unsere Aufgabe.
Oder etwas zugespitzt:
Und jetzt wende ich mich wieder dem Eigentlichen zu.
Also vermutlich dem nächsten Nebenschauplatz, aus dem versehentlich wieder ein kleines Projekt wird.
---
*we're not behaving like insects.*
In diesem Sinne: bleibt eigenwillig. Und habt ein erholsames, sonniges Wochenende.
---
#PromptDrivenDevelopment #SpecDrivenDevelopment #VibeCoding #GitHubCopilot #AIAssistedDevelopment #Softwareentwicklung #DeveloperTools

## Über den Autor

Benjamin Lam nutzt einen erstaunlich großen Teil des Internets, um seine Gedanken zu posten. Falls du irgendwo etwas findest, das hier noch nicht archiviert ist: her damit.
