
unos = -1

try:
    while True:
        unos = float(input("Unesite ocijenu u intervalu [0.0,1.0]: "))

        if (unos >= 0.0 and unos <= 1.0):
            break
        else:
                print("Pogresan unos")

except:
    print("greska")


if unos >= 0.9 and unos <= 1.0:
    print("A")
elif unos >= 0.8:
    print("B")
elif unos >= 0.7:
    print("C")
elif unos >= 0.6:
    print("D")
else:
    print("F")