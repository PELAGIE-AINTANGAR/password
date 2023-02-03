import hashlib
    


caractere_min=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
caractere_maj=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chiffre=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
caracter_special=['!', '@', '$', '#', '*', '^', '%']
length=8                                                                                                      
i=0
min=0
maj=0
spe=0
chif=0
while True:
    password=input("entrez le mot de passe:")
    
    
    if len(password)>=8:
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
        if caractere_min and caractere_maj and caracter_special and chiffre:
            
            password_hash= hashlib.sha256()
            password_hash.update(password.encode('utf-8'))
            password_hasher=password_hash.hexdigest()
            print(password_hasher)
            print("le mot de passe est valide")
            break
        else:
            print("le mot de passe est invalide")
    else:
        print("le mot de passe est court")   
    
   


    