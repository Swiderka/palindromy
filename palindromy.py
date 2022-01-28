
text=  input("Czy to palindrom? Podaj tekst: ")
def is_palindrome(text):
    
    if type(text) == str:
      text = ''.join([symbol for symbol in text if symbol.isalpha()])
      return_text = text[::-1]
      if text.capitalize() == return_text.capitalize():
              return True
      else:
          return False
    else:
        print("Invalid input\nFunction works only with strings")

print(is_palindrome(text))
