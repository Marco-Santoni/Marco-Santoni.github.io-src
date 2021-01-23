Title: Models of Data Science teams: Chess vs Checkers
Date: 2021-01-31 09:35
Slug: chess_vs_checkers_teams
Status: draft

One of the key decisions to take when building a data science team is the **mix of roles**. This means choosing the right mix of background and of activities that each member of the team should have. I'll compare two models of teams I've experienced so far and define them as **chess-team** model and **checkers-team** model.

## Chess-Team Model

The chess-team model is the common model we read about in literature. In a chess-team, each member of the team has a **specific role**. Roles are usually: _data engineers_, _data scientists_, and _machine learning engineers_. These roles typically correspond to different set of skills (eg ML and statistics vs coding and devops) and to different set of activities (model selection vs data preparation vs model deployment).

Similarly to a chess piece which has a clear role that is different from the other pieces, a member of a data science chess-team is assigned a subset of tasks in the development pipeline. Let's consider a simplistic development pipeline:

- data extraction
- model development
- model deployment

The three activities of this development pipeline correspond to the three roles of the team, and there is little space for confusion. A data engineer probably won't work a lot on the model development and selection, while a data scientist probably won't be the one deploying the model in production.

## Checkers-Team Model

The checkers-team model is a definition of a team model that I introduce in this post. In a checkers-team, each member of the team does not have a specific role because he may  in charge of working on **any step of the development** pipeline. There are no roles like _data engineer_ or _data scientist_ because taking such a role implies limiting the scope of activities a team member should work on. Let' make an example. In a checkers-team, there is no _data scientist_ because no one is in charge of model development only.

So, what is the role of someone working in a checkers-team? A member of the team can be defined as a **full-stack data developer**. A full-stack data developer is someone that for example works on data extraction _AND_ model development _AND_ model deployment. In a checkers-team, everyone works possibly on every piece of the development lifecycle. In this sense, the team is more similar to checkers pieces. There is no move that a piece can take and another piece cannot. Similarly, there is no activity that any team member cannot do. For example, everyone can contribute to building devops pipelines and automation.

Of course, every team member has a different **background** and a different set of skills from his/her teammates. One can come from a software engineering experience, another one can come from data science studies. However, the strategy of building a checkers-team is to invest in **training** team members to grow horizontally their set of skills.

## Pros and Cons

Let's consider some key differences between a chess and a checkers team model.

**Flexibility.** The balance of types of activities is not stable over time in a team. There can be times when there is a peak of work items in data engineering and little or no work items in ML model development. These peaks can be due to different phases of the data product development cycle or due to varying business requirements. A checkers-team is flexible and can adapt quickly to these peaks. A checkers-team could for example dedicate the entire team to develop data engineering pipelines in a Scrum sprint if needed. The same flexibility is not as easy in a chess-team model where you have constraints due to different skills and different responsibilities.

**Complexity.** Not every data science team is facing the same level of complexity in their projects. Imagine a team that is building an AI model for self-driving cars. It is a complex problem to solve that requires advanced skills in computer vision and AI. These skills cannot be learned quickly but usually need a specific education or career path. When facing such problems, you need team members which are specialists in area like vision or AI. A chess-team is designed to host specialists in certain fields and is designed to grow vertically such skills. In a checkers-team, there are not such specialists.

**awareness** and ownership of end-to-end


## When is a Team Model Right?
data science team is working on the core product of the company?
size of the team? medium to small?
saas and paas make it possible with litte effort
