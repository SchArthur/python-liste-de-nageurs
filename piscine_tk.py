#Arthur Schmitt
#30 novembre 2023
#gestion de liste de nageurs avec tkinter

from tkinter import *
from tkinter import ttk

listeNageur = []

def ajoutNageur(liste:list):
    """Ajoute une personne qui réalise une nage pendant certain nombre de longueur"""
    a = e_nage_qui.get()
    b = e_nage_quelle.get()
    c = e_longueur.get()
    liste.append((a,b,c))

def listeNageurs(liste:list):
    """Liste toutes les performances de tous les nageurs"""
    txt = ''
    for elt in liste:
        txt += str(elt[0]) + ", a nagé en : "+ str(elt[1]) + ". Pendants : " + str(elt[2]) + " longueur(s)."
    l_liste_resultat.config(text = txt)

fenetre = Tk()
fenetre.title('Gestion Piscine')

mainframe = ttk.Frame(fenetre, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
fenetre.columnconfigure(0, weight=1)
fenetre.rowconfigure(0, weight=1)

#Qui nage ?
l_nage_qui = ttk.Label(mainframe, text="Qui nage ?")
l_nage_qui.grid(column=0,row=0)
e_nage_qui = ttk.Entry(mainframe, width=10)
e_nage_qui.grid(column=1,row=0)

#Quelle nage ?
l_nage_quelle = ttk.Label(mainframe, text="Quelle nage ?")
l_nage_quelle.grid(column=0,row=1)
e_nage_quelle = ttk.Entry(mainframe, width=10)
e_nage_quelle.grid(column=1,row=1)

#Combien de longueur ?
l_longueur = ttk.Label(mainframe, text="Combien de longueurs ?")
l_longueur.grid(column=0,row=2)
e_longueur = ttk.Entry(mainframe, width=10)
e_longueur.grid(column=1,row=2)

#Ajout
b_ajout = ttk.Button(mainframe, text="Ajout", command = lambda: ajoutNageur(listeNageur))
b_ajout.grid(column=1,row=3)

#Liste Nageur
b_liste = ttk.Button(mainframe, text="Liste nageurs", command = lambda: listeNageurs(listeNageur))
b_liste.grid(column=0,row=6)

#Cherche nage
l_cherche_nage = ttk.Label(mainframe, text="Cherche nage : ")
l_cherche_nage.grid(column=0,row=4)
e_cherche_nage = ttk.Entry(mainframe, width=10)
e_cherche_nage.grid(column=1,row=4)
b_cherche_nage = ttk.Button(mainframe, text="rechercher", command = lambda: ajoutNageur(listeNageur))
b_cherche_nage.grid(column=2,row=4)

#Cherche nageurs
l_cherche_nageurs = ttk.Label(mainframe, text="Cherche nageur : ")
l_cherche_nageurs.grid(column=0,row=5)
e_cherche_nageurs = ttk.Entry(mainframe, width=10)
e_cherche_nageurs.grid(column=1,row=5)
b_cherche_nageurs = ttk.Button(mainframe, text="rechercher", command = lambda: ajoutNageur(listeNageur))
b_cherche_nageurs.grid(column=2,row=5)

#Resultats
l_liste_resultat = ttk.Label(mainframe, text='Resultats')
l_liste_resultat.grid(column=0,row=7)

fenetre.mainloop()