import json

config = json.load(open("config.json", "r"))

possibleLetters = "".join([config["password_character_types"][name]
                           for name in config["password_content"]["character_types"]])
print("Possible Letters:", possibleLetters)
print("\n")

for pwd_length in range(config["password_content"]["min_length"], config["password_content"]["max_length"] + 1):
    print("Generating password with", pwd_length, "letters")

    current_psw = "".join([possibleLetters[0] for i in range(pwd_length)])
    print("Password starting at ", current_psw)



    print()
