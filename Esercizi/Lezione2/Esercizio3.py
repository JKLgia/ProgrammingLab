"""
Funzione che permette di verificare se la parola inserita e' un
palindromo, ovvero può esser letta in entrambi i versi:
Da sinistra a destra e da destra a sinistra.
"""

def palindromo(stringa):
    result = False
    
    if(stringa == stringa[::-1]):
        result = True
    
    return result

frase = "alta"

print("La frase e' palindroma: {:b}".format(palindromo(frase)))
        