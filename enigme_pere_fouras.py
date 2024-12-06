import json
import random

def charger_enigmes():
    with open('enigmesPF.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)
        return donnees

def enigme_pere_fouras():
    donnees=charger_enigmes()
    nb_essais=3
    liste=[]
    for i in donnees:
        liste.append(i["question"])
    enigme=random.choice(liste)
    for i in donnees:
        if i["question"] == enigme:
            reponse=i["reponse"]
    print(enigme)
    while nb_essais>0:
        utilisateur_rep=input("Saisir une réponse")
        if reponse==utilisateur_rep:
            print("vous avez gagner une clé")
            return True
        else:
            nb_essais-=1
            if nb_essais>0:
                print("La réponse est incorrecte, il vous reste", nb_essais)
            else:
                print("Vous avez échoué à l'énigme la solution était: ", reponse)
                return False