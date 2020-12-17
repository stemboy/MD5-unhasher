import hashlib
import json
import time
from multiprocessing import Process

from config import config

possibleLetters = "".join([config["password_character_types"][name]
                           for name in config["password_content"]["character_types"]])


def loop_digit(current_str, place, pws, outer=False):
    processes = list()

    for letter in possibleLetters:
        current_str[place - 1] = letter

        if place == 1:
            pw = "".join(_letter for _letter in current_str)
            pws[hashlib.md5(pw.encode()).hexdigest()] = pw

        else:
            if place == config["password_creation"]["length_for_new_process"] + 1:

                if possibleLetters.index(letter) == len(possibleLetters)-1:
                    p = Process(target=loop_digit, args=(current_str, place - 1, pws), kwargs={"outer": True})
                    p.start()

                else:
                    p = Process(target=loop_digit, args=(current_str, place - 1, pws))
                    p.start()

                processes.append(p)


            else:
                loop_digit(current_str, place - 1, pws)

        if outer and config["development"]["minor_logging"]:
            print("Outer letter maker at", possibleLetters.index(letter)+1, "in", len(possibleLetters))

    for p in processes:
        p.join()



def create():
    total_start_time = time.time()
    print("Possible Letters:", possibleLetters)
    print("\n")

    all_pws = {}

    for pwd_length in range(config["password_content"]["min_length"], config["password_content"]["max_length"] + 1):
        print("Generating passwords with", pwd_length, "letters")

        start_time = time.time()

        current_pwd = ["□" for _ in range(pwd_length)]
        pws = {}
        loop_digit(current_pwd, pwd_length, pws, outer=True)

        end_time = time.time()

        print("Created", len(pws), "passwords in", end_time-start_time, "seconds")
        print("\n")

        all_pws.update(pws)

    with open('MD5_hashes_to_pws.json', 'w') as outfile:
        start_time = time.time()
        json.dump(all_pws, outfile, indent=4)
        end_time = time.time()

        print("Saved", len(all_pws), "passwords in", end_time - start_time, "seconds")
        print("\n")

    total_end_time = time.time()

    print("Generated", len(all_pws), "passwords of", config["password_content"]["min_length"], "to",
          config["password_content"]["max_length"], "length with the characters '" + str(possibleLetters) + "' in",
          total_end_time-total_start_time, "seconds")





if __name__ == '__main__':
    create()
