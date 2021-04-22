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

> May your application’s evolution be rapid and your deployments be frequent.

I love this wish 😊

> All of the difficulty in replication lies in handling changes to replicated data, and that’s what this chapter is about. We will discuss three popular algorithms for replicating changes between nodes: _single-leader_, _multi-leader_, and _leaderless replication_. Almost all distributed databases use one of these three approaches.

I found this quote in the introduction to the _Replication_ chapter of the book. I heard often mentioning these replication mechanism, but for the first time I did a deep dive in the topic (that is not as easy as I would have expected). Kleppmann throughout the book makes you clear one thing: there are many things that can go wrong around data (timestamp alignment, networking, nodes down, etc), and they will go wrong at some point.

> Because of this risk of skew and hot spots, many distributed datastores use a hash function to determine the partition for a given key. A good hash function takes skewed data and makes it uniformly distributed.

And fortunately this hashing is often managed under the hood by datastores themselvs, eg Azure Cosmos.

> Atomicity, isolation, and durability are properties of the database, whereas consistency (in the ACID sense) is a property of the application. The application may rely on the database’s atomicity and isolation properties in order to achieve consistency, but it’s not up to the database alone. Thus, the letter C doesn’t really belong in ACID.

Interesting to read that the _C_ in such a popular acronym is there just to make the acronym work.

> Errors will inevitably happen, but many software developers prefer to think only about the happy path rather than the intricacies of error handling.

True story, but experience helps thinking a bit more to the _sad path_.

> Simply dumping data in its raw form allows for several such transformations. This approach has been dubbed the sushi principle: "raw data is better"

I have been following the _sushi principle_ in the last year without being aware of this definition. Nice name!
