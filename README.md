# Einführung Logging: Einfache Anwendung erstellen, die Logausgaben liefert

## Abgabetermin
10. März, 23:59

## Aufgabenstellung
Bitte erstelle eine HTTP API, entweder mit Node (express/nestjs) oder Python (fastapi), die folgende Routen bereitstellt:

- (GET) /info
- (GET) /debug
- (GET) /error
- (GET) /fatal

Definiere eine ENV Variable für LOG_LEVEL, die folgende Werte enthalten kann:
- INFO
- DEBUG
- ERROR
- FATAL

Implementiere in den Routen jeweils eine Funktion, die entsprechend des gesetzten Loglevels eine Logmeldung ausgibt. Wenn der Loglevel auf INFO gesetzt ist, dann soll die (GET) /info Route eine Info-Logmessage ausgeben.

Beispiele:
- 2024-03-08T11:10:35.689Z info: This is an info message
- 2024-03-08T11:10:35.687Z error: This is an error message 
- 2024-03-08T11:10:35.688Z debug: This is a debug message 
- 2024-03-08T11:10:35.688Z fatal: This is a fatal message

## Abgabe
Die fertige Anwendung bitte in ein GIT Repo pushen und den Link zum eurem Repo hier abgeben.

## Config
./setup.sh

## Execute
./exe.sh