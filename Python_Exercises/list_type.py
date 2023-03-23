

#list favorite sports, list first and last, replace one of them. show whole list.
#wypisuje z listy ppierwszy i ostatni sport, zaminia jedną z pozycji z listy, wuisuje całą listę
sport_list =["siatkówka", "koszykówka", "balet", "szachy"]

print(f"pierszy sport to:, {sport_list[0]},   ostatni to:, {sport_list[-1]}")
sport_list[1] = "kolarstwo"
print(f"lista sportow: , {sport_list}")


#pyta o 3 ulubione posiłki,zamienia je na listę.
meals_list =[]
meals = input("podaj 3 ulubione potrawy: ")
meals_list = meals.split(',')
print(meals_list)

#pyta o numer telefonu, anonimizuje go dodając 3 kreski zamiast 3 cyfr

number = input ("podaj numer telefonu")
anonimize_number = number[:6] + "-"* (len(number)-6)
print(F"numer zanonimizowany:, {anonimize_number}")


