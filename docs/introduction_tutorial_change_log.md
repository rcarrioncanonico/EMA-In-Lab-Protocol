# Introduction Tutorial Change Log
**Original:** `Introduction_Tutorial.ipynb`
**Revised:** `Introduction_Tutorial_v2.ipynb`

---

## Summary

The original tutorial is a useful first draft but reads more as a reference list than a
beginner workflow. v2 restructures the same content into a linear, step-by-step sequence
and fills in several gaps that would confuse a student with no prior programming experience.
The original file was **not modified**.

---

## Section-by-Section Comparison

### Cell 1 — "Getting Your Computer Ready for Data Science"

| | Original | v2 |
|---|---------|-----|
| **Content** | Bullet list pointing to an external tutorial (neuraldatascience.io); mentions VS Code, Miniconda, and PowerShell fix as sub-bullets | Explicit numbered steps; PowerShell fix moved to its own dedicated step (Part 2.2) |
| **Tone** | Assumes reader will figure out the external tutorial on their own | Explicitly tells the reader what to do at each step |
| **Downloads** | Mentions VS Code and Miniconda but does not provide direct download links in a table | Section 2.1 lists every download with URL and save-as instructions in a table |
| **External dependency** | Reader must follow an entirely different tutorial first | No mandatory external tutorial; everything needed is in the notebook itself |

**Rationale:** The original approach outsourced onboarding to an external resource. Beginners often get lost or give up when sent to a different tutorial mid-workflow. v2 keeps everything in one place while linking supplementary resources at the end.

---

### Cell 2 — "Basic Information of Sources" (intro paragraph)

| | Original | v2 |
|---|---------|-----|
| **Content** | One-paragraph overview mentioning the five cognitive tasks and three modes (Using/Editing/Making) | Restructured as a "What This Tutorial Covers" section with explicit learning outcomes and a level-selection table |
| **Level system** | Hinted at in cells 8–10 (Using/Editing/Making) as separate stub cells at the end | Introduced up front in a clear Level 1 / Level 2 / Level 3 table with a study path for each |

**Rationale:** Students need to know their goal before reading tool descriptions. Placing the level system at the start lets readers self-select the relevant parts.

---

### Cells 3–7 — "GitHub", "Pavlovia", "m-Path", "PsychoJS", "Local Lab Infrastructure"

| | Original | v2 |
|---|---------|-----|
| **Order** | Presented as five independent section headers with no visual link between them | Presented after a relationship diagram that shows how they connect |
| **Diagram** | None | ASCII pipeline diagram in Part 1.1; full Mermaid diagram in `docs/figures/program_relationships.mmd` |
| **GitHub** | Described but no steps for using it; three external links listed | Same links retained; key concept of "commit" briefly explained; steps deferred to Part 4.1 |
| **Pavlovia** | One paragraph | Same content + data-flow diagram showing `.py → Pavlovia → JS → phone` |
| **m-Path** | One paragraph | Same content + placed in context of the Level 2 data collection pipeline |
| **PsychoJS** | One paragraph | Same content + note explaining why it matters (Python features may behave differently in web version) |
| **Lab vs. EMA** | Described in one paragraph without structure | Added as a comparison table in Part 4.5 |

**Rationale:** Tool descriptions without relationships are hard to absorb. The diagram and comparison table let a reader see the system as a whole before reading the details.

---

### Cell 8 — PsychoPy

| | Original | v2 |
|---|---------|-----|
| **Content** | Description of PsychoPy; download link; Python 3.10 note | Same content; download link retained; Python 3.10 requirement given explicit rationale (environment isolation) |
| **Standalone vs. env** | Mentioned together without distinction | Separated: standalone = GUI Builder (optional); `psychopy_env` = scripting in VS Code (required) |
| **Placement** | After the platform descriptions, before the stub "Using/Editing/Making" cells | Integrated into Part 1.2 tool-by-tool descriptions |

**Rationale:** The distinction between PsychoPy standalone and the conda environment is a frequent source of confusion. Making it explicit prevents students from installing only the standalone and wondering why VS Code cannot find PsychoPy.

---

### Cells 9–10 — "Using", "Editing", "Making" (stub cells)

| | Original | v2 |
|---|---------|-----|
| **Content** | Three one-line stub headings with placeholder text | Expanded into Parts 5, 7, and (deferred to Configuration Tutorial) |
| **"Using"** | "Using the already programmed software for data collection" | Part 5: Step-by-step instructions to run the N-back task and find data output |
| **"Editing"** | "Here we can paste the code, and create cells for modifying this quote" | Part 7: Backup protocol, edit targets table, recommended workflow, pointer to Configuration_Modification_Tutorial |
| **"Making"** | "from 0? using what we learn such as ai copilot assistant for coding" | Removed from v2 (not in scope for Level 1–3 as defined; can be a separate tutorial) |

**Rationale:** The original stubs served as placeholders. In v2 the "Using" and "Editing" goals are given full treatment. "Making from scratch" is a topic large enough to deserve its own tutorial; including it as a stub creates false expectations.

---

## Content Added in v2 (not in original)

| New content | Location in v2 | Feedback item addressed |
|-------------|---------------|------------------------|
| Level 1 / 2 / 3 user path system | Part 0 (title cell) + level tables | Feedback #7: Support 3 user levels |
| Tool relationship diagram (ASCII) | Part 1.1 | Feedback #6: Visualize tool relationships |
| Tool relationship diagram (Mermaid) | `docs/figures/program_relationships.mmd` | Feedback #6 |
| Explicit downloads table with URLs | Part 2.1 | Feedback #3: List programs/files to download |
| Step-by-step Windows setup | Parts 2.2–2.6 | Feedback #5: Remove back-and-forth; make step-by-step |
| VS Code UI location guidance (status bar diagram) | Part 2.6 | Feedback #4: Visual guidance for VS Code UI |
| Terminal mode explanation (front door vs. REPL) | Part 2.7 | Originally in Psychopy Tutorial only; surfaced here |
| PsychoPy sanity check without `core.quit()` | Part 3 | In-Jupyter constraint; Feedback #5 |
| EMA deployment pipeline (Level 2) | Part 6 | Feedback #7 Level 2 |
| Backup protocol before editing | Part 7.1 | Feedback #7 Level 3 |
| "What to Read Next" table | End of notebook | Feedback #2: Clarify overall goal and tutorial build-up |
| `docs/Psychopy_Quickstart_Guide.md` | Separate file | Feedback #1: Separate PDF-style first-steps guide |

---

## Content Removed or Deferred in v2

| Removed content | Original location | Reason |
|----------------|------------------|--------|
| Pointer to neuraldatascience.io as primary setup resource | Cell 1 | Replaced by self-contained steps; link retained in "Further Reading" |
| "Making from scratch" stub | Cell 10 | Out of scope for defined levels; deferred to future tutorial |
| Raw GitHub resource list without context | Cell 3 | Retained links but integrated them into a table with descriptions |

---

## Terminology Changes

| Original term | v2 term | Reason |
|--------------|---------|--------|
| "Mini-Anaconda" | "Miniconda" | Official name |
| "Psychopy" (mixed case) | "PsychoPy" (official capitalization) | Consistency |
| "enviroment" (typo) | "environment" | Spelling |
| "convinient" (typo) | Removed / rewritten | Spelling |
| "psyochopy enviroment" (typo) | `psychopy_env` | Consistent code formatting + spelling |
| "powercell" | "PowerShell" | Correct name |

---

## Structural Changes

| Change | Rationale |
|--------|-----------|
| All content organized into numbered Parts (1–7) | Linear reading path; easy to reference by section number |
| Level-gating of sections | Prevents beginners from reading irrelevant advanced content |
| Kernel metadata set to `psychopy_env` | Ensures notebook runs with the correct interpreter by default |
| `core.quit()` removed from all code cells | Avoids killing the Jupyter kernel; `win.close()` used instead |
| Windows-specific commands used throughout | Target audience is Windows users per project spec |

---

## Feedback Item Cross-Reference

| Feedback item | Where addressed |
|--------------|----------------|
| 1) Separate PDF-style first-steps guide | `docs/Psychopy_Quickstart_Guide.md` |
| 2) Clarify overall goal and tutorial build-up | v2 title cell; "What to Read Next" table |
| 3) List programs/files to download explicitly | v2 Part 2.1 (downloads table) + Quickstart Guide Section 2 |
| 4) Visual guidance for VS Code UI locations | v2 Part 2.6 (status bar ASCII diagram) + Quickstart Guide Section 4 |
| 5) Remove back-and-forth; make step-by-step | v2 Parts 2–7 (linear numbered steps); original's reference-list structure replaced |
| 6) Visualize tool relationships | v2 Part 1.1 (ASCII); `docs/figures/program_relationships.mmd` (Mermaid) |
| 7a) Level 1: single-timepoint lab data | v2 Part 5; Quickstart Guide Section 5 |
| 7b) Level 2: EMA smartphone tasks | v2 Part 6; Quickstart Guide Section 6 |
| 7c) Level 3: adjust existing task | v2 Part 7; Quickstart Guide Section 7 |
