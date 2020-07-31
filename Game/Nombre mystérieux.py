import random

number = random.randint(0, 100)

print("Nombre Mystérieux - Cherche le nombre entre 0 et 100 en suivant les indications ! Credits: ")

validation = False

while validation == False:
    choix = int(input())


    if choix == number:
        validation = True
        print("Bravo ! Le nombre était: ", number, " !")
    if choix > number:
        print("Le nombre est plus petit !")
    if choix < number:
        print("Le nombre est plus grand !")
    

print('Fin de la partie !')