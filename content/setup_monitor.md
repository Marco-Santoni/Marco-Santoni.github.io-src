Title: Is Lakehouse Monitoring worth it?
Date: 2025-08-23 09:41
Status: published

I've created a toy Lakehouse Monitoring in Databricks setup to explore its features and capabilities. The goal is to understand how it works and what benefits it can bring. Here's an overview of what I cover in this post:

- [How to Setup a toy Lakehouse Monitoring](#setup-a-toy-lakehouse-monitoring)  
    - Dashboard
    - Alerts
- [Pricing](#pricing)  
- [My opinion on what I've seen](#my-opinion-on-what-ive-seen)  
- [Where's Databricks going?](#wheres-databricks-going)  
    - My2C

If you want to know more about what Databricks' Lakehouse Monitoring can do, I recommend checking out the official documentation. I have prepared a basic map of concepts that can help you get started.

![Lakehouse Monitoring Concepts Map](./images/map_of_concepts_lakehouse_monitoring.svg)

<h2 id="setup-a-toy-lakehouse-monitoring">How to Setup a toy Lakehouse Monitoring</h2>

Let's start by creating a table we can work with. It should be a time-series table


```sql
create table workspace.default.sales (
    timestamp TIMESTAMP,
    amount DOUBLE
)
```


I then create a basic notebook `insert 1h of data.ipynb` to fill table with data. Then, setup a job to run that notebook every hour.

I'll not add the code here because it is quite basic. It randomly adds records to the table with random values (within the time windown of the hour).


```sql
select * from workspace.default.sales
limit 10
```

<style scoped>
  .table-result-container {
    max-height: 300px;
    overflow: auto;
  }
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
  }
  th, td {
    padding: 5px;
  }
  th {
    text-align: left;
  }
</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>timestamp</th><th>amount</th></tr></thead><tbody><tr><td>2025-08-22T08:58:07.929Z</td><td>22.570402586080093</td></tr><tr><td>2025-08-22T08:51:51.929Z</td><td>20.713874028846366</td></tr><tr><td>2025-08-22T09:03:54.929Z</td><td>21.97633174572098</td></tr><tr><td>2025-08-22T08:28:44.929Z</td><td>27.94416169489641</td></tr><tr><td>2025-08-22T09:05:29.929Z</td><td>21.307407500066127</td></tr><tr><td>2025-08-22T08:17:03.929Z</td><td>22.37476392747984</td></tr><tr><td>2025-08-22T09:05:05.929Z</td><td>26.446829879517953</td></tr><tr><td>2025-08-22T08:42:32.929Z</td><td>27.86840740526422</td></tr><tr><td>2025-08-22T08:33:55.929Z</td><td>27.236961570798947</td></tr><tr><td>2025-08-22T08:42:30.929Z</td><td>25.395336538015343</td></tr></tbody></table></div>

Then, let's create the Monitor via Unity Catalog Explorer 👇

I set up the monitor as `TimeSeries` profile. I pointed out the `timestamp` column and a granularity of 1 hour. The schedule of the monitor is actually daily.

Below, a screenshot of the Unity Catalog Explorer page to create the Lakehouse Monitoring.

![Screenshot of Unity Catalog Explorer page to create the Lakehouse Monitoring](./images/create_monitor.png)

What happens after the creation of the Monitoring? By default, two new tables are created

- `<table_name>_profile_metrics`
- `<table_name>_drift_metrics`

Let's inspect them


```sql
SHOW TABLES IN workspace.default;
```

<style scoped>
  .table-result-container {
    max-height: 300px;
    overflow: auto;
  }
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
  }
  th, td {
    padding: 5px;
  }
  th {
    text-align: left;
  }
</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>database</th><th>tableName</th><th>isTemporary</th></tr></thead><tbody><tr><td>default</td><td>sales</td><td>false</td></tr><tr><td>default</td><td>sales_drift_metrics</td><td>false</td></tr><tr><td>default</td><td>sales_profile_metrics</td><td>false</td></tr><tr><td></td><td>_sqldf</td><td>true</td></tr></tbody></table></div>

```sql
select * from workspace.default.sales_profile_metrics
```

<style scoped>
  .table-result-container {
    max-height: 300px;
    overflow: auto;
  }
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
  }
  th, td {
    padding: 5px;
  }
  th {
    text-align: left;
  }
</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>window</th><th>log_type</th><th>logging_table_commit_version</th><th>monitor_version</th><th>granularity</th><th>slice_key</th><th>slice_value</th><th>column_name</th><th>count</th><th>data_type</th><th>num_nulls</th><th>avg</th><th>min</th><th>max</th><th>stddev</th><th>num_zeros</th><th>num_nan</th><th>min_length</th><th>max_length</th><th>avg_length</th><th>non_null_columns</th><th>frequent_items</th><th>median</th><th>distinct_count</th><th>percent_nan</th><th>percent_null</th><th>percent_zeros</th><th>percent_distinct</th></tr></thead><tbody><tr><td>List(2025-08-22T08:00:00.000Z, 2025-08-22T09:00:00.000Z)</td><td>INPUT</td><td>26</td><td>0</td><td>1 hour</td><td>null</td><td>null</td><td>:table</td><td>1344</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>List(timestamp, amount)</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>List(2025-08-22T08:00:00.000Z, 2025-08-22T09:00:00.000Z)</td><td>INPUT</td><td>26</td><td>0</td><td>1 hour</td><td>null</td><td>null</td><td>amount</td><td>1344</td><td>double</td><td>0</td><td>25.059042979855878</td><td>20.0007185120017</td><td>29.99500143216646</td><td>2.8817003714622857</td><td>0</td><td>0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>25.133808306174608</td><td>1277</td><td>0.0</td><td>0.0</td><td>0.0</td><td>95.01488095238095</td></tr><tr><td>List(2025-08-22T08:00:00.000Z, 2025-08-22T09:00:00.000Z)</td><td>INPUT</td><td>26</td><td>0</td><td>1 hour</td><td>null</td><td>null</td><td>timestamp</td><td>1344</td><td>timestamp</td><td>0</td><td>null</td><td>1.755850122929519E9</td><td>1.755853196019946E9</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>1.755851952929519E9</td><td>1161</td><td>null</td><td>0.0</td><td>null</td><td>86.38392857142857</td></tr><tr><td>List(2025-08-22T09:00:00.000Z, 2025-08-22T10:00:00.000Z)</td><td>INPUT</td><td>26</td><td>0</td><td>1 hour</td><td>null</td><td>null</td><td>timestamp</td><td>1192</td><td>timestamp</td><td>0</td><td>null</td><td>1.755853200929519E9</td><td>1.755856792565437E9</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>1.755854777019946E9</td><td>997</td><td>null</td><td>0.0</td><td>null</td><td>83.64093959731544</td></tr><tr><td>List(2025-08-22T09:00:00.000Z, 2025-08-22T10:00:00.000Z)</td><td>INPUT</td><td>26</td><td>0</td><td>1 hour</td><td>null</td><td>null</td><td>:table</td><td>1192</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>List(timestamp, amount)</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>List(2025-08-22T09:00:00.000Z, 2025-08-22T10:00:00.000Z)</td><td>INPUT</td><td>26</td><td>0</td><td>1 hour</td><td>null</td><td>null</td><td>amount</td><td>1192</td><td>double</td><td>0</td><td>24.847526487373074</td><td>20.01063581181195</td><td>29.99539398790598</td><td>2.8880160456500867</td><td>0</td><td>0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>24.694267025212234</td><td>1192</td><td>0.0</td><td>0.0</td><td>0.0</td><td>100.0</td></tr><tr><td>List(2025-08-22T10:00:00.000Z, 2025-08-22T11:00:00.000Z)</td><td>INPUT</td><td>26</td><td>0</td><td>1 hour</td><td>null</td><td>null</td><td>amount</td><td>941</td><td>double</td><td>0</td><td>24.969054277784952</td><td>20.015936515703217</td><td>29.981071930502402</td><td>2.846773237150427</td><td>0</td><td>0</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>24.969920953185955</td><td>925</td><td>0.0</td><td>0.0</td><td>0.0</td><td>98.29968119022317</td></tr><tr><td>List(2025-08-22T10:00:00.000Z, 2025-08-22T11:00:00.000Z)</td><td>INPUT</td><td>26</td><td>0</td><td>1 hour</td><td>null</td><td>null</td><td>timestamp</td><td>941</td><td>timestamp</td><td>0</td><td>null</td><td>1.755856803565437E9</td><td>1.755860399121952E9</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>1.755858763121952E9</td><td>857</td><td>null</td><td>0.0</td><td>null</td><td>91.07332624867162</td></tr><tr><td>List(2025-08-22T10:00:00.000Z, 2025-08-22T11:00:00.000Z)</td><td>INPUT</td><td>26</td><td>0</td><td>1 hour</td><td>null</td><td>null</td><td>:table</td><td>941</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>List(timestamp, amount)</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>List(2025-08-22T11:00:00.000Z, 2025-08-22T12:00:00.000Z)</td><td>INPUT</td><td>26</td><td>0</td><td>1 hour</td><td>null</td><td>null</td><td>:table</td><td>995</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>List(timestamp, amount)</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td></tr></tbody></table></div>

The **profile** table has a row for each pair

- `window` (the beginning and end of every hour)
- `column_name` every column of the table. In addition, it adds a special row `:table` to compute the table-level profile.

Optionally, it can slice on column values when specified at the time of the creation of the _Monitor_

For each row, it computes a bunch of statistics like `avg`, `quantiles`, `min`, `max`, etc. (when applicable, eg for float columns).


```sql
select * from workspace.default.sales_drift_metrics
```

<style scoped>
  .table-result-container {
    max-height: 300px;
    overflow: auto;
  }
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
  }
  th, td {
    padding: 5px;
  }
  th {
    text-align: left;
  }
</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>window</th><th>granularity</th><th>monitor_version</th><th>slice_key</th><th>slice_value</th><th>column_name</th><th>data_type</th><th>window_cmp</th><th>drift_type</th><th>count_delta</th><th>avg_delta</th><th>percent_null_delta</th><th>percent_zeros_delta</th><th>percent_distinct_delta</th><th>non_null_columns_delta</th><th>js_distance</th><th>ks_test</th><th>wasserstein_distance</th><th>population_stability_index</th><th>chi_squared_test</th><th>tv_distance</th><th>l_infinity_distance</th></tr></thead><tbody><tr><td>List(2025-08-22T11:00:00.000Z, 2025-08-22T12:00:00.000Z)</td><td>1 hour</td><td>0</td><td>null</td><td>null</td><td>:table</td><td>null</td><td>List(2025-08-22T10:00:00.000Z, 2025-08-22T11:00:00.000Z)</td><td>CONSECUTIVE</td><td>-418</td><td>null</td><td>null</td><td>null</td><td>null</td><td>List(0, 0)</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>List(2025-08-22T09:00:00.000Z, 2025-08-22T10:00:00.000Z)</td><td>1 hour</td><td>0</td><td>null</td><td>null</td><td>:table</td><td>null</td><td>List(2025-08-22T08:00:00.000Z, 2025-08-22T09:00:00.000Z)</td><td>CONSECUTIVE</td><td>-152</td><td>null</td><td>null</td><td>null</td><td>null</td><td>List(0, 0)</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>List(2025-08-22T10:00:00.000Z, 2025-08-22T11:00:00.000Z)</td><td>1 hour</td><td>0</td><td>null</td><td>null</td><td>:table</td><td>null</td><td>List(2025-08-22T09:00:00.000Z, 2025-08-22T10:00:00.000Z)</td><td>CONSECUTIVE</td><td>-251</td><td>null</td><td>null</td><td>null</td><td>null</td><td>List(0, 0)</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>List(2025-08-22T11:00:00.000Z, 2025-08-22T12:00:00.000Z)</td><td>1 hour</td><td>0</td><td>null</td><td>null</td><td>timestamp</td><td>timestamp</td><td>List(2025-08-22T10:00:00.000Z, 2025-08-22T11:00:00.000Z)</td><td>CONSECUTIVE</td><td>-418</td><td>null</td><td>0.0</td><td>null</td><td>-5.604875005841791</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>List(2025-08-22T09:00:00.000Z, 2025-08-22T10:00:00.000Z)</td><td>1 hour</td><td>0</td><td>null</td><td>null</td><td>timestamp</td><td>timestamp</td><td>List(2025-08-22T08:00:00.000Z, 2025-08-22T09:00:00.000Z)</td><td>CONSECUTIVE</td><td>-152</td><td>null</td><td>0.0</td><td>null</td><td>-2.742988974113132</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>List(2025-08-22T10:00:00.000Z, 2025-08-22T11:00:00.000Z)</td><td>1 hour</td><td>0</td><td>null</td><td>null</td><td>timestamp</td><td>timestamp</td><td>List(2025-08-22T09:00:00.000Z, 2025-08-22T10:00:00.000Z)</td><td>CONSECUTIVE</td><td>-251</td><td>null</td><td>0.0</td><td>null</td><td>7.4323866513561825</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td><td>null</td></tr><tr><td>List(2025-08-22T11:00:00.000Z, 2025-08-22T12:00:00.000Z)</td><td>1 hour</td><td>0</td><td>null</td><td>null</td><td>amount</td><td>double</td><td>List(2025-08-22T10:00:00.000Z, 2025-08-22T11:00:00.000Z)</td><td>CONSECUTIVE</td><td>-418</td><td>0.013276990751066364</td><td>0.0</td><td>0.0</td><td>-0.21172707932451829</td><td>null</td><td>null</td><td>List(0.049, 0.3829208808885818)</td><td>0.16058939377867895</td><td>0.028216393260236203</td><td>null</td><td>null</td><td>null</td></tr><tr><td>List(2025-08-22T10:00:00.000Z, 2025-08-22T11:00:00.000Z)</td><td>1 hour</td><td>0</td><td>null</td><td>null</td><td>amount</td><td>double</td><td>List(2025-08-22T09:00:00.000Z, 2025-08-22T10:00:00.000Z)</td><td>CONSECUTIVE</td><td>-251</td><td>0.12152779041187856</td><td>0.0</td><td>0.0</td><td>-1.7003188097768316</td><td>null</td><td>null</td><td>List(0.038, 0.4228041687817168)</td><td>0.14481617304902772</td><td>0.021676869284417942</td><td>null</td><td>null</td><td>null</td></tr><tr><td>List(2025-08-22T09:00:00.000Z, 2025-08-22T10:00:00.000Z)</td><td>1 hour</td><td>0</td><td>null</td><td>null</td><td>amount</td><td>double</td><td>List(2025-08-22T08:00:00.000Z, 2025-08-22T09:00:00.000Z)</td><td>CONSECUTIVE</td><td>-152</td><td>-0.21151649248280435</td><td>0.0</td><td>0.0</td><td>4.985119047619051</td><td>null</td><td>null</td><td>List(0.062, 0.014853915612309707)</td><td>0.21231645982023184</td><td>0.022438267042335924</td><td>null</td><td>null</td><td>null</td></tr></tbody></table></div>

The **drift** table is similar to the profile table. The **drift** table has a row for each pair

- `window` (the beginning and end of every hour)
- `column_name` every column of the table. In addition, it adds a special row `:table` to compute the table-level profile.

In addition, it has the `window_cmp`, where _cmp_ stands for _compare_. All the statistics are compared against another window (the previous one). There are various statistics like

- `count_delta`
- `ks_test`, in statistics, the Kolmogorov–Smirnov can be used to test whether two samples came from the same distribution

#### Dashboard

Lakehouse Monitoring creates also a dashboard automatically that displays the data in these _profile and drift_ tables.

😓 However, I find this dashboard too crowded and not ready to use. You need to work on it to customize it by yourself.

#### Alerts
Monitor alerts are created and used the same way as other Databricks SQL alerts. You create a Databricks SQL query on the monitor profile metrics table or drift metrics table. You then create a Databricks SQL alert for this query.

<h2 id="pricing">Pricing</h2>

Lakehouse Monitoring is billed under a serverless jobs SKU. You can monitor its usage via `system.billing.usage` table or via the Usage dashboard at Account console.

You need to pay attention. I expect that the costs may rise for columns with high number of columns if you don't finetune the monitor.


```sql
SELECT usage_date, sum(usage_quantity) as dbus
FROM system.billing.usage
WHERE
  usage_date >= DATE_SUB(current_date(), 30) AND
  sku_name like "%JOBS_SERVERLESS%" AND
  custom_tags["LakehouseMonitoring"] = "true"
GROUP BY usage_date
ORDER BY usage_date DESC
```

<style scoped>
  .table-result-container {
    max-height: 300px;
    overflow: auto;
  }
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
  }
  th, td {
    padding: 5px;
  }
  th {
    text-align: left;
  }
</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>usage_date</th><th>dbus</th></tr></thead><tbody><tr><td>2025-08-22</td><td>1.852757467777777736</td></tr></tbody></table></div>


<h2 id="my-opinion-on-what-ive-seen">My opinion on what I've seen</h2>  

Lakehouse monitoring is all about these two profile and drift tables. It is a kind of brute force approach that runs standardized monitoring over the specified table and stores the output in the profiling tables. Is it convenient? It depends on what you're looking for. It is not a free lunch.

**Pros 🟢**

- It takes little **effort** to setup. By default common controls are applied to all columns in the monitored table.
- Most common monitoring scenarios are covered by `TimeSeries` profile or by `Snapshot` profile (I left apart the inference-ML for the sake of simplicity). The **setup time** is shorter when compared to anything made by yourself.
- You have a framework ready to use. You save the time required designing it, and you avoid reinventing the wheel. You can **focus on your business** needs rather than on data engineering stuff.
- I like the simple but effective **design** of the _drift_ metric table and of the windowing. Making something like this by yourself will probably let you hit against some hidden edge-case (like anytime you work with time and dates). 

**Cons 🔴**

- Once the metrics are computed in the profile and drift tables, only half of the job is done. You still have to decide **what** to monitor and **how** to do it. You're probably not interested in monitor any single column in any row of the metric tables (otherwise you may alerted by too many false alarms). A finetuning of the actual alerts is still required, and it is not coming for free.
- You can't know in advance the overall **cost** of the monitoring. You need to try with a realistic (production-alike) scenario and monitor soon how much you're paying. I expect it to depend mainly on
    - the data volume
    - the columns in the table
    - the frequency of the controls
 
<h2 id="wheres-databricks-going">Where's Databricks going?</h2>

In addition to Lakehouse Monitoring, Databricks has released a feature (in Beta) of [data quality monitoring](https://docs.databricks.com/aws/en/lakehouse-monitoring/data-quality-monitoring). This new monitoring

- is quicker to setup. It is toggle on an entire Schema and monitors all the tables in the schema.
- monitors only simple freshness and completeness quality controls
- has no parametrization
- still needs alerts to be set manually

I made a short recap here.

| Feature                    | Lakehouse Monitoring                          | Data Quality Monitoring (Beta)            |
|----------------------------|-----------------------------------------------|-------------------------------------------|
| Scope | Table. It is set at table level. It monitors the table and its columns. | Schema. It is set at schema level and monitors all tables in such schema. |
| Setup | Choose the profile, eventual slicing, window and frequency. | On-off on the schema. |
| What is monitored | Various statistics as snapshot, time series, and inference. | Freshness (is data recent?) and completeness (is the volume as expected?) |
| Customization              | Limited | No |
| Alert | To be set manually on the output table. | To be set manually on the output table. |


#### My2C

🟢 I think Databricks is going in the right direction. Fast adoption of basic quality controls. Avoid the "_didn't notice data is old in production_" moments with little effort.

🔴 The alerting setup is still quite SQL-based and there is some trial-and-error around it. I would expect that a basic alert should be enabled by default.
