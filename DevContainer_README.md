# Dev Container Setup Guide

## Einleitung

Dieses Projekt verwendet einen Dev-Container, um eine konsistente Entwicklungsumgebung zu gewährleisten. Diese Anleitung beschreibt, wie das Repository in einem Dev-Container geöffnet und die Anwendung gestartet wird.

## Schritte zur Einrichtung

1. **VS Code und Dev Containers Erweiterung installieren**
   - Stelle sicher, dass du [Visual Studio Code](https://code.visualstudio.com/) und die Erweiterung "Dev Containers" installiert hast.

2. **Repository klonen**
   ```bash
   git clone <repository-url>
   cd my_docker_project
   ```

3. **Dev-Container öffnen**
   - Öffne das Projekt in VS Code.
   - Öffne die Kommando-Palette (F1) und wähle `Remote-Containers: Reopen in Container`.

4. **Anwendung starten**
   - Nach dem Öffnen des Containers in VS Code kannst du die Anwendung starten.
   - Öffne eine neue Terminalinstanz und führe folgenden Befehl aus:
     ```bash
     python src/main.py
     ```

## Debugging

- Du kannst Debugging direkt in VS Code nutzen, indem du `F5` drückst.

## Wichtige Extensions

- **Python**: Unterstützt die Python-Entwicklung mit Features wie IntelliSense, Linting und Debugging.
- **Pylance**: Bietet leistungsstarkes IntelliSense und Typprüfung für Python.
- **Docker**: Ermöglicht die Verwaltung von Docker-Containern und -Images direkt in VS Code.

## Datenbankintegration

- Das Projekt verwendet eine PostgreSQL-Datenbank.
- Der Datenbankinhalt kann über pgAdmin überprüft werden, das unter `http://localhost:8080` erreichbar ist (Standard-Login: admin@admin.com / admin).

## WordPress

- WordPress ist unter `http://localhost:3000` erreichbar.

## Sicheres Handling sensibler Daten

- Verwende die `.env`-Datei, um sensible Daten zu speichern. Diese Datei wird nicht ins Repository eingecheckt.
- Die Struktur der `.env`-Datei ist in der `env-schema.txt`-Datei dokumentiert.
