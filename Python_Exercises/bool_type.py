# pyta o ceny produktów i porównuje je.

product1 = float(input("podaj cenę pierwszego produktu :"))
product2 = float(input("podaj cenę drugiego produktu :"))
product3 = float(input("podaj cenę trzeciego produktu :"))

print(f"czy cena pierwszego produktu jest wieksza niż cena drugiego produktu ? {product1 > product2}")
print(f"czy cena pierwszego produktu jest mniejsza niż cena drugiego produktu ? {product1 < product2}")
print(f"czy cena drugiego produktu jest wieksza niż cena trzeciego produktu ? {product2 > product3}")
print(f"czy cena drugiego produktu jest mniejsza niż cena trzeciego produktu ? {product2 < product3}")
print(f"czy cena pierwszego produktu jest wieksza niż cena trzeciego produktu ? {product1 > product3}")
print(f"czy cena pierwszego produktu jest mniejsza niż cena trzeciego produktu ? {product1 <product3}")

#pyta o listę zakupów, wyświetla czy lista jest długa
shopping= input("podaj liste zakupow oddzielajac kazdy produkt przecinkiem: ")
shopping_list = list(shopping.split(','))
print(shopping_list)
print(f"lista zakupow jest dluga: {len(shopping_list) > 5}")



start_value = int(input("podaj początkową wartość lokaty: "))
percent = int(input("podaj oprocentowanie: "))
years = int(input("podaj czas trwania lokaty w latach: "))
value = start_value*(1 + percent / 100) ** years
print("wartość koncowa lokaty to:", value, "zł")
print(f"czy wartosc lokaty wzrosła o conajmniej 10% {value >= 1.1*start_value}")
