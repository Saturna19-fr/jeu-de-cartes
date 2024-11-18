<!-- On peut faire du HTML dans certaines proportions en .md -->
<!-- Ce fichier est idéalement à lire directement sur GitHub, puisqu'il utilise des formulations de mise en page uniquement présentes sur GitHub. Dans le cas contraire, il pourra y avoir des problèmes de mise en page -->
<div align="center">
    <img src="docs/assets/Header.png" />
    <h1>Jeu de Cartes: Projet de NSI</h1>
    <h3>Projet réalisé par Thibault MOREZ, Thomas FARO et Hugo Castel.</h3>
</div>

# Overview
Le projet de NSI conciste à faire un jeu de cartes qu'on peut utiliser dans plusieurs jeux. Nous allons créer un jeu à partir de ces classes, le **jeu de la Bataille**.

# Installation

> [!IMPORTANT]  
> En fonction de la plateforme utilisée, la différence est l'installation.

## Winwows NT
L'installation sur Windows NT est la plus simple:

Prérequis:
- Python 3.11.x (3.11.9 recommandée)
- Le gestionnaire de paquets **pip**
- Git, pour cloner le dépôt (optionnel)
- Savoir lire et comprendre des étapes simples

### Récupérer le code
Afin de récupérer le code, nous avons besoin de **cloner** le dépot (repository) depuis Github, ou de télécharger une archive contenant les fichiers.

Pour cloner avec Git:

1. Ouvrez un terminal `cmd.exe` ou `powershell.exe`
2. Dans l'emplacement que vous aurez choisi, exécutez la commande
```bash
git clone https://github.com/Saturna19-fr/jeu-de-cartes.git
```

### Installer les dépendances
Les dépendances sont des bouts de codes provenant de plusieurs paquets pour nous simplifier la vie. N'est il pas magnifique de déléguer le travail ?

Dans un **terminal**, lancez la commande suivante
```bash
pip install -r requirements.txt
```

Cette commande installe les dépendances requises pour faire tourner dans les conditions optimales le programme.
*Cette installation est globale. Pour n'installer que les dépendances sur le dossier en cours, vous pouvez installer un [environnement virtuel](https://docs.python.org/fr/3/tutorial/venv.html).*

### Lancer le code
**O Captain, my Captain!** Il est temps de laisser la magie s'opérer.

Dans votre terminal, exécutez votre plus beau `python main.py`.


## Linux
Prérequis:
- Python 3.11
- Le gestionnaire de paquets **pip3**
- Git, pour cloner le dépôt
- Savoir lire et comprendre des étapes simples
- Google s'il y a des bugs, parce que je vais faire efficace


### Récupérer le code
Dans le terminal, lancer:

```bash
git clone https://github.com/Saturna19-fr/jeu-de-cartes.git
```

### Installer les dépendances

Il faut créer un environnement virtuel dans votre répertoire.

En fonction de la distribution, on peut avoir des méthodes différentes pour installer des paquets.

> Pour certaines distributions, on devra installer un package supplémentaire:
>
> ```sh
> apt-get install -y python3-venv
> ```

Dans un terminal, dans le répertoire de notre projet, lancer la commande

```sh
python3 -m venv ./venv
```

(Décomposée: `python3` pour le programme, `-m` pour le module, `venv` pour le nom du module qui crée les **V**irtual **env**ironnements, et `./venv` pour le chemin de notre env à partir du répertoire actuel.)

L'environnement doit être **activé**, donc on va faire à la suite la commande:

```sh
source ./venv/bin/activate
```

Et enfin, pour installer les paquets, on utilisera le gestionnaire pip3,

```sh
pip3 install -r requirements.txt
```

<!-- https://www.youtube.com/watch?v=AYYcBjtxp84 -->

# Tests
Les tests sont sous ./tests, avec Unittest.
On peut les voir sur Python avec Unittest ou sinon sur [Github (Workflow)](https://github.com/Saturna19-fr/jeu-de-cartes/actions/workflows/python_tests.yml)

- [x] Longueur du paquet si y'a toutes les cartes
- [ ] S'il y a des dupliqués

- [x] Simuler une bataille avec x cartes
