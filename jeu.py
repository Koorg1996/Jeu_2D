import pandas as pd
import numpy as np
import carte, mur, vide, joueur, objectif

class jeu():
    def __init__(self, carte):
        self.carte = carte
        self.carte.joueur.objectifs = 0
    
    def deplacement_possible(self, i, j):
        if self.carte.still_inside(i, j) and self.carte.what_is_there(i, j) in [vide,objectif]:
            return True
        else:
            return False
    
    def poussable(self, objet):
        if type(objet) == boite:
            return True
        else:
            return False
        
    def deplacement(self, objet, i, j):
        if self.deplacement_possible(i,j):
            try:
                i_0, j_0  = objet.location[0], objet.location[1]
            except:
                objet.location = self.carte.trouver_location(objet)
                i_0, j_0 = objet.location[0], objet.location[1]
            if self.carte.what_is_there(i, j) == objectif and type(objet) == joueur:
                self.carte.joueur.objectifs += 1
            self.carte.deplacement(i_0, j_0, i, j)
            objet.location = [i,j]
        else:
            return
        
    def deplacement_haut(self, objet):
        try:
            i_0, j_0  = objet.location[0], objet.location[1]
        except:
                objet.location = self.carte.trouver_location(objet)
                i_0, j_0 = objet.location[0], objet.location[1]                
        i, j = i_0 - 1, j_0
        object_here = self.carte.what_object_is_there(i,j)
        if self.poussable(object_here):
            self.deplacement_haut(object_here)
        self.deplacement(objet, i,j)
        
    def deplacement_bas(self, objet):
        try:
            i_0, j_0  = objet.location[0], objet.location[1]
        except:
                objet.location = self.carte.trouver_location(objet)
                i_0, j_0 = objet.location[0], objet.location[1]
                
        i, j = i_0 + 1, j_0
        object_here = self.carte.what_object_is_there(i,j)
        if self.poussable(object_here):
            self.deplacement_bas(object_here)
        self.deplacement(objet,i,j)
        
    def deplacement_gauche(self, objet):
        try:
            i_0, j_0  = objet.location[0], objet.location[1]
        except:
                objet.location = self.carte.trouver_location(objet)
                i_0, j_0 = objet.location[0], objet.location[1]
                
        i, j = i_0, j_0 - 1
        object_here = self.carte.what_object_is_there(i,j)
        if self.poussable(object_here):
            self.deplacement_gauche(object_here)
        self.deplacement(objet,i_0,j_0-1)
        
    def deplacement_droite(self, objet):
        try:
            i_0, j_0  = objet.location[0], objet.location[1]
        except:
                objet.location = self.carte.trouver_location(objet)
                i_0, j_0 = objet.location[0], objet.location[1]
                
        i, j = i_0, j_0 + 1
        object_here = self.carte.what_object_is_there(i,j)
        if self.poussable(object_here):
            self.deplacement_gauche(object_here)
        self.deplacement(objet,i_0,j_0+1)        

    def bouger(self,objet):
        direction = input("Vers ou ? ZQSD ")
        if direction == "Z":
            self.deplacement_haut(objet)
        elif direction == "S":
            self.deplacement_bas(objet)
        elif direction == "Q":
            self.deplacement_gauche(objet)
        elif direction == "D":
            self.deplacement_droite(objet)
        else:
            return
    
    def victoire(self):
        if self.carte.joueur.objectifs == self.carte.nbr_objectifs:
            return True
        else:
            return False
    
    def _main_(self):
        
        self.carte.affichage()
        while not self.victoire():
            self.bouger(self.carte.joueur)
            self.carte.affichage()
        print("Bravo")

