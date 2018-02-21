# von Stefan Maibücher, Handelsblatt Fachmedien
# Skript, das aus einer Onix Datei alle Coverbilder lokalisiert, diese runterlädt und ablegt.
# Die Bilder werden im cover Unterordner mit dem Namen <<ISBN>>.png abgelegt


'''
USAGE: python onix-png-download.py <<NAME-ESV-DATEI>>.xml

Falls es zu Fehlern bei der Verbindung kommt, muss der Proxy in der Konsole gesetzt werden:

set http_proxy=proxy.vhb.de:80
set https_proxy=proxy.vhb.de:80

'''

import os
import sys
from builtins import len
from lxml import etree
import requests


# Das Skript erwartet als Kommandozeilenparamter die ESV XML Datei
filename = sys.argv[1]

print(filename)

esv_doc = etree.parse(filename)

namespaces={'ns': 'http://www.editeur.org/onix/2.1/short'}

# XPATH Ausdruck, der alle PNG Bilder lokalisiert:
products_images = esv_doc.xpath('/*/ns:product/ns:mediafile/ns:f117/text()', namespaces=namespaces)

#print(products_images, len(products_images)) # zum Testen

# Verzeichnis für Bilder erstellen, falls nicht vorhanden:
directory = 'cover'
if not os.path.exists(directory):
    os.makedirs(directory)

for pi in products_images:
    # Die ISBN Nummer ist immer an derselben Stelle in der URL zu finden:
    image_name= 'cover/'+pi.split("/")[-3]+".png"
    r = requests.get(pi, stream=True)
    with open(image_name, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)
    print("Datei: " + image_name + " geschrieben.")

print("Alle Bilder runtergeladen und abgelegt.")


