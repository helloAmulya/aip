# ATBS Chapters 1–9 — Reference Sheet

Built from _Automate the Boring Stuff with Python_ (1st-edition numbering: Ch 7 Regex, Ch 8 Reading/Writing Files, Ch 9 Organizing Files) and from the scripts in your `aip` repo.

---

## 1. Printing and input (Ch 1)

| You want                     | Write                                 | Result                                |
| ---------------------------- | ------------------------------------- | ------------------------------------- |
| Change the separator         | `print("a", "b", sep="-")`            | `a-b`                                 |
| Stay on the same line        | `print("loading", end="...")`         | next print continues on the same line |
| Insert variables             | `print(f"{name} is {age}")`           | f-string, use this by default         |
| Old style (the book uses it) | `print("%s is %d" % (name, age))`     | same output                           |
| `.format` style              | `print("{} is {}".format(name, age))` | same output                           |
| See hidden spaces/quotes     | `print(repr(s))` or `print(f"{s!r}")` | `'  hi  '`                            |

```python
name, score = "Asha", 92.456
print("a", "b", sep="-")                 # a-b
print("no newline", end=" | ")
print("next")                            # no newline | next
print(f"{name:<10}|{score:>8.1f}|")      # Asha      |    92.5|   (< left, > right, .1f = 1 decimal)
print(f"{1234567:,}")                    # 1,234,567
print(f"{name:^10}|")                    # centered
print(repr("  hi  "))                    # '  hi  '
```

Core functions: `input()` always returns a **string**; `int()`, `float()`, `str()` convert; `len()` counts items or characters.

```python
age = int("27") + 1        # convert before doing maths
print(age, type(age))      # 28 <class 'int'>
print("5" + "3", int("5") + int("3"))   # 53 8   (string join vs addition)
```

---

## 2. Flow control (Ch 2)

| Piece                      | Syntax                                              |
| -------------------------- | --------------------------------------------------- |
| Comparison                 | `==  !=  <  >  <=  >=` (`=` assigns, `==` compares) |
| Boolean                    | `and  or  not`                                      |
| Branch                     | `if … :` / `elif … :` / `else:`                     |
| Loop while true            | `while cond:`                                       |
| Loop N times               | `for i in range(5):` → 0..4                         |
| Range with start/stop/step | `range(2, 10, 2)` → 2,4,6,8                         |
| Leave the loop             | `break`                                             |
| Skip to next round         | `continue`                                          |
| Quit program               | `import sys; sys.exit()`                            |

```python
for i in range(10, 0, -1):          # countdown
    if i % 2 == 0:
        continue                    # skip even numbers
    print(i)
    if i == 3:
        break                       # stop at 3
```

---

## 3. Functions and errors (Ch 3)

```python
def greet(name, greeting="Hello"):      # default argument
    return f"{greeting}, {name}!"

print(greet("Asha"))
print(greet("Asha", greeting="Hi"))     # keyword argument

count = 0
def bump():
    global count                        # without this, count would be a new local variable
    count += 1

def safe_int(text):
    try:
        return int(text)
    except ValueError:                  # catch the specific error, not everything
        return None

bump()
print(count, safe_int("12"), safe_int("abc"))    # 1 12 None
```

Rules to remember: a function with no `return` gives back `None`. Local variables disappear when the function ends. Code in the global scope cannot see a function's locals.

---

## 4. Lists and tuples (Ch 4)

| Task                            | Code                                                  |
| ------------------------------- | ----------------------------------------------------- |
| Index / last item               | `a[0]`, `a[-1]`                                       |
| Slice (end is excluded)         | `a[1:3]`, `a[:2]`, `a[::-1]` (reversed)               |
| Add to end / insert             | `a.append(x)`, `a.insert(i, x)`                       |
| Remove by value / by index      | `a.remove(x)`, `del a[i]`, `a.pop()` **(bonus: pop)** |
| Position of a value             | `a.index(x)`                                          |
| Sort in place / new sorted list | `a.sort()`, `sorted(a)` (add `reverse=True`)          |
| Membership                      | `x in a`, `x not in a`                                |
| Join lists                      | `a + b`, repeat `a * 3`                               |
| Convert                         | `list("abc")`, `tuple(a)`                             |
| Unpack                          | `x, y, z = a`                                         |

```python
nums = [5, 3, 8, 1]
nums.sort(reverse=True)
print(nums)                     # [8, 5, 3, 1]
point = (3, 4)                  # tuple: cannot be changed
x, y = point
for i, n in enumerate(nums):    # (bonus) index + value together
    print(i, n)
```

**Mutable vs immutable.** Lists and dicts can change in place. Strings, tuples and numbers cannot, because operations on them make new objects.

```python
import copy

a = [1, 2, [3, 4]]
b = a                       # same list, not a copy
b.append(9)
print(a)                    # [1, 2, [3, 4], 9]  -> a changed too

c = a.copy()                # shallow copy (a[:] does the same)
d = copy.deepcopy(a)        # deep copy, safe for nested lists
a[2].append(5)
print(c[2], d[2])           # [3, 4, 5] [3, 4]   -> shallow copy still shares the inner list
```

---

## 5. Dictionaries (Ch 5)

| Task                     | Code                                                   |
| ------------------------ | ------------------------------------------------------ |
| Read safely              | `d.get(key, default)`                                  |
| Check a key              | `key in d`                                             |
| Loop                     | `for k, v in d.items():` (also `.keys()`, `.values()`) |
| Set only if missing      | `d.setdefault(key, default)`                           |
| Delete                   | `del d[key]`, `d.pop(key)`                             |
| Pretty print nested data | `pprint.pprint(d)` / `pprint.pformat(d)`               |

```python
import pprint

words = "the cat and the hat and the bat".split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1            # the counting pattern

top = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:3]   # (bonus) sort by value
print(top)                                       # [('the', 3), ('and', 2), ('cat', 1)]

groups = {}
for w in words:
    groups.setdefault(w[0], []).append(w)        # group words by first letter
pprint.pprint(groups)

contacts = [{"name": "Ravi", "tags": ["hospital"]}, {"name": "Priya", "tags": []}]
for c in contacts:                               # to search a list of dicts you must LOOP
    if c["name"].lower() == "ravi":
        print("found", c)
```

---

## 6. Strings (Ch 6)

| Method                                                        | What it does        | Example → result                     |
| ------------------------------------------------------------- | ------------------- | ------------------------------------ |
| `upper()` `lower()`                                           | change case         | `"Hi".lower()` → `'hi'`              |
| `isupper()` `islower()`                                       | check case          |                                      |
| `isalpha()` `isalnum()` `isdecimal()` `isspace()` `istitle()` | check content       | `"abc1".isalpha()` → `False`         |
| `startswith(x)` `endswith(x)`                                 | check the ends      | `"a.pdf".endswith(".pdf")` → `True`  |
| `split()` / `split(",")`                                      | string → list       | `"a b  c".split()` → `['a','b','c']` |
| `"sep".join(list)`                                            | list → string       | `"-".join(["a","b"])` → `'a-b'`      |
| `strip()` `lstrip()` `rstrip()`                               | trim **edges only** | `"  hi ".strip()` → `'hi'`           |
| `replace(old, new)`                                           | swap text anywhere  | `"a,b".replace(",", "")` → `'ab'`    |
| `ljust(n)` `rjust(n)` `center(n)`                             | pad to width        | `"7".rjust(3)` → `'  7'`             |
| `find(x)` **(bonus)**                                         | position or -1      |                                      |
| slicing                                                       | `s[::-1]` reverses  |                                      |

```python
s = "  Patient  said   pain!!  "
clean = " ".join(s.lower().strip().replace("!", "").split())   # collapses inner spaces too
print(repr(clean))                    # 'patient said pain'

print("ASDfooASD".strip("ASD"))        # 'foo'  -> strip treats the argument as a SET of characters, edges only
print("ASDfooASDbar".replace("ASD", " "))   # ' foo bar'  -> replace for removing text in the middle

print("Hello\nWorld")                  # \n newline, \t tab, \\ backslash, \' quote
print(r"C:\new\table")                 # raw string: backslashes stay as typed
text = """multi
line"""                                # triple quotes keep line breaks
print(text.split("\n"))
```

Clipboard (third-party: `pip install pyperclip`):

```python
# skip-test  (needs a desktop clipboard)
import pyperclip
pyperclip.copy("hello")
print(pyperclip.paste())
```

Command-line arguments (used in your `pw.py`):

```python
# skip-test  (run it as:  python3 pw.py email)
import sys
if len(sys.argv) < 2:
    print("Usage: python3 pw.py [account]")
    sys.exit()
account = sys.argv[1]       # sys.argv[0] is the script name
```

On Mac/Linux, a first line `#! /usr/bin/env python3` plus `chmod +x pw.py` lets you run `./pw.py email`.

---

## 7. Regular expressions (Ch 7)

```python
import re

text = "Call 415-555-1234 or 415-555-9999. Mail asha@example.com"
phone = re.compile(r"\d{3}-\d{3}-\d{4}")
print(phone.search(text).group())       # first match -> 415-555-1234
print(phone.findall(text))              # all matches -> ['415-555-1234', '415-555-9999']
print(phone.sub("XXX-XXX-XXXX", text))  # replace matches
print(re.sub(r"\s+", " ", "too    many   spaces"))   # collapse any run of whitespace

m = re.search(r"(\d+)-(\d+)-(\d{4})", "due 7-4-2026")
print(m.group(1), m.group(2), m.group(3), m.groups())   # 7 4 2026 ('7', '4', '2026')
```

| Syntax                            | Meaning                                                                             |
| --------------------------------- | ----------------------------------------------------------------------------------- |
| `\d`, `\w`, `\s`                  | Digit / word character / whitespace (`\D`, `\W`, `\S` mean the opposite)            |
| `.`                               | Any character except newline                                                        |
| `*`, `+`, `?`                     | Zero or more / one or more / zero or one                                            |
| `{3}`, `{2,4}`                    | Exactly 3 / between 2 and 4                                                         |
| `[abc]`, `[^abc]`, `[a-z]`        | Any of / none of / character range                                                  |
| `^`, `$`                          | Start / end of string                                                               |
| `( )`                             | Capture group (numbered from 1; `group(0)` is the whole match)                      |
| `a\|b`                            | `a` or `b`                                                                          |
| `*?`, `+?`                        | Non-greedy matching (shortest match)                                                |
| `re.I`, `re.DOTALL`, `re.VERBOSE` | Ignore case / let `.` match newlines / allow comments and whitespace in the pattern |

Always write patterns as raw strings: `r"..."`. Your `renameDates.py` is a good real example: group 1 is the text before the date, groups 2/4/6 are month/day/year, group 8 is the text after.

---

## 8. Reading and writing files (Ch 8)

### Paths

| Task                       | Code                                                    |
| -------------------------- | ------------------------------------------------------- |
| Join parts safely          | `os.path.join("folder", "file.txt")`                    |
| Current folder / change it | `os.getcwd()`, `os.chdir(path)`                         |
| Absolute path              | `os.path.abspath("x")`                                  |
| Relative to a base         | `os.path.relpath(path, start)`                          |
| Folder part / file part    | `os.path.dirname(p)`, `os.path.basename(p)`             |
| Name and extension         | `os.path.splitext("report.pdf")` → `('report', '.pdf')` |
| Exists? file? folder?      | `os.path.exists(p)`, `isfile(p)`, `isdir(p)`            |
| Size in bytes              | `os.path.getsize(p)`                                    |
| List one folder            | `os.listdir(folder)` (names only)                       |
| Make folders (parents too) | `os.makedirs(path, exist_ok=True)`                      |

Relative paths such as `"../gclab"` depend on **where you run the script from**, not where the script lives. When something "can't be found", print `os.getcwd()` first.

### Opening files

| Mode            | Meaning                            |
| --------------- | ---------------------------------- |
| `"r"` (default) | read, file must exist              |
| `"w"`           | write, **erases** the old content  |
| `"a"`           | append to the end                  |
| `"w+"` / `"r+"` | read and write (`w+` erases first) |
| `"rb"` / `"wb"` | binary (images, zips)              |

```python
import os

os.makedirs("demo", exist_ok=True)
path = os.path.join("demo", "notes.txt")

with open(path, "w") as f:               # `with` closes the file for you, even if an error happens
    f.write("line one\n")                # write() does NOT add a newline; it returns the character count
    f.write("line two\n")

with open(path, "a") as f:               # append
    f.write("line three\n")

with open(path) as f:
    whole = f.read()                     # one big string
with open(path) as f:
    lines = f.readlines()                # list of lines, each still ending in \n
with open(path) as f:
    for line in f:                       # best for big files: one line at a time
        print(line.strip())

print(len(lines), repr(whole[:8]))       # 3 'line one'

f = open(path, "w+")                     # the open()/close() style from the book
f.write("abc")
f.seek(0)                                # jump back to the start before reading
print(f.read())                          # abc
f.close()
```

### Saving variables

```python
import shelve, pprint

with shelve.open("mydata") as db:        # a dict-like file on disk
    db["cats"] = ["Zophie", "Pooka"]
with shelve.open("mydata") as db:
    print(db["cats"], list(db.keys()))   # ['Zophie', 'Pooka'] ['cats']

cats = [{"name": "Zophie", "age": 4}]
with open("mycats.py", "w") as f:        # save a variable as Python source
    f.write("cats = " + pprint.pformat(cats) + "\n")
```

---

## 9. Organizing files (Ch 9)

### Copy, move, rename, delete

| Task                             | Code                                     | Watch out for                                                                                     |
| -------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Copy a file                      | `shutil.copy(src, dst)`                  | `dst` can be a folder or a full new filename; **same name in the folder is overwritten silently** |
| Copy a whole folder              | `shutil.copytree(src, new_dst)`          | `new_dst` must not exist yet                                                                      |
| Move a file or folder            | `shutil.move(src, dst)`                  | into an existing folder it keeps its name; to a full file path it **overwrites** that file        |
| Rename                           | `shutil.move(old, new)` (or `os.rename`) |                                                                                                   |
| Delete one file / empty folder   | `os.unlink(p)` / `os.rmdir(p)`           | permanent                                                                                         |
| Delete a folder and all contents | `shutil.rmtree(p)`                       | permanent, no undo                                                                                |
| Safe delete (recycle bin)        | `send2trash.send2trash(p)`               | `pip install send2trash`; use this one                                                            |

```python
import os, shutil

os.makedirs("lab/inbox", exist_ok=True)
with open("lab/a.txt", "w") as f:
    f.write("a")

shutil.copy("lab/a.txt", "lab/inbox")            # copy into a folder, keeps the name
shutil.copy("lab/a.txt", "lab/a_copy.txt")       # copy under a new name
shutil.copytree("lab/inbox", "lab/inbox_backup") # whole folder
shutil.move("lab/a_copy.txt", "lab/renamed.txt") # rename
print(sorted(os.listdir("lab")))                 # ['a.txt', 'inbox', 'inbox_backup', 'renamed.txt']

# dry-run habit: print what WOULD happen first, then switch the real call on
for name in os.listdir("lab"):
    print("would delete:" if name.endswith(".txt") else "keep:", name)
    # send2trash.send2trash(os.path.join("lab", name))     # enable only after checking the printout
```

### Walking a folder tree

```python
import os

for folder, subfolders, files in os.walk("."):       # visits the folder, then every subfolder, at every depth
    print("in:", folder)                              # folder is the path as a string
    for name in files:                               # files is a list of names (not paths)
        full = os.path.join(folder, name)            # build the real path yourself
        print("   ", full, os.path.getsize(full))

# prune a folder from the walk (your reviseZipfunc.py does this):
for folder, subfolders, files in os.walk("."):
    subfolders[:] = [d for d in subfolders if d != "__pycache__"]   # edit IN PLACE with [:] or the prune is ignored
```

### ZIP files

```python
import zipfile, os

os.makedirs("pack/sub", exist_ok=True)
for p in ["pack/a.txt", "pack/sub/b.txt"]:
    with open(p, "w") as f:
        f.write("data " * 100)

# create
with zipfile.ZipFile("pack.zip", "w", zipfile.ZIP_DEFLATED) as z:       # ZIP_DEFLATED = actually compress
    for folder, subs, files in os.walk("pack"):
        for name in files:
            full = os.path.join(folder, name)
            z.write(full, arcname=os.path.relpath(full, "pack"))        # arcname = the path stored INSIDE the zip

# inspect and extract
with zipfile.ZipFile("pack.zip") as z:
    print(z.namelist())                                  # ['a.txt', 'sub/b.txt']
    info = z.getinfo("a.txt")
    print(info.file_size, info.compress_size)            # original vs compressed bytes
    z.extractall("unpacked")                             # everything
    z.extract("a.txt", "just_one")                       # one file
```

Without `arcname`, `z.write(full)` stores the path exactly as you gave it. If `full` is an absolute path, the zip contains the whole `Users/<you>/...` chain. That is what the current `backupZipFile.py` does. Use `arcname=os.path.relpath(...)` for a clean archive.

### Quick lookup: "how do I…?"

| I want to…                           | Use                                                                 |
| ------------------------------------ | ------------------------------------------------------------------- |
| list everything inside a folder tree | `os.walk`                                                           |
| find all `.pdf` files (any case)     | `name.lower().endswith(".pdf")` inside an `os.walk` loop            |
| avoid overwriting when copying       | check `os.path.exists(dest)` first, then add `_1`, `_2` to the name |
| rename every file matching a pattern | `re.compile(...)` + `os.listdir` + `shutil.move`, print first       |
| back up a folder to a numbered zip   | your `backupZipFile.py` (loop until `os.path.exists` is False)      |
| make sure a folder exists            | `os.makedirs(path, exist_ok=True)`                                  |
| get the extension                    | `os.path.splitext(name)[1].lower()`                                 |
| count things by category             | the dict counting pattern (`d[k] = d.get(k, 0) + 1`)                |

**(bonus) `pathlib`** is the modern way to write the same path code, and the book's newer editions use it:

```python
from pathlib import Path

p = Path("sandbox") / "downloads" / "photo1.jpg"     # / joins paths
print(p.name, p.suffix, p.stem, p.parent)             # photo1.jpg .jpg photo1 sandbox/downloads
print(p.exists())                                     # False if you have not run the sandbox script
for pdf in Path(".").rglob("*.pdf"):                  # recursive search, replaces os.walk + endswith
    print(pdf)
```

---

## 10. Gotchas checklist

1. `input()` returns text. Convert with `int()` before maths.
2. `=` assigns, `==` compares.
3. `b = a` on a list makes **one** list with two names. Use `.copy()` or `copy.deepcopy()`.
4. `x in list_of_dicts` compares against the dicts themselves. Loop and compare `d["key"]` instead.
5. `strip("abc")` removes any of those characters from the **edges only**. Use `replace()` for the middle.
6. `.replace()` removes one exact piece of text. For "any number of dots", use `re.sub` (Ch 7).
7. `"." and ","` evaluates to `","`. `and` is not "both"; list the items instead.
8. `w` mode erases the file when you open it. `a` appends.
9. `write()` doesn't add `\n`. `print()` does.
10. `os.walk` gives names, not paths: always `os.path.join(folder, name)`.
11. `shutil.copy` into a folder silently overwrites a file with the same name, so two `notes.txt` files from different folders collide.
12. `shutil.move`, `rmtree` and `unlink` have no undo. Print first, then act, or use `send2trash`.
13. Relative paths depend on the folder you run from. Print `os.getcwd()` when a file "isn't found".
14. Compare to `None` with `is None`, not `== None`.
15. Use `with open(...)` so files always close.
