Title: Backtest your guardrails
Date: 2026-11-01
Status: published

Putting a guardrail in front of every LLM is easy. Knowing how many legitimate prompts it will block is much harder.

Once an LLM gateway becomes the central entry point of a platform, it's the obvious place for cross-cutting controls. Prompt injection and jailbreak detection are the first candidates. One config change, and every assistant behind the gateway is protected.

That's exactly the trap. I recently took part in an architecture review on guardrails, and the decision we reached was not to start with enforcement. We start with a backtest.

## A guardrail is a classifier

A guardrail looks at a prompt and decides: allow or block. That makes it a classifier, and like any classifier it is wrong in two ways:

- **False negative**: an attack goes through.
- **False positive**: a legitimate prompt gets blocked.

We'd never deploy a classifier in front of every request without measuring its errors first. A guardrail doesn't get an exemption because it's labelled "security".

## The error you don't see

The two errors aren't equally visible.

A missed injection becomes an incident. Someone notices, someone investigates, someone tunes the policy.

A blocked legitimate prompt becomes a user who rephrases, gives up, or quietly stops using the assistant. Nobody opens a ticket for that. The cost is real, but it never reaches the team that configured the guardrail.

So teams naturally optimise for the error they can see. That's how a security control turns into a quality problem.

Base rates make it worse. Most traffic is legitimate. Take illustrative numbers: 100,000 prompts, 1 in 1,000 is an attack, and the guardrail catches 90% of attacks while wrongly flagging 1% of legitimate prompts.

| | Count |
|---|---|
| Attacks | 100 |
| Attacks blocked | 90 |
| Legitimate prompts | 99,900 |
| Legitimate prompts blocked | **999** |

A guardrail that sounds accurate blocks about eleven legitimate prompts for every attack it stops. The numbers are made up; the shape isn't.

## Backtest on the traces you already have

If your LLM traffic is already traced (in our case with MLflow), you already have an evaluation set: real conversations, from real users, on real use cases.

The idea is the same as backtesting a trading strategy. You don't run it with real money first. You replay history through it and look at what it would have done:

- which requests get intercepted
- where false positives and false negatives show up
- which configurations deserve to move to the next step

The output isn't just a metric. Every flagged trace is something a human can review and label, and those labels are evidence for deciding whether a policy is ready.

## What a backtest can't tell you

There's a catch. Historical production traffic is overwhelmingly benign. Replaying it tells you a lot about false positives, and very little about false negatives: you can't measure how many attacks you miss if there are almost none in the data.

So a backtest on real traces answers one question well: *what would this policy break?* For *what would it miss?*, you need a different set: seeded or red-team prompts. The two complement each other; neither replaces the other.

## Observe, evaluate, enforce

The pattern isn't new. Browsers have `Content-Security-Policy-Report-Only`. WAFs run in detection mode before prevention mode. In [fitness functions]({filename}fitness-functions-data-mesh.md), a policy can warn before it fails the build.

Guardrails should follow the same path:

<div class="mermaid">
flowchart LR
    T[Historical traces] --> E[Policy in<br/>evaluation mode]
    E --> R[Review + labels<br/>FP / FN evidence]
    R -- promote --> P[Policy in<br/>enforcement mode]
    U[Live traffic] --> G[LLM Gateway]
    P -. applied at .-> G
    G --> L[LLM]
</div>

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

Two design choices matter here:

- **Evaluation is separate from live traffic.** The backtest runs offline on stored traces. Nothing in the production path changes while we're measuring.
- **Promotion is an explicit step.** A policy moves from evaluation to enforcement because the evidence supports it, not because it was easy to switch on.

One global policy is also unlikely to fit everything. What looks "normal" for a coding assistant is very different from what looks normal for a document assistant. The gateway is the right place to *apply* guardrails; it's not necessarily the right place to assume one configuration fits all.

## The hard part is deciding when a policy has earned the right to block

We're at the start: the design is settled, the backtest is about to run. I don't have results to share yet.

But the question has already changed. It's no longer "which guardrails do we turn on?" It's "what evidence do we need before a guardrail is allowed to say no?" That's a question the gateway can't answer. The traces can.
