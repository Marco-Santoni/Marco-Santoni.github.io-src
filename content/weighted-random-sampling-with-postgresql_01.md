Title: Weighted Random Sampling with PostgreSQL
Date: 2016-08-23 16:22
Author: mrsantoni
Category: Code
Slug: weighted-random-sampling-with-postgresql
Status: published

You have a table like the following:

\[code language="sql"\]  
CREATE TABLE weights (  
color varchar primary key,  
weight float  
);

INSERT INTO weights (color, weight)  
VALUES  
('red', 8),  
('blue', 3),  
('green', 10),  
('yellow', 10);  
\[/code\]

The table lists the weights associated with certain colors. Imagine a
weight representing how much you like that color.

Now, you want to add 1000 colored tiles to your website. You want the
color of the tiles to be **sampled at random** according to the
*weights* table.

We'll write a PostgreSQL script that implements such random sampling.
I'll write the **entire query first**, and then explain each part
separately.

\[code language="sql"\]  
CREATE TABLE sampled\_colors AS  
WITH weights\_with\_sum AS (  
SELECT  
color,  
weight,  
weight\_sum  
FROM weights  
CROSS JOIN (SELECT sum(weight) AS weight\_sum FROM weights) s  
),  
sampling\_probability AS (  
SELECT  
color,  
weight / weight\_sum AS prob  
FROM weights\_with\_sum  
),  
sampling\_cumulative\_prob AS (  
SELECT  
color,  
sum(prob) OVER (order by color) AS cum\_prob  
FROM sampling\_probability  
),  
cumulative\_bounds AS (  
SELECT  
color,  
COALESCE(  
lag(cum\_prob) OVER (ORDER BY cum\_prob, color),  
0  
) AS lower\_cum\_bound,  
cum\_prob AS upper\_cum\_bound  
FROM sampling\_cumulative\_prob  
),  
samples AS (  
SELECT  
generate\_series(1, 1000) AS sample\_idx,  
random() AS sample  
)  
SELECT  
color  
FROM samples  
JOIN cumulative\_bounds ON  
sample::numeric &lt;@ numrange(lower\_cum\_bound::numeric,
upper\_cum\_bound::numeric, '(\]');  
\[/code\]

Let's look at one piece at a time.

\[code language="sql"\]  
WITH weights\_with\_sum AS (  
SELECT  
color,  
weight,  
weight\_sum  
FROM weights  
CROSS JOIN (SELECT sum(weight) AS weight\_sum FROM weights) s  
),  
sampling\_probability AS (  
SELECT  
color,  
weight / weight\_sum AS prob  
FROM weights\_with\_sum  
)  
SELECT \*  
FROM sampling\_probability;  
-- output:  
color | prob  
--------+--------------------  
red | 0.258064516129032  
blue | 0.0967741935483871  
green | 0.32258064516129  
yellow | 0.32258064516129  
\[/code\]

Here, we're just normalizing the weights. Each weight is divided by the
total sum of the weights. In this way, we are re-writing each weight as
a **discrete probability** of that color being sampled.

\[code language="sql"\]  
...  
sampling\_cumulative\_prob AS (  
SELECT  
color,  
sum(prob) OVER (order by color) AS cum\_prob  
FROM sampling\_probability  
),  
cumulative\_bounds AS (  
SELECT  
color,  
COALESCE(  
lag(cum\_prob) OVER (ORDER BY cum\_prob, color),  
0  
) AS lower\_cum\_bound,  
cum\_prob AS upper\_cum\_bound  
FROM sampling\_cumulative\_prob  
)  
SELECT \*  
FROM cumulative\_bounds;  
-- output:  
color | lower\_cum\_bound | upper\_cum\_bound  
--------+--------------------+--------------------  
blue | 0 | 0.0967741935483871  
green | 0.0967741935483871 | 0.419354838709677  
red | 0.419354838709677 | 0.67741935483871  
yellow | 0.67741935483871 | 1  
\[/code\]

In this piece of code, we're are representing the weights as a
**cumulative** distribution function.

\[code language="sql"\]  
...  
samples AS (  
SELECT  
generate\_series(1, 1000) AS sample\_idx,  
random() AS sample  
)  
SELECT  
color  
FROM samples  
JOIN cumulative\_bounds ON  
sample::numeric &lt;@ numrange(lower\_cum\_bound::numeric,
upper\_cum\_bound::numeric, '(\]');  
\[/code\]

In the last part, we're sampling 1000 times a random number between 0
and 1. We then assign this sample to the corresponding color based on
the values of the cumulative function. For example, if the first sample
is 0.45, it will match the *'red'* range (0.41-0.67). Therefore, that
sample will be *'red'*.

The result of the query is a table filled with 1000 colors sampled at
random based on the weights.

\[code language="sql"\]  
SELECT \*  
FROM sampled\_colors  
LIMIT 10;  
-- output:  
color  
--------  
green  
green  
red  
yellow  
yellow  
green  
blue  
red  
red  
red  
\[/code\]

Can we check that the result is correct? Were the weights really taken
into account?

\[code language="sql"\]  
SELECT  
color,  
count(\*)  
FROM sampled\_colors  
GROUP BY 1;  
-- output:  
color | count  
--------+-------  
yellow | 309  
green | 320  
red | 276  
blue | 95  
\[/code\]

The proportion of samples is quite close to the proportion of the
weights. This similarity is clear if we compare this table with the
discrete probability table above.
