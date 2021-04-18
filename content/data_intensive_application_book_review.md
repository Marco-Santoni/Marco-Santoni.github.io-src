Title: Book Review: Designing Data-Intensive Applications
Date: 2021-04-10 07:31
Slug: review_designing_data_intensive
Status: published

[Designing Data-Intensive Applications](https://dataintensive.net/) by Martin Kleppmann was not a quick-read. Let me be clear, it is not such a long book (the paper version is 400 pages), but it is so dense of information that takes some time to go through. The book covers indeed a broad spectrum of data technologies and is dense of details in each paragraph. So, be ready before starting the journey.

![Ocean of distributed data]({static}/images/data_map.jpg)

What did I learn from the book? I'll take few quotes from my notes.

> An architecture that is appropriate for one level of load is unlikely to cope with 10 times that load. If you are working on a fast-growing service, it is therefore likely that you will need to rethink your architecture on every order of magnitude load increase — or perhaps even more often than that.

We need to be able to test, develop, and change quickly our architecture. The book covers the main data solution designs, but you need a team and an organizaiton that is able to adapt and improve the architecture constantly. And more importantly, avoid [premature optimization](http://wiki.c2.com/?PrematureOptimization) as much as possible. Prefer simplicity over complexity.

> If the same query can be written in 4 lines in one query language but requires 29 lines in another, that just shows that different data models are designed to satisfy different use cases. It’s important to pick a data model that is suitable for your application.

Don't focus on data processing performance only, data models and query languages do matter. The overall simplicity and readability of the solution design should be taken into account when choosing the data model.

> On the surface, a data warehouse and a relational OLTP database look similar, because they both have a SQL query interface. However, the internals of the systems can look quite different, because they are optimized for very different query patterns. Many database vendors now focus on supporting either transaction processing or analytics workloads, but not both.

We experienced this difference in my team. We started by building a data warehouse on top of SQL, but we run into performance issues quite soon. The statement by Kleppmann may seem obvious, but there are plenty of organization building data warehouses on SQL for a variety of reasons.

> ... we will explore some of the most common ways how data flows between processes: via databases,  via service calls (eg REST and RPC), and via asynchronous message passing (eg MQTT, AMQP).

I find this an amazing summary. In the end, any data flow architecture falls in one these 3 categories, isn't it true?

> When you deploy a new version of your application (of a server-side application, at least), you may entirely replace the old version with the new version within a few minutes. The same is not true of database contents: the five-year-old data will still be there, in the original encoding, unless you have explicitly rewritten it since then. This observation is sometimes summed up as data outlives code.

Migrating data is harder than updating an application (and there are richer tools available for deploying an application than migrating a database).
