#1 Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.
dictionnaire = {"a": 1, "b": 2, "c": 3, "d": 4}

cles = dictionnaire.keys()
valeurs = []

for cle in cles:
    valeur = dictionnaire[cle]
    valeurs.append(valeur)

# Affichez la liste de valeurs
print(valeurs)

#2 Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè

# Demandez à l'utilisateur d'entrer une valeur
valeur = input("Entrez une valeur : ")

# Vérifiez si la valeur a des accolades devant ou derrière
a_des_accolades_devant = valeur.startswith("{")
a_des_accolades_derriere = valeur.endswith("}")

# Affichez le résultat
if a_des_accolades_devant:
    print("La valeur a des accolades devant.")
if a_des_accolades_derriere:
    print("La valeur a des accolades derrière.")
if not a_des_accolades_devant and not a_des_accolades_derriere:
    print("La valeur n'a pas d'accolades ni devant ni derrière.")


#3Pakouri yon diksyonè, epi afiche tout kle yo.

dictionnaire = {"a": 1, "b": 2, "c": 3, "d": 4}

# Parcourez les clés du dictionnaire et affichez-les
for cle in dictionnaire:
    print(cle)


#4Pakouri yon diksyonè, epi afiche tout valè yo.
dictionnaire = {"a": 1, "b": 2, "c": 3, "d": 4}

# Parcourez les valeurs du dictionnaire et affichez-les
for valeur in dictionnaire.values():
    print(valeur)

#5 Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
dictionnaire_original = {"a": 1, "b": 2, "c": 3, "d": 4}

# Initialisez un nouveau dictionnaire pour la copie
dictionnaire_copie = {}

# Parcourez les éléments du dictionnaire original
for cle, valeur in dictionnaire_original.items():
    if isinstance(valeur, (int, float, str)):
        # Utilisez eval pour créer une copie du dictionnaire
        dictionnaire_copie[cle] = eval(repr(valeur))

# Affichez la copie
print("Dictionnaire original :", dictionnaire_original)
print("Dictionnaire copie :", dictionnaire_copie)


#6 Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo. Ekzanp:

dictionnaire_original = {
    "cle1": "valeur1",
    "cle2": 42,
    "cle3": "valeur2",
    "cle4": 3.14,
}

dictionnaire_modifie = {}

# Parcourez les éléments du dictionnaire original
for cle, valeur in dictionnaire_original.items():
    if isinstance(valeur, str):
        # Si la valeur est une chaîne, ajoutez des underscores avant et après
        valeur_modifiee = f"_{valeur}_"
    else:
        # Si la valeur n'est pas une chaîne, conservez-la telle quelle
        valeur_modifiee = valeur

    # Ajoutez l'élément au dictionnaire modifié
    dictionnaire_modifie[cle] = valeur_modifiee

# Affichez le dictionnaire modifié
print("Dictionnaire original :", dictionnaire_original)
print("Dictionnaire modifié :", dictionnaire_modifie)


#7 Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman

dictionnaire_original = {
    "cle1": "123",
    "cle2": "42",
    "cle3": "non_nombre",
    "cle4": "9876",
}

# Initialisez un nouveau dictionnaire pour les valeurs numériques
dictionnaire_numerique = {}

# Parcourez les éléments du dictionnaire original
for cle, valeur in dictionnaire_original.items():
    if isinstance(valeur, str) and all(char.isdigit() for char in valeur):
        # Utilisez isinstance pour vérifier que la valeur est une chaîne,
        # et all() pour vérifier que tous les caractères sont des chiffres.
        dictionnaire_numerique[cle] = valeur

# Affichez le dictionnaire avec les valeurs numériques
print("Dictionnaire original :", dictionnaire_original)
print("Dictionnaire avec les valeurs numériques :", dictionnaire_numerique)



#8 Pakouri yon disksyonè, pou w mete l sou fòm lis, kote chak eleman nan disksyonè sa, vin sou fòm tipl(kle, valè) anndan lis la


dictionnaire = {
    "cle1": "valeur1",
    "cle2": "valeur2",
    "cle3": "valeur3",
}

# Utilisez une liste de compréhension pour créer la liste de tuples
liste_tuples = [(cle, valeur) for cle, valeur in dictionnaire.items()]

# Affichez la liste de tuples
print(liste_tuples)


#9 Pakouri yon lis tipl, pou w mete l sou fòm diksyonè.
liste_tuples = [("cle1", "valeur1"), ("cle2", "valeur2"), ("cle3", "valeur3")]

# Initialisez un dictionnaire vide
dictionnaire = {}

# Parcourez les tuples et ajoutez-les au dictionnaire
for cle, valeur in liste_tuples:
    dictionnaire[cle] = valeur

# Affichez le dictionnaire résultant
print(dictionnaire)


#10 Kole 2 diksyonè ansanm pou fè youn, kote si gen eleman ki gen menm kle ap konkatene valè, swivan kondisyon sa yo:

dictionnaire1 = {"a": 1, "b": 2}
dictionnaire2 = {"c": 3, "d": 4}

# Utilisez l'opérateur d'union pour fusionner les dictionnaires (à partir de Python 3.9)
dictionnaire_fusionne = dictionnaire1 | dictionnaire2

# Le dictionnaire_fusionne contient maintenant la fusion des deux dictionnaires
print(dictionnaire_fusionne)
























