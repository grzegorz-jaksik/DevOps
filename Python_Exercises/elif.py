# #kalkulator kredytowy oraz lokaty

typ_kalkulatora = input("wybierz typ kalkulatora: 1 - kredytowy, 2 - lokaty: ")
if typ_kalkulatora == "1":
    kwota = float(input("podaj kwotę kredytu: "))
    oprocentowanie = float(input("podaj oprocentowanie: "))
    wklad = float(input("Podaj wysokość wkładu własnego: "))
    liczba_lat = float(input("Na ile lat jest kredyt? "))
    przychod = float(input("Podaj miesięczny przychód: "))
    wydatki = float(input("podaj wysokość miesięcznych wydatków: "))

    rata = (kwota * oprocentowanie / 100) / 12 + kwota / (liczba_lat * 12)
    srodki = przychod - wydatki
    wartosc_nieruchomosci = kwota + wklad

    print(f"wysokość raty: {rata:.2f}")
    print(f"miesięczny dochód (środki): {srodki:.2f}")
    print(f"wartość nieruchomości: {wartosc_nieruchomosci:.2f}")

    if wklad < 0.1 * wartosc_nieruchomosci:
        print(f"nie dostaniesz, wkład własny minimum 10%")
    else:
        if (0.1 * wartosc_nieruchomosci <= wklad <= 0.2 * wartosc_nieruchomosci and srodki - 2000 > rata) or (
                wklad > 0.2 * wartosc_nieruchomosci and srodki - 1000 > rata):
            print("dostaniesz")
        else:
            print("nie dostaniesz")
elif typ_kalkulatora == "2":
    start_value = int(input("podaj początkową wartość lokaty: "))
    percent = int(input("podaj oprocentowanie: "))
    years = int(input("podaj czas trwania lokaty w latach: "))
    value = start_value * (1 + percent / 100) ** years
    print("wartość koncowa lokaty to:", value, "zł")
    print(f"czy wartosc lokaty wzrosła o conajmniej 10% {value >= 1.1 * start_value}")

else:
    print("wybrałeś niepoprawną opcję")

#test coopera

age = int(input("podaj swój wiek "))
sex = input("podaj płeć (M/K) ")
distance = int(input("podaj swój dystans "))

if age == 13 or age == 14:
    if sex == "M":
        if distance > 2700:
            print("Bardzo dobrze")
        elif 2400 < distance < 2700:
            print("dobrze")
        elif 2200 < distance < 2399:
            print("Średnio")
        elif 2100 < distance < 2199:
            print("żle")
        else:
            print("bardzo żle")
    elif sex == "K":
        if distance > 2000:
            print("Bardzo dobrze")
        elif 1900 < distance < 2000:
            print("dobrze")
        elif 1600 < distance < 1899:
            print("Średnio")
        elif 1500 < distance < 1599:
            print("żle")
        else:
            print("bardzo żle")
else:
    print("nie ma takiego numeru")
