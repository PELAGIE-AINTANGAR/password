import json   #import la bibliotheque json
import hashlib #import la bibliotheque hashlib


#je definis les differents caracteres,longueur et les compteurs

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
    
       
# ouvre le fichier users.json en mode lecture et charge son contenu dans la variable data
with open('users.json') as mon_fichier :
    data = json.load(mon_fichier)
  


        


#je definis une fonction pour verifier la validite du mot de passe
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
  
#je definis une fonction pour hacher le mot de passe
     
def fichier_has():
    #sha256 = hashlib.sha256()
    #sha256.update(passwords().encode('utf-8'))
    password_hash = hashlib.sha256(passwords().encode('utf-8')).hexdigest() #je l'ai en faite en une ligne grace a l'aide  des amies qui m'on explique que je pourrais le faire en une ligne
    return password_hash

#je declara la fonction pour ajouter le mot de passe au fichier json
def add_password():
    global data
    
    #vérifie si l'utilisateur est présent dans les données "data" et si la fonction fichier hash ne figure pas déjà 
    if users in data and fichier_has() not in data[users]:
        data[users].append(fichier_has())  # il ajoute le mot de passe hacher à la liste des données de l'utilisateur
    elif users not in data: #verifier si l'utilisateur n'est pas present dans data
        data.update({users:[fichier_has()]})    #il ajoute l'utilisateur avec sa première entrée de hash de fichier
        
    #cette bloc écrit les données mises à jour dans un fichier nommé "users.json"      
    with open('users.json', 'w') as mon_fichier:
        json.dump(data, mon_fichier, indent=4, separators=(",", ": "))


    
add_password()
     


    