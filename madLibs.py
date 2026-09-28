import os

text = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

os.makedirs("libsMad", exist_ok=True)

toDisplay = open("libsMad/org_statement.txt", "w+")  # w+ or read + write

toReplace = open("libsMad/rep_statement.txt", "w+")

toDisplay.write(text)
toDisplay.seek(0)

print(toDisplay.read())


# get the tags separated from the main text

words = text.split()
tags = []

for word in words:
    word = word.strip(".,!?;:")  # remove unwanted symbol in tags
    if word.isupper() and len(word) > 2 and word not in tags:
        tags.append(word)
print(tags)

# tags = ["ADJECTIVE", "NOUN", "VERB"]

for tag in tags:

    if tag in text:
        usr_input = input(f"Enter an {tag}: ")
        text = text.replace(tag, usr_input)
        # for now use simple logic to replace all occurrences
        # later, logic for different inputs for repeated placeholders will be added

toReplace.write(text)
toReplace.seek(0)

print("\n———————————————————\n", "The file is now replaced:", toReplace.read())

toReplace.close()
toDisplay.close()
