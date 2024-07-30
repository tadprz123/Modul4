def calculator(operation, *args):
    if operation == 1:
        return sum(args)
    elif operation == 2:
        if len(args) != 2:
            raise ValueError("W odejmowaniu można podać tylko dwie wartości.")
        return args[0] - args[1]
    elif operation == 3:
        result = 1
        for arg in args:
            result *= arg
        return result
    elif operation == 4:
        if len(args) != 2:
            raise ValueError("W dzieleniu można podać tylko dwie wartości.")
        if args[1] == 0:
            raise ZeroDivisionError("Dzielenie przez 0 jest niedozwolone w dziedzinie R.")
        return args[0] / args[1]
    else:
        raise ValueError("Błędne działanie.")

if __name__ == "__main__":
    operation = int(input("Podaj działanie (1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie): "))
    if operation in [1, 3]:
        numbers = input("Podaj składniki oddzielone przecinkiem: ").split(",")
        args = [int(number) for number in numbers]
    elif operation in [2, 4]:
        num1 = int(input("Podaj pierwszy składnik: "))
        num2 = int(input("Podaj drugi składnik: "))
        args = (num1, num2)
    else:
        print("Błędne działanie.")
        exit()

    try:
        result = calculator(operation, *args)
        print(f"Wynik: {result}")
    except ValueError as e:
        print(f"Błąd: {e}")
    except ZeroDivisionError as e:
        print(f"Błąd: {e}")