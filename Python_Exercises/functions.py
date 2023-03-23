# #liczy pole prostokąta
def pole_prostokata(bok1, bok2):
    return  int(bok1) * int(bok2)
bok1 = input("podaj 1 bok prostokata")
bok2 = input("podaj 2 bok prostokąta")
print(f"pole prostokąta wynosi: {pole_prostokata(bok1,bok2)}")


#liczy średnią predkość na podstawie podaego dystansu i czasu. funkcja wykozystana do liczenia
#sredniej predkosci samochodu i roweru

def av_speed(distance, time):
    return int(distance)/int(time)

run_speed = input("podaj czas biegu(w godzinach): ")
run_distance =input("podaj dystans biegacza: ")

bike_time =  input("podaj czas przejazdu kolarza(w godzinach):  ")
bike_distance = input("podaj przejechany dystans: ")

car_time =  input("podaj czas przejazdu samochodem(w godzinach):  ")
car_distance = input("podaj przejechany dystans: ")

print(f"średnia prędkość biegu: {av_speed(run_distance, run_time)} km/h")
print(f"średnia prędkość kolarza: {av_speed(bike_distance, bike_time)} km/h")
print(f"średnia prędkość samochodu: {av_speed(car_distance, car_time)} km/h")




#pyta o wydatki w kazdej kategorii, oblicza procentowy udział każdej z kategorii w całości i wypisuje najbardziej znaczącą kategorię:
#uwzględnia funkcje
def expediture_input():
    categories = {}
    next_category = ''
    while True:
        next_category = input("podaj kategorię wydatów, jeżeli chcesz zakończyć podaj X ")
        if next_category == "X":
            break
        next_expediture = ""
        cat_expeditures_list = []
        while True:
            next_expediture = input(f"podaj kolejny wydatek w kategorii {next_category} by zakończyć podaj X ")
            if next_expediture == "X":
                break
            cat_expeditures_list.append(next_expediture)
        categories[next_category] = cat_expeditures_list
    return categories

def expeditures_sum(categories):
    categories_sum = {}
    for category, expediture in categories.items():
        category_expeditures_sum = 0
        for expediture in categories[category]:
            category_expeditures_sum = category_expeditures_sum + float(expediture)
        categories_sum[category] = category_expeditures_sum
    return categories_sum


def expeditures_percentage(categories_sum):
    all_expeditures_sum = 0
    for expeditures in categories_sum.values():
        all_expeditures_sum = all_expeditures_sum + float(expeditures)
    print(f"suma wydatków:  {all_expeditures_sum}")
    max_valuable_category_exp = 0
    for category in categories_sum:
        print(f"kategoria {category} zajmuje procentowo {(categories_sum[category] / all_expeditures_sum * 100):.2f}")
        if categories_sum[category] > max_valuable_category_exp:
            max_valuable_category_exp = categories_sum[category]
            max_valuable_category_name = category
    print(f"Najwięcej wydajesz na: {max_valuable_category_name}")

categories_with_exp = expediture_input()
categories_with_sum_exp = expeditures_sum(categories_with_exp)
expeditures_percentage(categories_with_sum_exp)