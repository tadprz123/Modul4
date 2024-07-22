def name_surname(name):
    effect = "Dzień dobry %s!" % name
    return effect
if __name__ == "__main__":
    name_surname_text = input("Podaj imię i nazwisko: ")
    done = name_surname_text
    name_surname_result = name_surname(done)
    print(name_surname_result)

