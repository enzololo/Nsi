import time

with open("la_disparition.txt", "r", encoding="utf-8") as FichierTexte:
    texte = FichierTexte.read()
    
motif = "bonjour"

def recherche_native(motif, texte):
    n = len(texte)
    m = len(motif)
    compteur_occurence = 0
    compteur = 0 
    debut = time.time()
    for s in range(n-m):
        compteur_temp = 0 
        for i in range(m):
            compteur+= 1
            if texte[s + i] == motif[i]:
                compteur_temp += 1 
        if compteur_temp == m:  
            compteur_occurence += 1

    fin = time.time()

    return compteur_occurence , fin-debut , compteur



def dico(motif):
    dictionnaire = {}
    l = len(motif)   
    for i in range(l-1):
        lettre = motif[i]
        dictionnaire[lettre] = l-i-1
    return dictionnaire

print(dico(motif))

def boyer_moore_horspool(texte, motif):
    size = len(texte) 
    taille = len(motif)
    position = []
    compteur = 0 
    debut = time.time()
    if(taille<= size):#regarde si la taille du texet est superieur a celle du motif
        decalage = dico(motif)#cree le dictionnaire du motif 
        i = 0
        trouve = False
        while(i<= size-taille):#boucle pour rechercher tt les elements dans un texte sans en faire plus
            for j in range (taille-1,-1,-1):
                trouve = True
                compteur += 1 
                if(texte[i+j]!= motif[j]):
                    if(texte[i+j] in decalage and decalage[texte[i+j]]<=j):
                        i+= decalage[texte[i+j]]
                    else:
                        i+= j +1
                    trouve = False
                    break
            if(trouve):
                position.append(i)
                i=i+1
                trouve = False

    fin = time.time()

    return position , fin-debut , compteur


print(recherche_native(motif, texte))



print(boyer_moore_horspool(texte, motif))


