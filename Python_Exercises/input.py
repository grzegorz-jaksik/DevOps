#input function


# prgogram pyta o wiek i przelicza go na miesiace
age = input("ile masz lat?")
month = int(age)*12
print("masz", age, "lat, czyli",month, "miesiecy" )


#program pyta ile przechodzisz km tygodniowo i podaje ile tygodni zajmie okrązenie ziemi

distance = input("ile km przeszedles w tym tygodniu? ")
equator = 40075
EarthTime = equator / int(distance)
print("ziemie przejdziesz w ", EarthTime, "tygodni")


#oblicza wartosc lokaty

start_value = int(input("podaj początkową wartość lokaty: "))
percent = int(input("podaj oprocentowanie: "))
years = int(input("podaj czas trwania lokaty w latach: "))
value = start_value*(1 + percent / 100) ** years
print("wartość koncowa lokaty to:", value, "zł")