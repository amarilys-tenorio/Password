import hashlib
import json

password = input("Créer un mot de passe:\n")

def valid(password):
    if len(password) < 8:
        print ("Votre mot de passe doit contenir au moins 8 caractères.")

    min = False
    maj = False
    chiffre = False
    spe = False

    for i in range (len(password)):
        if password[i] >= "a" and password[i] <= "z":
            min = True

        if password[i] >= "A" and password[i] <= "Z":
            maj = True

        if password[i] >= "0" and password[i] <= "9":
            chiffre = True

        if password[i]=="@" or password[i]=="#" or password[i]=="$" or password[i]=="!" or password[i]=="?" or password[i]=="%":
            spe = True

    if min==False:
        print("Votre mot de passe doit contenir au minimum une lettre minuscule.")

    if maj==False:
        print("Votre mot de passe doit contenir au minimum une lettre majuscule.")

    if chiffre==False:
        print("Votre mot de passe doit contenir au minimum un chiffre.")

    if spe==False:
        print("Votre mot de passe doit contenir au moins un caractère spécial.")

    elif (min==True, maj==True, chiffre==True, spe==True):
        password = password.encode()
        crypt = hashlib.sha256(password)
        mdp_crypte = crypt.hexdigest()
        print(mdp_crypte)
        print("Mot de passe valide!")

    # On lit si il y a deja le meme 
    f = open("mdp.json", "r")
    # Si il y a pas on l'inscrit
    f = open("mdp.json", "w")
    f.write("Mot de passe :")
    f.write(str(password))
    # Le scrypté aussi 
    f.write("Mot de passe crypte :")
    f.write(str(mdp_crypte))
    f.close()


valid(password)