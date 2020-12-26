Title: Weighted Random Sampling with PostgreSQL
Date: 2016-08-23 16:22
Slug: 2016/08/23/weighted-random-sampling-with-postgresql
Status: published

You have a table like the following:

```sql
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
```

The table lists the weights associated with certain colors. Imagine a
weight representing how much you like that color.

Now, you want to add 1000 colored tiles to your website. You want the
color of the tiles to be **sampled at random** according to the
*weights* table.

We'll write a PostgreSQL script that implements such random sampling.
I'll write the **entire query first**, and then explain each part
separately.

```sql
CREATE TABLE sampled_colors AS
WITH weights_with_sum AS (
SELECT
color,
weight,
weight_sum
FROM weights
CROSS JOIN (SELECT sum(weight) AS weight_sum FROM weights) s
),
sampling_probability AS (
SELECT
color,
weight / weight_sum AS prob
FROM weights_with_sum
),
sampling_cumulative_prob AS (
SELECT
color,
sum(prob) OVER (order by color) AS cum_prob
FROM sampling_probability
),
cumulative_bounds AS (
SELECT
color,
COALESCE(
lag(cum_prob) OVER (ORDER BY cum_prob, color),
0
) AS lower_cum_bound,
cum_prob AS upper_cum_bound
FROM sampling_cumulative_prob
),
samples AS (
SELECT
generate_series(1, 1000) AS sample_idx,
random() AS sample
)
SELECT
color
FROM samples
JOIN cumulative_bounds ON
sample::numeric <@ numrange(lower_cum_bound::numeric,
upper_cum_bound::numeric, '(]');
```

Let's look at one piece at a time.

```sql
WITH weights_with_sum AS (
SELECT
color,
weight,
weight_sum
FROM weights
CROSS JOIN (SELECT sum(weight) AS weight_sum FROM weights) s
),
sampling_probability AS (
SELECT
color,
weight / weight_sum AS prob
FROM weights_with_sum
)
SELECT *
FROM sampling_probability;
-- output:
color | prob
--------+--------------------
red | 0.258064516129032
blue | 0.0967741935483871
green | 0.32258064516129
yellow | 0.32258064516129
```

Here, we're just normalizing the weights. Each weight is divided by the
total sum of the weights. In this way, we are re-writing each weight as
a **discrete probability** of that color being sampled.

```sql
...
sampling_cumulative_prob AS (
SELECT
color,
sum(prob) OVER (order by color) AS cum_prob
FROM sampling_probability
),
cumulative_bounds AS (
SELECT
color,
COALESCE(
lag(cum_prob) OVER (ORDER BY cum_prob, color),
0
) AS lower_cum_bound,
cum_prob AS upper_cum_bound
FROM sampling_cumulative_prob
)
SELECT *
FROM cumulative_bounds;
-- output:
color | lower_cum_bound | upper_cum_bound
--------+--------------------+--------------------
blue | 0 | 0.0967741935483871
green | 0.0967741935483871 | 0.419354838709677
red | 0.419354838709677 | 0.67741935483871
yellow | 0.67741935483871 | 1
```

In this piece of code, we're are representing the weights as a
**cumulative** distribution function.

```sql
...
samples AS (
SELECT
generate_series(1, 1000) AS sample_idx,
random() AS sample
)
SELECT
color
FROM samples
JOIN cumulative_bounds ON
sample::numeric <@ numrange(lower_cum_bound::numeric,
upper_cum_bound::numeric, '(]');
```

In the last part, we're sampling 1000 times a random number between 0
and 1. We then assign this sample to the corresponding color based on
the values of the cumulative function. For example, if the first sample
is 0.45, it will match the *'red'* range (0.41-0.67). Therefore, that
sample will be *'red'*.

The result of the query is a table filled with 1000 colors sampled at
random based on the weights.

```sql
SELECT *
FROM sampled_colors
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
```

Can we check that the result is correct? Were the weights really taken
into account?

```sql
SELECT
color,
count(*)
FROM sampled_colors
GROUP BY 1;
-- output:
color | count
--------+-------
yellow | 309
green | 320
red | 276
blue | 95
```

The proportion of samples is quite close to the proportion of the
weights. This similarity is clear if we compare this table with the
discrete probability table above.
