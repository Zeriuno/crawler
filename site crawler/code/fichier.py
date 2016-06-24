# fichiers, modes d'ouvertures
# monFichier = open("fichier.txt", "r", encoding = "utf-8")
# monFichier = open("fichier.txt", "w", encoding = "utf-8")
# monFichier = open("fichier.txt", "a", encoding = "utf-8")


# création et ecriture
monFichier2 = open("resultatscrawling.txt", "w", encoding="utf-8")
monFichier2.write("TEST ECRITURE FICHIER !")
monFichier2.close()

# creation et ecriture bis
mesLignes = ["ligne 1\n", "ligne 2\n", "ligne 3\n"]
monFichier3 = open("fichier3.txt", "w", encoding="utf-8")
monFichier3.writelines(mesLignes)
monFichier3.close()

# ecrire du texte dans un fichier à partir d'une saisie

maQuestion = input("Quel jour sommes-nous ?")
print(maQuestion)


monFichier.close()
