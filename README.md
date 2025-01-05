# PYFORT

Arthur Morineaux, Melvin Chaigneau  

## Description :

Bienvenue sur Pyfort !  
Pyfort est un jeu opposant 2 équipes contenant de 1 à 3 joueurs, qui vont s'affronter dans une succession de mini-jeux, dans le but d'obtenir 3 clés et ainsi accéder à l'épreuve finale. L'équipe gagnante est la première à réunir ses clés et à remporter l'épreuve finale.  

Nous avons décidé d'opter pour un affichage graphique rendant ainsi, nous l'espérons, l'expérience plus immersive.  


## Fonctionnalités principales :  

Vous avez la possibilité de choisir le nombre de joueurs par équipe, d'entrer leur nom et prénom. S'ils n'ont jamais joué, leurs noms et prénoms sont ajoutés à la base de données. Tout ceci se fait dans la fonction `composer_equipe`.  

Vous avez également la possibilité d'accéder au leaderboard, afin de voir les noms des joueurs ayant le plus souvent gagné. Ce sont les fonctions `leaderboard` (un algorithme de tri par nombre de points) et `afficher_leaderboard`, qui permettent d'afficher le leaderboard par pages de 5 joueurs.  

Une fois en jeu, les équipes doivent, chacune leur tour, choisir un joueur pour participer à l'épreuve, puis choisir la catégorie. Une épreuve sera alors tirée au hasard parmi celles présentes dans la catégorie choisie. Ce sont les fonctions `choisir_joueur` et `menu_epreuves`.  



## Technologies Utilisées :  

Nous avons utilisé uniquement Python, avec les librairies **pygame**, **json**, **time**, et **random**.  
Nous avons ajouté un environnement virtuel contenant pygame. Néanmoins, si vous souhaitez utiliser votre propre environnement, installez pygame grâce à la commande suivante dans le terminal :  

python -m pip install pygame


## Utilisation :  

Vous avez juste à lancer `Main.py`.  



## Documentation technique :  

### Algorithme du jeu :  
1. La partie commence, les joueurs choisissent le nombre de joueurs par équipe.  
2. On compose les équipes (`composition_equipe`).  
3. La première équipe commence, elle choisit un de ses joueurs (`choisir_joueur`).  
4. Il choisit la catégorie, et le jeu se lance (`menu_epreuves`).  
5. La fonction `menu_epreuves` est appelée depuis `Main.py` et va chercher un jeu aléatoire, qui renverra `True` ou `False` selon que l'épreuve est réussie ou non. À son tour, `menu_epreuves` renvoie `True` ou `False` à la boucle principale dans `Main.py`.  
6. C'est la même chose pour la deuxième équipe. La boucle continue tant qu'aucune n'a atteint 3 clés.  
7. Si une des deux atteint 3 clés, le même principe s'applique : l'épreuve finale est lancée et renvoie `True` ou `False`.  
8. Si l'équipe gagne, tous les joueurs de l'équipe remportent un point et gravissent ainsi le leaderboard.  


### Détails des fonctions implémentées :  
- **`composition_equipe`** : Demande le nombre de joueurs par équipe, puis leurs noms et prénoms un par un, en les ajoutant dans la base de données s'ils ne sont pas présents. Elle renvoie deux listes de prénoms représentant les deux équipes.  
- **`choisir_joueur`** : Demande à une équipe de choisir un des joueurs de l'équipe.  
- **`menu_epreuves`** : Contient les listes des épreuves des différentes catégories et appelle une épreuve aléatoire contenue dans la catégorie choisie. Elle renverra `True` ou `False`.  
- **`leaderboard`** : Trie les joueurs de la base de données dans l'ordre des points et renvoie une liste triée.  
- **`afficher_leaderboard`** : Groupe par 5 les joueurs avec la possibilité de faire défiler les pages.  


### Fonctions graphiques :  
Pour faciliter la transition entre console et affichage graphique, nous avons un fichier `fenetre_graphique` qui contient des fonctions facilitant l'utilisation de l'interface :  
- **`afficher_texte`** : Affiche un texte à l'écran avec une taille et une position données (remplace un `print`).  
- **`entrer_texte`** : Crée une zone de texte et renvoie la saisie de l'utilisateur (remplace un `input`).  
- **`choix_multiples`** : Crée un nombre de boutons demandés en paramètre avec un texte donné au milieu, et renvoie le numéro du bouton sélectionné.  



## Gestion des Entrées et Erreurs :  
- Les entrées sont assez libres : par exemple, on peut répondre "couscous" quand on demande la factorielle de 4, mais cela entraînera la perte de l'épreuve, bien sûr.  
- Nous avons utilisé (rarement) la fonction `try` lorsque nous étions bloqués sur une erreur pendant longtemps, notamment dans notre algorithme de tri pour le leaderboard (qui n'est sans doute pas très optimisé pour un très grand nombre de joueurs).  

### Bugs :  
- Aucun bug à proprement parler, mais peut-être quelques décalages graphiques en raison des différences de taille d'écran, malgré nos efforts pour utiliser les proportions de l'écran.  
- Les cases de saisies n'ont pas été créées pour des noms de famille trop longs.  


## Journal de Bord :  

Nous avons commencé dès que le projet a été annoncé, car nous savions qu'une interface graphique nous prendrait du temps, et qu'on ne pourrait pas travailler dessus pendant les vacances.  
Nous avons commencé par faire un Milanote pour nous organiser avec toutes les fonctions demandées (`Milanote.pdf`).  
Nous avons malheureusement raté le dépôt intermédiaire, car nous n'avions pas vu qu'il fermait à 12h.  

### Répartition du travail :  
- L'élève habitué au code a fait l'interface graphique ainsi que la structure du jeu.  
- L'élève qui a commencé cette année s'est occupé d'une grande partie des épreuves.  


