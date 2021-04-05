Title: Book Review: Designing Data-Intensive Applications
Date: 2021-04-10 07:31
Slug: review_designing_data_intensive
Status: published

[Designing Data-Intensive Applications](https://dataintensive.net/) was not a quick-read. Let me be clear, it is not such a long book (the paper version is 400 pages), but it is so dense of information that takes some time to go through. The book covers indeed a broad spectrum of data technologies and is dense of details in each paragraph. So, be ready before starting the journey.

![Ocean of distributed data]({static}/images/data_map.jpg)

What did I learn from the book? I'll take few quotes from my notes.

> An architecture that is appropriate for one level of load is unlikely to cope with 10 times that load. If you are working on a fast-growing service, it is therefore likely that you will need to rethink your architecture on every order of magnitude load increase — or perhaps even more often than that.

We need to be able to test, develop, and change quickly our architecture. The book covers the main data solution designs, but you need a team and an organizaiton that is able to adapt and improve the architecture constantly. And more importantly, avoid [premature optimization](http://wiki.c2.com/?PrematureOptimization) as much as possible. Prefer simplicity over complexity.

> If the same query can be written in 4 lines in one query language but requires 29 lines in another, that just shows that different data models are designed to satisfy different use cases. It’s important to pick a data model that is suitable for your application.

Don't focus on data processing performance only, data models and query languages do matter. The overall simplicity and readability of the solution design should be taken into account when choosing the data model
