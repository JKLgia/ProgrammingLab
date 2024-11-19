"""
Si scrive la funzione che permette il calcolo di un numero 
inserito manualmente e calcolarne il fattoriale
"""

def fattoriale(n):
    if(int(n)==1):
        return 1
    else:
        return int(n) * (fattoriale(int(n)-1))

n = input("Inserire valore del quale calcolare fattoriale: ")
print("Il fattoriale calcolato e' : {:d}".format(int(fattoriale(n))))