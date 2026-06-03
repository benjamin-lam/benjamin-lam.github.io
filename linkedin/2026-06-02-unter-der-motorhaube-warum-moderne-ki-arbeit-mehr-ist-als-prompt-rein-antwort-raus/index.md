---
title: "Unter der Motorhaube: Warum moderne KI-Arbeit mehr ist als „Prompt rein, Antwort raus“"
slug: "unter-der-motorhaube-warum-moderne-ki-arbeit-mehr-ist-als-prompt-rein-antwort-raus"
source: "LinkedIn"
source_slug: "linkedin"
source_url: "https://de.linkedin.com/pulse/unter-der-motorhaube-warum-moderne-ki-arbeit-mehr-ist-benjamin-lam-evr3f"
first_published: "2026-06-02"
archived_at: "2026-06-03"
status: "aktuell"
tags:
  - "ki"
  - "llm"
  - "prompting"
  - "entwicklung"
  - "arbeitswelt"
  - "infrastruktur"
canonical_url: "https://benjamin-lam.github.io/linkedin/2026-06-02-unter-der-motorhaube-warum-moderne-ki-arbeit-mehr-ist-als-prompt-rein-antwort-raus/"
description: "Archivierte Veröffentlichung von Benjamin Lam. Erstveröffentlicht am 02.06.2026 auf LinkedIn."
---

# Unter der Motorhaube: Warum moderne KI-Arbeit mehr ist als „Prompt rein, Antwort raus“

## Hinweis zur Erstveröffentlichung

Dieser Artikel erschien zuerst am 02.06.2026 auf LinkedIn.

Original: https://de.linkedin.com/pulse/unter-der-motorhaube-warum-moderne-ki-arbeit-mehr-ist-benjamin-lam-evr3f

## Artikel

Wenn heute über KI gesprochen wird, fällt oft dieser Satz:
Das ist nicht falsch.
Aber es ist inzwischen ungefähr so vollständig wie:
Stimmt irgendwie. Hilft aber nur begrenzt, wenn man verstehen will, warum moderne Fahrzeuge bremsen, lenken, navigieren, einparken, warnen, Daten sammeln und mit anderen Systemen kommunizieren.
Bei KI passiert gerade etwas Ähnliches.
Das neuronale Netz im Kern bleibt wichtig. Natürlich. Ohne Modell keine Antwort. Ohne Wahrscheinlichkeiten kein Text. Ohne Training keine Muster.
Aber wer heute mit Coding-Agenten, KI-gestützten Workflows oder Werkzeugen wie Claude Code, Codex, Cursor, DeepSeek-Setups oder anderen agentischen Systemen arbeitet, merkt schnell:
Da passiert längst mehr als nur:
```text
Text rein
wahrscheinliche Antwort raus
```
Zwischen Eingabe und Ergebnis entsteht ein Arbeitsraum.
Und genau dieser Arbeitsraum wird gerade zur eigentlichen Schnittstelle zwischen Mensch und KI.
---
Das klassische Chatfenster wirkt einfach.
Ich schreibe etwas. Die KI antwortet. Ich schreibe weiter. Die KI antwortet wieder.
Das ist die Oberfläche.
Aber moderne KI-Systeme arbeiten zunehmend nicht mehr nur als Antwortgeneratoren, sondern als Agenten in einer Umgebung. Sie können Dateien lesen, Dateien verändern, Befehle ausführen, externe Werkzeuge aufrufen, Zwischenergebnisse prüfen und ihre nächsten Schritte anhand dieser Ergebnisse anpassen. OpenAI beschreibt Tools in den Agents SDK-Dokumenten genau in diesem Sinne: Werkzeuge lassen Agenten Aktionen ausführen — etwa Daten abrufen, Code laufen lassen, APIs aufrufen oder sogar mit einem Computer interagieren.
Anthropic beschreibt Claude Code ähnlich als agentisches Coding-Werkzeug, das in der Lage ist, Dateien zu lesen, Kommandos auszuführen, Code zu editieren und Kontext zu verwalten.
Das ist eine wichtige Verschiebung.
Denn sobald eine KI nicht mehr nur antwortet, sondern handelt, reicht die alte Frage nicht mehr aus:
Die bessere Frage lautet:
Und damit sind wir nicht mehr nur beim Prompt. Wir sind beim Arbeitsraum.
---
Ein moderner KI-Arbeitsraum besteht aus mehreren Schichten.
Nicht alle sind immer sichtbar. Manche Anbieter zeigen sie teilweise. Manche verstecken sie tief in Protokollen, Agent-Traces, Tool-Calls oder internen Abläufen.
Aber konzeptionell sind sie da.
Am Anfang steht nicht einfach „ein Prompt“, sondern ein Arbeitsauftrag.
Was soll passieren? Was soll nicht passieren? Welche Dateien sind betroffen? Welche Regeln gelten? Wann ist die Aufgabe fertig?
Das klingt nach Bürokratie. Ist es aber nicht.
Es ist der Unterschied zwischen:
und:
Der zweite Auftrag gibt der KI einen Arbeitsrahmen. Der erste gibt ihr eine Einladung zum Raten.
---
Früher haben wir viel über Prompt Engineering gesprochen.
Also: Wie formuliere ich die perfekte Eingabe?
Das bleibt nützlich. Aber es reicht nicht mehr.
Anthropic beschreibt diese Entwicklung als Übergang von Prompt Engineering zu Context Engineering: Es geht nicht mehr nur darum, die richtigen Worte in einen Prompt zu schreiben, sondern darum, den gesamten Kontextzustand zu gestalten, der dem Modell zur Verfügung steht — Systemanweisungen, Tools, externe Daten, Gesprächsverlauf, Dateien und Zwischenergebnisse.
Das ist ein entscheidender Punkt.
Denn KI arbeitet nicht mit „Wissen“ im menschlichen Sinn, sondern mit dem Kontext, der ihr gerade zugänglich ist. Und dieser Kontext ist begrenzt. Je länger eine Sitzung wird, desto größer wird die Gefahr, dass wichtige Informationen verwässern, in den Hintergrund rutschen oder mit neuen Informationen kollidieren. Anthropic beschreibt Kontext ausdrücklich als kritische, aber endliche Ressource für Agenten.
Für die Praxis bedeutet das:
Der Arbeitsraum muss den Kontext pflegen.
Nicht alles ist immer gleich wichtig. Nicht jede alte Nachricht gehört dauerhaft in den Vordergrund. Nicht jede Datei muss gelesen werden. Nicht jede Regel darf vergessen werden.
Der Arbeitsraum entscheidet mit darüber, was die KI gerade sieht — und was nicht.
---
Eine KI trifft ständig Annahmen.
Über dein Ziel. Über deine Architektur. Über deine Zielgruppe. Über Dateinamen. Über Datenformate. Über das, was du „eigentlich“ gemeint haben könntest.
Das ist nicht automatisch schlecht. Ohne Annahmen käme sie oft gar nicht ins Arbeiten.
Gefährlich wird es, wenn diese Annahmen unsichtbar bleiben.
Dann verstecken sie sich im Ergebnis.
Bei Texten merkt man das vielleicht an einem falschen Ton. Bei Konzepten an einer verschobenen Zielgruppe. Bei Code an einer Änderung, die technisch funktioniert, aber nicht in dein System passt.
Ein guter Arbeitsraum macht Annahmen sichtbar.
Zum Beispiel:
```text
Ich nehme an:
- Die Zielgruppe ist nicht rein technisch.
- Es darf keine neue Bibliothek eingeführt werden.
- Die bestehende API soll unverändert bleiben.
- Die Änderung betrifft nur die Oberfläche.
```
Dann kann der Mensch sagen:
```text
stimmt
falsch
unklar
muss geprüft werden
```
Das ist kein Luxus. Das ist Qualitätskontrolle.
---
Viele moderne Coding-Agenten arbeiten mit einer Planungsphase.
Man sieht das in unterschiedlichen Formen: als expliziten Plan, als Todo-Liste, als Agent-Loop, als Zwischenschritt, als Tool-Trace oder als internes Arbeitsprotokoll.
Der Punkt ist immer ähnlich:
Die KI soll nicht sofort losrennen.
Sie soll erst zerlegen:
```text
1. Relevante Dateien finden
2. Bestehendes Verhalten verstehen
3. Änderung planen
4. Risiken prüfen
5. Umsetzung vorbereiten
6. Ergebnis testen
```
Anthropic betont bei agentischen Systemen außerdem, dass menschliche Reviews weiterhin entscheidend bleiben, selbst wenn automatisierte Tests helfen, Funktionalität zu prüfen. Denn ob eine Lösung zu den größeren Systemanforderungen passt, ist nicht allein eine Testfrage.
Das ist ein schöner Realitätscheck.
Tests können sagen:
Der Mensch muss oft sagen:
---
Hier wird der Unterschied zum klassischen Chat besonders deutlich.
Ein LLM allein schreibt Text. Ein Agent mit Tools kann handeln.
Tool-Calls sind die Stellen, an denen die KI ein Werkzeug benutzt:
```text
Datei lesen
Datei ändern
Shell-Befehl ausführen
Test starten
API aufrufen
Websuche durchführen
Datenbank prüfen
Patch anwenden
```
OpenAI beschreibt in den Agents SDK-Dokumenten verschiedene Werkzeugtypen, darunter gehostete Tools, lokale Runtime-Tools, Funktionsaufrufe, Agents-as-Tools und Codex-bezogene Aufgaben.
Anthropic beschreibt für Claude Code ebenfalls eine Agent-Umgebung mit eingebauten Werkzeugen zum Lesen, Ausführen und Bearbeiten, inklusive Optionen für Sessions, Freigaben, Hooks, Checkpointing, Kostenverfolgung und Observability.
Das ist der Moment, in dem KI-Arbeit real wird.
Nicht mehr:
Sondern:
Und sobald etwas verändert wird, brauchen wir Kontrolle.
---
Ein guter Arbeitsraum braucht Stoppschilder.
Nicht als Misstrauen gegenüber der KI. Sondern als Respekt vor Verantwortung.
Vor allem bei Aktionen mit Folgen:
```text
Dateien ändern
Code ausführen
Daten löschen
Deployments starten
E-Mails versenden
Tickets schließen
APIs aufrufen
```
Ein Freigabepunkt bedeutet:
Das ist für mich einer der wichtigsten Unterschiede zwischen Spielerei und produktiver KI-Arbeit.
Nicht die KI trägt Verantwortung. Der Mensch trägt Verantwortung.
Aber dafür muss der Arbeitsraum dem Menschen überhaupt die Möglichkeit geben, Verantwortung sinnvoll auszuüben.
Ein einzelnes Chatfenster mit langer Historie ist dafür oft zu weich. Ein strukturierter Arbeitsraum mit Plan, Annahmen, Scope und GO ist deutlich belastbarer.
---
Jetzt kommt der Teil, der mich besonders interessiert.
Die großen Anbieter verstecken viel davon in Arbeitsprotokollen, Agent-Traces, Tool-Calls, Session-Summaries oder internen Planungsphasen.
Das ist verständlich. Nicht jede Nutzerin und jeder Nutzer will jede Zwischenbewegung sehen.
Aber für alle, die mit KI ernsthaft arbeiten wollen, ist genau diese Spur wertvoll.
Ein Agent-Trace kann zeigen:
```text
Welche Aufgabe wurde verstanden?
Welche Dateien wurden gelesen?
Welche Tools wurden benutzt?
Welche Fehler traten auf?
Welche Entscheidung wurde getroffen?
Welche Änderung wurde geschrieben?
Welche Prüfung wurde durchgeführt?
```
OpenAI beschreibt Traces als Möglichkeit, agentisches Verhalten sichtbar zu machen: Prompts, Tool-Calls, Handoffs zwischen Agenten, MCP-Server-Aufrufe, Codex-CLI-Aufrufe, Ausführungszeiten, Dateiänderungen sowie Fehler und Warnungen können aufgezeichnet werden.
Das ist nicht nur Debugging.
Das ist Nachvollziehbarkeit.
Und Nachvollziehbarkeit ist die Voraussetzung dafür, aus KI-Arbeit zu lernen.
---
Natürlich sieht man diese Entwicklung im Coding besonders deutlich.
Code ist konkret. Dateien ändern sich. Tests laufen durch oder scheitern. Diffs zeigen Unterschiede. Deployments haben sichtbare Folgen.
Aber das Prinzip betrifft nicht nur Code.
Auch bei Texten, Konzepten, Strategien, Präsentationen, Angeboten, Prozessen oder Recherchen entsteht ein Arbeitsraum.
Nehmen wir einen Artikel.
Auch dort gibt es:
```text
Ziel
Zielgruppe
Ton
Nicht-Ziele
Annahmen
Struktur
Entwurf
Review
Überarbeitung
Veröffentlichung
Feedback
```
Oder ein Angebot.
```text
Kundensituation
Leistungsumfang
Risiken
Annahmen
Ausschlüsse
Preislogik
Freigabe
Versionierung
Nachverhandlung
```
Oder ein Konzept.
```text
Problem
Rahmenbedingungen
Stakeholder
Optionen
Entscheidung
Umsetzungsplan
offene Fragen
nächster Schritt
```
In allen Fällen gilt:
KI produziert nicht einfach nur Output.
Sie arbeitet innerhalb eines Rahmens.
Wenn dieser Rahmen unsichtbar bleibt, wirkt KI wie Magie. Wenn er sichtbar wird, wird KI zu Handwerk.
---
Ich glaube, viele Diskussionen bleiben an einer Stelle hängen.
Ja, LLMs erzeugen Antworten auf Basis statistischer Muster.
Aber daraus folgt nicht, dass moderne KI-Systeme nur Zufallsantworten ausspucken.
Ein einzelnes Modell berechnet Wahrscheinlichkeiten. Ein agentisches System baut darum herum aber eine Arbeitsumgebung:
```text
Kontextauswahl
Tool-Zugriff
Planung
Zwischenergebnisse
Validierung
Freigaben
Speicher
Protokolle
Wiederholbarkeit
```
Das Modell bleibt probabilistisch. Der Arbeitsraum versucht, diese Probabilistik zu rahmen.
Oder anders gesagt:
Das ist der eigentliche Stand der Technik.
Nicht: Die KI denkt wie ein Mensch. Nicht: Die KI ist nur Autocomplete. Sondern: KI wird zunehmend in Systeme eingebettet, die Arbeitsschritte organisieren, Kontext kuratieren, Werkzeuge nutzen und Ergebnisse überprüfbarer machen.
---
Vibe Coding ist verführerisch.
Man beschreibt grob, was man möchte. Die KI liefert Code. Man klickt, testet, korrigiert, macht weiter.
Das fühlt sich schnell an. Und oft funktioniert es erstaunlich gut.
Bis es das nicht mehr tut.
Das Problem ist selten der eine große Fehler.
Das Problem sind viele kleine Verschiebungen:
```text
eine unbemerkte Annahme
ein vergessener Constraint
eine Änderung außerhalb des Scopes
ein fehlender Fehlerfall
eine neue Abhängigkeit
eine Designentscheidung, die nie entschieden wurde
ein Ergebnis, das gut aussieht, aber am Ziel vorbeigeht
```
Genau hier braucht Vibe Coding einen Arbeitsraum.
Nicht, um die Leichtigkeit zu zerstören. Sondern, um sie nutzbar zu machen.
Ein guter Arbeitsraum sagt nicht:
Er sagt:
Das ist der Unterschied zwischen Chaos und Handwerk.
---
Ich glaube nicht, dass jede:r ein Konzernsystem braucht.
Nicht alle brauchen Multi-Agent-Orchestrierung, Vektor-Datenbanken, automatische Tool-Ausführung, eigene Sandboxes, Rechteverwaltung, Team-Kollaboration und Agent-Telemetrie.
Für viele würde schon eine kleine lokale Werkbank reichen.
Eine Werkbank, die sichtbar macht:
```text
Was wollte ich?
Was habe ich der KI gegeben?
Welche Annahmen standen im Raum?
Welcher Plan wurde freigegeben?
Welches Ergebnis kam zurück?
Was wurde geprüft?
Was habe ich daraus gelernt?
```
Das wäre keine Konkurrenz zu großen Coding-Assistenten.
Es wäre eher das, was in einer Werkstatt auf der Arbeitsplatte liegt:
```text
Skizze
Notizbuch
Messwerkzeug
Checkliste
Werkstück
Prüfprotokoll
Lernzettel
```
Keine Magie. Keine Plattform-Romantik. Keine Blackbox.
Nur ehrliche Handwerksarbeit.
---
Ein minimaler KI-Arbeitsraum könnte aus diesen Stationen bestehen:
```text
1. Rohidee
2. Nordstern
3. Kontext
4. Leitplanken
5. Definition of Done
6. Annahmen
7. Plan
8. GO
9. Promptpaket
10. Ergebnis
11. Review
12. Entscheidung
13. Learning
```
Das klingt schlicht.
Aber genau darin liegt die Kraft.
Der Arbeitsraum zwingt nicht zur Bürokratie. Er zwingt zur Sichtbarkeit.
Er fragt:
```text
Was ist das Ziel?
Was darf nicht passieren?
Was nimmt die KI gerade an?
Was ist der nächste Schritt?
Wer hat ihn freigegeben?
Was kam heraus?
Was lernen wir daraus?
```
Das ist nicht nur für Entwickler:innen relevant.
Das ist relevant für alle, die KI nicht nur als Antwortmaschine nutzen wollen, sondern als Arbeitsmittel.
---
Vielleicht ist die wichtigste Erkenntnis diese:
Wir müssen aufhören, nur über Prompts zu sprechen.
Prompts sind wichtig. Aber Prompts sind nicht der ganze Prozess.
Der Prompt ist der Auftrag am Anfang. Der Arbeitsraum ist das System, das daraus kontrollierte Arbeit macht.
Die Zukunft der KI-Arbeit wird deshalb nicht nur davon abhängen, welches Modell besser ist.
Sondern auch davon, welche Arbeitsräume wir darum herum bauen:
```text
sichtbar oder versteckt
kontrolliert oder blind
lokal oder vollständig ausgelagert
nachvollziehbar oder flüchtig
menschgeführt oder automatisiert um jeden Preis
```
Genau dort liegt die eigentliche Gestaltungsfrage.
Nicht:
Sondern:
---
Die alte Beschreibung „Ein LLM berechnet das statistisch wahrscheinlichste nächste Wort“ ist nicht falsch.
Aber sie erklärt nicht mehr ausreichend, wie moderne KI-Arbeit tatsächlich aussieht.
Denn zwischen Prompt und Ergebnis liegt inzwischen ein ganzer Arbeitsraum:
```text
Kontext
Planung
Tools
Annahmen
Freigaben
Reviews
Protokolle
Lernschleifen
```
Wer nur auf die Antwort schaut, sieht das Ergebnis.
Wer auf den Arbeitsraum schaut, sieht die Arbeit.
Und genau dort wird KI interessant.
Nicht als Magie. Nicht als Ersatz für Denken. Nicht als Autopilot ohne Verantwortung.
Sondern als Werkzeug, das umso besser wird, je sichtbarer, klarer und kontrollierbarer der Raum ist, in dem wir mit ihm arbeiten.
Oder kurz:

---
Lesezeichen zu diesem Post:
- OpenAI Agents SDK – Tools [https://openai.github.io/openai-agents-python/tools/ ](https://openai.github.io/openai-agents-python/tools/)
- Claude Code Docs – Agent SDK Overview [https://code.claude.com/docs/en/agent-sdk/overview ](https://code.claude.com/docs/en/agent-sdk/overview)
- Anthropic – Effective context engineering for AI agents [https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Anthropic – Building effective agents [https://www.anthropic.com/engineering/building-effective-agents ](https://www.anthropic.com/engineering/building-effective-agents)
- OpenAI Cookbook – Building Consistent Workflows with Codex CLI & Agents SDK [https://developers.openai.com/cookbook/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk ](https://developers.openai.com/cookbook/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk)


## Über den Autor

Benjamin Lam nutzt einen erstaunlich großen Teil des Internets, um seine Gedanken zu posten. Falls du irgendwo etwas findest, das hier noch nicht archiviert ist: her damit.
