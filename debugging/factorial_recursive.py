#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description de la fonction:
    Cette fonction calcule le factoriel d'un nombre donné.

    Paramètres:
    - n : int
        Le nombre entier dont on souhaite calculer le factoriel.

    Retour:
    - int
        Le résultat du calcul du factoriel de n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
