Title: Error when restarting Databricks streaming job
Date: 2020-04-19 18:00
Slug: error_restarting_databricks_streaming
Status: published

This is an error I encountered when I have a Spark Streaming job running on Databricks 6.1. Consider the case I have to update a running streaming query. Databricks [recommends](https://docs.databricks.com/spark/latest/structured-streaming/production.html#configure-jobs-to-restart-streaming-queries-on-failure) to always start (and restart too?) a streaming query on a **new** dedicated cluster. However, in some scenario you might not be able to do so, and you may want to:

- cancel the job run
- update the notebooks
- restart the job run

By taking these steps, I encountered these error:

```
Concurrent update to the log. Multiple streaming jobs detected for ...

# or

Multiple streaming queries are concurrently using ... [checkpoint]
```

They did not occur every time I restarted the query, but most of the times. When restarting 2-3 times, the issue was solved and the streaming query run smoothly. By investigating a bit more the error, we found that cancelling a job run via Databricks CLI was not letting the stream query close smoothly. What happened? The running query was not closing cleanly the [checkpoints](https://docs.databricks.com/spark/latest/structured-streaming/production.html#enable-checkpointing). So, when a new job run started, it raised an error because it found a corrupted checkpoint.

## Solution

You can

- upgrade do Databricks 6.3 and set [spark.sql.streaming.stopActiveRunOnRestart](https://docs.databricks.com/release-notes/runtime/6.3.html#improvements) to true
- wait for Databricks 7 to be release where this configuration is enabled by default
