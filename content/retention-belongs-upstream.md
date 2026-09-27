Title: Retention belongs upstream
Date: 2026-09-27
Status: published

Should a data lake decide when to delete data? The intuitive answer is yes: it stores the data, so it should clean it up.

I think the opposite. A data lake should not have retention rules of its own. It should execute the rules of whoever owns the data, reliably and verifiably.

I recently took part in a review of how retention works on a data lake. The interesting part wasn't the technology. It was deciding *who* gets to decide.

## The trap: a second set of rules

The source system that produces the data already has retention rules. A customer record lives for N years after the contract ends. A transaction is kept for a period set by business rules.

If the data lake defines its own retention on top of that, you now have two sources of truth. They drift. The source changes a rule, the lake doesn't notice. Nobody owns the gap between the two, and that gap is where the risk lives.

## Retention follows the chain of contracts

The model I argue for: retention flows along the same contracts that data flows along. Each link applies what it receives from upstream.

<div class="mermaid">
flowchart LR
    S[Source system<br/>owns the rules] -- contract --> SA[Source-aligned<br/>data product]
    SA -- contract --> CA[Consumer-aligned<br/>data product]
    S -. deletion events .-> SA
    SA -. deletion events .-> CA
    P[Platform<br/>standards + automation] -. enforces .-> SA
    P -. enforces .-> CA
</div>

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

A **source-aligned data product** has no retention logic. It applies the rules of its source system, as stated in the contract between them. When the source deletes a record, it emits a deletion event, and the data product removes the record. The source decides; the data product follows.

Why? Because the owner of the business logic is the owner of the retention logic. The team that knows what a record *means* is the team that knows how long it may live. A data engineer on the lake side can't answer that question, and shouldn't try.

## Consumer-aligned products are where it gets hard

One level down, the same pattern should apply: the source-aligned product is upstream, the consumer-aligned product follows.

But a consumer-aligned product rarely maps one to one to a single input. It joins data from two domains. It aggregates. It anonymises. When a record is deleted upstream, what happens to a monthly aggregate that counted it? To a feature table that combined it with data from another domain?

Pure inheritance doesn't answer that. Someone has to decide. I see two options:

| | Upstream contract decides | Downstream owner decides |
|---|---|---|
| Where the rule lives | In the upstream contract: "aggregates may be kept, raw records must go" | In the consumer-aligned product's own retention policy |
| Strength | Explicit, one owner per rule | Flexible, fits cross-domain products |
| Weakness | Contracts get complex fast, especially across domains | Less standardisation, more policies to verify |

Neither is free. The upstream contract keeps ownership clean but pushes a lot of complexity into contracts. Downstream ownership is pragmatic, but only works if that owner is real, named, and accountable. What matters is that the choice is explicit. A consumer-aligned product with *no* declared answer is the one that will keep deleted data forever.

## The platform enforces the standard, not the policy

So what's left for the platform? A lot, actually. The platform doesn't decide *what* the retention is. It decides *how* retention is expressed, propagated and checked, in the same way for every domain.

A few mechanisms that make this concrete:

- **Retention as a mandatory contract field.** A data product can't be deployed without declaring its retention: either inherited from a named upstream contract, or owned, with a named owner. Validated in CI, not in a spreadsheet.
- **Standard deletion events.** One event format for "this record is gone", propagated automatically along the lineage. Every data product that consumes it logs that it was applied.
- **Automated drift checks.** Periodic jobs compare what the contract declares with what the storage actually holds: records older than their retention, deletion events never acknowledged, products whose upstream contract has changed.

The platform is strict on the form and neutral on the content. That's what gives you a standard across domains without centralising decisions the platform isn't qualified to make.

## The hard part is ownership

The tools to delete data, propagate events and run checks mostly exist already. What doesn't exist by default is a clear answer to "who decided this retention, and who checks it's still applied?"

Without that answer, the risk stays, whatever the tooling. With it, the data lake stops being the place where retention is decided and becomes what it should be: the place where it's executed.
