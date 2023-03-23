#liczy wystapienie każdej cyfry w nr tel.

nr_tel = input("podaj nr tel:  ")
for cyfra in range(1,10):
    print(f"cyfra {cyfra} występuje:  {nr_tel.count(str(cyfra))}")

#kalkulator kredytu, rata malejąca

kwota_kredyu = int(input("Podaj kwotę kredytu:  "))
oprocentowanie = float(input("Podaj oprocenowanie:  "))
czas_trwania = int(input("Podaj czas trwania w latach:  "))
koszty_pocz =  float(input("Podaj koszty początkowe:  "))

suma_rat = 0
kapital_mies = kwota_kredyu / (czas_trwania*12)
for miesiac in range(1,czas_trwania * 12 + 1):
    pozostaly_kapital = kwota_kredyu - (miesiac -1 ) * kapital_mies
    rata = (pozostaly_kapital*oprocentowanie/100)/12+kapital_mies
    suma_rat = suma_rat + rata
    print(f"rata {miesiac} wynosi: {rata:.2f}")
print(f"oddasz bankowi: {(suma_rat+koszty_pocz):.2f}")