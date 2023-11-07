#1kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.

def inverse_mot(mot):
    mot_inverse = mot[::-1]
    return mot_inverse

mot_original = "hello"
mot_inverse = inverse_mot(mot_original)
print("Mot original :", mot_original)
print("Mot inversé :", mot_inverse)


#2kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik.

import random
import string

def generer_code_aleatoire(n):
    caracteres = string.ascii_letters
    code = ''.join(random.choice(caracteres) for _ in range(n))
    return code


code_aleatoire = generer_code_aleatoire(8)
print("Code aléatoire :", code_aleatoire)

#3kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon.

import random
import string


def generer_code_aleatoire_sans_repetition(n):
    caracteres = string.ascii_letters
    if n > len(caracteres):
        raise ValueError("Le nombre de caractères demandé dépasse le nombre de caractères disponibles.")

    code = random.sample(caracteres, n)
    code = ''.join(code)
    return code


# Exemple d'utilisation de la fonction pour générer un code de 8 caractères sans répétition
code_aleatoire = generer_code_aleatoire_sans_repetition(8)
print("Code aléatoire sans répétition :", code_aleatoire)

#4 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.
import random
import string


def generer_code_alphanumerique_sans_repetition(n):
    caracteres = string.ascii_letters + string.digits
    if n > len(caracteres):
        raise ValueError("Le nombre de caractères demandé dépasse le nombre de caractères alphanumériques disponibles.")

    code = random.sample(caracteres, n)
    code = ''.join(code)
    return code

code_alphanumerique = generer_code_alphanumerique_sans_repetition(8)
print("Code alphanumérique sans répétition :", code_alphanumerique)



#5Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan. Nan yon SLUG, tout karaktè ki akseptab yo se: alfanimerik ak "-"

import re

def generer_slug(chaine):
    # Supprimez les caractères non alphanumériques (sauf les tirets)
    chaine = re.sub(r'[^a-zA-Z0-9-]', '', chaine)
    # Remplacez les espaces par des tirets
    chaine = chaine.replace(' ', '-')
    # Remplacez plusieurs tirets consécutifs par un seul tiret
    chaine = re.sub(r'-+', '-', chaine)
    # Convertissez en minuscules
    chaine = chaine.lower()
    return chaine

chaine = "Ceci est une chaîne avec des caractères spéciaux! 123"
slug = generer_slug(chaine)
print("Chaîne originale :", chaine)
print("Slug généré :", slug)



#6 Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil

def separer_lettres_avec_virgules(mot):
    lettres_separees = ', '.join(mot)
    return lettres_separees

mot = "Bonjour"
lettres_separees = separer_lettres_avec_virgules(mot)
print("Mot original :", mot)
print("Lettres séparées avec virgules :", lettres_separees)



#7 Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè.
def crypter_mot(mot):
    mot_crypte = []
    for lettre in mot:
        if 'a' <= lettre <= 'z':
            # Pour les lettres minuscules
            index = ord(lettre) - ord('a') + 1
            mot_crypte.append(str(index))
        elif 'A' <= lettre <= 'Z':
            # Pour les lettres majuscules
            index = ord(lettre) - ord('A') + 1
            mot_crypte.append(str(index))
        else:
            # Pour d'autres caractères (non alphabétiques)
            mot_crypte.append(lettre)

    return '-'.join(mot_crypte)

mot = "Hello"
mot_crypte = crypter_mot(mot)
print("Mot original :", mot)
print("Mot crypté :", mot_crypte)


#8 Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè.

def decrypter_mot(mot_crypte):
    indices = mot_crypte.split('-')
    mot_decrypte = []

    for indice in indices:
        if indice.isdigit():
            index = int(indice)
            if 1 <= index <= 26:
                # Pour les indices valides (1 à 26)
                lettre = chr(ord('a') + index - 1)
                mot_decrypte.append(lettre)
        else:
            # Si l'indice n'est pas un chiffre, conservez le caractère original
            mot_decrypte.append(indice)

    return ''.join(mot_decrypte)

mot_crypte = "8-5-12-12-15"
mot_decrypte = decrypter_mot(mot_crypte)
print("Mot crypté :", mot_crypte)
print("Mot décrypté :", mot_decrypte)

#9 Kreye yon fonksyon ki ap pran 2 paramèt, epi ki pèmite valè yo. Answit li retounen tou 2 valè yo sou fòm Tuple.

def permuter_et_retourner(a, b):
    # Échangez les valeurs de a et b
    a, b = b, a
    # Retournez les deux valeurs sous forme de tuple
    return a, b

# Exemple d'utilisation de la fonction
valeur1 = 10
valeur2 = 20
resultat = permuter_et_retourner(valeur1, valeur2)
print("Valeur 1 après permutation:", resultat[0])
print("Valeur 2 après permutation:", resultat[1])

#10 Kreye yon fonksyon ki ap pran yon non an paramèt, epi ki retounen inisyal yo. Atansyon ak non konpoze ak tirè yo.

def initiales_du_nom(nom):
    mots = nom.split()  # Divisez le nom en mots
    initiales = [mot[0].upper() for mot in mots]  # Prenez la première lettre de chaque mot en majuscules
    return ''.join(initiales)  # Concaténez les initiales pour former un seul mot

# Exemple d'utilisation de la fonction
nom = "John Doe"
initiales = initiales_du_nom(nom)
print("Nom complet :", nom)
print("Initiales :", initiales)
































































































































