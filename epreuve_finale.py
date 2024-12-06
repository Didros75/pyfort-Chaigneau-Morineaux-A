import json

def salle_De_Tresor():
    with open('indicesSalle.json', 'r', encoding='utf-8') as f:
        jeu_tv = json.load(f)
    liste = []
    print(jeu_tv)
    for i in jeu_tv:
        liste.append("a")
    print(liste)

salle_De_Tresor()