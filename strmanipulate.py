spam = "this is amulya's ratna"


print(spam)


print("Hello there!\nHow are you?\nI'm doing fine.")
print(r"this is raw string\'s")  # r at start print the string as it is

print(""" this is 

a 

multiline comment
and it wil print it as it is

""")

"""
multiline can also be used

like this

"""


hello = "asbuhre"

print(hello[::-1])  # reversed str


teststr = "anfiubd ninfUQoq41y02"

checkalp = "Title This Is"

print(teststr.isdecimal())
print(checkalp.istitle())

"""

isalpha() returns True if the string consists only of letters and is not blank.

• isalnum() returns True if the string consists only of letters and numbers
and is not blank.

• isdecimal() returns True if the string consists only of numeric characters
and is not blank.

• isspace() returns True if the string consists only of spaces, tabs, and new-
lines and is not blank.

• istitle() returns True if the string consists only of words that begin with
an uppercase letter followed by only lowercase letters.

"""


# split and join


joist = "T".join(["cats", "rats", "bats"])


print(joist)

splist = "this is splitting the string".split()
print(splist)  # this will by default split by space, but we can specify

spest = "catsTratsTbats".split("T")
print(spest)


nspam = """Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob"""

print(nspam.split("\n"))

"""
rjust(), ljust(), center() -> these all are for justifying the text

strip(), lstrip(), rstrip() -> removes whitespaces


"""
print("hello".center(20))
print("             jello dfnffcbvzxca    ".strip())

letspec = "ASDseeASDhowASDonlyASDspecifiedASDwordASDisASDremoved"

print(letspec.strip("ASD"))
""" this will not work to remove the ASD from the text, as strip only works at the start and end only


in short do not use it like that, instead use replace() if want to remove specific word
"""

print("output:", letspec.replace("ASD", " "))  # remove the asd and add spaces

#  paste in clipboard -> pyperclip

import pyperclip

pyperclip.copy("this from pyper")
