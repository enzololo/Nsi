def vide():
    return []

def est_vide(pile):
    return len(pile) <= 0

def empiler(a,pile):
    pile.append(a)
    
def depiler(pile):
    if est_vide(pile)==False:
        return pile.pop()
    else:
        print("la pile est vide")
        
def sommet(pile):
    if est_vide(pile)==False:
        return pile[-1]
    else:
        print("la pile est vide")

    
