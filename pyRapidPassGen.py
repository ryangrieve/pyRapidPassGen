from secrets import choice
from string import ascii_letters, digits, punctuation

print("\npyRapidPassGen - A simple password generator using python.")


def password_gen(chars, number_pass, special_chars):
    print("\nGenerating passwords...\n")
    x = [ascii_letters, digits]
    if special_chars == "y":
        x.append(punctuation)
    for i in range(number_pass):
        print("".join(choice("".join(x)) for i in range(chars)))
    print("\npyRapidPassGen task complete.\n")


def user_config():
    while True:
        print("\nPlease answer a few quick questions: \n")
        try:
            chars = int(input("> How long should the password be? (eg: 20): "))
            number_pass = int(input("> How many passwords? (eg: 5): "))
            special_chars = str(input("> Use special characters? (y/n): "))
            if special_chars not in ["y", "n"]:
                raise ValueError
        except ValueError:
            print("\n**Invalid option response, please try again.**")
            continue
        password_gen(chars, number_pass, special_chars)
        if input("Restart? (y/n): ") == "y":
            continue
        else:
            quit("\npyRapidPassGen closing...")


user_config()
