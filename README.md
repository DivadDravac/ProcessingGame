# ProcessingGame

Jeu de carte 1v1 configurable, programmé en Python. 

## Introduction

Dans le cadre du projet de fin de module "Programmer avec Python", les élèves de l'ESIGELEC doivent réaliser un programme pour atester de leur montée en compétence. Etant enseignant, je propose un projet test ne répondant bien évidement à aucun sujets donnés. Cette démarche a pour but de motiver les élèves à développer proprement, documenter leur code et produire une application simple à maintenir.

## Concept du jeu
Le jeu s'apparente au jeu de carte "Le PDG" dans lequel il est nécessaire de défausser le plus rapidement possible sa main. Il se joue dans sa première version en 1v1 mais pourrait être amélioré en free for all en partie à plusieur. 
Deux programmes s'affrontent sur un microprocesseur. Le but pour chacun des programmes est de ne plus avoir à executer 

## Les règles


### Les zones
Le plateau de jeu possède plusieurs zones : 
- La bibliothèque : Elle est la même pour les deux joueurs. Ces 100 cartes y sont disposées en pile de manière aléatoire face cachée. A chaque fois qu'un joueur doit piocher, il doit prendre la première carte au dessus de la bibilothèque et l'ajouter à sa main.
- La main : Elle n'est visible que par le joueur qui en est propriétaire (sauf dans des cas précis précisés ci-après). 
- Le processeur : Cette zone centrale recoi tous les programmes qu'elle ddoit executer.


### La séquence de base

De base chaque joueur joue chacun son tour. Lors de son tour le joueur passe par plusieurs phases : 

- Début de tour : Le tour de joueur commence
- Pioche : Le joueur à qui c'est le tour pioche une carte
- Joue : Le joueur à qui c'est le tour pose une carte sur la pile du processeur
- Execute : Le processeur execute la pile si une carte execution est posée (cf execution). Le processeur execute les cartes comme une pile d'assiètes. La première à être executée est la dernière à avoir été posée et la dernière est la première à avoir été posé sur la zone vide.
- Fin de tour : C'est l'étape de fin de tour

#### Execution

#### 

### Les conditions de fin de jeu
Plusieurs conditions permettent de déclancher la fin de la partie : 
- Si un joueur n'a plus de cartes en main, il gagne la partie. 
- Si un joueur ne peut plus piocher de carte de la bibliothèque, il perd la partie.
- Si un joueur créé une boucle infinie, il perd la partie.

### Les cibles

Il existe plusieurs cibles valides : 
- Une carte : Elle peut être séléctionnée aléatoirement, avec sa position dans la zone du processeur ou par selection de l'utilisateur.
- Cartes d'une zone : Toutes les cartes des zones suivantes peuvent être ciblées :
    - La main d'un joueur
    - Le terrain d'un joueur
    - La défausse
    - Le processeur

## Le projet

### Les cartes

Un set de carte doit être présent sous la forme d'un dossier (ici Bibliothèque). L'image est un simple fichier PNG qui porte un nom contenant le nom de la carte, son type et ses fonction. Toutes ses informations sont séparées du caractère "$". Chaque carte peut avoir jusqu'a 6 séquences déclanchées lors des différents états du processeur. Chaque  Ainsi il y a :
 
- une séquence déclanchée pour les étapes de début du tour des joueurs
- une séquence déclanchée pour les étapes de fin du tour des joueurs
- une séquence déclanchée à chaque pioche
- une séquence déclanchée à chaque défausse
- une séquence déclanchée à chaque carte jouée sur le migroprocesseur
- une séquence déclanchée lors de l'execution de la carte

Chaque fonction est 

- cible 
    - A : Toutes les cartes d'une zone
    - S : Une carte selectionnée
    - ? : Une carte au hasard
    - § : La dernière carte de la pile
 - Une zone
    - O : Toutes les zones
    - = : La bibliothèque
    - P : Le processeur
    - D : La défausse
    - T / t : Le terrain du joueur / de l'adversaire
    - M / m : La main du joueur / de l'adversaire
- une action 
    - @ : pour déplacer
    - +/- : pour ajouter un marqueur
- une destination
    - = : La bibliothèque
    - P : Le processeur
    - D : La défausse
    - T / t : Le terrain du joueur / de l'adversaire
    - M / m : La main du joueur / de l'adversaire
La fonction est executée seulement si elle est correcte, sinon elle n'est pas executée.
