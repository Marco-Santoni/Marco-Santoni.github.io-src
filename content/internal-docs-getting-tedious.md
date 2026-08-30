Title: Internal docs getting tedious
Date: 2026-08-30
Status: published

Has AI improved the way we write and maintain internal documentation? Not by default. What I'm seeing is documentation getting *longer*, not more effective.

Maybe I'm biased — I'm not a fan of long text. So when I open a doc page written by an LLM in its default verbose style, that bias kicks in before I've judged the content. I dislike the page even when what's written is perfectly valid.

## What are internal docs for?

That's the question to start from.

Should they cover libraries or tools that are already documented publicly? No — that copy goes stale, and any LLM you're pairing with already knows the public docs. A link beats a stale mirror.

Internal docs should detail only what's specific to your process or your product. Everything else earns a link, not a page.

## LLMs like text. Humans don't.

Left unchecked, an LLM writing docs alongside you pads every section: one sentence becomes a paragraph, one paragraph becomes three. I get bored fast reading long paragraphs, and I doubt I'm the only one.

**Before** (LLM default style):

> In order to configure the retry policy for the ingestion service, it's important to understand that the system provides a flexible mechanism allowing developers to customize how failed requests are retried. This is achieved through a configuration parameter, `retry_policy`, which can be set in the service's configuration file. By adjusting this parameter appropriately, teams can ensure transient failures are handled gracefully without manual intervention, improving the overall reliability of the pipeline.

**After**:

> Set `retry_policy` in the service config to control retries on failed ingestion requests. Default: 3 retries, exponential backoff.

Same information, a fifth of the words.

A few rules I now give my AI assistants when they touch documentation:

| Instead of | Do this |
|---|---|
| Long paragraphs | Fewer words |
| Re-explaining a public library/tool | Link to it, describe only the delta |
| Prose describing a flow | A mermaid diagram |
| Prose listing options or edge cases | A table |

Nothing fancy — just enough friction to stop a doc page from growing for its own sake. I personally instruct my AI assistants with these guidelines.
