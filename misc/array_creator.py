import hashlib
import json
import multiprocessing
import time
import os

import appdirs

from misc.config import config

possibleCharacters = ""

if config.getboolean("character_types", "lowercase"):
    possibleCharacters = possibleCharacters + str(config.get("string_character_types", "lowercase"))
if config.getboolean("character_types", "uppercase"):
    possibleCharacters = possibleCharacters + str(config.get("string_character_types", "uppercase"))
if config.getboolean("character_types", "numbers"):
    possibleCharacters = possibleCharacters + str(config.get("string_character_types", "numbers"))
if config.getboolean("character_types", "special"):
    possibleCharacters = possibleCharacters + str(config.get("string_character_types", "special"))
if config.getboolean("character_types", "space"):
    possibleCharacters = possibleCharacters + str(config.get("string_character_types", "space"))


def loop_digit(current_str, place, strings, hashes, encrypt_func, is_outer=False, is_pool_outer=False,
               parent_character=None):
    if place == config.getint("string_creation", "length_for_new_process"):
        pool = multiprocessing.Pool(processes=config.getint("string_creation", "processes"))
        print("New pool created")
        print()

    for character in possibleCharacters:
        current_str[place] = character

        if is_outer and config.getboolean("development", "outer_logging"):
            print("Outer character maker | Progress = {:02d}".format(possibleCharacters.index(character) + 1), "out of",
                  len(possibleCharacters))

        elif is_pool_outer and config.getboolean("development", "pool_loop_outer_logging"):
            print("Outest in pool loop character maker | Process = {:02d}".format(
                multiprocessing.current_process()._identity[0]),
                "| Parent Progress = {:02d}".format(possibleCharacters.index(parent_character) + 1), "out of",
                "| Parent character = ", str(parent_character),
                "| Progress = {:02d}".format(possibleCharacters.index(character) + 1), "out of",
                len(possibleCharacters),
                "| Character = ", str(character), "| Current string =", current_str)

        if place == 0:
            string = "".join(_character for _character in current_str)
            hashes.append(encrypt_func(string.encode()).hexdigest())
            strings.append(string)

        elif place == config.getint("string_creation", "length_for_new_process"):

            pool.apply_async(loop_digit, args=(current_str.copy(), place - 1, strings, hashes, encrypt_func),
                             kwds={"is_pool_outer": True, "parent_character": character})

        else:
            loop_digit(current_str, place - 1, strings, hashes, encrypt_func)

    if place == config.getint("string_creation", "length_for_new_process"):
        print()
        print("Waiting for pool to finish")
        print()
        pool.close()
        pool.join()


def create():
    total_start_time = time.time()
    print("Possible characters:", possibleCharacters)
    print("\n")

    last_len = 0

    manager = multiprocessing.Manager()
    all_strings = manager.list("")
    all_hashes = manager.list("")

    if config.get("encryption", "type") == "md5":
        encrypt_func = hashlib.md5
    elif config.get("encryption", "type") == "sha1":
        encrypt_func = hashlib.sha1
    elif config.get("encryption", "type") == "sha3-256":
        encrypt_func = hashlib.sha3_256
    else:
        raise Exception(config.get("encryption", "type") + " is not a valid encryption type (md5, sha1, sha3-256)")

    print("Encrypting with", config.get("encryption", "type"), "using the func", encrypt_func)

    for string_length in range(config.getint("string_content", "min_length"),
                               config.getint("string_content", "max_length") + 1):
        print("Generating strings with", string_length, "characters")

        start_time = time.time()

        current_string = ["□" for _ in range(string_length)]
        loop_digit(current_string, string_length - 1, all_strings, all_hashes, encrypt_func, is_outer=True)

        end_time = time.time()

        print("Created", len(all_hashes) - last_len, "strings in", end_time - start_time, "seconds")
        print("\n")

        last_len = len(all_hashes)

    usrDataDir = os.path.join(appdirs.user_data_dir(), "md5-unhasher")

    if not os.path.exists(os.path.join(usrDataDir, "encryptions")):
        os.mkdir(os.path.join(usrDataDir, "encryptions"))
        print("Encryptions folder does not exist so was created")

    name = config.get("encryption", "type") + "_" + possibleCharacters + "_" + \
           config.get("string_content", "min_length") + " to " + \
           config.get("string_content", "max_length") + '.hashes_to_strings.json'
    path = os.path.join(usrDataDir, "encryptions", name)

    with open(path, 'w') as outfile:
        start_time = time.time()
        all_hashes_and_arrays = dict(zip(all_hashes, all_strings))
        json.dump(all_hashes_and_arrays, outfile, indent=4)
        end_time = time.time()

        print("Saved", len(all_hashes_and_arrays), "strings in", end_time - start_time, "seconds")
        print("\n")

    total_end_time = time.time()

    print("Generated and saved", len(all_hashes), "strings of", config["string_content"]["min_length"], "to",
          config.getint("string_content", "max_length"),
          "length with the characters '" + str(possibleCharacters) + "' in",
          total_end_time - total_start_time, "seconds")
    print("The file is at", path)


if __name__ == '__main__':
    import os

    os.chdir(os.path.split(os.path.dirname(globals()["__file__"]))[0])

    create()
