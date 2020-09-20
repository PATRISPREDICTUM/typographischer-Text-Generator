# typographischer-Text-Generator
### Sorry für den unsaubern code! Es handelt sich nur um einen Prototypen
kleines Python Projekt aus 2019 um 2 Texte zu einem 3d Modell zusammen zu fügen.
Als output erhält man ein .obj file, welches beide Texte kombiniert

## Installation
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

`--Resolution int | default 40` Regelt sie voxel auflösung des 3D objektes. je höher die Auflösung umso länger dauert das Generieren des Objektes

`--Base bool | default FALSE` Generiert eine Platform unter dem Text

`--TextA | default "ERROR"` Gibt den TextA an

`--TextB | default ` Gibt den TextB an

### Beispiel:
```
python 223d.py --Resolution 30 --Base 1 --TextA PATRIS --TextB PREDICTUM
```

