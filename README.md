# Molekulare Daten von Bakterien in einem Knowledge Graph

Dieses Projekt zielt darauf ab, molekulare Daten von Bakterien aus der Datenbank *Regulon DB* zu sammeln und in einen Knowledge Graph zu überführen. Dabei wurden mehrere Schritte durchlaufen, um die Daten zu extrahieren und zu strukturieren.

## Inhalt

1. [Einführung](#einführung)
2. [Zielsetzung](#zielsetzung)
3. [Schritte zur Datenbeschaffung](#schritte-zur-datenbeschaffung)
   - [Schritt 1: Sammlung der Regulon-Namen und Links von RegulonDB](#schritt-1-sammlung-der-regulon-namen-und-links-von-regulondb)
   - [Schritt 2: Sammlung Daten zu Regulons (GraphQL API von RegulonDB)](#schritt-2-sammlung-daten-zu-regulons-graphql-api-von-regulondb)
4. [Daten Preparen & Hochladen (PyWikiBot)](#daten-preparen--hochladen-pywikibot)

## Einführung

In diesem Projekt wurden molekulare Daten von Bakterien aus *Regulon DB* in einen Knowledge Graph überführt, um komplexe biologische Informationen zu vernetzen und zugänglich zu machen.

## Zielsetzung

Das Hauptziel war es, verschiedene Daten zu Regulons, die eine Gruppe von gemeinsam regulierten Genen repräsentieren, in einen Knowledge Graph zu integrieren. Diverse Daten von Regulons wurden aus der Datenbank Regulon DB extrahiert und in einen Knowledge Graph anhand von WikiData überführt.
Diese Strukturierung hilft bei der Analyse und dem Verständnis biologischer Systeme.

## Schritte zur Datenbeschaffung
Alle Schritte können nochmal explizit und in Detail aus Instructions_Regulon_KG.pdf entnommen werden.

### Schritt 1: Sammlung der Regulon-Namen und Links von RegulonDB 

Im ersten Schritt wurden die Namen der Regulons sowie die entsprechenden Links zu ihren Einträgen in *Regulon DB* gesammelt. Diese Informationen wurden in einem Dictionary gespeichert, wobei die Regulon-Namen als Schlüssel und die Links als Werte dienten.

Um die Regulon-Namen und Links zu sammeln, wurde ein Webscraping-Skript mit Selenium implementiert. Das Skript navigierte durch die Webseite und extrahierte die benötigten Informationen, um sie in einer strukturierten Form zu speichern.

Siehe Datei - 1.Webscrape_Regulon_links.ipynb

### Schritt 2: Sammlung Daten zu Regulongs (GraphQL API von RegulonDB) 

Nach der Sammlung der Basisinformationen bestand der nächste Schritt darin, detailliertere Daten zu extrahieren, wie z.B.:
- **Regulatorisches Triplett und Wirkung:** Informationen darüber, ob ein Regulator als Repressor, Aktivator oder beides wirkt.
- **Genomische Positionen:** Start- und Endpositionen bestimmter DNA-Abschnitte.

Eine direkte CSV-Exportoption war nicht verfügbar, und ein vollständiges Webscraping wurde vermieden, um den Datenverkehr zu schonen.

##### Nutzung der GraphQL API

Bei der Inspektion der Webseite wurde festgestellt, dass die Daten über eine GraphQL API geladen werden. Durch die Analyse des Netzwerkverkehrs konnten spezifische API-Endpunkte und Anfragen identifiziert werden. Diese API wurde dann verwendet, um gezielt Daten mit eine Python Skript abzufragen.

Siehe Datei - 2.get_regulon_data_graphql.ipynb

## Daten Preparen & Hochladen (PyWikiBot)

### Schritt 3: Formatierung der Daten für Wikidata

- **Wikidata-Muster:**
Wikidata nutzt eine strukturierte Form von Daten, die als Tripel (Subjekt, Prädikat, Objekt) organisiert sind. Diese Tripel repräsentieren einfache Aussagen und bilden die Grundlage für den Knowledge Graph.

- **Datenstrukturierung:**  
  Wir haben die Daten aus der RegulonDB gemäß diesem Muster neu strukturiert. Der Vorteil dieser Strukturierung ist, dass sie sowohl maschinenlesbar als auch für menschliche Benutzer nachvollziehbar ist.

- **Vorgehensweise:**  
  - **Subjekt:** Regulon-Namen (z.B. DicF, DsrA)  
  - **Prädikat:** Beziehungen oder Eigenschaften (z.B. reguliert, interagiert mit)  
  - **Objekt:** Zielgene oder -elemente (z.B. Zielgene wie "GcvB" oder "McaS")  


### Schritt 4: Daten auf WikiData hochladen - PyWikiBot

Die Daten wurden mit dem PyWikiBot auf WikiData hochgeladen.
Siehe Dokumentation zu dem Package hier:  https://pypi.org/project/pywikibot/

