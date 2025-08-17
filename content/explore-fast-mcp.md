Title: Learn basics of MCP with FastMCP
Date: 2025-08-17 08:35
Slug: explore_fast_mcp
Status: published

I was looking for a resource to get a deeper understanding of MCP (Model Context Protocol). Rather than looking for resources or books, I opted for RTFM. Actually not the MCP manual as I would not have fun reading protocol specs. I took [FastMCP](https://gofastmcp.com/getting-started/welcome) and went through the docs. I was not just reading the docs. While reading the docs, I was:

- sketching a concept map
- coding some basic hello-world examples

I enjoyed this approach because it was quite rapid (I could not invest days but rather hours) while practical and hands on. The concept map helps keeping some notes for me in future. Notes you write by yourself are the ones that stick best.

## Concept map

I used [draw.io](https://www.drawio.com/) to draw the concept map and exported to SVG for best web rendering. You can explore it here 👇

<img src="./images/fastmcp_concepts.svg" width="800" alt="A concept diagram of the main FastMCP Pyhon library components." />

## Little codebase

I made a basic server and client with streamable HTTP transport mode. Everything is in this [repo](https://github.com/Marco-Santoni/explore-fast-mcp). There is a basic example for each key component of an MCP server

- tool
- resource
- prompt

## Opinions about MCP

I'll share a couple of opinions I got while exploring MCP and FastMCP.

### Evolving rapidly

FastMCP is evolving according to the MCP specs of course. These specs are quite recent. The first stable version was in November 2024 while the latest (and third) in June 2025. I read about an important feature like _Structured Output_ and found it was only [few weeks old](https://modelcontextprotocol.io/specification/2025-06-18/changelog) at the time of my reading. It is a great sign that things are moving so fast, but, at the same time, you should consider this quick evolution if you're working on a **production-ready** application.

You may want to stay simple and minimize the overall engineering investment. You may find yourself investing in engineering features that few months later might be supported by the protocol or by the ecosystem

## Good design

I appreaciated the design of the protocol and of FastMCP itself. It is simple enough and based on three elements (tools, resources, prompts), but still catches a large amount of needs of agent applications. There are useful interfaces and features for common needs like

- interactive input by users
- progress monitoring
- logging and messaging
- sampling from client's LLM

The design is **composable** making it scalable for larger applications. An MCP server can literally _import_ another MCP server or mount it. The name-clashes or duplicates can be handled explictly by developers.

## Rich ecosystem

FastMCP is one example of the ecosystem of tools and frameworks that is growing around MCP. The ecosystem is what matters (more than the protocol design).

## Engineering is still THE thing

Building an MCP server is still an engineering and design job. Should feature X of my server be a resource? Or a tool? Should this input be parametrized? There will be no correct or wrong answers to these questions. Design styles will emerge and the touch of software architects will emerge to make sure things can scale and are easy to maintain.
