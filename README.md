# hbfm-onix-file-downloader

*Skript, das aus einer Onix Datei alle Coverbilder lokalisiert, diese runterlädt und ablegt. Die Bilder werden im **cover** Unterordner mit dem Namen **\<\<ISBN>>.png** abgelegt.*

## Conda Umgebung:

[Conda Dokumentation hier](https://docs.anaconda.com/anaconda-cloud/user-guide)

This file may be used to create an environment using:

`$ conda create --name env --file onix-png-download.txt`

platform: win-64

## Usage:
`conda activate env`
`python onix-png-download.py <<NAME-ESV-DATEI>>.xml`

Falls es zu Fehlern bei der Verbindung kommt, muss der Proxy in der Konsole gesetzt werden:

`set http_proxy=proxy.vhb.de:80`
`set https_proxy=proxy.vhb.de:80`

Dauerhaft Umgebungsvariablen in Windows speichern:
`setx http_proxy proxy.vhb.de:80`
`setx https_proxy proxy.vhb.de:80`
