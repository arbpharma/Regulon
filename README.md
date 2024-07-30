# Molekulare Daten von Bakterien in einem Knowledge Graph

Dieses Projekt zielt darauf ab, molekulare Daten von Bakterien aus der Datenbank *Regulon DB* zu sammeln und in einen Knowledge Graph zu überführen. Dabei wurden mehrere Schritte durchlaufen, um die Daten zu extrahieren und zu strukturieren.

## Inhalt

1. [Einführung](#einführung)
2. [Zielsetzung](#zielsetzung)
3. [Schritte zur Datenbeschaffung](#schritte-zur-datenbeschaffung)
   - [Schritt 1: Sammlung der Regulon-Namen und Links](#schritt-1-sammlung-der-regulon-namen-und-links)
   - [Schritt 2: Sammlung detaillierter Daten & Nutzung der GraphQL API](#schritt-2-sammlung-detaillierter-daten--nutzung-der-graphql-api)
4. [Zusammenfassung und Ausblick](#zusammenfassung-und-ausblick)

## Einführung

In diesem Projekt wurden molekulare Daten von Bakterien aus *Regulon DB* in einen Knowledge Graph überführt, um komplexe biologische Informationen zu vernetzen und zugänglich zu machen.

## Zielsetzung

Das Hauptziel war es, verschiedene Daten zu Regulons, die eine Gruppe von gemeinsam regulierten Genen repräsentieren, in einen Knowledge Graph zu integrieren. Diverse Daten von Regulons wurden aus der Datenbank Regulon DB extrahiert und in einen Knowledge Graph anhand von WikiData überführt.
Diese Strukturierung hilft bei der Analyse und dem Verständnis biologischer Systeme.

## Schritte zur Datenbeschaffung
Alle Schritte können nochmal explizit und in Detail aus Instructions_Regulon_KG.pdf entnommen werden.

### Schritt 1: Sammlung der Regulon-Namen und Links von RegulonDB - 1.Webscrape_Regulon_links.ipynb

Im ersten Schritt wurden die Namen der Regulons sowie die entsprechenden Links zu ihren Einträgen in *Regulon DB* gesammelt. Diese Informationen wurden in einem Dictionary gespeichert, wobei die Regulon-Namen als Schlüssel und die Links als Werte dienten.

Um die Regulon-Namen und Links zu sammeln, wurde ein Webscraping-Skript mit Selenium implementiert. Das Skript navigierte durch die Webseite und extrahierte die benötigten Informationen, um sie in einer strukturierten Form zu speichern.

### Schritt 2: Sammlung Daten zu Regulongs (GraphQL API von RegulonDB) - 2.get_regulon_data_graphql.ipynb

Nach der Sammlung der Basisinformationen bestand der nächste Schritt darin, detailliertere Daten zu extrahieren, wie z.B.:
- **Regulatorisches Triplett und Wirkung:** Informationen darüber, ob ein Regulator als Repressor, Aktivator oder beides wirkt.
- **Genomische Positionen:** Start- und Endpositionen bestimmter DNA-Abschnitte.

Eine direkte CSV-Exportoption war nicht verfügbar, und ein vollständiges Webscraping wurde vermieden, um den Datenverkehr zu schonen.

##### Nutzung der GraphQL API

Bei der Inspektion der Webseite wurde festgestellt, dass die Daten über eine GraphQL API geladen werden. Durch die Analyse des Netzwerkverkehrs konnten spezifische API-Endpunkte und Anfragen identifiziert werden. Diese API wurde dann verwendet, um gezielt Daten mit eine Python Skript abzufragen.

## Daten Preparen & Hochladen (PyWikiBot)
### Schritt 3 & 4: Daten in Form bringen und hochladen - PyWikiBot



