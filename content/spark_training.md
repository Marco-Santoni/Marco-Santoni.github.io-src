Title: Learning by teaching
Date: 2023-01-28 09:35
Slug: learning_by_teaching
Status: published

The picture below was taken just at the beginning of the exam of the course called _Apache Spark for Data Analysis_ at [ITS Rizzoli](https://www.itsrizzoli.it/en/home-en/) in Milan on November 2022. I was the one taking the picture because I was actually the lecturer of this course. In this post, I'll tell you why I ended up teaching this course.

![The day of the exam]({static}/images/spark_exam.jpg)

## Learning

I have been working daily with Apache Spark for three years so far, and I've been implementing a variety of batch and streaming data transformations with it. I felt I knew the basics of the framework so that I was autonomous in creating new jobs. However, I wanted to go deeper in understanding how Spark works and what are the best practices to follow (or the antipatterns to avoid).

Rather than studying by myself a book about Spark or something like that, I asked myself: "_why not teaching an introductory course_"? And that was actually a good idea. I found that **teaching** has been an extremely effective way to **learn**. My course consisted of 44 hours of training spanning on 11 lessons over 2 months. While that may look not that large, preparing 44 hours of training material and designing the lessons requires a dense preparation on the topic you are teaching. I decided to design the course with more practice than theory and with plenty of live coding.

So, preparing this course has been an amazing opportunity to actually learn how Apache Spark works. After the end of the course, I have the impression I've truly improved my coding skills in PySpark way more than what I would have achieved by any dedicated training.


## Impact

The [ITS](https://en.wikipedia.org/wiki/Istituto_tecnico_superiore) is a 2 years technical school dedicated to 19-20 years old students. It is an alternative to academy studies, and it is designed to be shorter and with a technical foucs. These ITS schools often focus on areas or skills that are in high demand by the job market. Therefore, students are often able to find their first job soon.

My goal was helping young developers learning a key technology like Spark. Knowing Spark is almost a requirement for applying to Data Engineer positions, and the role of the Data Engineer is one with the highest demand in the tech job market. So, I decided to design the course I would have liked to follow 3 years ago to speed up learning these skills. I liked the idea of giving my contribute in supporting these young developers finding their first job in the Data domain.

## Teaching

When you know a topic or a technology, it does not mean you are able to teach it. Teaching is a complex task where you cannot take anything for given and need find the good pace for the class. In a class of 23 students, I found a variety of expertises or a variety of backgrounds meaning that you need to balance them for teaching at the good rythm.

Another challenge is how not to make a lecture boring and having a good mix of theory and practive because you'll find both students that look for more of one or for more of the other. Teaching this course was then also an opportunity to improve my teaching skills, and these are not skills that you apply only during lectures. They are actually communication skills that you can apply and distill ona daily basis when working.

## Revenue

I liked the idea of having a small second revenue, and, before starting preparing the course, I thought teaching would have been a great idea because I would have been paid to learn. The salary of a lecturer in the tech domain can vary a lot depending on the context, but it is generally ranging from 40-200 euro per hour (this is not an official statistic, it's just an approximation). However, this salary does **not account** for the preparation of the training. So, is _revenue_ actually a good reason to teach? Probably not if you give this course only once or twice. The effort of the preparation is so large that the revenue will not compensate for it. If instead you have the opportunity to repeat the same training over and over, than it starts to make sense on the economical side too.

## Opportunity

Three years ago I just would not have had the time to prepare a course like this. Why? I use to spend 2 hours per day commuting. I now have instead the chance to work from home quite often, and this gives me 1-2 hours of extra life. I was then able to prepare the course material incrementally over a couple of months before the course started.

The opportunity came when I [interviewed Andrea Biancini](https://open.spotify.com/episode/4OWbyxGWcEPcQULpNTiNqU) at Intervista Pythonista podcast. Thanks to him, I knew a bit more about the tech education and training world and heard for the first time about ITS. Then, the idea was sticking in my head because I was looking forward to experience being a lecturer for the first time.

## Course design

When you prepare a course, the nice part is that you can actually design the course you would like to attend. My course then consisted mainly of live coding sessions that started with a brief introduction of a topic (eg Spark APIs, Streaming, etc) and then ended with an excercise on that topic that the students could try to solve. I decided to [open source](https://github.com/Marco-Santoni/databricks-from-scratch/tree/main/training-spark) the trainig material I prepared so that any other student or teach may benefit from it when needed. To simplify the course setup, I run the coding sessions on [Databricks community edition](https://community.cloud.databricks.com/login.html) so that students only needed a browser and an internet connection to work on a Spark cluster.

What helped the design of the cours was adopting a textbook. Having a textbook speeds up the design of the contents of the course and gives the students a reference resource in case they want to go deeper on the topic. I chose [Learning Spark](https://pages.databricks.com/rs/094-YMS-629/images/LearningSpark2.0.pdf) second edition by Damji et al. that is made freely available by Databricks.
