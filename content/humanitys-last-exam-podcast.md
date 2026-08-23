Title: Humanity's Last Exam: scores are climbing fast, but the question set has a selection bias
Date: 2026-08-23
Status: published

I listened to the [Linear Digressions](https://lineardigressions.com/episodes/2026/8/16/better-know-a-benchmark-humanitys-last-exam) episode on Humanity's Last Exam (HLE), part of their recurring "Better Know a Benchmark" series. Two things stuck with me: how fast the headline score has moved, and a subtle selection bias baked into how the questions were built.

## The score, and how fast it moved

![HLE Dataset design, [source](https://labs.scale.com/leaderboard/humanitys_last_exam)]({static}/images/humanity_score_overview.avif)

HLE was built by the Center for AI Safety and Scale AI on a simple, almost aggressive premise: collect thousands of graduate-level questions, across a huge spread of domains, that human experts could answer but AI models couldn't. At launch, that worked. While benchmarks like MMLU and GPQA were already saturating — models clearing 60-80%+ — the best models on HLE scored somewhere between 3% and 13%.

A year later, top models are clearing 50% and climbing. A benchmark designed to be "the last exam" is being chewed through far faster than its authors expected. The episode also flags something practical: the same model can show a 10-18 percentage point spread depending on which leaderboard reports it (Scale's own, llmstats.com, artificialanalysis.ai), which is a good reminder that "the score" on any benchmark is really a score-plus-methodology, not a single number.

## The bias in how questions were selected

The more interesting part of the episode, to me, is the curation pipeline. One of the first filtering steps for a candidate HLE question was an "LLM difficulty check": if an LLM could already answer it correctly, the question was thrown out.

That sounds like a reasonable way to keep a benchmark hard. But it has a nasty side effect — it systematically selects for questions where the credited (human-written) answer might actually be *wrong* and the LLM's rejected answer was *right*. Any question where the model happened to be correct got filtered out of the set, regardless of whether the model was correct because it reasoned well or because the "expert" answer was flawed. The pipeline had no way to tell those two cases apart, and it structurally favored the second explanation whenever there was a mismatch, since human answers were trusted by default. The episode cites estimates that roughly 30% of the chemistry and biology answers may be wrong for exactly this reason.

It's a good illustration of a general trap in benchmark design: optimizing a dataset for "makes the model fail" is not the same as optimizing it for "measures a real capability gap." If your filter for inclusion correlates with your filter for correctness, you've quietly built ground-truth noise into the part of the benchmark that matters most — the hard tail everyone is trying to close.

## Takeaway

Rising HLE scores are genuine progress, but the 50%-and-climbing number should be read next to the label-noise caveat, not instead of it. When a benchmark is explicitly built to be adversarial to the systems it measures, the adversarial selection process itself becomes something you have to audit — not just the model.

### References

[Linear digressions](https://lineardigressions.substack.com/p/better-know-a-benchmark-humanitys)

Image above: [Scale labs](https://labs.scale.com/leaderboard/humanitys_last_exam)

