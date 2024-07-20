def palindromes(str):
    #funkcja porównuje wyraz od przodu i od tyłu
    str = str.lower()
    from_end = str[::-1]
    if str == from_end:
        return True
    else:
        return False
print(palindromes("Oko"))
