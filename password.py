import hashlib

mot_de_passe = input("Créer un mot de passe:\n")

def valid(password):
    if len(password) < 8:
        print ("Votre mot de passe doit contenir au moins 8 caractères.")

    min = False
    maj = False
    chiffre = False
    spe = False

    for i in range(len(password)):
        if password[i]>="a" and password[i]<="z":
            min = True

        if password[i]>="A" and password[i]<="Z":
            maj = True

        if password[i]>="0" and password[i]<="9":
            chiffre = True

        if password[i]=="!" or password[i]=="@" or password[i]=="#" or password[i]=="$" or password[i]=="%" or password[i]=="^" or password[i]=="&" or password[i]=="*":
            spe = True

    if min == False:
        print ("Votre mot de passe doit contenir au moins 1 minuscule.")

    if maj == False:
        print ("Votre mot de passe doit contenir au moins 1 majuscule.")

    if chiffre == False:
        print ("Votre mot de passe doit contenir au moins 1 chiffre.")

    if spe == False:
        print ("Votre mot de passe doit contenir au moins 1 caractère spécial.")

    elif (min==True, maj==True, chiffre==True, spe==True):
        password = mot_de_passe
        password = password.encode()
        crypt = hashlib.sha256(password)
        mdp_crypte = crypt.hexdigest()
        print(mdp_crypte)
        print("Mot de passe valide!")

valid(mot_de_passe)