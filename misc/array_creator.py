import hashlib
import json
import multiprocessing
import time

from misc.config import config

possibleLetters = "".join([config["password_character_types"][name]
                           for name in config["password_content"]["character_types"]])



def mapped_loop_digit(args):
    loop_digit(*args, is_pool=True)


def loop_digit(current_str, place, hashes, is_outer=False, is_pool=False):
    if place == config["password_creation"]["length_for_new_process"]:
        pool_items = list()
        """with multiprocessing.Pool(config["password_creation"]["processes"]) as pool:
            pool.map(mapped_loop_digit, [(current_str, place - 1, hashes) for i in range(91)])
            pool.join()"""



    for letter in possibleLetters:
        current_str[place] = letter


        if place == 0:
            string = "".join(_letter for _letter in current_str)
            print(string)
            time.sleep(0.5)
            hashes[hashlib.md5(string.encode()).hexdigest()] = string

        elif place == config["password_creation"]["length_for_new_process"]:
            pool_items.append((current_str, place - 1))

        else:
            loop_digit(current_str, place - 1, hashes)



        if is_outer and config["development"]["minor_logging"]:
            print("Outer letter maker at", possibleLetters.index(letter)+1, "in", len(possibleLetters))



    if place == config["password_creation"]["length_for_new_process"]:
        args = list()
        for item_args in pool_items:
            args.append((item_args[0], item_args[1], hashes))

        with multiprocessing.Pool(processes=10) as pool:
            pool.map(mapped_loop_digit, args)
            pool.close()
            pool.join()




def create():
    total_start_time = time.time()
    print("Possible Letters:", possibleLetters)
    print("\n")

    all_hashes = {}
    last_len = 0

    for pwd_length in range(config["password_content"]["min_length"], config["password_content"]["max_length"] + 1):
        print("Generating passwords with", pwd_length, "letters")

        start_time = time.time()

        current_string = ["□" for _ in range(pwd_length)]
        loop_digit(current_string, pwd_length - 1, all_hashes, is_outer=True)

        end_time = time.time()

        print("Created", len(all_hashes)-last_len, "passwords in", end_time-start_time, "seconds")
        print("\n")

        last_len = len(all_hashes)

    with open('md5_hashes_to_hashes.json', 'w') as outfile:
        start_time = time.time()
        json.dump(all_hashes, outfile, indent=4)
        end_time = time.time()

        print("Saved", len(all_hashes), "passwords in", end_time - start_time, "seconds")
        print("\n")

    total_end_time = time.time()

    print("Generated", len(all_hashes), "passwords of", config["password_content"]["min_length"], "to",
          config["password_content"]["max_length"], "length with the characters '" + str(possibleLetters) + "' in",
          total_end_time-total_start_time, "seconds")





if __name__ == '__main__':
    import os
    os.chdir(os.path.split(os.path.dirname(globals()["__file__"]))[0])

    create()
