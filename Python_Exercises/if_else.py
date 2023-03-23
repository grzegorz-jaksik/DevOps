porównuje produkty
eggs = float(input("podaj cenę jajek:"))
sugar = float(input("podaj cenę cukru :"))
milk = float(input("podaj cenę mleka :"))


print(f"czy jajka są droższe od cukru?")
if eggs > sugar:
    print("tak")
else:
    print("nie")
print(f"czy cukier jest droższy od mleka")
if sugar > milk:
    print("tak")
else:
    print("nie")

#czy lista zakupów jest długoa?
shopping= input("podaj liste zakupow oddzielajac kazdy produkt przecinkiem: ")
shopping_list = list(shopping.split(','))
print(shopping_list)
if len(shopping_list) > 5:
    print(f"lista zakupow jest dluga")
else:
    print(f"lista zakupow jest krótka")


#pyta o wydatki, podaje na co wydaje się najwięcej i ile to jest procen całej kwoty.
jedzenie = float(input("ile wydajesz na jedzenie?"))
rozrywka = float(input("ile wydajesz na rozrywkę?"))
oplaty = float(input("ile wydajesz na płaty?"))
inne = float(input("ile wydajesz na inne?"))

suma_wydatkow = jedzenie + rozrywka + oplaty + inne
wydatki_proc = {}
wydatki_proc["jedzenie"] = jedzenie/suma_wydatkow * 100
wydatki_proc["rozrywka"] = rozrywka/suma_wydatkow * 100
wydatki_proc["opłaty"] = oplaty/suma_wydatkow * 100
wydatki_proc["inne"] = inne/suma_wydatkow * 100

najwieksza_kategoria = "jedzenie"

if wydatki_proc["rozrywka"] > wydatki_proc[najwieksza_kategoria]:
    najwieksza_kategoria = "rozrywka"
if wydatki_proc["opłaty"] > wydatki_proc[najwieksza_kategoria]:
    najwieksza_kategoria = "opłaty"
if wydatki_proc["inne"] > wydatki_proc[najwieksza_kategoria]:
    najwieksza_kategoria = "inne"


print(f"najwiecej wydajesz na {najwieksza_kategoria}, co stanowi {wydatki_proc[najwieksza_kategoria]:.2f} całości wydatków")


#pyta o oceny końcowe z przedmiotów, sprawdza czy przechodzisz do nast klasy.
#przechodzisz w wypadku braku jedynek albo w jednej jedynki oraz średniej > 3.5

fizyka = int(input("Podaj ocenę z fizyki:"))
polski = int(input("Podad ocenę z polskiego:"))
matematyka = int(input("Podaj ocenę z matematyki:"))
religia = int(input("Podaj ocenę z religii:"))

ile_jedynek = 0

if fizyka == 1:
    ile_jedynek += 1
if polski == 1:
    ile_jedynek += 1
if matematyka == 1:
    ile_jedynek += 1
if religia == 1:
    ile_jedynek += 1

średnia =(fizyka + matematyka + polski + religia)/4
if ile_jedynek == 0:
    print("liczba jedynek wynosi 0, zdałeś !")
else:
    if ile_jedynek == 1:
        if średnia > 3.5:
            print("masz jedną jedynkę, ale średnia jest powyżej 3.5, zdałeś !")
        else:
            print("masz 1 jedną jedynkę, ale za niską średnią")
    else:
        print("masz za dużo jedynek, nie zdałeś")

#pyta o imię i sprawdza czy to imię żeńskie(dla uproszczenia imiona żeńskie to te kończące się na "a")

name = input("podaj swoje imiono: ")
last_letter = name[-1:]
print(last_letter)
if last_letter == "a":
    print("jesteś kobietą")
else:
    print("jesteś mężczyzną")
