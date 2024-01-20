import math

def wykonaj_operacje(a, b, operacja):
    if operacja == '+':
        return a + b
    elif operacja == '-':
        return a - b
    elif operacja == '*':
        return a * b
    elif operacja == '/':
        return a / b if b != 0 else "Nie można dzielić przez zero"
    else:
        return None

while True:
    try:
        num1 = float(input("Podaj pierwszą liczbę: "))
        operator = input("Podaj operację (+, -, *, /): ")
        num2 = float(input("Podaj drugą liczbę: "))

        wynik = wykonaj_operacje(num1, num2, operator)
        if wynik is None:
            print("Nieprawidłowa operacja")
        else:
            print(f"Wynik: {wynik}")

    except ValueError:
        print("Nieprawidłowe dane wejściowe. Podaj poprawne liczby.")

    if input("Czy chcesz wykonać kolejne obliczenia? (T/N): ").upper() != 'T':
        break
