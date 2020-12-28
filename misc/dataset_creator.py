import hashlib
import json
import multiprocessing
import shutil
import time
import os

from kivy import Logger

from misc.config import config
from misc.functions import log, getUsrDataDir, log_warning
from misc.multiprocessingPoolWithExceptions import Pool

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
               length_for_new_process, save_mode, save_length, save_path, is_outer=False, is_pool_outer=False,
               parent_character=None):
    if is_pool_outer:
        pass

    if not no_save and save_mode == "small_length" and place == save_length:
        string_dataset = string_dataset.__deepcopy__({})
        hash_dataset = hash_dataset.__deepcopy__({})

    if place == length_for_new_process:
        pool = Pool(processes=config.getint("string_creation", "processes"))
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
                len(possibleCharacters),
                "| Parent character = ", str(parent_character),
                "| Progress = {:02d}".format(possibleCharacters.index(character) + 1), "out of",
                len(possibleCharacters),
                "| Character = ", str(character), "| Current string =", current_str)

        if place == 0:
            string = "".join(_character for _character in current_str)
            hash_dataset.append(encrypt_func(string.encode()).hexdigest())
            string_dataset.append(string)

            if save_mode != "one_file" and save_mode != "total_length":
                if save_mode == "mass_file":
                    pass

                elif save_mode == "folder":
                    pass

                elif not save_mode == "small_length":
                    Logger.critical("Dataset Creator: " + str(save_mode) + " is not a valid save mode")

        elif place == length_for_new_process:
            pool.apply_async(loop_digit,
                             args=(current_str.copy(), place - 1, string_dataset, hash_dataset, encrypt_func,
                                   print_func, no_save, length_for_new_process, save_mode, save_length, save_path),
                             kwds={"is_pool_outer": True, "parent_character": character})

        else:
            loop_digit(current_str, place - 1, string_dataset, hash_dataset, encrypt_func, print_func, no_save,
                       length_for_new_process, save_mode, save_length, save_path)

    if place == length_for_new_process:
        print_func()
        print_func("Waiting for pool to finish")
        print_func()
        pool.close()
        pool.join()

    if not no_save and save_mode == "small_length" and place == save_length:
        stuff = current_str[place + 1:]

        if len(stuff) == 0:
            stuff.append("IDKplaceIs " + str(place + 1))

        with open(os.path.join(save_path, "".join(stuff) + ".json"), 'w') as outfile:
            start_time = time.time()
            all_hash_dataset_and_arrays = dict(zip(hash_dataset, string_dataset))
            json.dump(all_hash_dataset_and_arrays, outfile, indent=4)
            outfile.close()
            end_time = time.time()

            print_func("")
            print_func("Saved", len(all_hash_dataset_and_arrays), "strings in", end_time - start_time, "seconds")
            print_func("")


def create(no_save=False):
    print_func = log
    print_func_warning = log_warning

    name = config.get("encryption", "type") + "_" + possibleCharacters + "_" + \
           config.get("string_content", "min_length") + "_to_" + \
           config.get("string_content", "max_length")

    if not no_save:
        if not os.path.exists(os.path.join(getUsrDataDir(), "encryption_datasets")):
            os.mkdir(os.path.join(getUsrDataDir(), "encryption_datasets"))
            print_func("encryption_datasets folder does not exist so was created")

        folder_path = os.path.join(getUsrDataDir(), "encryption_datasets", name)
        info_path = os.path.join(folder_path, "info.json")

        if os.path.exists(folder_path):
            print_func_warning(name, "already exists, removing directory")
            shutil.rmtree(folder_path)

        os.mkdir(folder_path)
        print_func("Created a new dataset folder")

        if config.get("string_creation", "save_mode") == "one_file":
            dataset_path = os.path.join(folder_path, "dataset.json")

        else:
            dataset_path = os.path.join(folder_path, "dataset")
            os.mkdir(dataset_path)
            print_func("Created a new dataset folder")

        info = {
            "encryption": config.get("encryption", "type"),
            "min_length": config.get("string_content", "min_length"),
            "max_length": config.get("string_content", "max_length"),
            "characters": possibleCharacters,
            "current_length": 0
        }

        with open(info_path, "w") as outfile:
            json.dump(info, outfile, indent=4)
            outfile.close()

        print_func("Created info folder")
        print_func("\n")

    total_start_time = time.time()
    print_func("Possible characters:", possibleCharacters)
    print_func("\n")

    last_len = 0

    manager = multiprocessing.Manager()
    string_dataset = manager.list([])
    hash_dataset = manager.list([])

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

        revert_to_total_length_because_small_length_is_enabled_and_string_length_is_smaller_than_save_length = True if \
            not no_save and config.get("string_creation", "save_mode") == "small_length" and string_length < \
            config.getint("string_creation", "save_length") else False

        current_string = ["□" for _ in range(string_length)]
        loop_digit(current_string, string_length - 1, string_dataset, hash_dataset, encrypt_func, print_func, no_save,
                   config.getint("string_creation", "length_for_new_process"),
                   config.get("string_creation", "save_mode"), config.getint("string_creation", "save_length") - 1,
                   dataset_path, is_outer=True)

        end_time = time.time()

        print_func("Created", len(hash_dataset) - last_len, "strings and hashes in", end_time - start_time, "seconds")
        print_func("\n")

        last_len = len(hash_dataset)

        if (not no_save and config.get("string_creation", "save_mode") == "total_length") or \
                revert_to_total_length_because_small_length_is_enabled_and_string_length_is_smaller_than_save_length:
            path = os.path.join(dataset_path, str("IDKplaceIs " + str(string_length)) + ".json") if \
                revert_to_total_length_because_small_length_is_enabled_and_string_length_is_smaller_than_save_length \
                else os.path.join(dataset_path, str(string_length) + ".json")

            if revert_to_total_length_because_small_length_is_enabled_and_string_length_is_smaller_than_save_length:
                print_func("Reverted to total_length because small_length is smaller than save_length")

            with open(path, 'w') as outfile:
                start_time = time.time()
                all_hash_dataset_and_arrays = dict(zip(hash_dataset, string_dataset))
                json.dump(all_hash_dataset_and_arrays, outfile, indent=4)
                outfile.close()
                end_time = time.time()

                print_func("\n")
                print_func("Saved", len(all_hash_dataset_and_arrays), "strings in", end_time - start_time, "seconds")
                print_func("\n")

            string_dataset[:] = []
            hash_dataset[:] = []

        if not no_save:
            info["current_length"] = string_length

            with open(info_path, "w") as outfile:
                json.dump(info, outfile, indent=4)
                outfile.close()

    if not no_save and config.get("string_creation", "save_mode") == "one_file":
        with open(os.path.join(dataset_path), 'w') as outfile:
            start_time = time.time()
            all_hash_dataset_and_arrays = dict(zip(hash_dataset, string_dataset))
            json.dump(all_hash_dataset_and_arrays, outfile, indent=4)
            outfile.close()
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
        print_func("The dataset's file(s) is (are) at", dataset_path)


if __name__ == '__main__':
    os.chdir(os.path.split(os.path.dirname(globals()["__file__"]))[0])

    create()
