"""
La seguente funzione indica se dati tre numeri
questi possono essere dei lati di un triangolo
nel caso risultino essere dei lati ammissibili
si definisce la tipologia del triangolo (scaleno, rettangolo, isoscele)
"""
def typeTriangolo(a, b, c):
    if (a==b and a==c and b==c):
        print("I lati sono uguali, il trinagolo e' equilatero.")
        return "Equilatero"
    elif(a==b or b==c or c==a):
        print("Due lati sono uguali, il trinagolo e' isoscele.")
        return "Isoscele"
    else:
        print("I lati non sono uguali, il trinagolo e' scaleno.")
        return "Scaleno"


def verificaLati(a, b, c):
    sumab = a + b
    sumbc = b + c
    sumac = a + c

    if((sumab>c) and (sumbc>a) and (sumac>b)):
        print("I valori sono dei lati di un triangolo {:s}\n".format(typeTriangolo(a, b, c)))
    else:
        print("I valori inseriti non possono esser lati di un triangolo.")


a = input("Inserire valore lato 1: ")
b = input("Inserire valore lato 2: ")
c = input("Inserire valore lato 3: ")

verificaLati(int(a), int(b), int(c))


