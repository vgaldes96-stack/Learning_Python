# DATA SCIENCE CONTINUITY HANDOFF

Create a **minimum-sufficient continuity handoff** from all conversation context currently available to you so I can paste it into a fresh ChatGPT chat and continue learning Data Science from exactly where we stopped.

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

### Knowledge State
Classify relevant concepts as:

- **Understood:** demonstrated through correct reasoning, explanation or application.
- **Partial / Confused:** encountered but still needs reinforcement.
- **Exposed:** explained/shown but understanding has not been demonstrated.
- **Not Yet Covered:** only important prerequisites the next tutor must not assume.

Never treat “explained” as “understood.” When uncertain, classify conservatively.

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

### Evidence of Ability
Preserve significant exercises and questions only when they reveal my actual ability, including:
- what I solved independently;
- mistakes or misconceptions;
- hints required;
- skills still needing practice.

### Active Project / Dataset
When applicable preserve:
- objective;
- relevant dataset/files;
- important features/columns/target;
- preprocessing/analysis/models completed;
- results;
- decisions;
- unresolved issues;
- next work.

### Corrections
Preserve the final corrected state.

Mention an earlier mistake only if doing so helps prevent it recurring.

### Teaching State
Preserve only established:
- learning preferences;
- pacing;
- explanation style;
- useful analogies/examples;
- approaches that caused confusion or failed.

### Files
Do not assume the new chat has previous files.

When necessary write:

`REUPLOAD REQUIRED: <filename>`

Preserve conclusions about the file, not unnecessary copies of its contents.

---

## COMPRESSION

Remove:
- filler and greetings;
- repetition;
- unnecessary chronology;
- generic Data Science knowledge;
- obsolete discussion;
- redundant examples/exercises;
- long explanations whose conclusion is sufficient;
- details that would not change future teaching.

Prefer dense statements such as:

`Pandas: column selection understood; boolean masks introduced; combining conditions with & / | still confused.`

If context is healthy, compress aggressively.

If context reliability is questionable, favour preservation over extreme compression.

---

# OUTPUT ONLY THIS

# DATA SCIENCE CONTINUATION CONTEXT

## Current Goal & Position
[Goal + current topic + exact stopping point.]

## Learning Path
[Covered → current → next, only if established.]

## Knowledge State
**Understood:**  
[...]

**Partial / Confused:**  
[...]

**Exposed:**  
[...]

**Important Not Yet Covered:**  
[...]

## Coding / Maths State
[Relevant technical knowledge, ability, notation, libraries and difficulties.]

## Active Work
[Exact unfinished work and current state.]

## Important Work / Corrections
[Relevant exercises, projects, datasets, results, decisions, misconceptions and corrections.]

## Environment / Files
[Only relevant setup/files; mark required reuploads.]

## Teaching Preferences
[Only established preferences and useful/failed teaching approaches.]

## Next Step
[Unresolved questions + immediate recommended continuation.]

## DO
Add conversation-specific instructions where needed. Otherwise:
- continue from demonstrated knowledge;
- reinforce unresolved prerequisites;
- progress gradually;
- explain new terminology before relying on it;
- prefer intuitive beginner-friendly explanations before unnecessary formal complexity;
- let me attempt exercises when appropriate.

## DO NOT
Add conversation-specific warnings where needed. Otherwise:
- do not restart from the beginning;
- do not confuse exposure with mastery;
- do not assume understanding merely because something was explained;
- do not unnecessarily reteach understood material;
- do not skip unresolved prerequisites;
- do not suddenly increase difficulty;
- do not use unexplained advanced jargon, maths, syntax or functions;
- do not overwhelm me with premature edge cases or unnecessary theory;
- do not immediately solve exercises I should attempt;
- do not repeat failed explanations unchanged;
- do not contradict established corrections/results;
- do not assume access to unavailable files;
- do not invent history, progress, outputs or understanding.

## Continue From Here
[1–3 sentences telling the new tutor exactly how to resume.]

Before outputting, internally check:

**If the original chat vanished, could a capable beginner Data Science tutor continue correctly using only this handoff plus required reuploaded files?**

Add anything whose absence could materially change the next response. Remove anything that would not.

Output **ONLY the handoff**.