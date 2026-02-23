
Letter = (input("Enter the Character : "))

if('a' <= Letter <= 'z'):
    New_Letter = Letter.upper()
    print(New_Letter)
elif('A' <= Letter <= 'Z'):
    New_Letter = Letter.lower()
    print(New_Letter)