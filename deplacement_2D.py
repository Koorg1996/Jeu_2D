import pandas as pd
import numpy as np

class joueur():
    def __init__(self):
        self.icone = "o" 

class objectif():
    def __init__(self):
        self.icone = "*"

class mur():
    def __init__(self):
        self.icone = "x"

class vide():
    def __init__(self):
        self.icone = ""

class carte():
    def __init__(self, plan):
        self.shape = list(plan.shape)
        self.nbr_murs = 0
        self.nbr_objectifs = 0
        self.plan = plan.applymap(self.icone_to_classe)
        self.trouver_joueur()
        
    def classe_to_icone(objet):
        return objet.icone
        
    def affichage(self):
        print(self.plan.applymap(carte.classe_to_icone))
        return
    
    def trouver_location(self,objet):
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.plan.iloc[i,j] == objet:
                    return [i,j]
                else:
                    continue
        return
        
    def icone_to_classe(self, objet):
        if objet == "x":
            self.nbr_murs += 1
            return mur()
        elif objet == "o":
            return joueur()
        elif objet == "*":
            self.nbr_objectifs += 1
            return objectif()
        else:
            return vide()
    
    def still_inside(self, i, j):
        if i >= 0 and i < self.shape[0] and j >= 0 and j < self.shape[1]:
            return True
        else:
            return False
    
        
    def set_(self,objet,i,j):
        if self.still_inside(i, j):
            self.plan.iloc[i,j] = objet
            return
        else:
            return
    
    def get_(self,i,j):
        objet = self.plan.iloc[i,j]
        self.plan.iloc[i,j] = vide()
        return objet
    
    def what_is_there(self,i,j):
        return type(self.plan.iloc[i,j])
    
    def deplacement(self, i, j, i_2, j_2):
        if self.still_inside(i_2, j_2):
            obj = self.get_(i,j)
            self.set_(obj, i_2, j_2)
            return
        else:
            return
    
    def trouver_joueur(self):
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if type(self.plan.iloc[i,j]) == joueur:
                    self.joueur = self.plan.iloc[i,j]
                    self.joueur.location = [i,j]
                    return
                else:
                    continue
        return 

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

