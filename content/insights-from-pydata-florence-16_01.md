Title: Insights from PyData Florence 16
Date: 2016-04-20 06:05
Author: mrsantoni
Category: Events
Tags: Events
Slug: 2016/04/20/insights-from-pydata-florence-16
Status: published

I have just joined [PyData](https://www.pycon.it/p3/schedule/pycon7/)
conference in Florence, and I will list briefly some
interesting insights.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Oh my... We are already overcrowded <a href="https://twitter.com/pyconit">@pyconit</a> and it&#39;s *just* the beginning!! 🎉🎉 good job guys! 🙌🏻 <a href="https://twitter.com/hashtag/pycon7?src=hash">#pycon7</a></p>&mdash; (((Valerio Maggio))) (@leriomaggio) <a href="https://twitter.com/leriomaggio/status/720894471060201472">April 15, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

**Time Travel and Time Series Analysis with Pandas and Statsmodels,
[@hendorf.](http://twitter.com/hendorf)** The focus of the talk was time
series analysis. The speaker pointed out something that a data scientist
should not forget when doing such time series analysis. He pointed out
that the time level of aggregation is something to do with care when
doing such analysis. Do you take into account that February has a number
of days that accounts to only 90% of the number of days of March? If you
compare e.g. sales per month, you cannot just ignore this fact. In the
talk, I found out that statsmodels has some nice tools that perform
trend analysis and seasonality analysis.

**Machine learning and IoT for automatic presence detection of workers
on fall protection life lines,
[@stefanoterna](http://twitter.com/stefanoterna).** The talk was an
excellent overview of how TomorrowData is able to deploy machine
learning systems in the "real world". Their system uses neural networks
to detect a man walking on industrial cables. It was interesting to hear
about the different challenges that one has to consider in the Internet
of Things area due to hardware and environmental constraints. The fact
that they had to manually annotate the signals coming from an
accelerometer reminded me of [my
work](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=7346953&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D7346953)
about indoor localization. In this kind of areas, the data collection is
indeed a challenge due to its manual cost (compared to the datasets you
can easily collect through a web app).

**Introduzione a Orange Data Mining,
[@ericbonfadini](http://twitter.com/ericbonfadini).** Eric introduced
Orange Data Mining which is both a python library and a GUI for machine
learning projects. I found interesting the nice GUI. It allows to define
pipelines of jobs to mine data. You can quickly get insights about data
and play around with machine learning models. I see this tool as quite
useful mainly for didactic purposes. I think it can be a nice tool for
teachers to explain data mining and machine learning in a nice graphical
way. It is really suitable for lectures.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">&quot;Simple APIs and innovative documentation processes&quot; keynote by <a href="https://twitter.com/EGouillart">@EGouillart</a> now live <a href="https://twitter.com/PyData">@PyData</a> <a href="https://twitter.com/pyconit">@pyconit</a> <a href="https://twitter.com/hashtag/pydatait?src=hash">#pydatait</a> <a href="https://t.co/Gt8cxIyafJ">pic.twitter.com/Gt8cxIyafJ</a></p>&mdash; PyData Italy (@pydatait) <a href="https://twitter.com/pydatait/status/721235005746188289">April 16, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

**Simple APIs and innovative documentation processes: looking back at
the success of Scientific Python,
[@EGouillart](http://twitter.com/EGouillart).** The talk was the point
of view of a core developer of a scientific package like *scikit-image*.
The speaker gave nice insights about the API design choices that need to
be taken when you contribute to open source projects. For example, what
is the advantage of getting rid of most classes in your package and
mainly expose functions. The idea is that, if you get rid of the
boilerplate of classes, you are forced to expose/return just numpy
arrays which you can then easily integrate to other tools in your
pipeline, e.g. scikit-learn. Another thing to take into account is that
54% of the users of packages are running a Windows machine (although
probably the developers of such package don't). So, you need to take
into account the tech gap between the developers and the end users.
Finally, the speaker mentioned the power of Sphinx as a documentation
tool.

**Building Data Pipelines in Python,
[@marcobonzanini](http://twitter.com/marcobonzanini).** Luigi is an
awesome tool because simply it makes you feel relaxed when you are
running a data pipeline. You can programmatically define arbitrary
dependencies between tasks, and Luigi will make sure that the
dependencies are fulfilled. Marco's talk was a really nice intro to the
tool.

**Going Functional in the Python Data Science Stack,
[@data_hope](http://twitter.com/data_hope). **The speaker explained
the directed acyclic graphs that are behind functional programming. It
was interesting to hear about Dask package and how you can bring its
lazy evaluation model. Dask allows you to abstract your code and perform
operations on datasets that do not fit in memory. The speaker pointed
out that doing functional programming means to decouple "how" from
"what". You can just focus on "what" your algorithm should do, then you
just choose "how" it will do it (e.g. Dask).

**Reti Neurali in Python, [@spiunno](http://twitter.com/spiunno).** The
talk was a great overview of what are neural networks and how you can
implement them with Theano and Lasagne. The speaker was able give a talk
that was suitable both to beginners and both to an intermediate
audience. In particular, the Q&A session was really active, and
interesting topics were discussed, e.g. preventing overfitting,
computational costs, gravitational waves, etc. Regarding overfitting
prevention, I learnt about "dropout" which is a nice technique that
consists basically in dropping out links of the networks at random for
each sample. The advantage is that you prevent overfitting and reduce
the computational cost at the same time.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/hendorf">@hendorf</a> thank you for coming! enjoy your next conference :)</p>&mdash; PyCon Italy (@pyconit) <a href="https://twitter.com/pyconit/status/722763833387966465">April 20, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
