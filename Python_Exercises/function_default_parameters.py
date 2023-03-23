#funkcja która zmienia podaną liczbę na zakres, domyślnie +/- 10% wartości

def range(number, range_value = 0.1):
    range = number * range_value
    print(f"zakres wynosi +/- {range} ")

range(number = 10, range_value=0.2)


#Napisz funkcję, dodającą kolejne osoby do listy osób uczęszczających na zajęcia.
# Funkcja przyjmuje napis, który zawiera imiona rozdzielone przecinkiem oraz listę już zapisanych osób, która domyślnie jest pusta.

def persons_list(new_persons, alredy_joined = None):
    if alredy_joined == None:
        alredy_joined=[]
    new_persons_list = new_persons.split(',')
    for person in new_persons_list:
        alredy_joined.append(person)
    print(alredy_joined)

alredy_joined_list = ["kasia","basia","stasia"]
new_persons = input("podaj nowe osoby oddzielając każdą przecinkiem: ")
#persons_list(new_persons,alredy_joined=alredy_joined_list)
persons_list(new_persons)