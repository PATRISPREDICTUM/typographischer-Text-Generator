# typographischer-Text-Generator
### Sorry für den unsaubern Code! Jedoch ist es nur einen Prototyp...
kleines Python Projekt aus 2019 um 2 Texte zu einem 3d Modell zusammen zu fügen.
Als Output erhält man ein .obj File, welches beide Texte kombiniert

## Installation
### Dependencies
python 3.7

Um die Module zu Installieren:

```
pip install pillow numpy argparse
```


## Usage
### Hilfe anzeigen:
```  
python 223d.py -h

```
### Agrumente

`--Resolution int | default 40` Regelt sie Voxel Auflösung des 3-D Objektes. Je höher die Auflösung, umso länger dauert das Generieren des Objektes

`--Base bool | default FALSE` Generiert eine Plattform unter dem Text

`--TextA | default "ERROR"` Gibt den TextA an

`--TextB | default ` Gibt den TextB an

### Beispiel:
```
python 223d.py --Resolution 30 --Base 1 --TextA PATRIS --TextB PREDICTUM
```
output ist "output.obj"

### Ergebniss

![IMG1](https://github.com/PATRISPREDICTUM/typographischer-Text-Generator/blob/master/Bilder/Bild1.png?raw=true)
![IMG2](https://github.com/PATRISPREDICTUM/typographischer-Text-Generator/blob/master/Bilder/Bild2.png?raw=true)
![IMG3](https://github.com/PATRISPREDICTUM/typographischer-Text-Generator/blob/master/Bilder/Bild3.png?raw=true)

# Zukunft?
Eventuell wird es eine verbesserte Version in C/C++ geben, jedoch kann ich nichts versprechen, da wir momentan wenig zeit haben ...
Jedoch hat das Erstellen von diesem Projekt viel spaß gemacht
