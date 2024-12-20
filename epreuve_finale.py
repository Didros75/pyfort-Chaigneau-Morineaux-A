import json
import random

def salle_De_Tresor():
    with open('indicesSalle.json', 'r', encoding='utf-8') as f:
        jeu_tv = json.load(f)
        jeu_tv_annee=jeu_tv['Fort Boyard']
    liste_annee = []
    for i in jeu_tv_annee.keys():
        liste_annee.append(i)
    annee=random.choice(liste_annee)
    annee_emission=jeu_tv_annee[annee]
    liste_emission = []
    for i in annee_emission.keys():
        liste_emission.append(i)
    emission=random.choice(liste_emission)
    liste_indices=annee_emission[emission]['Indices']
    mot_code=annee_emission[emission]['MOT-CODE'].lower()
    print(liste_indices[0],",",liste_indices[1],"et",liste_indices[3])
    cpt=3
    reponse_correcte=False
    while cpt>0:
        reponse_joueur=input("Trouver le bon mot grâce aux indices : ").lower()
        if mot_code in reponse_joueur:
            reponse_correcte=True
            break
        else:
            cpt-=1
            print("Il vous reste",cpt,"essais")
            if cpt>0:
                if cpt==2:
                    print("le prochain indice est",liste_indices[4])
                else:
                    print("le prochain indice est",liste_indices[5])
            else:
                print("le mot secret était", mot_code)
    if reponse_correcte:
        print("Vous avez gagné")
        return True
    else:
        print("Vous avez perdu")
        return False