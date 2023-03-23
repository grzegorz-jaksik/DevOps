#pyta o oceny przy użyciu pentli while, liczy średnią przy pomocy pentli for

grades = []
sum = 0.0
grade = 0
while grade != 'X':
    grade = input("podaj kolejną ocenę, jeżeli chcesz zakończyć podaj literę X: ")
    if grade != 'X':
        grades.append(grade)

for index, grade in enumerate(grades):
    sum = sum + float(grades[index])
avr = sum / len(grades)
print(f"średnia wynosi: {avr}")

#pyta o numer telefonu, następnie wypisuje go z myślnikami
nr = input("podaj numer telefonu")
nr_with_dash = ""
for count,digit in enumerate(nr):
    nr_with_dash = nr_with_dash+(nr[count])
    if ((count + 1) % 3) == 0 and count + 1  < len(nr):
        nr_with_dash = nr_with_dash + "-"
print(f"numer z myślnikami {nr_with_dash}")


#pyta o wydatki w kazdej kategorii, oblicza procentowy udział każdego z wydatków w całości i wypisuje najbardziej znaczącą kategorię:

categories = {}
next_category = ''
while next_category != "X" :
    next_category = input("podaj kategorię wydatów, jeżeli chcesz zakończyć podaj X ")
    if next_category != "X" :
        next_expediture = ""
        expediture_sum = 0
        while next_expediture != "X":
            next_expediture = input(f"podaj kolejny wydatek w kategorii {next_category} by zakończyć podaj X ")
            if next_expediture != "X":
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