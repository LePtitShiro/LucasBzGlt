# If you see any flaws and best way to do it, let me know! I'm still just a beginner.

import random
import string

def listAlphabet(): # Returns a random list of lowercase and uppercase letters
  a = list(string.ascii_lowercase + string.ascii_uppercase)
  random.shuffle(a)
  return a

def listChiffre(): # Returns a list of digits from 0 to 9
    return list(k for k in range(10))

def listSpecialCaractere(): #Returns a list of special characters
    return ["#","ù",",","?","§","*","%","£","$","@"]


def generator_mdp():
    liste = []
    resultat = ''  # the variable that will be returned
    nb_caractere = int(input("How many characters do you want in your password ? "))

    if nb_caractere % 3 == 0: #Since our password is composed of 3 types of characters, we try that they are well distributed
        c = 0

        while c < (nb_caractere / 3):
            liste.append(random.choice(listAlphabet()))
            liste.append(str(random.choice(listChiffre())))
            liste.append(random.choice(listSpecialCaractere()))
            c += 1

        random.shuffle(liste)

    else: 
        c = 0
        c_2 = 0

        liste_v2 = []

        while c < (nb_caractere // 3):
            liste.append(random.choice(listAlphabet()))
            liste.append(str(random.choice(listChiffre())))
            liste.append(random.choice(listSpecialCaractere()))
            c += 1
        while c_2 < (nb_caractere % 3):
            liste_v2.append(random.choice(listAlphabet()))
            liste_v2.append(str(random.choice(listChiffre())))
            liste_v2.append(random.choice(listSpecialCaractere()))
            c_2 += 1

        random.shuffle(liste_v2)

        for k in range(nb_caractere % 3):
            liste.append(random.choice(liste_v2))

        random.shuffle(liste)


    for element in liste:
        resultat += element

    return resultat

  
  
