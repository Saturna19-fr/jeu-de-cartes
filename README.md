<!-- On peut faire du HTML dans certaines proportions en .md -->
<!-- Ce fichier est idéalement à lire directement sur GitHub, puisqu'il utilise des formulations de mise en page uniquement présentes sur GitHub. Dans le cas contraire, il pourra y avoir des problèmes de mise en page, qui sont résolus dans le fichier README_nongithub.md -->
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
*Cette installation est globale. Pour n'installer que les dépendences sur le dossier en cours, vous pouvez installer un [environnement virtuel](https://docs.python.org/fr/3/tutorial/venv.html).*

### Lancer le code
**O Captain, my Captain!** Il est temps de laisser la magie s'opérer.

Dans votre terminal, exécutez votre plus beau `python main.py`.

<!-- https://www.youtube.com/watch?v=AYYcBjtxp84 -->