# pyta o oceny, jeżeli jest jakaś jedynka, to następuje przerwanie z informacją o konieczności powt. klasy.
oceny = []
while True:
    kolejna_ocena = input("podaj kolejną ocenę,jeżeli chcesz zakonczyć podaj literę X: ")
    if kolejna_ocena == "X":
        break
    oceny.append(kolejna_ocena)

for ocena in oceny:
    if ocena == "1":
        print("musisz powtórzyć klasę")
        break
else:
    print("Gratulacje!")

#pyta o wydatki w kazdej kategorii, oblicza procentowy udział każdego z wydatków w całości i wypisuje najbardziej znaczącą kategorię:
#
categories = {}
next_category = ''
max_category_name = ''
while True:
    next_category = input("podaj kategorię wydatów, jeżeli chcesz zakończyć podaj X ")
    if next_category == "X" :
        break
    next_expediture = ""
    expediture_sum = 0
    while True:
        next_expediture = input(f"podaj kolejny wydatek w kategorii {next_category} by zakończyć podaj X ")
        if next_expediture == "X":
            break
        expediture_sum = expediture_sum + float(next_expediture)
        categories[next_category] = expediture_sum
expeditures_sum = 0
for category in categories:
    expeditures_sum = expeditures_sum + categories[category]
    max_category = 0
for category in categories:
    print(f"kategoria {category} zajmuje procentowo{categories[category]/expeditures_sum*100}")
    if categories[category] > max_category:
        max_category_name = category
print(max_category_name)

#podaj kilka cyfr, program wypisze tylko parzyste
numbers_list = []
numbers = input("Podaj kilka liczb, odzielając je przecinkiem: ")
numbers_list= numbers.split(',')

for number in numbers_list:
    if int(number) % 2 == 1:
        continue
    print(number)


