Title: My Talk about Superset [Python Milano Meetup]
Date: 2017-06-22 17:56
Slug: talk_python_pills
Status: published

Yesterday, I gave a talk [Python Milano Meetup](https://www.meetup.com/Python-Milano/events/239846600/). The Meetup was designed as Python pills: three 20-minutes talks in a row. The talks:

- Superset: data visualization at AirBnB - Marco Santoni
- Java Vs Python - Cesare Placanica
- pdb in action - [Lorenzo Mele](https://twitter.com/greenkey)

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Very nice talk of <a href="https://twitter.com/Airbnb">@Airbnb</a> <a href="https://twitter.com/hashtag/Superset?src=hash">#Superset</a> with <a href="https://twitter.com/MrSantoni">@MrSantoni</a> at <a href="https://twitter.com/hashtag/PythonMilano?src=hash">#PythonMilano</a>. I see juicy applications for us <a href="https://twitter.com/hashtag/BIM?src=hash">#BIM</a> guys. <a href="https://t.co/Pf1r9nhNEd">https://t.co/Pf1r9nhNEd</a></p>&mdash; Chiara Rizzarda (@CrShelidon) <a href="https://twitter.com/CrShelidon/status/877595912612311041">June 21, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

I presented [superset](https://github.com/airbnb/superset), the open source project by AirBnB. It is a data visualization platform developed in Python. It allows to create interactive dashboards. The setup time is extremely short. It interesting for enterprises because the package features deep and granular authorization policies. The dashboards can be designed by business users too. You can indeed design dashboards without writing SQL queries (but there's still the option to write SQL of course). `superset` can integrate to most SQL databases thanks to `SQLAlchemy` query layer. Furthermore, `druid.io` database is supported. I presented [atacmonitor](http://www.marcosantoni.com/monitoring_bus_frequencies_in_rome.html) as an example of a `superset` application.
