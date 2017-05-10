Title: Weighted Random Sampling with PostgreSQL [Follow-up]
Date: 2017-02-10 21:00
Slug: weighted_random_sampling_follow_up
Status: published

> I received valuable feedbacks by [Jim Nasby](https://www.linkedin.com/in/decibel/) regarding [the post](http://www.marcosantoni.com/2016/08/23/weighted-random-sampling-with-postgresql.html) about weighted random sampling with PostgreSQL. I will report here Jim's email.

Sadly, Common Table Expressions (CTE)s are *insanely* expensive, because
each one must be fully materialized. So in your example, you're
essentially creating 5 temp tables (one for each CTE). Obviously that's
not a big deal with only 4 weights and 1000 samples, but for other use
cases that overhead could really add up. Note that this is not the same
as the `OFFSET 0` trick...
You can get a similar breakdown of code by using subselects in `FROM`
clauses. That would look something like:

```sql
SELECT color
   FROM (<samples code>) AS samples
   JOIN (
     SELECT <cumulative_bounds SELECT>
       FROM (
         SELECT <sampling_cumulative_prob SELECT>
           FROM (....)
        ) AS sampling_cumulative_prob
     ) AS cumulative_bounds ON ...
```

Not as nice as `WITH`, but not horrible. You can also create temporary
views for each of the intermediate steps.

in weights_with_sum, you can get rid of the `join` in favor of `sum(weight)
OVER() AS weight_sum`.

Finally, `random()` produces `0.0 <= x < 1.0`, so the bounds on the `numrange`
should be `'[)'`, not `'(]'`. Personally, I would just create the `numrange`
immediately in `cummulative_bounds`, but that's mostly just a matter of style.

BTW, if you've got `plpythonu` loaded there's probably an easier way to
generate the set of ranges, which could then be joined to the random
samples.

BTW, `width_bucket(operand anyelement, thresholds anyarray)` (see *second*
instance on [docs](https://www.postgresql.org/docs/current/static/functions-math.html))
might be even faster; it'd definitely be simpler:

```sql
SELECT color[width_bucket(random(), thresholds)
   FROM generate_series(1,1000)
     , (
       SELECT array_agg(color) AS colors
           , array_agg(cum_prod) AS thresholds
         FROM sampling_cumulative_prod
     ) AS prob;
```
