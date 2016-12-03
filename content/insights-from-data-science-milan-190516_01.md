Title: Insights from Data Science Milan - 19/05/16
Date: 2016-05-20 17:56
Author: mrsantoni
Category: Events
Tags: Events
Slug: insights-from-data-science-milan-190516
Status: published

https://twitter.com/andreaesseci/status/733044189349482496

A new **Data Science meetup** is out in Milan. Two talks about Deep
Learning were given in the first event.

**Neural Networks and Deep Learning: An
Introduction. [@MilanHighTech](https://twitter.com/milanhightech).** The
first talk by Valentino Zocca was a quick intro to Deep Learning The
speaker was able to explain the role of the additional layers in a
neural network. Each layer is learning something, and each one is
learning a different representation of the output. In particular, each
additional layer is learning a more abstract representation of the
output.

![Face recognition](https://indico.io/blog/wp-content/uploads/2016/02/cnn_deeper.jpg){.alignnone
width="370" height="506"}

Each layer is learning a higher level of abstraction. In the example,
the first layer is learning the edges in the image; the second layer is
learning the parts of a face like the nose or the eye; the third layer
is learning large sections of a face. Ref: "*Convolutional Deep Belief
Networks for Scalable Unsupervised Learning of Hierarchical
Representations*", Lee et al.

**Bringing Deep Learning into production.**
[@axlpado](https://twitter.com/axlpado). The speaker gave his point of
view on deploying machine learning algorithms in production. There are a
variety of frameworks, and it's always easy to choose which one to
adopt. He gave a series of interesting tips, and I'll write here the
main ones.

You can write machine learning in many languages such as Python, Java,
R, Matlab, Scala, etc. A good guideline is: choose the one you know the
most. Do not add the complexity of learning a new language to the
complexity of designing the algorithm.

Different languages in different teams.

![Data science
languages]({filename}/images/20160519_193804-1.jpg){.alignnone
.size-full .wp-image-58 width="896" height="504"}

It can be challenge to bring machine learning models from a team to
another. The reason is that often teams work in different languages or
in different frameworks. This organization leads to complex deployment
processes.

![Tips for
deployment]({filename}/images/20160519_194315.jpg){.alignnone
.size-full .wp-image-59 width="896" height="504"}

Paolo recommended to have the entire team on the same framework. The
idea is to have the deployment pipeline as smooth as possible. It can be
an effort for the data scientists at the beginning to learn the data
engineer tools, but it can make the difference on the long term.

 