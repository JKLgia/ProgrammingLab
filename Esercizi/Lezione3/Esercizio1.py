"""
[Funzione 1 = fReadLine]
Permette di usare il metodo readLine per leggere le singole righe
e poi vengono contate quante volte la parola si ripete nella reale posizione.

[Funzione 2 = fReadLines]
Usa metodo readLines -> Restituisce una lista con singola riga come elemento della lista.
Piu corretto usare la prima riga.
"""
def fReadLine(file, stringa):
    result = 0
    list = []
    riga = file.readline()
    while riga != "":
        list.append(riga)
        riga = file.readline()
    print(list)
    
    for element in list:
        if stringa in element:
            result = result + 1       
    return result

def fReadLines(file, stringa):
    result = 0
    tmp = file.readlines() 
    print(tmp)
    for element in tmp:
        if stringa in element:
            result = result + 1
    return result


file = open(r"C:\Users\Media\Desktop\uniTS_AI\1_ANNO\I Semestre\Laboratorio Programmazione\GIT_CLONE\ProgrammingLab\Esercizi\Lezione3\file.txt", "r")
stringa = input("inserire parola da cercare nel file:")
print("La parola cercata e' presente {:d} volte nel file".format(int(fReadLine(file, stringa))))
print("La parola cercata e' presente {:d} volte nel file".format(int(fReadLines(file, stringa))))
file.close()

