import os
import re

# Pfad zur TeamViewer-Logdatei
log_file_path = "C:\\TeamViewer\\Logfiles\\TeamViewer15_Logfile.log"

# Regex-Muster zum Extrahieren von Verbindungsinformationen
connection_pattern = re.compile(r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}) (?P<event_type>\w+) (?P<session_id>\d+) (?P<partner_id>\d+) (?P<duration>\d+) (?P<username>.+) (?P<ip_address>.+):(?P<port>\d+)$")

# Liste zum Speichern der Verbindungsinformationen
connections = []

# Logdatei öffnen und lesen
with open(log_file_path, "r") as log_file:
    for line in log_file:
        # Verbindungsinformationen extrahieren
        match = connection_pattern.match(line)
        if match:
            connection_info = {
                "timestamp": match.group("timestamp"),
                "event_type": match.group("event_type"),
                "session_id": match.group("session_id"),
                "partner_id": match.group("partner_id"),
                "duration": match.group("duration"),
                "username": match.group("username"),
                "ip_address": match.group("ip_address"),
                "port": match.group("port"),
            }
            connections.append(connection_info)

# Auswertung der Verbindungsinformationen
for connection in connections:
    # Ausgabe der Verbindungsinformationen
    print(f"Verbindungszeitpunkt: {connection['timestamp']}")
    print(f"Ereignistyp: {connection['event_type']}")
    print(f"Sitzungs-ID: {connection['session_id']}")
    print(f"Partner-ID: {connection['partner_id']}")
    print(f"Dauer: {connection['duration']} Sekunden")
    print(f"Benutzername: {connection['username']}")
    print(f"IP-Adresse: {connection['ip_address']}")
    print(f"Port: {connection['port']}")
    print("")

# Zusätzliche Auswertungsmöglichkeiten:

# Filtern der Verbindungen nach bestimmten Kriterien (z. B. Ereignistyp, Partner-ID, IP-Adresse)
# Gruppieren der Verbindungen nach bestimmten Kriterien (z. B. Datum, Uhrzeit, Benutzername)
# Berechnen von Statistiken (z. B. Anzahl der Verbindungen, durchschnittliche Dauer der Verbindungen)

