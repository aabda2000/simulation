# -*- coding: utf-8 -*-
"""
Created on Sunday July  17 14:47:34 2022

@author: ahmad.abdallah
"""

import random
import numpy as np
import matplotlib.pyplot as plt

##################################################################################
# DEFINITION D'UN CERTAIN NOMBRE DE FONCTIONS UTILES AU COURS DE LA SIMULATION
##################################################################################

def init_dist(Matrice):

    M = len(Matrice[0])  # nombre d'abscisses
    # nombre d'ordonnées (a priori la matrice n'est pas forcément carrée)
    N = len(Matrice)
    # balayage de la matrice
    for i in range(N):
        for j in range(M):
            nombre_aleat_case = random.randint(1, 2)
    # 1= rouge, 2 =noir
            Matrice[i][j] = nombre_aleat_case

    return Matrice

def iter_dist(Matrice):

    M = len(Matrice[0])  # nombre d'abscisses
    # nombre d'ordonnées (a priori la matrice n'est pas forcément carrée)
    N = len(Matrice)
    # balayage de la matrice
    for i in range(N):
        for j in range(M):
            if Matrice[i][j] == 0:
                nombre_aleat_case= random.randint(1, 2)
                Matrice[i][j] = nombre_aleat_case


# fonction prenant en paramètre une matrice
# retournant toutes les coordonnées des points rouges/noirs(coefficients égaux à 1 ou 2)
def cases(Matrice, couleur):
    M = len(Matrice[0])  # nombre d'abscisses
    # nombre d'ordonnées (a priori la matrice n'est pas forcément carrée)
    N = len(Matrice)

    ListePoints = []  # liste qui contiendra les coordonées de tous les points

    # balayage de la matrice
    for i in range(N):
        for j in range(M):
            if Matrice[i][j] == couleur:
                # on ajoute les coordonnées du point rencontré à ListePoints
                ListePoints.append([j, i])

    return ListePoints

# fonction prenant en paramètre une matrice
# ON Fixe la couleur de l'équipe Bleue, Jaune

def casesFixées(Matrice, couleur):
    M = len(Matrice[0])  # nombre d'abscisses
    # nombre d'ordonnées (a priori la matrice n'est pas forcément carrée)
    N = len(Matrice)

    ListePointsFixes = []  # liste qui contiendra les coordonées de tous les points fixés

    # balayage de la matrice
    for i in range(N):
        for j in range(M):
            if Matrice[i][j] == couleur:
                Matrice[i][j] = couleur + 2
                # on ajoute les coordonnées du point
                ListePointsFixes.append([j, i])

    return ListePointsFixes

def initVerts(Matrice):
    M = len(Matrice[0])  # nombre d'abscisses
    # nombre d'ordonnées (a priori la matrice n'est pas forcément carrée)
    N = len(Matrice)

    # liste qui contiendra les coordonées de tous les points verts (neutres)
    ListePointsVerts = []

    # balayage de la matrice
    for i in range(N):
        for j in range(M):
            if Matrice[i][j] != 3 and Matrice[i][j] != 4:
                Matrice[i][j] = 0
                # on ajoute les coordonnées du point
                ListePointsVerts.append([j, i])

    return ListePointsVerts

# fonction qui permet l'affichage de l'évolution
# paramètre d'entrée : matrice modélisant l'espace
# retourne 5 listes:
    # les points verts (leurs abscisses et leurs ordonnées) ;
    # les points rouges (leurs abscisses et leurs ordonnées) ;
    # les points noirs (leurs abscisses et leurs ordonnées) ;
    # les points bleu (leurs abscisses et leurs ordonnées)
    # les points jaunes (leurs abscisses et leurs ordonnées)

def affichageCases(Matrice):
    # nombre d'abscisses
    M = len(Matrice[0])
    # nombre d'ordonnées
    N = len(Matrice)
    Xverts = []
    Yverts = []
    Xrouges = []
    Yrouges = []
    Xnoirs = []
    Ynoirs = []
    Xbleus = []
    Ybleus = []
    Xmages = []
    Ymages = []
    # balayage de la matrice
    for i in range(N):
        for k in range(M):
            # cas des points verts
            if Matrice[i][k] == 0:
                # on retient l'abscisse correspondante
                Xverts.append(longueur*k)
                # on retient l'ordonnee correspondante
                Yverts.append(longueur*i)
            # cas des points rouges
            elif Matrice[i][k] == 1:
                # on retient l'abscisse correspondante
                Xrouges.append(longueur*k)
                # on retient l'ordonnee correspondante
                Yrouges.append(longueur*i)

            # cas des points noirs
            elif Matrice[i][k] == 2:
                # on retient l'abscisse correspondante
                Xnoirs.append(longueur*k)
                # on retient l'ordonnee correspondante
                Ynoirs.append(longueur*i)
            elif Matrice[i][k] == 3:
                # on retient l'abscisse correspondante
                Xbleus.append(longueur*k)
                # on retient l'ordonnee correspondante
                Ybleus.append(longueur*i)

            elif Matrice[i][k] == 4:
                # on retient l'abscisse correspondante
                Xmages.append(longueur*k)
                # on retient l'ordonnee correspondante
                Ymages.append(longueur*i)

    return Xverts, Yverts, Xrouges, Yrouges, Xnoirs, Ynoirs, Xbleus, Ybleus, Xmages, Ymages


#############################################################################
# SIMULATION d'une distribution uniforme
#############################################################################

# DEFINITION DE L'ESPACE
# Longueur totale d'un côté de l'espace carré (en m)
L = 50
# Espace entre deux points (en m)
longueur = 10
# nombre de points observés sur une ligne du quadrillage
N = int(L/longueur) + 1
# représentation du quadrillage par une matrice carrée de taille N*N (modèle bidimensionnel)
Matrice = np.zeros((N, N))

# nombre de points bleu visé par la simulation
K = 24

# AFFICHAGE DU MAILLAGE AVANT DEPART DE LA SIMULATION (que des points verts)
# Construction de la liste des abscisses
X = []
for i in range(N):
    X.append(longueur*i)

# Affichage du maillage ligne par ligne avant départ de la simulation
for i in range(N):
    plt.plot(X, [i*longueur]*N, "o", color="green", markersize=40)

plt.pause(15)

Matrice = init_dist(Matrice)

print(Matrice)
# BOUCLE EFFECTUANT LA SIMULATION
ListeCasesBleus = []
ListeCasesMages = []
ListeCasesNoirs = []
ListeCasesRouges = []
OK = True
while (OK):
    # AFFICHAGE DES POINTS DANS MATPLOTLIB A CHAQUE ITERATION POUR SUIVRE L'EVOLUTION DE LA DISTRIBUTION
    Xrouges = affichageCases(Matrice)[2]
    Yrouges = affichageCases(Matrice)[3]
    Xnoirs = affichageCases(Matrice)[4]
    Ynoirs = affichageCases(Matrice)[5]

    # plt.plot(Xverts, Yverts, "o", color="green")
    plt.plot(Xrouges, Yrouges, "o", color="red", markersize=40)
    plt.plot(Xnoirs, Ynoirs, "o", color="black", markersize=40)
    # pause de 50 ms entre deux itérations (uniquement pour l'affichage)

    plt.pause(5)
    # à chaque itération on répertorie les coordonnées des points rouges et noirs dans une liste
    ListeCasesRouges = cases(Matrice, 1)
    ListeCasesNoirs = cases(Matrice, 2)
    if len(ListeCasesRouges) == K:
        K = K-len(ListeCasesRouges)
        # bleu
        casesFixées(Matrice, 1)

        if 0 == K:
            casesFixées(Matrice, 2)
            OK = False

    elif len(ListeCasesRouges) < K:
        K = K-len(ListeCasesRouges)
        # bleu
        casesFixées(Matrice, 1)

    elif len(ListeCasesRouges) > K:

        #K = len(ListeCasesRouges) - K
        # magenta
        casesFixées(Matrice, 2)

        #K=len(ListeCasesMages) -K

    ListeCasesBleus = cases(Matrice, 3)
    ListeCasesMages = cases(Matrice, 4)

    print("K=", K, "N=", N*N, "B=", len(ListeCasesBleus), "J=",
          len(ListeCasesMages), "R=", len(ListeCasesRouges))
    # AFFICHAGE DES POINTS DANS MATPLOTLIB A CHAQUE ITERATION
    Xverts = affichageCases(Matrice)[0]
    Yverts = affichageCases(Matrice)[1]

    Xbleus = affichageCases(Matrice)[6]
    Ybleus = affichageCases(Matrice)[7]
    Xmages = affichageCases(Matrice)[8]
    Ymages = affichageCases(Matrice)[9]

    plt.title('Les Bleus= '+str(len(ListeCasesBleus)) +
              ', Les Jaunes = '+str(len(ListeCasesMages)))
    plt.plot(Xverts, Yverts, "o", color="green", markersize=40)
    plt.plot(Xrouges, Yrouges, "o", color="red", markersize=40)
    plt.plot(Xnoirs, Ynoirs, "o", color="black", markersize=40)
    plt.plot(Xbleus, Ybleus, "o", color="blue", markersize=40)
    plt.plot(Xmages, Ymages, "o", color="yellow", markersize=40)
    # pause de 50 ms entre deux itérations (uniquement pour l'affichage, durée pas représentative de la réalité)
    plt.pause(5)

    if OK:
        initVerts(Matrice)
        Xverts = affichageCases(Matrice)[0]
        Yverts = affichageCases(Matrice)[1]
        plt.plot(Xverts, Yverts, "o", color="green", markersize=40)
        plt.pause(5)
        iter_dist(Matrice)

print("finish")
plt.show()
