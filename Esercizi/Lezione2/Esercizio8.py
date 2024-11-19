"""
Definizione di una lista che prende in input una lista di numeri interi
poi restituisce una lista con le scritte dei numeri in italiano
"""
def classif(n):
    match n:
        case 0:
            return "Zero"
        case 1:
            return "Uno"
        case 2:
            return "Due"
        case 3:
            return "Tre"
        case 4:
            return "Quattro"
        case 5: 
            return "Cinque"
        case 6:
            return "Sei"
        case 7:
            return "Sette"
        case 8:
            return "Otto"
        case 9:
            return "Nove"

def IntToStr(list1, list2):
    for index in range(int(len(list1))):
        list2.append(classif(list1[index]))
    return list2

listaUno = [1, 0, 5, 9, 4]
listaDue =  []

print(listaUno)
IntToStr(listaUno, listaDue)
print(listaDue)
