## Requirements
- pandas
- numpy
- matplotlip

## Befehle um Virtual Environment zu erstellen
### Windows:
- `.\.venv\Scripts\activate`
### Linux: 
- `sudo apt-get install python3-pip` (wenn noch nicht installiert)
- `sudo pip3 install virtualenv` (wenn noch nicht installiert)
- `virtualenv [Name des venv Ordners]` (Wenn das nicht funktioniert auf lokalen Ordner probieren auf dem man sicher alle Rechte hat und dann den ganzen Ordner kopieren)

## Befehle um Virtual Environment zu aktivieren
### Windows:
- `.\.venv\Scripts\activate`
### Linux:
- `source [Name des venv Ordners]/bin/activate`

### Um für Windows alles installieren zu können:
- Powershell als Admin ausführen
- Get-ExecutionPolicy -Lis    
- ausführen um zu sehen was erlaubt ist
- Set-ExecutionPolicy Unrestricted -Scope CurrentUser
- Erlaubt alles zu installieren
