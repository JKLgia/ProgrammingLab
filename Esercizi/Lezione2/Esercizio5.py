"""
Il seguente esercizio prende come input una lista e due indici di 
due elementi da scambiare il contenuto.

Prima stampa a video la lista con tutti gli elementi iniziali e poi 
quella nella quale i due elementi sono stati scambiati.
"""

#Popola gli elemnti della lista
def inserimentoDati(list, i, j):
    variable = list[int(i)]
    list[int(i)] = list[int(j)]
    list[int(j)] = variable

#Test della logica delle funzioni
dim = input("Inserimento lunghezza lista: ")
list = []
i = input("Inserire valore primo elemento da scambiare: ")
j = input("Inserire valore secondo elemento da scambiare: ")

for index in range (int(dim)):
    elemento=input("Inserire valore elemento {:d} della lista: ".format(index))
    list.append(elemento)

print("Lista senza scambio: ")
for ind in range(int(dim)):
    print("{:d}".format(int(list[ind])))

inserimentoDati(list, i, j)

print("Lista dopo scambio: ")
for nd in range(len(list)):
    print("{:d}".format(int(list[nd])))