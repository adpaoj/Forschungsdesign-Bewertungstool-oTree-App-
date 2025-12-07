# Forschungsdesign-Bewertungstool-oTree-App-
Diese oTree-Applikation ermöglicht es, verschiedene Forschungsdesigns (als Textdateien) zufällig und anonymisiert zu bewerten. Die Ergebnisse werden anschließend als CSV exportiert und dienen als Grundlage für unsere weitere Analyse und Entwicklung des KI-gestützten RAG-Systems.

## 🔧 Funktionalität der Anwendung

- Die App lädt automatisch alle .txt-Dateien aus dem Ordner designs/.
- Jede Datei enthält ein Forschungsdesign.
- Pro Datei wird eine Bewertungsrunde erzeugt.
- Die Reihenfolge der Designs wird für jede Sitzung zufällig gemischt.
- Für jedes Design werden folgende Daten gespeichert:
   - design_id (aus dem Dateinamen)
   - design_text (vollständiger Inhalt der .txt-Datei)
   - rating (Skala 1–7)
   - comment (optional)

## 📁 Vorbereitung: Designs hochladen
- Laden Sie im Ordner „designs“ für jedes Design eine TXT-Datei hoch.
- Der Dateiname muss eine Zahl sein. Die Zahl ist die design_id, die später in der Auswertung zugeordnet wird.
- Dateien werden automatisch sortiert und eingelesen.

## ▶️ Ablauf einer Bewertungssitzung

- Session-Link öffnen (wird vom Studierendenteam bereitgestellt)
- Die App zeigt ein kurzes Intro
- Jedes Design wird einzeln angezeigt
  - bitte Bewertung 1–7 abgeben
  - optional einen Kommentar eintragen
- Am Ende erscheint eine Danke-Seite

_*Eine Sitzung umfasst automatisch alle Designs, in zufälliger Reihenfolge._

## 📥 Export der Daten (CSV)

Nach Abschluss Ihrer eigenen Sitzung:
- Im Session-Link auf "Data" (oder „Daten“) gehen
- Rechts unten auf "Download CSV" klicken
- Die Datei wird als "all_apps_wide-YYYY-MM-DD.csv" heruntergeladen.

*Bitte diese CSV im MS Teams-Chat an uns senden*

## 🙏 Vielen Dank!

Falls Fragen entstehen oder das Tool nicht wie erwartet funktioniert, bitte einfach im Teams-Chat melden.
