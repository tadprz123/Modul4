def palindromes(str):
    #funkcja porównuje wyraz od przodu i od tyłu
    #wielkie litery mają znaczenie w porównywaniu, stąd str.lower()
    str = str.lower()
    from_end = str[::-1]
    if str == from_end:
        return True
    else:
        return False
print(palindromes("Oko"))
