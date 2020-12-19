import hashlib
import json
import multiprocessing
import time

from misc.config import config

possibleLetters = "".join([config["password_character_types"][name]
                           for name in config["password_content"]["character_types"]])





def mapped_loop_digit(args):
    loop_digit(*args, is_pool=True)


def loop_digit(current_str, place, strings, hashes, is_outer=False, is_pool=False):
    if place == config["password_creation"]["length_for_new_process"]:
        current_strings = list()



    for letter in possibleLetters:
        current_str[place] = letter

        if is_outer and config["development"]["minor_logging"]:
            print("Outer letter maker at", possibleLetters.index(letter)+1, "in", len(possibleLetters))

        elif is_pool and config["development"]["pool_minor_logging"]:
            print("Outest in pool letter maker for process", multiprocessing.current_process()._identity, "at", possibleLetters.index(letter)+1, "in", len(possibleLetters))


        if place == 0:
            #print(current_str)
            string = "".join(_letter for _letter in current_str)
            time.sleep(0.5)
            hashes.append(hashlib.md5(string.encode()).hexdigest())
            strings.append(string)
            #hashes[hashlib.md5(string.encode()).hexdigest()] = string

        elif place == config["password_creation"]["length_for_new_process"]:
            current_strings.append(current_str.copy())

        else:
            loop_digit(current_str, place - 1, strings, hashes)



    if place == config["password_creation"]["length_for_new_process"]:
        args = list()
        print("Starting a new pool")
        for string in current_strings:
            args.append([string, place - 1, strings, hashes])

        with multiprocessing.Pool(processes=config["password_creation"]["processes"]) as pool:
            pool.map(mapped_loop_digit, args)
            print(pool._pool)
            pool.close()
            pool.join()




def create():
    total_start_time = time.time()
    print("Possible Letters:", possibleLetters)
    print("\n")

    last_len = 0

    manager = multiprocessing.Manager()
    all_strings = manager.list("")
    all_hashes = manager.list("")

    for pwd_length in range(config["password_content"]["min_length"], config["password_content"]["max_length"] + 1):
        print("Generating passwords with", pwd_length, "letters")

        start_time = time.time()

        current_string = ["□" for _ in range(pwd_length)]
        loop_digit(current_string, pwd_length - 1, all_strings, all_hashes, is_outer=True)

        end_time = time.time()

        print("Created", len(all_hashes)-last_len, "passwords in", end_time-start_time, "seconds")
        print("\n")

        last_len = len(all_hashes)

    with open('md5_hashes_to_hashes.json', 'w') as outfile:
        start_time = time.time()
        all_hashes_and_arrays = dict(zip(all_strings, all_hashes))
        all_hashes_and_arrays = {k: v for k, v in sorted(all_hashes_and_arrays.items(), key=lambda item: item[1])}
        print(all_hashes_and_arrays)
        print(type(all_hashes_and_arrays))
        json.dump(all_hashes_and_arrays, outfile, indent=4)
        end_time = time.time()

        print("Saved", len(all_hashes_and_arrays), "passwords in", end_time - start_time, "seconds")
        print("\n")

    total_end_time = time.time()

    print("Generated", len(all_hashes), "passwords of", config["password_content"]["min_length"], "to",
          config["password_content"]["max_length"], "length with the characters '" + str(possibleLetters) + "' in",
          total_end_time-total_start_time, "seconds")





if __name__ == '__main__':
    import os
    os.chdir(os.path.split(os.path.dirname(globals()["__file__"]))[0])

    create()
