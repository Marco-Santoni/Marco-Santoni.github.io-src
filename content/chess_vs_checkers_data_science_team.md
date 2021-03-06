Title: Models of Data Science teams: Chess vs Checkers
Date: 2021-01-31 09:35
Slug: chess_vs_checkers_teams
Status: published

> How many data engineers should we hire? Are they too many compared to our data scientists?

One of the key decisions to take when building a data science team is the **mix of roles**. This means choosing the right mix of background and of activities that each member of the team should have. I'll compare two models of teams I've experienced so far and define them as **chess-team** model and **checkers-team** model.

## Chess-Team Model

The chess-team model is the common model we read about in literature. In a chess-team, each member of the team has a **specific role**. Roles are usually: _data engineers_, _data scientists_, and _machine learning engineers_. These roles typically correspond to different sets of skills (eg ML and statistics vs coding and devops) and to different set of activities (model selection vs data preparation vs model deployment).

Similarly to a chess piece which has a clear role that is different from the other pieces, a member of a data science chess-team is assigned a subset of the tasks that are part of the development pipeline. Let's consider a simplistic development pipeline:

- data preparation -> data engineer
- model development -> data scientists
- model deployment -> machine learning engineer

The three activities of this development pipeline correspond to the three roles of the team, and there is little space for confusion. A data engineer probably won't work a lot on the model development and selection, while a data scientist probably won't be the one deploying the model in production.

## Checkers-Team Model

The checkers-team model is a definition of a team model that I introduce in this post. In a checkers-team, each member of the team does not have a specific role because he may  in charge of working on **any step of the development** pipeline. There are no roles like _data engineer_ or _data scientist_ because taking such a role implies limiting the scope of activities a team member should work on. Let' make an example. In a checkers-team, there is no _data scientist_ because no one is in charge of model development **only**.

So, what is the role of someone working in a checkers-team? A member of the team can be defined as a **full-stack data developer**. A full-stack data developer is someone that for example works on data extraction _AND_ model development _AND_ model deployment. In a checkers-team, everyone works possibly on every piece of the development lifecycle. In this sense, the team is more similar to checkers pieces. There is no move that a piece can take and another piece cannot. Similarly, there is no activity that any team member cannot do. For example, everyone can contribute to building devops pipelines and automation.

Of course, every team member has a different **background** and a different set of skills from his/her teammates. One can come from a software engineering experience, another one can come from data science studies. However, the strategy of building a checkers-team is to invest in **training** team members to grow **horizontally** their set of skills.

## Pros and Cons

Let's consider some key differences between a chess and a checkers team model.

**Flexibility.** The balance of types of activities is not stable over time in a team. There can be times when there is a peak of work items in data engineering and little or no work items in ML model development. These peaks can be due to different phases of the data product development cycle or due to varying business requirements. A checkers-team is flexible and can adapt quickly to these peaks. A checkers-team could for example dedicate the entire team to develop data engineering pipelines in a Scrum sprint if needed. The same flexibility is not as easy in a chess-team model where you have constraints due to different skills and different responsibilities.

**Complexity.** Not every data science team is facing the same level of complexity in their projects. Imagine a team that is building an AI model for self-driving cars. It is a complex problem to solve that requires advanced skills in computer vision and AI. These skills cannot be learned quickly but usually need a specific education or career path. When facing such problems, you need team members which are specialists in area like vision or AI. A chess-team is designed to host specialists in certain fields and is designed to grow vertically such skills. In a checkers-team, there are not such specialists.

**Awareness.** A member of a checkers-team knows in details every phase of the development cycle. While he is designing a ML model, he is aware at the same time of how the release pipeline and the operations of the model work. He may take decisions during model selection that take into consideration where the model will be hosted and possible constraints of the production platform. On the other hand, a data scientist of a chess-team knows less details (because he has not being working on it by himself) of how the model will be deployed and run. This minor awareness may lead to assumptions taken during model development, and these assumptions can bring to more complexity to those in charge of deploying such model.

**Sense of Ownership.** In a checkers-team, you are in charge of both engineering data pipelines, developing models, and deploying them. Any issue that may occur in these phases is also _your_ issue. You can't delegate too much, and, therefore, you naturally feel responsible to contribute to the resolution. Distributing the ownership makes every team member more active in improving the development life cycle.

## When is a Team Model Right?

The answer depends on the context and the organization you work at. Is the data science team is working on the **core product** of the company? If this is the case, the models that are developed may need a level of specialization that can't just be achieved by a checkers-team.

Or is the team rather working on adding tiny features or on improving the operations of the company? In this case, probably you won't be developing state-of-the-art AI models, and you can rely existing **libraries or SaaS** that make life easier for you. As complexity is not an obstacle, going for checkers-team may be a good option.

What is the size of your data science team? Or even how many teams do you have? Large organizations go for multiple data teams. These teams may be divided **functionally** (eg 1 team of data engineers + 1 separate team of data sciensts) or they may be divided by **business units** (eg 1 data team for marketing and 1 data team for recommender system). You can't of course adopt the checkers-team model in an large organization that design the data teams by functions, but you may still adopt this model in a large organization that creates multiple self-organized teams each dedicated to a specific business unit.

A last point to consider is the **IT architecture**. A checkers-team requires the same person to work on very different tasks. This is viable only if the complexity of such tasks is small. Adopting **SaaS and PaaS** resources simplifies every task by hiding the complexity of managing and running the resources. They let you focus on your goal. For example, building an API endpoint hosted by a function-as-a-service is something feasible by a data scientist with a mathematical background. Doing the same from scratch on an on-premise server is not as feasible.
