
letter = input("Enter a letter: ").lower()

vowels = {'a', 'e', 'i', 'o', 'u'}


if len(letter) == 1 and letter.isalpha():
    if letter in vowels:
        print(f"The letter '{letter}' is a vowel.")
    else:
        print(f"The letter '{letter}' is not a vowel.")
else:
    print("Invalid input. Please enter a single letter.")
