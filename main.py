import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_question = 10


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1)
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"

    reponse_str = input(f" calculez {a} {operateur_str} {b} = ")
    reponse_int = int (reponse_str)
    calcul = a+b
    if o == 1:
        calcul = a*b
    if reponse_int == calcul:
        return True
    return False


nb_points = 0


for i in range(0,NB_question):
    print(f"question n° {i+1} sur {NB_question} :")
    if poser_question():
         print("reponse correcte")
         nb_points += 1
    else:
        print("reponse incorecte")
    print()

print(f"votre note est {nb_points} / {NB_question}")

moyenne = int(NB_question/2)

if nb_points == NB_question:
    print("excellent !")
elif nb_points == 0:
    print("révisez vos math !")
elif nb_points > moyenne:
    print("pas mal")
else:
    print("peut mieux faire")