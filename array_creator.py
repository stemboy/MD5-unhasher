import hashlib
import time

from config import config

possibleLetters = "".join([config["password_character_types"][name]
                           for name in config["password_content"]["character_types"]])


def loop_digit(current_str, place, pws, outer=False):
    for letter in possibleLetters:
        current_str[place - 1] = letter

        if place == 1:
            pw = "".join(_letter for _letter in current_str)
            pws[hashlib.md5(pw.encode())] = pw

        else:
            loop_digit(current_str, place - 1, pws)

        if outer:
            print("Outer letter maker at", possibleLetters.index(letter)+1, "in", len(possibleLetters))


def create():
    print("Possible Letters:", possibleLetters)
    print("\n")

    all_pws = {}

    for pwd_length in range(config["password_content"]["min_length"], config["password_content"]["max_length"] + 1):
        print("Generating passwords with", pwd_length, "letters")
        print()

        start_time = time.time()

        current_pwd = ["□" for _ in range(pwd_length)]
        pws = {}
        loop_digit(current_pwd, pwd_length, pws, outer=True)

        end_time = time.time()

        print(pws)
        print("Created", len(pws), "passwords in", end_time-start_time, "seconds")
        print("\n")

        all_pws = all_pws + pws

    print(all_pws)





if __name__ == '__main__':
    create()
