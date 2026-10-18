# Practice Set — ATBS Ch 1–9 (heavier on Ch 8–9)

Built from what's actually in your `aip` repo. Chapters 8–9 got the most tasks because that's where you are now.
Part A drills the tiny functions you'll use every day. Part D reuses and improves your own scripts.

## Setup (2 minutes)

1. Put `make_sandbox.py` in your practice folder and run `python3 make_sandbox.py`. It builds a `sandbox/` folder full of messy files. Re-run it any time to reset everything.
2. Keep your answers in new files, e.g. `practice/warmups.py`, `practice/files_b.py`. Commit each finished one to `aip`.
3. **Every task that moves, renames or deletes something gets a dry-run first.** Print the plan, check it, then switch the real call on. The sandbox is disposable, but the habit isn't.
4. Look things up in `atbs_ch1-9_reference.md`, but try from memory first. If you're stuck for more than 10 minutes, paste your code and tell me which piece is the blocker.

**If you only have time for 8 tasks:** A3, A8, B1, B4, D2, D4, D7, D9.

---

## Part A — Tiny functions (Ch 1–6) · ~10 min each

Write each as a function in `warmups.py` and call it with the sample input.

| #   | Task                                                                                                                                                                                          | Expect                                                                                                                |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| A1  | `normalise_name(s)`: trim, collapse inner spaces, capitalise each word. Input `"  aMULYA   rAtna  sHARMA "`                                                                                   | `"Amulya Ratna Sharma"`                                                                                               |
| A2  | `ask_int(prompt, low, high)`: keep asking until the user types a whole number inside the range. Use `while` + `try/except`.                                                                   | typing `abc`, `99`, `5` with range 1–10 returns `5`                                                                   |
| A3  | `count_words(text)` returns a dict of counts. `top_n(counts, n)` returns the n biggest as `(word, count)` pairs. This finishes your word-counter. Input `"the cat and the hat and the bat"`.  | `top_n(..., 3)` → `[('the', 3), ('and', 2), ('cat', 1)]`                                                              |
| A4  | `group_by_first_letter(words)` using `setdefault`. Same word list as A3.                                                                                                                      | `{'t': ['the','the','the'], 'c': ['cat'], 'a': ['and','and'], 'h': ['hat'], 'b': ['bat']}`                            |
| A5  | `is_palindrome(s)` ignoring case, spaces and punctuation.                                                                                                                                     | `"A man, a plan, a canal: Panama"` → `True`, `"hello"` → `False`                                                      |
| A6  | `chunk(lst, n)` splits a list into pieces of size n (use slicing and `range(0, len, n)`).                                                                                                     | `chunk([1,2,3,4,5,6,7], 3)` → `[[1,2,3],[4,5,6],[7]]`                                                                 |
| A7  | **Predict, then run.** Write your guess for each line first. See the snippet below.                                                                                                           |                                                                                                                       |
| A8  | Finish the contact book: `search_by_name(book, name)` (case-insensitive, returns the dict or `None`) and `list_by_tag(book, tag)` (returns a list of names). Use your four `sample_contacts`. | `list_by_tag(book, "hospital")` → `['Ravi Kumar', 'Shyam Mehta']`; `search_by_name(book, "SNEHA rao")` → Sneha's dict |

A7 snippet:

```python
a = [1, 2, 3]
b = a
c = a[:]
b.append(4)
c.append(5)
print(a, b, c)

def shout(words):
    words.append("!")
    return words

orig = ["hi"]
new = shout(orig)
print(orig is new, orig)
```

<details><summary>A7 answer (open after you've guessed)</summary>

`[1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 5]` and `True ['hi', '!']`. A function that changes a list in place changes the caller's list too, because both names point at the same object.

</details>

---

## Part B — Reading and writing files (Ch 8) · ~20–30 min each

Work on the files in `sandbox/text/`. Use `with open(...)` for every file.

| #   | Task                                                                                                                                                                                                                                                                                                                            | Expect                                                                                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| B1  | `clean_file(src, dst)`: read `messy_notes.txt`, drop blank lines, strip, lowercase, collapse inner spaces, remove `! ? *` and runs of dots. Write the result to `sandbox/cleaned_notes.txt`. Print how many lines went in and out.                                                                                              | `15 lines in, 12 lines out`                                                                       |
| B2  | `log(message)` appends one line to `sandbox/log.txt`. Call it 3 times, then read the file back and print the line count and the last line.                                                                                                                                                                                      | 3 lines                                                                                           |
| B3  | Using `shelve`, save `{"theme": "dark", "batch_size": 50}`. In a **separate run** of the script, open the shelf and print it.                                                                                                                                                                                                   | the same dict, from disk                                                                          |
| B4  | **Mad Libs v2**, your own TODO from `madLibs.py`. Read `madlib_template.txt`. The template has 6 placeholders, with `NOUN` ×3 and `ADJECTIVE` ×2. Ask for a **separate answer for every occurrence**, swap them in one at a time (hint: `replace(tag, answer, 1)`), print the story and save it to `sandbox/madlib_result.txt`. | you get asked 6 times                                                                             |
| B5  | Parse `contacts_raw.txt` into a list of dicts (`name` in Title Case, `phone` trimmed, `tags` as a list) and print it with `pprint`.                                                                                                                                                                                             | 4 dicts, e.g. `{'name': 'Shyam Mehta', 'phone': '9988776655', 'tags': ['hospital', 'colleague']}` |
| B6  | For `sandbox/downloads/photo1.jpg` print the folder, the filename, the extension, the size, and whether it exists.                                                                                                                                                                                                              | ext `.jpg`, size `220000`, `True`                                                                 |

---

## Part C — Regex (Ch 7, the chapter you skipped) · ~15 min each

Your `renameDates.py` already uses regex, so these will feel familiar. Use `sandbox/text/contact_info.txt`.

| #   | Task                                                                                                                               | Expect                                                                                |
| --- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| C1  | `re.findall` all email addresses. The line `Not an email: asha@ or @example.com` must **not** match.                               | 3 emails: `asha.k@example.com`, `ravi_kumar99@mail.co.in`, `support@o-health.example` |
| C2  | Find every date written as `D-M-YYYY`, `DD-MM-YYYY` or `MM/DD/YYYY`. The ISO date `2026-03-14` must **not** be included.           | `['03/14/2026', '14-03-2026', '7-4-2026', '12-12-2025']`                              |
| C3  | Mask every plain 10-digit phone number as `XXXXXX` + its last 4 digits, using `re.sub`. **Stretch:** also catch `+91 98765 43210`. | `9876543210` → `XXXXXX3210`                                                           |

---

## Part D — Organizing files (Ch 9) · the main event

Work on `sandbox/`. Put the helper from D0 in a module and import it in the others.

| #   | Task                                                                                                                                                                                                                                                | Expect                                                                                                          |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| D0  | Helper `unique_path(folder, name)`: return a path that doesn't exist yet. If `a.txt` is taken, try `a_1.txt`, then `a_2.txt`.                                                                                                                       |                                                                                                                 |
| D1  | Print `sandbox/downloads` as an indented tree (one level of indent per depth) with `os.walk`.                                                                                                                                                       | 2 subfolders, 15 files in total                                                                                 |
| D2  | Count files per extension, case-insensitive, with `(none)` for no extension.                                                                                                                                                                        | `{'(none)': 1, '.csv': 1, '.jpg': 3, '.pdf': 4, '.png': 1, '.py': 1, '.tar': 1, '.txt': 2, '.xlsx': 1}`         |
| D3  | List every file over 100,000 bytes, biggest first, as `size  relative/path`.                                                                                                                                                                        | 4 files: `old_backup.tar` 310000, `photo1.jpg` 220000, `old/2024/photo1.jpg` 150000, `screenshot.png` 130000    |
| D4  | **Sort by extension.** Copy every file under `downloads/` into `sandbox/sorted/<ext>/` (no dot, lowercase, `no_extension` for none). Use `unique_path` so name clashes never overwrite. Add a `DRY_RUN = True` switch that only prints.             | `pdf` has 4 files incl. `report_1.pdf`; `jpg` has 3 incl. `photo1_1.jpg`; `txt` has `notes.txt` + `notes_1.txt` |
| D5  | **Selective copy v2** (your `reviseZipfunc.py`): `copy_by_ext(src, dst, exts)`. Case-insensitive, name clashes handled, and it prints `copied N, skipped M`.                                                                                        | `[".pdf"]` → copied 4; `[".pdf", ".jpg"]` → copied 7                                                            |
| D6  | **Filling in the gaps** (book project). `sandbox/numbered/` has `spam001, 002, 004, 005, 007`. Rename so the numbers are continuous. Dry-run first.                                                                                                 | `spam001` … `spam005`; `spam003.txt` now holds `this is spam004`                                                |
| D7  | **renameDates v2.** Build the full list of planned renames and print it. Ask `Proceed? (y/n)`, then rename and write every `old -> new` pair to `sandbox/rename_log.txt`.                                                                           | 4 renames, 2 skipped (`summary_2026-03-14.txt`, `readme.txt`); `sales_12-01-2025.csv` → `sales_01-12-2025.csv`  |
| D8  | `undo_renames()` reads `rename_log.txt` and reverses every rename.                                                                                                                                                                                  | `reports/` is back to the original 6 names                                                                      |
| D9  | **Backup v2** (your `backupZipFile.py`): zip `sandbox/downloads` into `sandbox/downloads_1.zip` using `arcname=os.path.relpath(...)`, skip earlier backup zips, then print `namelist()`. Extract to `sandbox/restore_test` and compare file counts. | 15 entries, none starting with `Users/` or `tmp/`                                                               |
| D10 | `find_duplicate_names(folder)` returns `{filename: [paths]}` for names that appear more than once (use `setdefault`).                                                                                                                               | `notes.txt`, `photo1.jpg`, `report.pdf`, 2 paths each                                                           |

---

## Part E — Mini-projects (60–90 min, combine everything)

| #   | Project                                                                                                                                                                                      | Expect                                                                                                     |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| E1  | **Batch cleaner.** Run your B1 cleaner on every `.txt` under `sandbox/text/`, write results to `sandbox/cleaned/`, and print a summary table (`ljust` for the name, `rjust` for the counts). | `messy_notes.txt` 15 → 12; `contacts_raw.txt` 4 → 4; `madlib_template.txt` 1 → 1; `contact_info.txt` 6 → 6 |
| E2  | **Folder health report.** For `sandbox/downloads`, write `report.txt` with: total files, total size, per-extension count and size, the 3 largest files, and duplicate names.                 | 15 files, 1,188,085 bytes (about 1.13 MB), 3 duplicate names                                               |

---

## Suggested pacing

| Sessions (evenings) | Do                                                                          |
| ------------------- | --------------------------------------------------------------------------- |
| 1–2                 | Part A (A3 and A8 are the important ones, they close the loops from before) |
| 3–4                 | Part B                                                                      |
| 5                   | Part C, 3 tasks. Do it before starting a regex chapter                      |
| 6–9                 | Part D, in order. D4, D7 and D9 are the big ones                            |
| Weekend             | E1 or E2                                                                    |

When a task works, ask yourself the one question that matters: _would this still behave if the folder had two files with the same name, or an empty folder?_ If you can't say, test it.
