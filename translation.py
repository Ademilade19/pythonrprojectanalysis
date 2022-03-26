def translate(phrase):
    translation = ""
    for letter in translation:
        if letter in "AEIOUaeiou":
            translation += "g"
        else:
            translation += letter
    return translation


print(translate(input("Enter Phrase: ")))
