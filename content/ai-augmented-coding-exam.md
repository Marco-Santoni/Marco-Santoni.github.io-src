Title: An AI-augmented workflow for a yearly coding exam: authoring + grading
Date: 2026-04-27
Status: published

Each year I run an end-of-course coding exam for a Big Data Specialist class. The setup had ossified over time: I'd hand-author the exercises, hand-grade dozens of submissions over a weekend, and hand-write per-student feedback reports. It worked, but it didn't scale — and year-over-year consistency drifted because I was the only consistency check.

This year I rebuilt the workflow around **two AI-powered loops**:

1. **Authoring** — a coding agent generates a new yearly edition from a written rubric.
2. **Grading** — each student submission is graded per-exercise by the OpenAI API against a reference solution.

This post is about what I learned: *what to delegate to the AI, what to lock down with code, and where I still keep a human in the loop*. I won't show the actual exam content (it rotates yearly and is not meant to leak), but I'll show the surrounding scaffolding in detail.

## The constraints

The constraints set the shape of everything else:

- **Yearly editions.** Each year I publish a new edition with different specifics, so a leaked solution from last year is useless. The skills tested must stay the same.
- **Mixed delivery.** Several Python exercises (Pandas + SQL), one Power BI exercise, plus two open-ended discussion questions.

These constraints push toward a *templated* approach: the shape of the exam stays fixed, the contents rotate.

---

## Part 1 — Authoring: rubric-driven generation

The hard authoring problem isn't writing one good exercise. It's writing a new set of exercises that together feel **as hard as last year's, no more no less**. If the bonus is too easy this year, top students walk; if it's too hard, the class average tanks. Either way the score distribution becomes incomparable to previous cohorts.

### Step 1: write the rubric first

I wrote a single document — `editions/README.md` — that pins the *shape* of each exercise:

- Difficulty stars (⭐ to ⭐⭐⭐)
- Expected time (10–25 min)
- Concepts tested
- The SQL surface (`WHERE`, `JOIN`, `GROUP BY`, …)
- The Pandas surface (`groupby`, `dt.to_period`, `diff`, `fillna`, …)
- "Authoring guidance" describing **which knobs to turn between editions** and which to leave alone

The rubric is anchored to a known-good edition. So when I author the next year's edition, I'm not inventing complexity from scratch — I'm parametrising the same complexity over a different choice of table, dimension, time bucket, etc. This makes the next edition a *constrained transformation*, not an open-ended creative task — exactly the kind of work an LLM does well.

### Step 2: the authoring loop

<div class="mermaid">
flowchart LR
    R[editions/README.md<br/>complexity rubric] --> A[Coding agent<br/>Claude Code]
    P[Previous edition<br/>e.g. editions/2025/] --> A
    A --> D[Draft new edition:<br/>Esame, esercizio, soluzione, Domande]
    D --> V[Run soluzione.py<br/>against shared DB]
    V -- fail --> A
    V -- ok --> H[Human review:<br/>wording, ambiguity, fairness]
    H --> S[Ship to students]
</div>

I open a coding agent in the repo and prompt with something like:

> *"Generate the 2027 edition. Read `editions/README.md` for the rubric and `editions/2026/` as the most recent example. Create `editions/2027/Esame.md`, `esercizio.py`, `soluzione.py`, `Domande.md`. Verify the solution runs end-to-end against the shared SQLite DB and produces coherent CSVs. Don't reuse the entity from 2026."*

The agent reads the rubric and the most recent edition, drafts the four files following the contracted shape, runs the reference solution against the shared DB, reports row counts and a summary, and stops.

### What I deliberately did NOT delegate

- **Writing the rubric itself.** That's the institutional memory of "what does this exam test, at what level". An LLM shouldn't draft its own exam standards from scratch — but it can faithfully apply standards that already exist.
- **The choice of difficulty caps.** The bonus is hard *on purpose*. The agent doesn't get to make it easier because that's the local optimum on whatever it tried first.
- **Final review.** I read every word of the new edition. The agent is fast, not infallible — and exam wording in Italian needs a native ear.

### Pitfalls I hit, and how the rubric absorbed them

Three real bugs surfaced while authoring the second edition. Each one became a new line in the rubric so it doesn't recur.

The pattern: **whenever the AI got something subtly wrong in a way I had to think about, I codified the lesson in the rubric.** The rubric grows; future editions get safer.

---

## Part 2 — Grading: OpenAI API, one exercise at a time

After the exam, dozens of `esercizio.py` files land in `evaluation/exam_submissions/<student>/`. The hard part of grading isn't producing one good evaluation — it's producing many that are *consistent across students* and *fair across exercises*.

### The bedrock: a section-marker convention

The single most important infrastructure choice was forcing each submission to be **syntactically partitionable**. Each exercise is wrapped in explicit markers:

```python
# === EXCERCISE N START === do not edit this line
... student code ...
# === EXCERCISE N END === do not edit this line
```

Students see this clearly in the template. They are told, in writing and out loud, not to touch these lines. The evaluator's `extract_code_sections` is then a single regex.

### The grading pipeline

<div class="mermaid">
flowchart TD
    A[exam_submissions/<br/>student folder] --> B[load esercizio.py]
    B --> C[extract sections<br/>via marker regex]
    C --> D{for each<br/>exercise N}
    D --> E[build prompt:<br/>description + reference + student code]
    E --> F[OpenAI API call]
    F --> G[parse JSON:<br/>score + feedback]
    G --> H[merge into<br/>code_evaluation.json]
    D --> D
    H --> I[postprocess.py]
    I --> J[student_reports/<br/>Name.md]
</div>

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

Each exercise is graded **independently**. The prompt structure is identical across students.

A few details that made the pipeline reliable:

- **Reference comparison.** Every prompt includes the reference solution's code *for that exact exercise*. The model isn't grading in a vacuum; it's comparing against a known-good version on the same task.
- **Structured JSON output.** A fixed schema makes downstream merging trivial. No prose-parsing fragility.
- **Per-exercise scope.** The model never sees the whole file. It sees one exercise at a time. This keeps the reasoning *local*: a student who failed exercise 1 can still get full marks on exercise 5, and the model isn't tempted to "average vibes" across the file.
- **Resume from cache.** The merged `code_evaluation.json` is the source of truth. Re-running the evaluator only grades students that aren't already in it. A transient API failure no longer restarts a 2-hour batch.

### From JSON to per-student markdown

A short `postprocess.py` fans the merged JSON out into one markdown report per student:

```markdown
# Valutazione Mario Rossi

**Punteggio totale**: 17.0/20
**Percentuale**: 85.0%

## Esercizio 1
**Punteggio**: 5/5
**Feedback**:
- Implementazione corretta e completa
- Buon uso di ORDER BY e di un confronto stretto

## Esercizio 2
**Punteggio**: 4/5
**Punti di forza**:
- Join multi-tabella corretto
**Suggerimenti di miglioramento**:
- Considera l'uso di `parse_dates` direttamente in `read_sql_query`
...
```

Students get one file with a per-exercise breakdown. I do a final spot-check pass on a sample — usually the AI gradings line up with my own, with disagreement clustered on partially-correct solutions where partial credit is genuinely subjective. That's exactly where I want my human time to go.

---

## What stays human

- **Authoring sign-off.** I read every word of every new edition.
- **Open-ended discussion questions.** Each edition includes two `Domande.md` questions probing *why* the student did what they did. These are written or oral, reviewed by me. The signal is exactly the kind of thing that gets flattened by an LLM summary.

## Takeaway

The interesting question isn't "can AI grade exams" or "can AI write exams". Both are demonstrably yes, and have been for a while. The interesting question is **what's the smallest structure I need to put around the AI** so its output is consistent year-over-year and fair across dozens of students.

For me that turned out to be three pieces of scaffolding:

1. A **rubric** that locks down what must stay the same across editions.
2. A **marker convention** that gives the grader a clean unit of work.
3. A **resume cache** that makes the whole pipeline idempotent.

Once those three are in place, the AI does what it's good at — fluent text, code comparison, structured feedback — and I do what I'm good at — judging whether the result is fair, and updating the rubric when it isn't.

Net result: a process that used to take a weekend per edition and a weekend per grading round now takes a few hours of focused human review on top of the AI's first pass. And the year-over-year consistency, which used to live entirely in my head, now lives in a markdown file that I can hand to a colleague.
