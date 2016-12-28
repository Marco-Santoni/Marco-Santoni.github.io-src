Title: Insights from IEEE Big Data 16
Date: 2016-12-26 16:22
Slug: ieee_big_data_16
Status: published

I have attended the IEEE Big Data 16 conference in Washington DC. I thank my company for sponsoring the trip. The conference included a [special symposium](http://cci.drexel.edu/bigdata/bigdata2016/SpecialSymposium.html) dedicated to manufacturing. The symposium hosted some participants of the [Bosch Production Line Performance](https://www.kaggle.com/c/bosch-production-line-performance) competition from Kaggle.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">2016 IEEE International Conference on Big Data kicked off today in Washington, DC. Share highlights w/ hashtag <a href="https://twitter.com/hashtag/IEEEBigData16?src=hash">#IEEEBigData16</a> &amp; we’ll RT!</p>&mdash; IEEE Big Data (@ieeebigdata) <a href="https://twitter.com/ieeebigdata/status/805799488128425984">December 5, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

I'll list here a few notes I took during the conference.

- **Streaming Processing.** I heard about the most popular architectures nowadays, and I highly recommend reading the blog posts by the authors of such architectures:
    - [Lambda architecture](http://nathanmarz.com/blog/how-to-beat-the-cap-theorem.html)
    - [Kappa architecture](https://www.oreilly.com/ideas/questioning-the-lambda-architecture)
- **K-Spectral Centroid.** The K-Spectral Centroid algorithm clusters time series by their shape, and finds the most representative shape (the cluster centroid) for each cluster.
- **K-D Tree partition:** an algorithm for space partitioning.
- **Database Decay.** Interesting keynote by Michael Stonebraker. Shortly, large applications often share a centralized database used by different groups of a company. The DBA point of view:
    - High Risk. When changing a DB schema, I need to find applications all around in the company and update them accordingly (do I have budget for that?).
    - Low Risk. No change in schema, I do a workaround in data.
    - Claim. DBA want to lower the risk. --> no change in schema --> ER diagram diverges from reality --> database decay.
    - At some point, a total rewrite is the only way forward.
    - If you work in analytics getting data from operational DB, you realize data is getting more and more dirty.
- **PMML Scoring Engine.** Max Ferguson introduced what a Predictive Model Markup Language (PMML) is. Basically, if you train a model and want to share it in a different application, PMML is a standard that defines how models should be stored as an XML.
- **Uncertainty in RFs.** Random Forests can express uncertainty. One just needs to look at distribution of predictions among the decision trees of the model.
- **Bosch.** Rumi Ghosh introduced the data science team at Bosch.
    - Insight from production plants: plant managers prefer interpretable models (logistic regression or decision tree) over black box models.
    - Research directions:
      - Root cause analysis (via Bayesian inference)
      - Class imbalance
- **3 Approaches in Kaggle Competition.** [Bohdan Pavlyshenko](https://www.kaggle.com/bpavlyshenko) gave a talk on the three approaches he explored during the Kaggle competition about failure detection:
    - Pure machine learning approach. 2-Levels of model ensembling, a pure black-box.
    - Generalized Linear Model with Lasso regularization. Informative about feature impact.
    - Bayesian model in BUGS. It enables to obtain the estimate of the probability distribution for each coefficient.
- **FTLR.** Follow the regularized leader: a feature engineering method used to convert all categorical feature into one numerical feature.
- **CRF.** Conditional Random Fields is a class of predictive models used when the dataset is represented as a graph. Each node is a sample with a vector X and a target variable y.
