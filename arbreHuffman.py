#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 09:40:41 2020

@author: bernardintheo
"""

class arbreHuffman:
    
    def __init__(self,freq,label,fg=None,fd=None):
        self.freq=freq
        self.label=label 
        self.fg = fg
        self.fd = fd
        
        
    """
    redefinition de l'affichage 
    """
    def __str__(self):
        return "label"+self.label+" frequence : " + str(self.freq) + " gauche : " + str(self.fg.freq) + " droit : " + str(self.fd.freq)
    
    
    
    """
    redefinition de la comparaison >
    """
    def __gt__(self, other):
        if isinstance(other, arbreHuffman):
            if self.freq > other.freq:
                return True
            elif self.freq <= other.freq:
                return False
            
    """
    redefinition de la comparaison <
    """    
            
    def __lt__(self, other):
       if isinstance(other, arbreHuffman):
           if self.freq < other.freq:
               return True
           elif self.freq >= other.freq:
               return False
    
    
     #set de la classe arbre :
    def set_frequence(self,freq):
        self.freq=freq
    
    
    #get de la classe arbre :
    def getFreq(self):
        return self.freq
    
    def getFd(self):
        return self.fd
    
    def getFg(self):
        return self.fg
    
    
    #fonctions :
    def parcourir(self,chemin=None,res={}):
        """
        parcourir(arbre,String,Dictionary{String etiquette:String chemin}) -> return Dictionary{String etiquette:String chemin}
        fonction qui parcours un arbre en profondeur
        retourne le dictionnaire composé des étiquettes des feuilles et de leur code binaire ici appelé chemin
        """
        if self.getFd() is None and self.getFg() is None:
            res[self.label]=chemin
        if not self.getFg() is None:
            if chemin is None:
                self.getFg().parcourir('0')
            else:
                self.getFg().parcourir(chemin + '0')            
        if not self.getFd() is None:        
            if chemin is None:
                self.getFd().parcourir('1')
            else:
                self.getFd().parcourir(chemin + '1')            
        
        return res

    

    
    
    