import pandas as pd
import numpy as np

import joueur
import objectif
import mur
import vide


     
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
