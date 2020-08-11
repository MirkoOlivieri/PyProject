import random

def decision():
    x = input("Press y to roll again else press n \n")
    if(x == "y"):
        return True
    else:
        return False
def inglese():
    while(decision()):
        f= (random.randint(1, 6))
        if f == 1:
            print("+-------------+")
            print("|             |")
            print("|      0      |")
            print("|             |")
            print("+-------------+")
            print("The number drawn is " + str(f))
        if f == 2:
            print("+--=------------+")
            print("|       0       |")
            print("|               |")
            print("|       0       |")
            print("+---------------+")
            print("The number drawn is " + str(f))
        if f == 3:
            print("+--=-------------+")
            print("|        0       |")
            print("|        0       |")
            print("|        0       |")
            print("+----------------+")
            print("The number drawn is " + str(f))
        if f == 4:
            print("+--=-------------+")
            print("|  0         0   |")
            print("|                |")
            print("|  0         0   |")
            print("+----------------+")
            print("The number drawn is " + str(f))
        if f == 5:
            print("+--=-------------+")
            print("|  0         0   |")
            print("|       0        |")
            print("|  0         0   |")
            print("+----------------+")
            print("The number drawn is " + str(f))
        if f == 6:
            print("+--=-------------+")
            print("|  0         0   |")
            print("|  0         0   |")
            print("|  0         0   |")
            print("+----------------+")
            print("The number drawn is " + str(f))

def italiano():
    while(decision()):
        f = (random.randint(1, 6))
        if f == 1:
            print("+-------------+")
            print("|             |")
            print("|      0      |")
            print("|             |")
            print("+-------------+")
            print("Il numero estratto e' " + str(f))
        if f == 2:
            print("+--=------------+")
            print("|       0       |")
            print("|               |")
            print("|       0       |")
            print("+---------------+")
            print("Il numero estratto e' " + str(f))
        if f == 3:
            print("+--=-------------+")
            print("|        0       |")
            print("|        0       |")
            print("|        0       |")
            print("+----------------+")
            print("Il numero estratto e' " + str(f))
        if f == 4:
            print("+--=-------------+")
            print("|  0         0   |")
            print("|                |")
            print("|  0         0   |")
            print("+----------------+")
            print("Il numero estratto e' " + str(f))
        if f == 5:
            print("+--=-------------+")
            print("|  0         0   |")
            print("|       0        |")
            print("|  0         0   |")
            print("+----------------+")
            print("Il numero estratto e' " + str(f))
        if f == 6:
            print("+--=-------------+")
            print("|  0         0   |")
            print("|  0         0   |")
            print("|  0         0   |")
            print("+----------------+")
            print("Il numero estratto e' " + str(f))



lingua=input("Press I(Italian) or E(English) \n")
if(lingua=="I"):
    italiano()
    print('Arrivederci')
elif(lingua=="E"):    
    inglese()
    print('Goodbye')
else:
    print("Opzione non disponibile, arrivederci.")
