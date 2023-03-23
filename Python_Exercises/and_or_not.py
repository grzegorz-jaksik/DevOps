#kalkulator kredytowy

kwota = float(input("podaj kwotę kredytu: "))
oprocentowanie = float(input("podaj oprocentowanie: "))
wklad = float(input("Podaj wysokość wkładu własnego: "))
liczba_lat = float(input("Na ile lat jest kredyt? "))
przychod = float(input("Podaj miesięczny przychód: "))
wydatki = float(input("podaj wysokość miesięcznych wydatków: "))

rata = (kwota * oprocentowanie / 100)/12 + kwota / (liczba_lat * 12)
srodki = przychod - wydatki
wartosc_nieruchomosci = kwota + wklad

print(f"wysokość raty: {rata:.2f}")
print(f"miesięczny dochód (środki): {srodki:.2f}")
print(f"wartość nieruchomości: {wartosc_nieruchomosci:.2f}")

if wklad < 0.1 * wartosc_nieruchomosci:
    print(f"nie dostaniesz, wkład własny minimum 10%")
else:
    if  (0.1 * wartosc_nieruchomosci <= wklad <= 0.2 * wartosc_nieruchomosci and srodki - 2000 > rata) or (wklad > 0.2 * wartosc_nieruchomosci and srodki - 1000 > rata):
        print("dostaniesz")
    else:
        print("nie dostaniesz")


