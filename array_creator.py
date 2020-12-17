import json

config = json.load(open("config.json", "r"))

possibleLetters = "".join([config["password_character_types"][name]
                           for name in config["password_content"]["character_types"]])
print(possibleLetters)


