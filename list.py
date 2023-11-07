#1 Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif

n = 10
liste_divisible_par_2 = []

for i in range(n + 1):
    if i % 2 == 0:
        liste_divisible_par_2.append(i)

print(liste_divisible_par_2)


#2Ou gen yon lis antye, konvèti l an yon lis chenn.=

liste_entiers = [1, 2, 3, 4, 5]
liste_chaines = []

for entier in liste_entiers:
    liste_chaines.append(str(entier))

print(liste_chaines)

#3Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil

liste_minuscules = ["chaine1", "chaine2", "chaine3"]
liste_majuscules = [chaine.upper() for chaine in liste_minuscules]
print(liste_majuscules)

#4Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nouvelle_liste1 = [element for index, element in enumerate(liste) if index % 3 == 0]

print(nouvelle_liste1)

#5Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl.

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

nouvelle_liste = []

for i in range(0, len(liste), 3):
    groupe = liste[i:i+3]
    nouvelle_liste.append(groupe)

print(nouvelle_liste)

#6Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon.

liste_avec_doublons = [1, 2, 2, 3, 4, 4, 5, 5, 5]
liste_sans_doublons = list(set(liste_avec_doublons))

print(liste_sans_doublons)

#7Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.

liste1 = [1, 2, 3, 4, 5]
liste2 = [3, 4, 5, 6, 7]

# Utilisez un ensemble (set) pour trouver les éléments communs
ensemble1 = set(liste1)
ensemble2 = set(liste2)

# Utilisez l'opération d'intersection pour trouver les éléments communs
elements_communs = list(ensemble1.intersection(ensemble2))

print(elements_communs)

#8 Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.

liste1 = [1, 2, 3, 4, 5]
liste2 = [3, 4, 5, 6, 7]

# Convertissez les listes en ensembles
ensemble1 = set(liste1)
ensemble2 = set(liste2)

# Utilisez les opérations de différence symétrique pour obtenir les éléments distincts
elements_distincts = list(ensemble1.symmetric_difference(ensemble2))

print(elements_distincts)


#9Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman.

dictionnaire = {"a": 1, "b": 2, "c": 3, "d": 4}

# Liste des clés
cles = list(dictionnaire.keys())

# Liste des valeurs
valeurs = list(dictionnaire.values())

print("Liste des clés:", cles)
print("Liste des valeurs:", valeurs)


#10Reyini 3 lis ansanm, san okenn doublon.

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste3 = [7, 8, 9]

liste_combinee = liste1 + liste2 + liste3































