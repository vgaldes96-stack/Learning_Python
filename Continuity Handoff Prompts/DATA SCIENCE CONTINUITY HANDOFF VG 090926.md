My edits.

# DATA ANALYSIS CONTINUITY HANDOFF

Create a **minimum-sufficient continuity handoff** from all conversation context currently available to you so I can paste it into a fresh ChatGPT chat and continue learning Data Analysis from exactly where we stopped.

This is a **learning save-state, not a conversation summary**.

## OBJECTIVE

Preserve every detail that could materially affect:
- what I currently know;
- what I do not yet understand;
- how I should be taught;
- what work has already been completed;
- what we are currently doing;
- what should happen next.

Use the **fewest tokens possible without reducing reliable continuity**.

Preserve state, not transcript.

---

## CONTEXT RELIABILITY

First assess whether the available conversation context appears intact.

If exact context usage is available, consider it. Otherwise do not invent token counts or percentages.

Signs of possible degradation include forgotten earlier details, contradictions, repeated questions/explanations, lost exercise/project state, or uncertainty about previous discussion.

If degradation is likely:
- compress less aggressively;
- prioritise current work, demonstrated knowledge, confusion, prerequisites, corrections, relevant code/projects/results, and teaching preferences;
- never reconstruct missing history from assumptions.

If important earlier context may already be unavailable, include:

`CONTEXT WARNING: Some earlier context may no longer be reliably available. Do not infer missing learning history.`

---

## CAPTURE

Include only information that could realistically change the next tutor's response.

### Current State
- overall learning goal;
- current topic;
- exact point reached;
- unfinished question/exercise/code;
- immediate next step;
- established learning sequence, if any.

### Technical State
Compactly preserve relevant:
- Python;
- NumPy/pandas;
- plotting;
- statistics/maths;
- SQL;
- machine learning/scikit-learn;
- functions, syntax and terminology introduced;
- recurring mistakes;
- relevant formulas/notation;
- environment/tooling when it affects continuation.

Preserve exact names, values, formulas, outputs, errors, filenames, columns, variables, commands or versions when they matter.

### Corrections
Preserve the final corrected state.

Mention an earlier mistake only if doing so helps prevent it recurring.

### Teaching State
Preserve only established:
- learning preferences;
- pacing;
- explanation style;
- useful analogies/examples.


## COMPRESSION

Remove:
- repetition;
- unnecessary chronology;
- obsolete discussion;
- long explanations whose conclusion is sufficient;
- details that would not change future teaching.

Prefer dense statements such as:

`Pandas: column selection understood; boolean masks introduced; combining conditions with & / | still confused.`

If context is healthy, compress aggressively.

If context reliability is questionable, favour preservation over extreme compression.

---

# OUTPUT ONLY THIS

# DATA ANALYSIS CONTINUATION CONTEXT

## Current Goal & Position
[Goal + current topic + exact stopping point.]

## Learning Path
[Covered → current → next, only if established.]

## Coding / Maths State
[Relevant technical knowledge, ability, notation, libraries and difficulties.]

## Active Work
[Exact unfinished work and current state.]

## Important Work / Corrections
[Relevant exercises, projects, datasets, results, decisions, misconceptions and corrections.]

## Teaching Preferences
[Only established preferences and useful/failed teaching approaches.]

## Next Step
[Unresolved questions + immediate recommended continuation.]

## Continue From Here
[1–3 sentences telling the new tutor exactly how to resume.]

Before outputting, internally check:

**If the original chat vanished, could a capable beginner Data Analyst tutor continue correctly using only this handoff?**

Add anything whose absence could materially change the next response. Remove anything that would not.

Output **ONLY the handoff**.