Liste=["aime","auge","baie","brie","bris","bure","cage","cale","came","cape","cime","cire","cris","cure","dame","dime","dire","ducs","dues","duos","dure","durs","fart","fors","gage","gaie","gais","gale","gare","gars","gris","haie","hale","hors","hure","iris","juge","jure","kart","laie","lame","lime","lire","loge","luge","mage","maie","male","mare","mari","mars","mere","mers","mime","mire","mors","muet","mure","murs","nage","orge","ours","page","paie","pale","pame","pane","pape","pare","pari","part","paru","pere","pers","pipe","pire","pore","prie","pris","pues","purs","rage","raie","rale","rame","rape","rare","rime","rire","sage","saie","sale","sape","sari","scie","sure","taie","tale","tape","tare","tari","tige","toge","tore","tors","tort","trie","tris","troc","truc"]

def distance(mot1,mot2):
    dst = len(mot1)
    for i in range(len(mot1)):
        if mot1[i] == mot2[i]:
            dst -= 1
    return dst

def creation():
    dico = {}
    for mot in Liste:
        listetmp = []
        for mot2 in Liste:
            if distance(mot,mot2) == 1:
                listetmp.append(mot2)
        dico[mot] = listetmp
    return dico

def voisins(G,sommet):
    return G[sommet]

def DFS(G,depart):
    if depart not in som_visite:
        som_visite.append(depart)
    mes_voisins = [i for i in voisins(G, depart) if i not in som_visite]
    for voisin in mes_voisins:
        parents[voisin]=depart
        DFS(G,voisin)
    return parents

G = creation()

som_visite = []
parents = {}
parents['ours'] = None

#print(DFS(G, 'ours'))

arrivee= 'cage'
def chemin(arrivee, parents):
    chemin = [ ]
    courant = arrivee
    while courant != None:
        chemin = [courant] + chemin
        courant = parents[courant]
    return chemin

print(chemin(arrivee, parents))
