# Programme : Enzo_MOREAU_calculCRC.py
# Rôle      : Calcul du CRC d’un message binaire ou en lettre
# Auteur    : Enzo MOREAU
# Aides     : Wiki/Doc de python ,site reditte, chat gpt et les magnifique cours de Mm Belgran
# Date      : 13/10/2025
# Version   : 4.1

def calcul_crc(M, G):
    """Retourne le reste de la division XOR."""
    Mcrc = M << (G.bit_length() - 1)   # Ajout de zéros à la fin de M
    R = Mcrc
    while R >= G:
        decalage = R.bit_length() - G.bit_length()
        R = R ^ (G << decalage)
    return R

def ou_exclusive(M, G,fichier):
    """Calcule et affiche toutes les étapes du CRC + écrit dans un fichier résultat."""
    
    #verification de la longueur du message 
    if M.bit_length() < G.bit_length():
        with open(fichier, "w") as f:
            f.write("ERREUR : message trop court pour calculer le CRC")
        return
    
    Mcrc = M << (G.bit_length() - 1)
    R = calcul_crc(M, G)
    Mp = Mcrc | R
    
    resultat = []
    Rp = verifier_message(Mp,G,resultat)
    resultat.append("M (message) en binaire             : "+bin(M))
    resultat.append("M (message) en hexadécimal         : "+hex(M))
    resultat.append("G (polynôme) en binaire            : "+bin(G))
    resultat.append("G (polynôme) en hexadécimal        : "+hex(G))
    resultat.append("Mcrc (M avec zéros) en binaire     : "+bin(Mcrc))
    resultat.append("Mcrc (M avec zéros) en hexadécimal : "+hex(Mcrc))
    resultat.append("Reste CRC en binaire               : "+bin(R))
    resultat.append("Reste CRC en hexadécimal           : "+hex(R))
    resultat.append("M’ (message émis) en binaire       : "+bin(Mp))
    resultat.append("M’ (message émis) en hexadécimal   : "+hex(Mp))
    resultat.append("R’ (vérification) en binaire       : "+bin(Rp))
    resultat.append("R’ (vérification) en hexadécimal   : "+hex(Rp))

    # Écriture dans un fichier texte f etant une variable temporaire
    with open(fichier, "w") as f:
        f.write("\n".join(resultat))

def verifier_message(Mp,G,resultat):
    # Vérification de M’(X)/G(X)
    Rp = Mp 
    while Rp >= G:
        decalage = Rp.bit_length() - G.bit_length()
        Rp = Rp ^ (G << decalage)
        
    if Rp == 0:
        resultat.append("Transmission correcte")
    else:
        resultat.append("Erreur détectée : un ou plusieurs bits ont dû être modifiés.")       
    return Rp
        
def lire_message_ascii(fichier):
    """Lit un texte et renvoie son équivalent binaire en un entier."""
    with open(fichier, "r", encoding="utf-8") as f:
        texte = f.read().strip()
    binaire = "".join(format(ord(c), "08b") for c in texte)
    return int(binaire, 2)


def injecter_erreur(Mp):
    """Inverse le dernier bit de Mp."""
    return Mp ^ 1

# Programme principal

G = 0b1100000001111 

#Test 1
M1 = 0b1011000100101010
ou_exclusive(M1, G, "Enzo-MOREAU_ResultatTestM1.txt")

#Test 2
M2 = lire_message_ascii("Enzo-MOREAU_M2.txt")
ou_exclusive(M2, G, "Enzo-MOREAU_ResultatTestM2.txt")

# Test 3 : Injection d’erreur
resultat=[]
verifier_message(0b1011000100101011,G,resultat)
with open("Enzo-MOREAU_ResultatTestM3.txt", "w" , encoding="utf-8") as f:
            f.write(resultat[0])
            
# Test 4 : message trop court
M4 = 0b1010   # plus petit que le polynôme G
ou_exclusive(M4, G, "Enzo-MOREAU_ResultatTestM4.txt")

# Test 5  : 
M5 = 0b1111111111111  
ou_exclusive(M5, G, "Enzo-MOREAU_ResultatTestM5.txt")