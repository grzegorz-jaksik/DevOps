#prosi o wpisanie liczby tak długo aż będzie to licza parzysta, albo będzie więcej niż 10 prób
try_counter = 1
modulo = 1
while try_counter < 11 and modulo == 1:
    number = int(input("Podaj liczbę parzystą: "))
    modulo = number % 2
    if modulo == 0:
        print(f"dobrze, liczba {number} jest parzysta!")
    else:
        print(f"liczba {number} nie jest liczbą parzystą,  proba {try_counter} z 10")
        try_counter += 1

#pyta o numer telefonu, następnie wypisuje go z myślnikami
nr = input("podaj numer telefonu")
count = 0
nr_with_dash = ""
while count < len(nr):
    nr_with_dash = nr_with_dash+(nr[count])
    if ((count+ 1) % 3) == 0 and count + 1  < 9:
        nr_with_dash = nr_with_dash + "-"
    count += 1
print(f"numer z myślnikami {nr_with_dash}")

#pyta o dania a następnie wylicza je po kolei
counter = 0
dishes = input("podaj ulubione dania oddzielając każdą pozycję przecinkiem: ")
dishes_list = dishes.split(',')

while counter < len(dishes_list):
    print(f"danie numer {counter+1} to {dishes_list[counter]}")
    counter += 1