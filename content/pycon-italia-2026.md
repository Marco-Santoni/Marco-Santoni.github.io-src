Title: Talk at PyCon Italia 2026
Date: 2026-05-28
Slug: pycon-italia-2026
Status: published

<img src="../images/pycon-italia-2026/talk1.jpeg" width="400" />

In May 2026 I had the opportunity to speak at [PyCon Italia 2026](https://2026.pycon.it/en/event/chatting-with-data-safely-role-based-authorization-for-text-to-sql-agents) together with my colleague Igor Saggese. The talk was titled **"Chatting with Data, Safely: Role-Based Authorization for Text-to-SQL Agents"**.

Text-to-SQL agents let users query databases in plain language — which is powerful, but also opens up real security concerns: what happens when a user asks for data they're not supposed to see? Our talk addressed exactly this problem.

We presented the architecture we built at TeamSystem to enforce role-based access control on top of a Text-to-SQL pipeline. The core idea is to use [Open Policy Agent (OPA)](https://www.openpolicyagent.org/) as a policy manager that sits between the agent and the database. OPA evaluates each generated SQL query against a set of access policies before execution, ensuring that users can only retrieve data they are authorised to see — regardless of how they phrased the question.

<img src="../images/pycon-italia-2026/talk2.jpeg" width="400" />

A key insight from our work is that policies need to operate at the *row and column level*, not just at the table level. A manager can access all payroll records for their company; an employee can only access their own. OPA's partial evaluation makes it possible to translate these rules into SQL filters that are injected into the query at runtime, decoupling the policy logic entirely from the application code.

The talk was well received, and the Q&A showed strong interest in how to handle policy edge cases and multi-tenant scenarios. PyCon Italia was a great venue — an engaged audience and a lot of productive conversations afterwards.

The [event page](https://2026.pycon.it/en/event/chatting-with-data-safely-role-based-authorization-for-text-to-sql-agents) has further details about the talk.
