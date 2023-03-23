# progam pyta o cenę jabłek,wypisuje najtańsze

appleBiedronka = float(input("ile kosztują jabłka w Biedronce? "))
appleLidl =  float(input("Ile kosztują jabłka w Lidlu? "))
appleAldi = float(input("Ile kosztują jabłka w Aldi? "))

cheapestApple =  min(appleBiedronka, appleLidl, appleAldi)
print("najtańsze jabłka kosztują1:", cheapestApple)
