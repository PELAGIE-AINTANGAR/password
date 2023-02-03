import hashlib  #import la bibliotheque hashlib
    

#je definis les differents caracteres,longueur et les compteurs
caractere_min=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
caractere_maj=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chiffre=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
caracter_special=['!', '@', '$', '#', '*', '^', '%', '_', '-', ';', '.', '/']
length=8                                                                                                      
i=0
min=0
maj=0
spe=0
chif=0

#je fais une boucle qui s'execute tant que le mot de passe n'est pas valide
while True:
    password=input("entrez le mot de passe:") 
    
    #une condition pour verifier la longueur du mot de passe
    if len(password)>=8:
        
        #une boucle pour verifier les conditions de validités
        for i in password:
            if i in caractere_min:
                min=+1
            if i in caractere_maj:
                maj=+1
            if i in caracter_special:
                spe=+1
            if i in chiffre:
                chif=+1
            i=+1
        print(i,min,maj,spe,chif) 
        
        #verifie si le mot de passe contient au moins un des caractere de la condition
        if min >= 1 and maj >= 1 and spe >= 1 and chif>= 1:
            
            #hachage du mot de passe
            password_hash= hashlib.sha256()
            password_hash.update(password.encode('utf-8'))
            password_hasher=password_hash.hexdigest()
            print(password_hasher)
            print("le mot de passe est valide")
            break
        #si le mot de passe n'est pas valide il dit a l'utilisateur qui refait le mot de passe
        else:
            print("le mot de passe est invalide")
            
    #si la longueur du mot de passe est inferieur a 8 il lui renvoie le message en lui demandant un autre
    else:
        print("le mot de passe est court")   
    
   


    