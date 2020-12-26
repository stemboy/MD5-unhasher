import hashlib
import json
import multiprocessing
import time
import os

from kivy import Logger

from misc.config import config
from misc.functions import log, getUsrDataDir

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


def loop_digit(current_str, place, string_dataset, hash_dataset, encrypt_func, print_func, no_save,
               length_for_new_process, save_mode, is_outer=False, is_pool_outer=False,
               parent_character=None):
    if place == length_for_new_process:
        pool = multiprocessing.Pool(processes=config.getint("string_creation", "processes"))
        print_func("New pool created")
        print_func()

    for character in possibleCharacters:
        current_str[place] = character

        if is_outer and config.getboolean("development", "outer_logging"):
            print_func("Outer dataset maker | Progress = {:02d}".format(possibleCharacters.index(character) + 1),
                       "out of",
                       len(possibleCharacters))

        elif is_pool_outer and config.getboolean("development", "pool_loop_outer_logging"):
            print_func("Outest in pool loop dataset maker | Process = {:02d}".format(
                multiprocessing.current_process()._identity[0]),
                "| Parent Progress = {:02d}".format(possibleCharacters.index(parent_character) + 1), "out of",
                "| Parent character = ", str(parent_character),
                "| Progress = {:02d}".format(possibleCharacters.index(character) + 1), "out of",
                len(possibleCharacters),
                "| Character = ", str(character), "| Current string =", current_str)

        if place == 0:
            string = "".join(_character for _character in current_str)
            hash_dataset.append(encrypt_func(string.encode()).hexdigest())
            string_dataset.append(string)

            if save_mode != "one_file" and save_mode != "mass_mini_file":
                if save_mode == "mass_file":
                    pass

                elif save_mode == "folder":
                    pass

                else:
                    Logger.critical("Dataset Creator: " + str(save_mode) + " is not a valid save mode")

        elif place == length_for_new_process:

            pool.apply_async(loop_digit,
                             args=(current_str.copy(), place - 1, string_dataset, hash_dataset, encrypt_func,
                                   print_func, no_save, length_for_new_process, save_mode),
                             kwds={"is_pool_outer": True, "parent_character": character})

        else:
            loop_digit(current_str, place - 1, string_dataset, hash_dataset, encrypt_func, print_func, no_save,
                       length_for_new_process, save_mode)

    if place == length_for_new_process:
        print_func()
        print_func("Waiting for pool to finish")
        print_func()
        pool.close()
        pool.join()


def create(no_save=False):
    print_func = log

    total_start_time = time.time()
    print_func("Possible characters:", possibleCharacters)
    print_func("\n")

    last_len = 0

    manager = multiprocessing.Manager()
    string_dataset = manager.list("")
    hash_dataset = manager.list("")

    if config.get("encryption", "type") == "md5":
        encrypt_func = hashlib.md5
    elif config.get("encryption", "type") == "sha1":
        encrypt_func = hashlib.sha1
    elif config.get("encryption", "type") == "sha3-256":
        encrypt_func = hashlib.sha3_256
    else:
        raise Exception(config.get("encryption", "type") + " is not a valid encryption type (md5, sha1, sha3-256)")

    print_func("Encrypting with", config.get("encryption", "type"), "using the func", encrypt_func)

    for string_length in range(config.getint("string_content", "min_length"),
                               config.getint("string_content", "max_length") + 1):
        print_func("Generating strings with", string_length, "characters")

        start_time = time.time()

        current_string = ["□" for _ in range(string_length)]
        loop_digit(current_string, string_length - 1, string_dataset, hash_dataset, encrypt_func, print_func, no_save,
                   config.getint("string_creation", "length_for_new_process"),
                   config.get("string_creation", "save_mode"), is_outer=True)

        end_time = time.time()

        print_func("Created", len(hash_dataset) - last_len, "strings and hashes in", end_time - start_time, "seconds")
        print_func("\n")

        last_len = len(hash_dataset)

    if not no_save and config.get("string_creation", "save_mode") == "one_file":
        if not os.path.exists(os.path.join(getUsrDataDir(), "encryption_datasets")):
            os.mkdir(os.path.join(getUsrDataDir(), "encryption_datasets"))
            print_func("encryption_datasets folder does not exist so was created")

        name = config.get("encryption", "type") + "_" + possibleCharacters + "_" + \
               config.get("string_content", "min_length") + "_to_" + \
               config.get("string_content", "max_length") + '.hash_to_string_dataset.json'
        path = os.path.join(getUsrDataDir(), "encryption_datasets", name)

        with open(path, 'w') as outfile:
            start_time = time.time()
            all_hash_dataset_and_arrays = dict(zip(hash_dataset, string_dataset))
            json.dump(all_hash_dataset_and_arrays, outfile, indent=4)
            end_time = time.time()

            print_func("Saved", len(all_hash_dataset_and_arrays), "strings in", end_time - start_time, "seconds")
            print_func("\n")

        total_end_time = time.time()

    print_func("Generated and saved (unless no_save was true)", len(hash_dataset), "hashes and strings, of",
               config["string_content"]["min_length"], "to",
               config.getint("string_content", "max_length"),
               "in length, with the characters '" + str(possibleCharacters) + "' in",
               total_end_time - total_start_time, "seconds")

    if not no_save:
        print_func("The dataset's file(s) is (are) at", path)


if __name__ == '__main__':
    os.chdir(os.path.split(os.path.dirname(globals()["__file__"]))[0])

    create()
