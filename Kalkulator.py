print("Wybierz typ działania z poniższych opcji: ")
print("1 - Dodawanie")
print("2 - Odejmowanie")
print("3 - Mnożenie")
print("4 - Dzielenie")
print("5 - Potęgowanie")
print("6 - Dzielenie z Resztą")
dzialanie = int(input("Wybierz: "))

if dzialanie == 1: 
    a = int(input("Wpisz Pierwszą Liczbę : "))
    b = int(input("Wpisz Drugą Liczbę : "))
    c = a + b
    print(f"Wynikiem dodawania liczb {a} i {b} jest {c}")

elif dzialanie == 2:
    a = int(input("Wpisz Pierwszą Liczbę : "))
    b = int(input("Wpisz Drugą Liczbę : "))
    c = a - b
    print(f"Wynikiem odejmowania liczb {a} i {b} jest {c}")

elif dzialanie == 3:
    a = int(input("Wpisz Pierwszą Liczbę : "))
    b = int(input("Wpisz Drugą Liczbę : "))
    c = a * b
    print(f"Wynikiem mnożenia liczb {a} i {b} jest {c}")

elif dzialanie == 4:
    a = int(input("Wpisz Pierwszą Liczbę : "))
    b = int(input("Wpisz Drugą Liczbę : "))
    c = a / b
    print(f"Wynikiem dzielenia liczb {a} i {b} jest {c}")

elif dzialanie == 5:
    a = int(input("Wpisz Pierwszą Liczbę : "))
    b = int(input("Wpisz Drugą Liczbę : "))
    c = a ** b
    print(f"Wynikiem potęgowania liczb {a} i {b} jest {c}")

elif dzialanie == 6:
    a = int(input("Wpisz Pierwszą Liczbę : "))
    b = int(input("Wpisz Drugą Liczbę : "))
    c = a // b
    d = a % b 
    print(f"Wynikiem dzielenia liczb {a} i {b} jest {c} reszty {d}")

else:
    print("Podaj prawidłową opcję!")
