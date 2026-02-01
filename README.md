# Forschungsdesign-Bewertungstool-oTree-App-
Diese oTree-Applikation ermöglicht es, verschiedene Forschungsdesigns (als PDF) zufällig und anonymisiert zu bewerten. Die Ergebnisse werden anschließend als CSV exportiert und dienen als Grundlage für unsere weitere Analyse und Entwicklung des KI-gestützten RAG-Systems.

## 🔧 Funktionalität der Anwendung

- Die App lädt automatisch alle .pdf-Dateien aus dem Ordner designs/.
- Jede Datei enthält ein Forschungsdesign.
- Pro Datei wird eine Bewertungsrunde erzeugt.
- Die Reihenfolge der Designs wird für jede Sitzung zufällig gemischt.
- Für jedes Design werden folgende Daten gespeichert:
   - experiment_title (aus dem Dateinamen)
   - rating (Skala 1–5)
   - comment (optional)

## 📁 Vorbereitung: Designs hochladen
- Laden Sie im Ordner research_design_rater/static/research_design_rater/designs für jedes Design eine pdf-Datei hoch.
- Der Dateiname muss eine Zahl sein. Die Zahl ist die design id (experiment_title), die später in der Auswertung zugeordnet wird.
- Dateien werden automatisch sortiert und eingelesen.

## ▶️ Ablauf einer Bewertungssitzung

- Session-Link öffnen (wird vom Studierendenteam bereitgestellt)
- Die App zeigt ein kurzes Intro
- Jedes Design wird einzeln angezeigt
  - bitte Bewertung 1–5 abgeben
  - optional einen Kommentar eintragen
- Am Ende erscheint eine Danke-Seite

_*Eine Sitzung umfasst automatisch alle Designs, in zufälliger Reihenfolge._

## 📥 Export der Daten (CSV)

Nach Abschluss Ihrer eigenen Sitzung:
- Im Session-Link auf "Data" (oder „Daten“) gehen
- Rechts unten auf "Download CSV" klicken
- Die Datei wird als "all_apps_wide-YYYY-MM-DD.csv" heruntergeladen.

*Bitte diese CSV im MS Teams-Chat an uns senden*

## ⚙️ Metadaten generieren

Nach dem Export der oTree-Daten können aus der CSV-Datei automatisch strukturierte Metadaten für jedes Forschungsdesign erzeugt werden.

### Voraussetzungen
- Python 3.9 oder neuer  
- Installierte Python-Pakete (u. a. `pandas`, `PyPDF2`)
- Die exportierte oTree-CSV liegt im **Projekt-Root-Verzeichnis**
- Die PDF-Dateien befinden sich in folgenden Ordnern (je nach Sprache):
  - `research_design_rater/static/research_design_rater/designs/pdf_de/`
  - `research_design_rater/static/research_design_rater/designs/pdf_en/`

### Schritte

1. CSV-Datei in das Projektverzeichnis legen mit den Namen oTree_export.csv  

2. In den `scripts`-Ordner wechseln:
   ```bash
   cd scripts
   
3. Metadaten-Skript ausführen:
   ```bash
   python generate_metadata.py
   
4. Ergebnisse prüfen:
   
   Das Skript erzeugt für jedes Forschungsdesign eine .md-Datei mit Metadaten, darunter:

- durchschnittliche Bewertung
- Anzahl der Bewertungen
- Sprache (Deutsch oder Englisch, basierend auf der Ordnerstruktur)
- Seitenanzahl des PDFs

## 🙏 Vielen Dank!

Falls Fragen entstehen oder das Tool nicht wie erwartet funktioniert, bitte einfach im Teams-Chat melden.
