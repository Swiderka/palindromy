text= input("Czy to palindrom? Podaj tekst: ")
def palindrom(text):
    i = len(text)
    if i %2 == 1 and text[::1] == text[::-1]:
        return True
    elif i %2 == 0 and text[::1] == text[::-1]:
        return True
    else:
        return False


print(palindrom(text))