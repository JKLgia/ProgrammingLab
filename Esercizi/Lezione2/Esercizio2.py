"""
Per questo esercizio si deve calcolare 
quante volte una lettera e' contenuta in una parola.
"""

def verificaLettera(parola, lettera):
    somma = 0
    for carat in parola:
        if lettera == carat:
            somma = somma + 1
            print("Ho incrementato la variabile di ritorno.\n")

    print("{:d}\n".format(somma))
    return somma


lettera = 'a'
parola = "aranciata"
volte = verificaLettera(parola, lettera)
print("{:d}\n".format(volte))
print("La lettera e' presente nella parola {:d} volte".format(volte))
