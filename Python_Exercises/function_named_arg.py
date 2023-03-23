#liczy średnią predkość na podstawie podaego dystansu i czasu. funkcja wykozystana do liczenia
#sredniej predkosci samochodu i roweru

def av_speed(what_vehicle):
    time = float(input(f"rodzaj pojazdu: {what_vehicle}, czas przejazdu (w godzinach): "))
    distance = float(input(f"rodzaj pojazdu: {what_vehicle}, podaj pokonany dystans(w km): "))
    speed = distance/time
    print(f"średnia prędkość osiągnięta przez: {what_vehicle} wynosi {speed}: ")
    return

av_speed(what_vehicle = "rower")
av_speed(what_vehicle= "ałto")
av_speed(what_vehicle= "kuń")