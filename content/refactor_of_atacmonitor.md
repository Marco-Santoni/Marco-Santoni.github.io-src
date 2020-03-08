Title: New Work on atacmonitor.com
Date: 2020-03-08 18:00
Slug: refactor_atacmonitor
Status: published

![atacmonitor chart]({static}/images/atacmonitor_chart.png)

My side project [atacmonitor](http://www.atacmonitor.com/) features a new guise. Data is now being collected for __all bus and tram__ lines in Rome. Data pull is achieved via Python functions running on AWS Lambda. Data is then stored in MongoDB hosted in MongoDB Atlas. Atlas also provides the charts in the page. An overview of the new architecture is presented below.

![atacmonitor architecture]({static}/images/atacmonitor_architecture_2.png)

[Link](http://www.marcosantoni.com/monitoring_bus_frequencies_in_rome.html) to the post of the first release.
