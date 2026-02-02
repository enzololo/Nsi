"""
G = dict()
G['a'] = ['b','c']
G['b'] = ['a','d','e']
G['c'] = ['a','d']
G['d'] = ['b','c','e']
G['e'] = ['b','d','f','g']
G['f'] = ['e','g']
G['g'] = ['e','f','h']
G['h'] = ['g']
print(G.keys()) # affiche les clés
print(G.values()) # affiche les valeurs
print(len(G)) # affiche le nombre de clés
print(G['e'])# affiche la valeur de la clé ’e’

def sommets(G):
    return len(G)

def arrete(G):
    total = 0
    for elt in G:
        total+= len(G[elt])
    return total // 2

def degre_sommet(G, sommet):
    return len(G[sommet])

def sommet_plus_haut_degre(G):
    max_sommet = None
    max_degre = 0
    for elt in G:
        if len(G[elt]) > max_degre:
            max_degre = len(G[sommet])
            max_sommet = elt        
    return max_sommet, max_degre
"""
G = {'A': ('B','D'),'B': ('A','C','D'), 'C': ('B',),'D': ('A','B')}


def conversion1(G):
    sommets = sorted(G)         
    n = len(sommets)
    m = [[0]*n for k in range(n)]
    for i in range(n):
        for j in range(n):
            if sommets[j] in G[sommets[i]]:
                m[i][j] = 1
    return m


m = [ [0,1,0,1], [1,0,1,1], [0,1,0,0],[1,1,0,0]]

def conversion2(m):
    n = len(m)
    sommets = [chr(65+ i) for i in range(n)]
    G = {}
    for i in range(n):
        voisins = []
        for j in range(len(m)):
            if m[i][j] == 1:
                voisins.append(sommets[j])
        G[sommets[i]] = voisins
    return G

print(conversion1(G))
print(conversion2(m))




