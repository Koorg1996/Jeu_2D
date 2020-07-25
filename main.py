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
        
    def deplacement(self, objet, i, j):
        if self.deplacement_possible(i,j):
            i_0, j_0  = objet.location[0], objet.location[1]
            if self.carte.what_is_there(i, j) == objectif:
                self.carte.joueur.objectifs += 1
            self.carte.deplacement(i_0, j_0, i, j)
            objet.location = [i,j]
        else:
            return
        
    def deplacement_haut(self, objet):
        i_0, j_0  = objet.location[0], objet.location[1]
        self.deplacement(objet, i_0-1,j_0)
        
    def deplacement_bas(self, objet):
        i_0, j_0  = objet.location[0], objet.location[1]
        self.deplacement(objet,i_0+1,j_0)
        
    def deplacement_gauche(self, objet):
        i_0, j_0  = objet.location[0], objet.location[1]
        self.deplacement(objet,i_0,j_0-1)
        
    def deplacement_droite(self, objet):
        i_0, j_0  = objet.location[0], objet.location[1]
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

df = pd.DataFrame([["x","x","x","x","x"], ["x", "*","","o","x"],["x","x","x","","x"], ["x", "","","","*","x"]])
test = carte(df)
game = jeu(test)
game._main_()
