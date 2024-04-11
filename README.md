## Requirements
- pandas
- numpy
- matplotlip

## Befehle um Virtual Environment zu erstellen
### Windows:
- `python -m venv [Name des venv Ordners]`
### Linux: 
- `virtualenv [Name des venv Ordners]`
    - wenn virtualenv noch nicht installiert ist
        - `sudo apt-get install python3-pip`
        - `sudo pip3 install virtualenv`
    - Wenn das nicht funktioniert auf lokalen Ordner probieren auf dem man sicher alle Rechte hat und dann den ganzen Ordner kopieren
    
## Befehle um Virtual Environment zu aktivieren
### Windows:
- `.\[Name des venv Ordners]\Scripts\activate`
    - wenn es sich nicht aktivieren lässt
        - Powershell als Admin ausführen
        - ausführen um zu sehen was erlaubt ist `Get-ExecutionPolicy -Lis`    
        - Erlaubt alles zu installieren `Set-ExecutionPolicy Unrestricted -Scope CurrentUser`
### Linux:
- `source [Name des venv Ordners]/bin/activate`

