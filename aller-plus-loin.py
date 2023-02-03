import json
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

users=input("entrez votre identifiant:")
password=input("entrez le mot de passe:")
    
       

with open('users.json') as mon_fichier :
    data = json.load(mon_fichier)

print(data)   


        



def passwords():
    while True:
         
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
            if min >= 1 and maj >= 1 and spe >= 1 and chif>= 1:
                print(password)
                return password
            
            
            else:
                print("le mot de passe est invalide")
        else:
            print("le mot de passe est court")   
  
      
def fichier_has():
    #sha256 = hashlib.sha256()
    #sha256.update(passwords().encode('utf-8'))
    password_hash = hashlib.sha256(passwords().encode('utf-8')).hexdigest()
    return password_hash


def add_password():
    global data
    if users in data and fichier_has() not in data[users]:
        data[users].append(fichier_has())
    elif users not in data:
        data.update({users:[fichier_has()]})      
    with open('users.json', 'w') as mon_fichier:
        json.dump(data, mon_fichier, indent=4, separators=(",", ": "))


    
add_password()
     


    