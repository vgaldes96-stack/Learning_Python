# DATA SCIENCE CONTINUATION CONTEXT

## Current Goal & Position

Learn Python for data analysis, then progress towards data science. Beginner with a psychology degree, survey research experience and approximately six study hours/week.

Current topic is pandas data validation and counting overlapping reasons for reviewing records. The exercise now works. My latest question was why some counts were stored in variables before printing, while others used `print(mask.sum())` directly. Both approaches were explained, but I have not yet demonstrated that distinction independently.

Current exercise state is reliable. Earlier progress is recorded through continuity handovers and lesson notes; the exact pandas checkpoint before revision remains uncertain.

## Learning Path

Python/VS Code basics → variables/types/calculations → conditions → lists/loops → functions/dictionaries → files/error handling/CSV → **current: pandas selection, conversion, masks and validation summaries** → broader cleaning, analysis and visualisation → realistic survey portfolio projects → later NumPy, SQL and introductory machine learning.

## Knowledge State

**Understood:**

- Variables, common types, calculations, comparisons, conditionals, lists, counting and filtering with loops.
- Earlier handovers record function definitions/calls, arguments, local variables, `return`, dictionaries and nested participant records.
- Text/CSV reading, integer conversion, `try/except ValueError`, invalid-entry counts and IDs, means with an empty-list guard.
- Pandas CSV loading, column selection/assignment, `pd.to_numeric(..., errors="coerce")`, inclusive `.between(0, 10)`, filtering and `.loc[mask, columns]`.
- `.tolist()`, filtered `.mean()`, and applying `&`, `|`, `~` in working code.
- Successfully verified that `~valid_mask | ~completed_mask` and `~(valid_mask & completed_mask)` select identical records.
- Explained that reason counts can count a record more than once, while the combined review mask counts each row once.

**Partial / Confused:**

- Translating Boolean expressions into precise words. Sometimes predicted the wrong IDs despite correct code, overlooked missing scores, or reversed the wrong named mask.
- `.sum()` on a Boolean mask needed guidance. Initially used `df.loc[mask].sum()`, which sums selected columns.
- Storing a calculated count versus calculating it inside `print()` was just explained.
- Recurring exact-name errors; inclusive boundaries and placement of empty checks previously needed correction.
- Historical reinforcement areas include `enumerate()` with function calls, parameters versus global variables, default/keyword arguments, dictionary methods and reusable frequency counting.

**Exposed:**

- Counting Boolean values works because `True` contributes 1 and `False` contributes 0; applied with guidance.
- A calculated count can be assigned to a variable for reuse or passed directly to `print()`.
- Earlier `break` and `FileNotFoundError` coverage lacks verified independent exercises in the available records.

**Important Not Yet Covered:**

- Broader analysis/plotting, realistic portfolio projects, NumPy, SQL, scikit-learn and machine learning.
- Pandas all-invalid/empty-result mean handling has not been tested. Do not assume it behaves like the earlier plain-Python `None` guard.

## Coding / Maths State

Mean is `sum(scores) / len(scores)` in plain Python, or `selected_rows["score_numeric"].mean()` in pandas. Zero remains valid and contributes to the denominator. Earlier plain-Python empty-list handling explicitly returned `None`.

Pandas masks use `&`, `|`, `~`. `.loc[mask, "column"]` selects one column; `.loc[mask, ["a", "b"]]` selects several. Filtering retains original index labels.

In the current numeric column, missing scores make `.between(0, 10)` false. Therefore `~valid_mask` includes both missing and out-of-range scores. To count only numeric out-of-range scores, use:

```python
out_of_range_mask = ~valid_mask & ~missing_score_mask
```

## Active Work

Current file is `survey_check.csv`, containing:

```csv
participant_id,score,completed
S001,8,yes
S002,10,yes
S003,,yes
S004,12,no
S005,4,no
S006,,no
S007,0,yes
```

The corrected working logic is:

```python
import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("survey_check.csv")
df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

valid_mask = df["score_numeric"].between(0, 10)
completed_mask = df["completed"] == "yes"
missing_score_mask = df["score_numeric"].isna()

missing_count = missing_score_mask.sum()
out_of_range_mask = ~valid_mask & ~missing_score_mask
out_of_range_count = out_of_range_mask.sum()

incompleted_mask = ~completed_mask
review_mask = missing_score_mask | ~valid_mask | incompleted_mask

print("Missing scores:", missing_count)
print("Numeric scores outside 0-10:", out_of_range_count)
print("Incomplete questionnaires:", incompleted_mask.sum())
print("Records that need review:", review_mask.sum())
```

Expected counts are **2, 1, 3, 4** respectively. I reported that the code worked after the recommended fixes; I did not paste the final output.

Latest explanation offered this consistent alternative:

```python
incomplete_count = incompleted_mask.sum()
review_count = review_mask.sum()

print("Incomplete questionnaires:", incomplete_count)
print("Records that need review:", review_count)
```

These additional assignments were shown but have not yet been independently demonstrated. The existing `incompleted_mask` name is valid; keep naming consistent.

## Important Work / Corrections

- S004 is out of range **and** incomplete; S006 has a missing score **and** is incomplete. Reason counts sum to **6**, covering **4** review records. Missing and numeric out-of-range categories are separate here; overlap occurs with incompletion.
- Current `review_mask` works. `missing_score_mask` is redundant in that expression because `~valid_mask` already includes missing scores.
- `pandas.errors.EmptyDataError: No columns to parse from file` occurred at CSV loading. Checking/populating/saving the CSV resolved it.
- Previously wrote `~mask = ...`, causing a syntax error. Assign to a plain variable name and reverse the existing mask on the right: `review_mask = ~eligible_mask`.
- Previously assigned one mask name and used another in `.loc`. Run the complete script to verify names and execution order.
- Earlier six-row `scores.csv` contained P001=7/yes, P002=0/yes, P003=missing/yes, P004=8/no, P005=12/yes, P006=-1/no. Eligible IDs were P001/P002, mean **3.5**. Completed-with-invalid IDs were P003/P005. Review IDs were P003/P004/P005/P006.
- Earlier text-file revision confirmed valid scores `[7, 0, 8]`, invalid count 1, mean 5.0. All-invalid text gave `[]`, invalid count 2, mean `None`.

## Environment / Files

Windows 11, VS Code, Python 3.13.15. Script path reported:

```text
C:\Users\nicky\Desktop\Learning_Python\Python lessons and exercises\lessons_week11,12.py
```

CSV files belong beside the script because `Path(__file__).with_name(...)` is used. Save data and code before running. Previous issues included editing an unsaved CSV and confusion about the working directory.

Latest notes are `Python_Week12_Lesson21_Notes.pdf`, dated 17 November 2026; its week/lesson label was inferred from the preceding Week 11, Lesson 20 notes. The current session is 18 November; no new lesson number has been agreed. No reupload is necessary to continue the exercise above.

## Teaching Preferences

Accessible British English, survey/research examples, terminology explained before use. Give coherent, manageable exercises that combine ideas; avoid breaking every minor step into a separate task. Let me attempt code before revealing a full solution. When stuck, provide targeted hints/templates and explain execution using concrete values. Identify the exact line or indentation behind errors.

## Next Step

Briefly check my understanding of storing versus directly printing a count, preferably by asking me to store and print all four counts consistently. Then consolidate the current validation summary before gradually extending the analysis. Do not repeat the earlier mask-equivalence exercise; it has now succeeded.

## DO

- Continue from the working dataset and demonstrated code.
- Reinforce Boolean wording, mask counting and variable reuse through application.
- Credit successful code separately from reasoning that needed correction.
- Explain new syntax before expecting its use.

## DO NOT

- Restart Python or pandas basics.
- Treat supplied corrections as independent mastery.
- Confuse missing scores with numeric out-of-range scores.
- Add overlapping reason counts to obtain the number of review records.
- Assume all-invalid pandas results, plotting or machine learning are understood.
- Invent lesson numbers, progress or outputs.

## Continue From Here

Resume immediately after the explanation that `count = mask.sum(); print(count)` stores the result for reuse, while `print(mask.sum())` prints the calculation directly. Invite a short application using the four current counts, then progress from the validated survey summary.