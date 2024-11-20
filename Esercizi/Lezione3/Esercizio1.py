import os

def function (stringa):
    result = 0
    file = open("file.csv", 'r')
    for line in file:
        element = line.split(',')
        if stringa in element:
            result = result + 1        
    file.close()
    return result

stringa = "Ciao"
print(os.path.abspath("file.csv"))
print("La parola cercata e' presente {:d} volte nel file".format(int(function(stringa))))

