# Programme : Enzo_MOREAU_calculChecksum.py
# Rôle      : Calcul du checksum de la trame ICMP
# Auteur    : Enzo MOREAU
# Date      : 13/10/2025
# Version   : 2.3

def calculchecksum (CaptureICMP):
    octe = True   
    for elt in CaptureICMP:
        if elt > 0xFF:  
            octe = False
    if octe == True:
        print("La liste est en octets, elle a ete convertit en lots de 16 bits")
        mots16 = []
        for i in range(0, len(CaptureICMP), 2):
            mot = (CaptureICMP[i] << 8) + (CaptureICMP[i+1])
            mots16.append(mot)
        CaptureICMP = mots16
    #Mise à zéro du champ checksum 
    CaptureICMP[1] = 0x0000
    #  Calcul du checksum 
    somme = sum(CaptureICMP)
    for i in range(2):
        print(f"ret{i+1}val{i+1}  {hex(somme)}")
        somme = (somme & 0xFFFF) + (somme >> 16)
    print("val3", hex(somme))
    checksum = 0xFFFF - somme
    print("Checksum calculé :", (checksum))
    
    
#Programme principale
    
# Partie ICMP en lots de 16 bits
CaptureICMP = [0x0800, 0x4CAE, 0x0001, 0x00AD, 0x6162, 0x6364, 0x6566, 0x6768, 0x696A, 0x6B6C, 0x6D6E, 0x6F70, 0x7172, 0x7374, 0x7576, 0x7761, 0x6263, 0x6465, 0x6667, 0x6869]
# Partie ICMP en lots de 8 bits
#CaptureICMP = [0x08, 0x00, 0x4C, 0xAE, 0x00, 0x01, 0x00, 0xAD, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F, 0x70,0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x61,0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69]
# Assemblage en mots de 16 bits
calculchecksum(CaptureICMP)