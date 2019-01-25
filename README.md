# musik
## Instalation:
### Option 1 ausfuehrbare datei herunterladen:
#### Windows:
- downloaden sie die datei ***windows/musik-{version}.exe***
- fuehren sie diese datei aus
#### Linux:
- downloaden sie die datei ***linux/musik-{version}***
- fuehren sie diese datei aus
### Option 2 compilieren:
- installieren sie [Python 3](https://www.python.org/ )

- oefnen sie eine Komandozentrale
- geben sie ein (benoetigt einen root zugang): 
```bash
pip3 install pyinstaller
```
- downloaden sie den ordner ***source/***
- extrahieren sie die gedownloadete **zip datei**
- gehen sie in den Ordner wo sie die Datei extrahiert haben das machen sie mit   ```cd <ordner>```
- jetzt geben sie ein:
```bash
pyinstaller --onefile main.py
cd dist
ls
```
jetzt werden sie eine datei sehen die man ausfuehren kann.

