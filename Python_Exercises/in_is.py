#pyta o listę zakupów, sprawdza czy jest na niej chleb lub bułki

zakupy = input("Podaj listę zakupów oddzielając kolejne pozycje przecinkami: ")
zakupy_lista = []
zakupy_lista = zakupy.split(',')

if "bułki"  in zakupy_lista or "chleb" in zakupy_lista:
    print("na liście są bułki lub chleb")
else:
    print("na liscie nie ma chleba ani bułek")


#pyta o numer tel i sprawdza czy jest zero

nr_tel = input("Podaj nr telefonu: ")

if "0" in nr_tel:
    print("w numerze jest conajmniej jedno zero")
else:
    print("w numerze nie ma zer")

# podejemy wartość value i sprawdzamy czy jest False, True, None

value = False

if value is None:
    print("wartość value jest None")
elif value is True:
    print("wartość value jest True")
elif value is False:
    print("wartość value jest False")
else:
    print("wartość value jest inną wartością")