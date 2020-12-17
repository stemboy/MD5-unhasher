import json
import time

config = json.load(open("config.json", "r"))

possibleLetters = "".join([config["password_character_types"][name]
                           for name in config["password_content"]["character_types"]])


def loop_digit(current_str, place, pswds, outer=False):
    for letter in possibleLetters:
        current_str[place - 1] = letter

        if place != 1:
            loop_digit(current_str, place - 1, pswds)

        else:
            pswds.append("".join(l for l in current_str))

        if outer:
            print("Outer letter maker at", letter, "in", possibleLetters)


def create():
    print("Possible Letters:", possibleLetters)
    print("\n")

    for pwd_length in range(config["password_content"]["min_length"], config["password_content"]["max_length"] + 1):
        print("Generating passwords with", pwd_length, "letters")
        print()

        start_time = time.time()

        current_pwd = ["□" for i in range(pwd_length)]
        pswds = list()
        loop_digit(current_pwd, pwd_length, pswds, outer=True)

        end_time = time.time()

        print()
        print("Created", len(pswds), "passwords in", end_time-start_time, "seconds")

        print()


create()
