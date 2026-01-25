"""
Enzo et Timothée 
Programme permetant de créer un arbre binaire visuellement 
"""

from PIL import Image, ImageDraw, ImageFont
#importe la bibliotheque PIL


class ArbreBinaire:
    """
    Entrée : une valeur
    Rôle :placer la valeur 
    Sortie : un noeud contenant une valeur et deux sous-arbres(un autre mini arbre)
    """

    def __init__(self, valeur):#constructeur
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def ajout_gauche(self, valeur):#methode pour ajouter un fils gauche
        """
        Entrée : valeur
        Rôle : ajouter un fils gauche au noed
        """
        self.gauche = ArbreBinaire(valeur)

    def ajout_droit(self, valeur):#methode pour ajouter un fils droit
        """
        Le même rôle que ajout gauche mais pour le droit 
       """
        self.droit = ArbreBinaire(valeur)


# Exemple d'arbre (sera modifié par le professeur)
arbre = ArbreBinaire("F")
arbre.ajout_gauche("W")
arbre.gauche.ajout_droit("K")
arbre.gauche.ajout_gauche("F")
arbre.ajout_droit("coucou")
arbre.droit.ajout_gauche("a")


def tracer(arbre, nom_fichier):
    """
    Entrée : un arbre binaire, un nom de fichier
    Rôle : dessiner l’arbre binaire dans une image
    Sortie : une image d un arbre binaire voulut
    """
    
    img = Image.new("RGB", (800, 900))#creation de l image
    draw = ImageDraw.Draw(img) #ce qui permet de dessiner

    # Fond blanc
    for x in range(800):
        for y in range(900):
            img.putpixel((x, y), (255, 255, 255))


    font = ImageFont.truetype("arial.ttf", 20)#met la police en arial attention il peut y avoir une petit erreur si le pc ne dispose pas de cette police


    def dessiner_noeud(arbre, x, y, largeur):
        """
        Entrée : un noeud, des coordonnés, une largeur
        Rôle : dessiner un noeud et ses fils
        """
        if arbre is None:#verifie que l arbre existe et si non ca retourne rien
            return

        draw.text((x, y), str(arbre.valeur), fill="black", font=font)#ecriture du texte au coordone xy de couleur noir et de police definit avant

        y_suivant = y + 150 #espacement entre pere et fils dans la hauteur
        demi_largeur = largeur // 2#sert a placer dans la largeur le prmier termes ainsi que les suivants

        if arbre.gauche is not None:#si il y a un fils gauche
            xg = x - demi_largeur#calcul la pos horizontale du fils droit
            draw.line([(x, y + 25), (xg, y_suivant)], fill="black", width=2)#creer un trait entre le parents et les coordonne du fils que l on vient de definir avec un trait noir de largeur 2
            dessiner_noeud(arbre.gauche, xg, y_suivant, demi_largeur)#recree la memme chose en modifiant les parametres en prenant ceux du fils et ainsi de suite

        if arbre.droit is not None:#la meme chose que a gauche maus pour le cote droit
            xd = x + demi_largeur
            draw.line([(x, y + 25), (xd, y_suivant)], fill="black", width=2)
            dessiner_noeud(arbre.droit, xd, y_suivant, demi_largeur)
    dessiner_noeud(arbre, 400, 50, 200)#c est l emplacement du premier points soit une largeure de 400 on commence a 50 en dessous du plafond et une largeure de 200 soit 1sur 4 de la largeur de l image

    img.save(nom_fichier)#sauvegarde le fichier
    img.show()#affiche a l ecran 


tracer(arbre, "meilleur_arbre_binaire.png")#appele de la fonction tracer en nommant le fivhier maillleur arbre binaire
