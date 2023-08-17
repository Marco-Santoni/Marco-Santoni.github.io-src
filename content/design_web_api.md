Title: Reading "The Design of Web APIs"
Date: 2023-08-27 07:35
Slug: design_web_api
Status: published

Why bothering reading a book about design of web APIs when working in data science like I do? I found this book called _The Design of Web APIs_ by [Arnaud Lauret](https://apihandyman.io/about/) and decided to give it a try.

![The Design of Web APIs]({static}/images/bookshelf/webapi.jpg)

## Why reading it

Data science is shifting towards turning models and solutions as API products. And this can be true not only when you develop a product you actually sell publicly. Even when developing a data product inside an organization, you may want to expose your data service via APIs.

So, when you are at this point of developing an APIs, there are plenty of design decisions to take (eg which routes to expose, which result codes, which response payload, etc.). If you start this design process without some guidelines, you may spend plenty of energies on trying to answer these design questions or even risk to introduce technical debt that you will pay later.

## What is the book about

The book states that, when you take the role of an _API designer_, you are just like a designer of real-world object. An API is made for users and shuold help **them** to achieve **their** goals. API designers should avoid that internal details of the backend affect the design of the APIs. The focus of the designer is to simplify the job of the consumer.

> Usability is what distinguishes awesome APIs from mediocre or passable ones.

The book is focused on shifting your point of view **from the provider to the consumer**. It may seem obvious and everyone might agree on it, but it is not that straightforward to make it happen because we may have bias or we may take design shorcuts that simplify the development of our backend. The author introduces methods like _API goals canvas_ to help us listing out the needs of the user and focusing on them.

![Example of design tradeoffs]({static}/images/api_design_tradeoff.png)

You will find in the books charts or schemas like the one above that explain the design choices you can face on a daily basis. In this example, you may want to stick to fully REST compliace with a `POST /orders`. Or you may want to relax this constraint via a non-REST design like `POST /cart/check-out` that might actually be more intuitive for the consumer developers.

## And more technicalities

The book has a focus on these design choices (eg the _resource expansion_ pattern for nested object in API responses), but is a good source of knowledge to learn more about some technical details around APIs that you can use on a daily basis. For example, you will read chapters about

- OpenAPI Specification
- OAuth2
- features of HTTP you might not be using (eg there are around 200 different standard HTTP headers)
- data format standards like _ISO 4217_ for currrencies or _ISO 8601_ for date and time-related data
- etc.

## All about dev experience

It is the first book I read so far entirely dedicated to developer experience. How can we improve the productivity and the overall satisfaction of the developers using our APIs?

By reading it, you can learn an approach that goed beyond designing web APIs. You learn to focus on what simplifies the life of a developer, and I'm sure this thinking has an effect on how you write your code, your internal tools or even your docs.
