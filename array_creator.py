import hashlib
import time

from config import config

possibleLetters = "".join([config["password_character_types"][name]
                           for name in config["password_content"]["character_types"]])


def loop_digit(current_str, place, pwds, outer=False):
    for letter in possibleLetters:
        current_str[place - 1] = letter

        if place == 1:
            pwd = "".join(l for l in current_str)
            pwds[hashlib.md5(pwd.encode())] = pwd

        else:
            loop_digit(current_str, place - 1, pwds)

        if outer:
            print("Outer letter maker at", possibleLetters.index(letter)+1, "in", len(possibleLetters))


def create():
    print("Possible Letters:", possibleLetters)
    print("\n")

    all_pwds = {}

    for pwd_length in range(config["password_content"]["min_length"], config["password_content"]["max_length"] + 1):
        print("Generating passwords with", pwd_length, "letters")
        print()

        start_time = time.time()

        current_pwd = ["□" for i in range(pwd_length)]
        pwds = {}
        loop_digit(current_pwd, pwd_length, pwds, outer=True)

        end_time = time.time()

        print(pwds)
        print("Created", len(pwds), "passwords in", end_time-start_time, "seconds")
        print("\n")

        all_pwds = all_pwds + pwds

    print(all_pwds)





if __name__ == '__main__':
    create()
