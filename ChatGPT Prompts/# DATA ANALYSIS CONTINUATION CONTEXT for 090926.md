# DATA ANALYSIS CONTINUATION CONTEXT

## Current Goal & Position

Beginner learning Python for a future career in data analysis, possibly data science later, at roughly 6 self-study hours/week. Has psychology degree, quantitative national/international survey experience, rusty intermediate-level maths, and began with no coding experience.

Currently in Week 3: completed core loop concepts and started functions.

Exact stopping point: learned function definitions, calls, parameters and arguments, then attempted to combine a two-parameter function with `enumerate()`. Corrected code was provided, but user has not yet independently recreated it:

```python
def show_response(participant_number, response):
    print("Participant", participant_number, "response:", response)


responses = ["Yes", "No", "Yes"]

for participant_number, response in enumerate(responses, start=1):
    show_response(participant_number, response)
```

Expected output:

```text
Participant 1 response: Yes
Participant 2 response: No
Participant 3 response: Yes
```

## Learning Path

Python/VS Code/GitHub basics → variables, types and calculations → Boolean/conditional logic → lists and summaries → loops, counting and filtering → **current: functions** → dictionaries → files and error handling → pandas/tabular data → cleaning, analysis and visualisation → realistic survey/research portfolio projects → later NumPy, SQL and introductory machine learning.

Do not rush into libraries before core Python is understood.

## Coding / Maths State

Demonstrated/covered:

* Python versus VS Code; Python 3.13.15 (64-bit) on Windows 11; runs `.py` files in VS Code.
* GitHub purpose understood; repository workflow initiated in VS Code and branch published, but routine commit/push workflow is not yet established through repeated use.
* `print()` with text, numbers, variables and comma-separated values.
* Variables, assignment, naming, case sensitivity and stored values.
* Types: `str`, `int`, `float`, `bool`; quotes create strings.
* Arithmetic: `+`, `-`, `*`, `/`, `**`, `%`; brackets/order of operations; `/` returns a float; decimals use `2.5`, not `2,5`.
* Comparisons; Boolean logic using `and`, `or`, `not`.
* `if`/`elif`/`else`; indentation, chained comparisons, boundaries and condition order; only the first true branch runs.
* Lists: creation, mutability, zero-based/negative indexing, replacement, slicing; `append()`, `insert()`, `remove()`, `pop()`, `len()`, `in`, `not in`, `count()`, `index()`, `sort()`, `sorted()`, `reverse()`, `sum()`, `min()`, `max()`.
* Mean: `sum(values) / len(values)`; number of observations may be denoted `n`.
* `sort()`/`append()` mutate and return `None`; `sorted()` creates a new list.
* `for item in list`; nested conditions; accumulators; filtering with `.append()`.
* `range(start, stop, step)`: start included, stop excluded.
* `enumerate(collection, start=1)` supplies counter and value. Skipped items retain original enumeration numbers.
* `break` ends the whole loop; `continue` skips the current iteration.
* Missing-value filtering with sentinel values such as `-1` or `99`.
* `while` loops: initial value, condition and update; `Ctrl+C` interrupts an infinite loop.
* Functions: `def`, function body, function call, parameter versus argument, multiple parameters; function must be defined before it is called.
* A function definition stores instructions; every call executes its complete body.

Not covered: `return`, variable scope, default/keyword arguments, dictionaries, files, structured exception handling, NumPy, pandas, plotting, SQL, scikit-learn or applied dataset projects.

## Active Work

Consolidate functions called from loops. User’s attempted code correctly defined:

```python
def show_response(participant_number, response):
    print("Participant", participant_number, "response:", response)
```

but incorrectly used:

```python
for participant_number, response in enumerate(show_response, start=1):
    show_response(response)
```

Correction established:

* `enumerate()` processes the list: `enumerate(responses, start=1)`.
* The function is called inside the loop.
* Both required arguments must be supplied:
  `show_response(participant_number, response)`.

No unanswered question is pending. Next new concept is functions that `return` values.

## Important Work / Corrections

Correct classification pattern independently produced:

```python
for score in survey_scores:
    if score >= 7:
        print(score, "High")
    elif 4 <= score <= 6:
        print(score, "Medium")
    else:
        print(score, "Low")
```

Correctly counted and filtered medium scores:

```python
survey_scores = [3, 8, 6, 9, 4, 7, 2]
medium_count = 0
medium_scores = []

for score in survey_scores:
    if 4 <= score <= 6:
        medium_count += 1
        medium_scores.append(score)
```

Result: `2` and `[6, 4]`.

Independently completed missing-value exercise:

```python
wellbeing_scores = [7, 99, 5, 8, 3, 99, 6]
valid_count = 0
valid_scores = []

for score in wellbeing_scores:
    if score == 99:
        continue

    valid_count += 1
    valid_scores.append(score)
```

Result: `5` and `[7, 5, 8, 3, 6]`.

Correctly completed a `while`/`continue` exercise skipping record `5` from `1–7`. Understood that every path must update the counter; otherwise `continue` can create an infinite loop.

Recurring points to monitor:

* Exact variable names matter; undefined names cause `NameError`; hyphens mean subtraction, so use underscores.
* Initialise accumulators/filtered lists before loops; otherwise they reset each iteration.
* Place summary `print()` statements outside loops when output is required once.
* `survey_number + 1` does not update the variable; use `survey_number += 1`.
* Indentation determines code blocks.
* `range(1, 11, 2)` generates odd numbers; begin at `2` for evens.
* Calling a two-parameter function with one argument causes `TypeError`.
* When predicting function output, count how many times the function is called.

A Week 3 PDF was created covering `range()`, `enumerate()`, `break`, `continue`, filtering, `while` loops, functions, terminology, roadmap and checkpoint.

## Teaching Preferences

* Clear, beginner-friendly, structured explanations; define terminology before using it.
* Use survey, participant and research examples where possible.
* Explain why code behaves as it does, especially indentation and execution order.
* Let user attempt exercises before showing solutions.
* Use VS Code exercises at meaningful checkpoints, particularly when combining concepts; avoid an exercise after every minor point.
* Continue through straightforward material without repeatedly asking whether user is ready.
* Maintain an explicit roadmap, accurate week label and exact stopping point.
* Periodic notes should be PDF-style with distinct headings, contents, page numbers, creation date/time, definitions, roadmap/current checkpoint and cumulative checklist.

## Next Step

First ask the user to independently recreate or repair the function-plus-`enumerate()` example to confirm the correction. Then introduce `return`: distinguish printing a result from returning it, assigning a returned value to a variable, and using returned values in later calculations. After suitable function practice, proceed to dictionaries.

## Continue From Here

Resume Week 3 at functions used inside loops, without reteaching basic loops or lists. Briefly verify the corrected `show_response()` pattern, then teach `return` gradually with survey-style examples and allow the user to attempt the next combined exercise before revealing the solution.
