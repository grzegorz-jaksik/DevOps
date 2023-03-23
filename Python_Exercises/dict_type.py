#słownik z tematami

subiects = {
    "polski": 5,
    "angielski": 6,
    "metematyka": 2,
    "religia": 3,
}

print(subiects)

#drzewa genealogiczne

my_family = {
    "Imie": "Grzegorz",
    "Nazwisko": "Jaksik",
    "rok": 1985,
    "Rodzice":[
        {
            "Imię":"Hanna",
            "Nazwisko": "Zakolska",
            "rok": 1962,
            "Rodzice":[]
        },
        {
            "Imię":"Janusz",
            "Nazwisko":"Jaksik",
            "rok":1962,
            "Rodzice":[]
        }
    ]
}
print (my_family)
#pyta o wydatki, liczy ile na nie wydajemy procentowo na każda kategorię, wypisuje najbardziej znaczący wydatek
wydatki = {}
wydatki["jedzenie"] = float(input("ile wydajesz na jedzenie?"))
wydatki["rozrywka"] = float(input("ile wydajesz na rozrywkę?"))
wydatki["opłaty"] = float(input("ile wydajesz na płaty?"))
wydatki["inne"] = float(input("ile wydajesz na inne?"))


suma_wydatkow = sum(list(wydatki.values()))
wydatki_proc = {}
wydatki_proc["jedzenie"] = wydatki["jedzenie"]/suma_wydatkow * 100
wydatki_proc["rozrywka"] = wydatki["rozrywka"]/suma_wydatkow * 100
wydatki_proc["opłaty"] = wydatki["opłaty"]/suma_wydatkow * 100
wydatki_proc["inne"] = wydatki["inne"]/suma_wydatkow * 100


ktory_wydatek = input("podaj kategorie wydatków z grupy:jedzenie, rozrywka, opłaty, inne: ")

print(f"na {ktory_wydatek} wydales {wydatki[ktory_wydatek]}, co stanowi {wydatki_proc[ktory_wydatek]}  % całości")