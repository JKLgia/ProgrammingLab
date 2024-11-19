"""
Creazione di una funzione che permette di verificare se due liste
in input possiedono un elemento in comune
"""

def equalList(list1, list2):
    result = False
    for t in range(len(list1)):
        for i in range(len(list2)):
            if(list1[t] == list2[i]):
                result = True
                return result


listaUno = [1, 2, 3, 4, 5]
listaDue = [6, 7, 8, 3, 10]

print("=1 elemento in comune, =0 elemento non in comune ... Risultato: {:b}".format(bool(equalList(listaUno, listaDue))))

