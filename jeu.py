import pandas as pd
import carte, mur, vide, joueur, objectif
  
class jeu():
    def __init__(self):
        self.carte = carte(1)
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
            i_0, j_0 = objet.location[0], objet.location[1]
            if self.carte.what_is_there(i, j) == objectif and type(objet) == joueur:
                self.carte.joueur.objectifs += 1
            self.carte.deplacement(i_0, j_0, i, j)
            objet.location = [i,j]
        else:
            return
    
    def deplacement_ZQSD(self, objet, direction):
        i_0, j_0  = objet.location[0], objet.location[1]
        
        if direction == "Z":
            i, j = i_0 - 1, j_0
        elif direction == "S":
            i, j = i_0 + 1, j_0
        elif direction == "Q":
            i, j = i_0, j_0 - 1
        elif direction == "D":
            i, j = i_0, j_0 + 1
        else:
            return
        object_here = self.carte.what_object_is_there(i,j)
        if self.poussable(object_here):
            self.deplacement_ZQSD(object_here, direction)
        self.deplacement(objet, i,j)
        
     

    def bouger(self,objet):
        direction = input("Vers ou ? ZQSD ")
        if direction == "Z":
            self.deplacement_ZQSD(objet, "Z")
        elif direction == "S":
            self.deplacement_ZQSD(objet, "S")
        elif direction == "Q":
            self.deplacement_ZQSD(objet, "Q")
        elif direction == "D":
            self.deplacement_ZQSD(objet, "D")
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


