# musik
## Instalation:
### Option 1 ausfuehrbare datei herunterladen:
#### Windows:
- downloaden sie die datei ***windows/musik-{version}.exe***
- üehren sie diese datei aus und folgen sie den schritten vom Installer.
- öfnen sie nun das programm "Musik".
### Option 2 compilieren:
- installieren sie [Python 3](https://www.python.org/ )

- oefnen sie eine Komandozentrale
- geben sie ein (benötigt einen root zugang): 
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

