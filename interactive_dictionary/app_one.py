import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    count = 1

    if word in data:
        print("")

        for definition in data[word]:
            print("{}. {}".format(count, definition))
            count += 1
        return ""
    elif word.capitalize() in data:
        print("")

        for definition in data[word.capitalize()]:
            print("{}. {}".format(count, definition))
            count += 1
        return ""
    elif word.upper() in data:
        print("")

        for definition in data[word.upper()]:
            print("{}. {}".format(count, definition))
            count += 1
        return ""
    elif get_close_matches(word.capitalize(), data.keys()):
            closest_word = get_close_matches(word, data.keys())[0]
            user_answer = (input("Did you mean {}? Enter Y if yes or N if no: ".format(closest_word))).lower()

            print("")

            while user_answer != "y" or user_answer != "n":
                if user_answer == "y":
                    for definition in data[closest_word]:
                        print("{}. {}".format(count, definition))
                        count += 1
                    return ""
                elif user_answer == "n":
                    print("We didn't find it. Let's try again.")
                    word = input("Enter a word: ")
                    return translate(word)
                else:
                    print("We didn't understand your answer.")
                    user_answer = (input("Did you mean {}? Enter Y if yes or N if no: ".format(closest_word))).lower()
    elif get_close_matches(word, data.keys()):
        closest_word = get_close_matches(word, data.keys())[0]
        user_answer = (input("Did you mean {}? Enter Y if yes or N if no: ".format(closest_word))).lower()

        print("")

        while user_answer != "y" or user_answer != "n":
            if user_answer == "y":
                for definition in data[closest_word]:
                    print("{}. {}".format(count, definition))
                    count += 1
                return ""
            elif user_answer == "n":
                print("We didn't find it. Let's try again.")
                word = input("Enter a word: ")
                return translate(word)
            else:
                print("We didn't understand your answer.")
                user_answer = (input("Did you mean {}? Enter Y if yes or N if no: ".format(closest_word))).lower()
    else:
        return print("The word doesn't exist. Please double check it.")



word = input("Enter a word: ")
translate(word)
