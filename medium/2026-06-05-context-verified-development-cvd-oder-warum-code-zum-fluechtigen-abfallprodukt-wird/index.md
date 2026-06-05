---
title: "Context-Verified Development (CVD) — oder: Warum Code zum flüchtigen Abfallprodukt wird"
slug: "context-verified-development-cvd-oder-warum-code-zum-fluechtigen-abfallprodukt-wird"
source: "Medium"
source_slug: "medium"
source_url: "https://medium.com/@benjaminlam_46803/context-verified-development-cvd-oder-warum-code-zum-fl%C3%BCchtigen-abfallprodukt-wird-4053765301b3"
first_published: "2026-06-05"
archived_at: "2026-06-05"
status: "aktuell"
tags:
  - "Contextverifieddev"
  - "Cvd"
  - "Context"
  - "Development"
  - "Verified"
canonical_url: "https://benjamin-lam.github.io/medium/2026-06-05-context-verified-development-cvd-oder-warum-code-zum-fluechtigen-abfallprodukt-wird/"
description: "Archivierte Veröffentlichung von Benjamin Lam. Erstveröffentlicht am 05.06.2026 auf Medium."
---

# Context-Verified Development (CVD) — oder: Warum Code zum flüchtigen Abfallprodukt wird

## Hinweis zur Erstveröffentlichung

Dieser Artikel erschien zuerst am 05.06.2026 auf Medium.

Original: https://medium.com/@benjaminlam_46803/context-verified-development-cvd-oder-warum-code-zum-fl%C3%BCchtigen-abfallprodukt-wird-4053765301b3

## Artikel

Das macht keinen Sinn. Es gibt eine Person, von der ich weiß, dass sie innerlich zuckt, wenn das Wort „macht“ im Kontext mit Sinn auftaucht. Und das war irgendwie ansteckend, aber mein Kopf hat sich damit arrangiert — das ist in der heutigen Alltagssprache völlig in Ordnung.

Ein schlechter Herrenwitz ist ein schlechter Herrenwitz. Trotzdem wird in manchen Runden gelacht. Er wird geduldet. Er wird ertragen.
Die wohl bekannteste verfilmte Liebesgeschichte funktioniert nur deshalb, weil Konventionen gebrochen wurden und ein Passagier der dritten Klasse plötzlich Platz in der Upper Class nimmt.

Ein normaler Tag ist voller Regelbrüche, Ausnahmen und Abkürzungen. Diese Unschärfe, diese Abweichungen vom Eigentlichen begleiten uns durch den Tag.
Sie beginnen damit, dass ein Daily plötzlich eine Überraschung bereithält. Eine unerwartete Nachricht. Ein Geburtstag — was zugegeben ebenfalls überraschend sein kann. Und endet bei manchen mit dem Zugeständnis: „Okay, aber nur eine halbe Stunde länger. Dann geht’s ins Bett.“

Manch einer hat jetzt vielleicht den Ausspruch von Marc Terenzi im Ohr: „The Regels sind the Regels und wir müssen them einhalten!“ Aber genau das sind die Regeln.
„Die Ausnahme bestätigt die Regel.“ Der Kontext schlägt die Vorschrift.

Und das ist die Welt, in der wir leben. Die Welt, in der wir arbeiten.

Vielleicht ist es genau diese Alltags-Unschärfe, die uns zeigt, wie schwer es ist, im Kontext zu bleiben — und warum wir in der Softwareentwicklung so dringend neue Modelle brauchen.
Wie komme ich jetzt darauf? Ähm … ja. Wieder dieses KI-Thema. Eines dieser nebenläufigen Gespräche, im Rahmen von „Und? Was hast du letzte Woche mit KI gemacht?“ oder die Frage: Wo stehen wir, wo geht die Reise hin?

Ein Satz, der in der letzten Zeit, zumindest in meiner Bubble, immer häufiger fällt, ist: „Wir löschen einfach den Code und lassen die KI ihn neu schreiben.“ Klingt nach Science-Fiction? Ja, irgendwie schon, aber ist die Realität von Context-Verified Development (CVD) — zumindest theoretisch.
In den letzten Monaten haben wir den Hype um Vibe Coding erlebt. Ich habe mich intensiv mit Prompt Driven Development (PDD) beschäftigt und habe mir sogar ein eigenes Manifest dazu geschrieben: Prompt Driven Development (PDD) — Ein Manifest gegen das bequeme Raten. Ziemlich holprig, aber wer es noch einmal nachlesen will: https://benjamin-lam.de/2026/01/13/prompt-driven-development-pdd/

Wir haben gelernt, strukturierte Prompts zu schreiben.
Aber Hand aufs Herz: Wer von uns hat noch nicht erlebt, dass eine KI bei einer großen Codebase plötzlich essentielle Architekturregeln vergisst und subtilen Legacy-Code produziert? Reines Prompting läuft in eine Sackgasse. Es schützt uns nicht vor dem schleichenden Kontrollverlust.
Eine mögliche Lösung, die immer wieder in Fachgesprächen auftaucht, heißt: Context-Verified Development (CVD). Und es wirkt wie der fundamentale Shift: Weg von: „Ich schreibe einen präzisen Text-Prompt, um Code zu generieren.“ Hin zu: „Ich definiere ein unerbittliches Kontext-Modell, gegen das KI-Agenten jede Änderung vollautomatisch verifizieren müssen.“
Der Gedanke bei CVD: Code wird zum flüchtigen Abfallprodukt. Wenn der Kontext (Architektur, Security, Business-Logik) absolut wasserdicht und maschinenlesbar dokumentiert ist, kann die KI den Code jederzeit komplett verwerfen und fehlerfrei neu aufbauen.
Klingt gut, aber hier stehen wir vor der ersten Hürde: „absolut wasserdicht und maschinenlesbar dokumentiert“. Ich bin jetzt schon etwas länger im Geschäft — manch eine Leser:in war vielleicht noch nicht geboren, als ich meine ersten Gehversuche mit Computern gemacht habe.
Commodore Plus 4, Basic — damals war ziemlich schnell Schluss mit Basic abtippen, weil ich versucht habe, mir ein Notebook zu bauen, in dem ich das Kabel abgeschnitten habe und versucht habe, die losen Enden mit einer Batterie zu verbinden. (Ich war 8.)
Ups, kleiner Drift. Wo war ich noch gleich? Ach ja: Context-Verified Development (CVD). „Wir löschen einfach den Code und lassen die KI ihn neu schreiben.“

Vielleicht ist dieser kleine gedankliche Ausflug selbst schon ein Beispiel dafür, wie schnell man den Kontext verliert — und warum wir ihn in der Softwareentwicklung explizit machen müssen.
Nein, die erste Hürde: „absolut wasserdicht und maschinenlesbar dokumentiert“. Wer das Geschäft kennt, schmunzelt jetzt vielleicht, liegt lachend auf dem Boden oder schaut verschämt auf den Boden. Dokumentation? „Pah!“

Aber was, wenn Architekturentscheidungen, Sicherheitsregeln, Domänenwissen, Business-Ziele und technische Randbedingungen so präzise dokumentiert sind, dass KI-Agenten ihre Arbeit permanent dagegen prüfen können?
Weg von: „Ich schreibe einen möglichst präzisen Prompt, damit die KI den richtigen Code erzeugt.“ Hin zu: „Ich definiere einen überprüfbaren Kontext, innerhalb dessen die KI arbeiten darf.“

Wenn es einen Startpunkt gibt, dann diesen: „absolut wasserdicht und maschinenlesbar dokumentiert“. Nicht als Ideal, sondern als notwendige Voraussetzung.
In dieser Welt wird Code fast zu einem flüchtigen Artefakt. Die wertvolle Ressource ist nicht mehr die Implementierung selbst, sondern das Wissen darüber, warum das System genau so gebaut wurde.

Ob wir diesen Punkt tatsächlich erreichen, weiß ich nicht. Aber ich habe das Gefühl, dass genau dort die nächste große Diskussion beginnt.

Vielleicht verschiebt sich die Rolle von Entwickler:innen langfristig ein Stück weit:

- Weniger Syntax.
- Mehr Architektur.
- Weniger Implementierungsdetails.
- Mehr Kontextmodellierung.
- Weniger „Wie schreibe ich den Code?“
- Mehr „Wie beschreibe ich das System so präzise, dass Mensch und Maschine dieselbe Realität verstehen?“

Denn genau das haben wir in der Softwareentwicklung schon immer getan — meist ohne es ausdrücklich zu benennen. Das ist unser Arbeitsraum. Unsere Realität.
Wir modellieren Geschäftsprozesse. Wir dokumentieren Entscheidungen. Wir definieren Regeln, Randbedingungen und Erwartungen. Wir versuchen, ein gemeinsames Verständnis davon zu schaffen, wie die Welt aussieht und wie sich ein System darin verhalten soll.

Nicht der Algorithmus steht dabei im Mittelpunkt. Nicht das Framework. Nicht die Programmiersprache. Sondern die Lösung eines Problems in einem ganz bestimmten Kontext.
Software war schon immer der Versuch, Komplexität auf ein für Menschen beherrschbares Maß zu reduzieren.

Vielleicht verändert KI deshalb weniger die eigentliche Aufgabe von Entwickler:innen, als wir glauben. Vielleicht zwingt sie uns lediglich dazu, etwas explizit zu machen, das bisher oft implizit in Meetings, Dokumentationen, Architekturen und den Köpfen der Beteiligten gelebt hat:
Kontext. Den gemeinsamen Bezugsrahmen, der dafür sorgt, dass Menschen und Maschinen nicht nur dieselben Worte verwenden, sondern tatsächlich dieselbe Realität beschreiben.

Der Gedanke wirkt kühn — und genau deshalb lohnt es sich, ihn weiterzudenken.

we’re not behaving like insects

Benjamin Lam (blame76)

## Über den Autor

Benjamin Lam nutzt einen erstaunlich großen Teil des Internets, um seine Gedanken zu posten. Falls du irgendwo etwas findest, das hier noch nicht archiviert ist: her damit.
