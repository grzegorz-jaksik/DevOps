#oblicza wartosc lokaty i zaokrągla wynik do 2 miejsc po przecinku

# start_value = int(input("podaj początkową wartość lokaty: "))
# percent = int(input("podaj oprocentowanie: "))
# years = int(input("podaj czas trwania lokaty w latach: "))
# value = start_value*(1 + percent / 100) ** years
# print(f"wartość koncowa lokaty to: {value:.2f} zł")

#pyta i imie i liczy ile imię ma liter

countLetters = len(input("podaj swoje imie: "))
print(f"Twoie imię ma {countLetters} liter")


#pyta o miejscowość i poprawia 1 litere na durzą

city = input("w jakiej miejscowosci mieszkasz?")
city_title = city.title()
print(f"twoja miejsowosć to {city_title}")


#zmienia format tablic na same duże litery bez spacji i znaków innych niż litery

ford = "ab100100"
audi = "EEE 123123"
citroen = "Zk-300300"
honda = "AB210210"

ford_final = ford.upper()
audi_final = audi.replace(' ','')
citroen_upper = citroen.upper()
citroen_final = citroen_upper.replace('-','')
honda_final = honda

print(ford_final)
print(audi_final)
print(citroen_final)
print(honda_final)