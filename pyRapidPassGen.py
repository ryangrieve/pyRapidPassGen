from string import ascii_letters, digits, punctuation
from secrets import choice

print("\npyRapidPassGen - A simple password generator using python.\n")
user_option = input("Begin options questionnaire? (y/n): ")

if user_option == "y":

    def user_config():
        def error_message():  # Error message
            print("\n**Invalid option response, please try again.**\n")
            user_config()

        print("\nPlease answer a few quick questions: \n")  # Questionnaire
        try:
            chars, number_pass, special_chars = (
                int(input(">> How long should the password be? (eg: 20): ")),
                int(input(">> How many passwords are required? (eg: 5): ")),
                str(input(">> Use special characters? (y/n): ")),
            )
        except Exception:
            error_message()

        print("\nGenerating passwords...\n")  # Generator
        for i in range(number_pass):
            CHARACTERS = (ascii_letters, digits, punctuation)
            try:
                if special_chars == "y":
                    x = [CHARACTERS[i] for i in [0, 1, 2]]
                elif special_chars == "n":
                    x = [CHARACTERS[i] for i in [0, 1]]
                password = "".join(choice("".join(x)) for i in range(chars))
            except Exception:
                error_message()
            print(password)

        restart = input("\npyRapidPassGen task complete.\n\nRestart? (y/n): ")
        user_config() if restart == "y" else quit()

    user_config()
else:
    quit("pyRapidPassGen closing...")
