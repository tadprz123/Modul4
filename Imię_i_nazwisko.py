def name_surname(name):
    effect = "Dzień dobry %s!" % name
    return effect
if __name__ == "__main__":
    name_surname_text = input("Podaj imię i nazwisko: ")
    done = name_surname_text
    name_surname_result = name_surname(done)
    print(name_surname_result)
"""
def shopping(items, payment='card', shop='local'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result
if __name__ == "__main__":
    items_text = input("Podaj produkty rozdzielone przecinkiem: ")
    items = items_text.split(', ')
    shopping_result = shopping(items)
    print(shopping_result)
"""
