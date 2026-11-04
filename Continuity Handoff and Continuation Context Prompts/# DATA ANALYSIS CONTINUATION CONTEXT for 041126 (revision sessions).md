# DATA ANALYSIS CONTINUATION CONTEXT

## Current Goal & Position

Learn Python for data analysis, then progress towards data science. I paused after starting pandas and DataFrames. I’m revising earlier material before resuming the learning plan. My last successful exercise read three scores from a text file. The next exercise, handling an invalid entry, has been assigned but not attempted in this chat.

CONTEXT WARNING: Some earlier context may no longer be reliably available. Do not infer missing learning history.

## Learning Path

Variables, types and calculations → conditions → lists and loops → functions and dictionaries → text files, error handling and CSVs → introductory pandas/DataFrames. Current revision has reached text files. Next: practise error handling, revisit CSV cleaning, then return to pandas selection, filtering and combining conditions. My exact pandas checkpoint is uncertain. I have calculated a filtered-group mean in plain Python during revision.

## Coding / Maths State

- I can loop through a list of participant dictionaries, count completed questionnaires, collect IDs with `.append()`, and combine conditions using `and`. I correctly predicted and obtained `['P02', 'P04']` when filtering for completion and `score >= 7`.
- I calculated a mean using `sum(completed_scores) / len(completed_scores)` after filtering. I understand why `[0]` gives a mean of `0.0`, while `[]` should return `None`. I needed help placing the empty-list check.
- Previously introduced: `while`, `enumerate()`, function parameters and defaults, dictionary `.get()`, `FileNotFoundError`, `ValueError` and `csv.DictReader`. Earlier CSV work produced a mean valid score of `6.67` from three valid scores and identified `P004` as invalid. These topics have not all been independently demonstrated during this revision. `enumerate()` and parameter versus global variable have needed reinforcement.

## Active Work

Windows 11, VS Code, Python 3.13.15. `scores.txt` is beside the script in `C:\Users\nicky\Desktop\Learning_Python\exercises`. Last working code, with the diagnostic path print omitted:

```python
from pathlib import Path

file_path = Path(__file__).with_name("scores.txt")
scores = []

with open(file_path, "r") as file:
    for line in file:
        clean_line = line.strip()
        score = int(clean_line)
        scores.append(score)

print(scores)
```

Confirmed output: `[7, 0, 8]`. The pending exercise asks me to change the file to four lines, `7`, `0`, `missing`, `8`, then adapt this loop. No revised code or output has been submitted.

## Important Work / Corrections

- `0` starts a counter. `[]` starts a collection. When filtering, put `.append()` inside the `if` and `return` after the loop. `print()` displays a value. `return` sends it back to the caller.
- Check `if not completed_scores:` **after** collecting all scores and **before** division. Checking immediately after `.append()` cannot detect an empty list.
- `readlines()` returns a list. Looping through the file gives one string at a time for `.strip()` and `int()`. The path issue is resolved: `open("scores.txt")` looked in the VS Code working folder, while `open(file_path, "r")` uses the path beside the script. The filename is `scores.txt`, plural.

## Teaching Preferences

I began without coding experience. I have a psychology degree, survey research experience and about six hours a week to study. Use accessible British English, small survey-like datasets and one manageable exercise at a time. Let me predict or write the code, then review my attempt. When correcting an error, identify the line or indentation involved and explain what Python does with a concrete value.

## Next Step

Keep the working file path. Initialise `invalid_count = 0` before the loop. Practise `try` and `except ValueError` **inside the loop** so `missing` increases the counter and processing continues to `8`. Expected results: `scores == [7, 0, 8]` and `invalid_count == 1`.

## Continue From Here

Resume with the pending invalid-score exercise and invite me to paste my attempt before showing a solution. Check that `0` is retained and that `8` is still read after `missing`. Once this is comfortable, continue with CSV revision before returning to pandas.