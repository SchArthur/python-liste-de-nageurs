#Arthur Schmitt
#30 novembre 2023
#gestion de liste de nageurs avec tkinter

from tkinter import *
from tkinter import ttk

listeNageur = []

def ajoutNageur(liste:list):
    """Ajoute une personne qui réalise une nage pendant certain nombre de longueur"""
    a = e_nage_qui.get().lower()
    b = e_nage_quelle.get().lower()
    c = e_longueur.get()
    if (a != '') & (b != '') & (c.isdigit()):
        liste.append((a,b,c))
        e_nage_qui.delete(0, 'end')
        e_nage_quelle.delete(0, 'end')
        e_longueur.delete(0, 'end')
        l_liste_resultat.config(text = "Ajouté avec succées")
    else :
        l_liste_resultat.config(text = "Erreur d'ajout")


def rechercheNageur(liste:list):
    """Liste toutes les performances d'un nageur en particulier"""
    nom = e_cherche_nageurs.get().lower()
    liste_nageur = []
    for elt in liste:
        if elt[0]==nom:
            liste_nageur.append(elt)

    txt = ''
    if len(liste_nageur) == 0:
        l_liste_resultat.config(text = "Aucune information trouvée sur ce nageur.")
    else:
        for elt in liste_nageur:
            txt += str(elt[0]).capitalize() + ", a nagé en : "+ str(elt[1]) + ". Pendants : " + str(elt[2]) + " longueur(s)." + '\n'
        l_liste_resultat.config(text = txt)


def rechercheNage(liste:list):
    """Liste toutes les longueurs d'une nage en particulier"""
    nage = e_cherche_nage.get().lower()
    nbr_longueurs = 0
    for elt in liste:
        if elt[1]==nage:
            nbr_longueurs += int(elt[2])

    if nbr_longueurs > 0 :
        txt = ("Au total " + str(nbr_longueurs) + " longueur(s) nagée(s) en " + nage + '.')
        l_liste_resultat.config(text = txt)
    else:
        l_liste_resultat.config(text = "Aucune information trouvée sur cette nage.")


def listeNageurs(liste:list):
    """Liste toutes les performances de tous les nageurs"""
    txt = ''
    for elt in liste:
        txt += str(elt[0]).capitalize() + ", a nagé en : "+ str(elt[1]) + " pendants " + str(elt[2]) + " longueur(s)." + '\n'
    l_liste_resultat.config(text = txt)


def total_longueurs(liste:list):
    """Liste des infos sur les stats de la liste des nageurs"""
    longueurs = 0
    for elt in liste:
        longueurs += int(elt[2])
    txt = "Au total, " + str(longueurs) + " longueurs ont été nagées."
    l_liste_resultat.config(text = txt)


def save(liste:list):
    "sauvegarde la liste en creer un fichier liste.txt"
    fichier = open("liste.txt", 'w')
    txt = ''
    for elt in liste:
        txt += elt[0]+'/'+elt[1]+'/'+elt[2]+'-'
    fichier.write(txt)
    fichier.close()
    l_liste_resultat.config(text = "Enregistré avec succées")


def load(liste:list):
    """Charge la liste à partir d'un fichier liste.txt"""
    fichier = open("liste.txt",'r')
    text_fichier = fichier.readline()
    liste_lignes = text_fichier.split('-')
    liste_lignes = liste_lignes[ : -1]
    for i in range(len(liste_lignes)):
        liste_lignes[i] = liste_lignes[i].split('/')
    fichier.close()
    liste.clear()
    for elt in liste_lignes:
        liste.append(elt)
    l_liste_resultat.config(text = "Liste chargée avec succées")
        

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
text_valide = ttk.Label(mainframe, text="")
text_valide.grid(column=2,row=3)

#Liste Nageur
b_liste = ttk.Button(mainframe, text="Liste nageurs", command = lambda: listeNageurs(listeNageur))
b_liste.grid(column=0,row=7)

#Cherche nage
l_cherche_nage = ttk.Label(mainframe, text="Cherche nage : ")
l_cherche_nage.grid(column=0,row=4)
e_cherche_nage = ttk.Entry(mainframe, width=10)
e_cherche_nage.grid(column=1,row=4)
b_cherche_nage = ttk.Button(mainframe, text="rechercher", command = lambda: rechercheNage(listeNageur))
b_cherche_nage.grid(column=2,row=4)

#Cherche nageurs
l_cherche_nageurs = ttk.Label(mainframe, text="Cherche nageur : ")
l_cherche_nageurs.grid(column=0,row=5)
e_cherche_nageurs = ttk.Entry(mainframe, width=10)
e_cherche_nageurs.grid(column=1,row=5)
b_cherche_nageurs = ttk.Button(mainframe, text="rechercher", command = lambda: rechercheNageur(listeNageur))
b_cherche_nageurs.grid(column=2,row=5)

#Stats Nageur
b_liste = ttk.Button(mainframe, text="Total longueurs", command = lambda: total_longueurs(listeNageur))
b_liste.grid(column=1,row=7)

#Resultats
l_frame_resultats = Frame(fenetre, bd=2, background="white", relief=SUNKEN, width= 100)
l_frame_resultats.grid(column=0,row=8,columnspan=3, sticky="we")
l_liste_resultat = ttk.Label(l_frame_resultats, background="white", text='Resultats')
l_liste_resultat.grid(column=0,row=0)

#Sauvegarde/Load
b_liste = ttk.Button(mainframe, text="Enregistrer", command = lambda: save(listeNageur))
b_liste.grid(column=0,row=8)
b_liste = ttk.Button(mainframe, text="Charger", command = lambda: load(listeNageur))
b_liste.grid(column=1,row=8)

load(listeNageur)

fenetre.mainloop()