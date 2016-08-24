Title: A Simple Machine Learning Pipeline
Date: 2016-06-19 10:37
Author: mrsantoni
Category: Uncategorized
Slug: a-simple-machine-learning-pipeline
Status: published

This post contains the code that I used in my talk at Python Milano
Meetup on [June 22nd
2016](http://www.meetup.com/Python-Milano/events/231710577/). The talk
was a quick overview of **Pipeline**, a nice API by *scikitlearn* to
abstract your machine learning algorithm. It is based on the Boston
[Housing Data Set](https://archive.ics.uci.edu/ml/datasets/Housing).

We'll just load the data set from *sklearn*.

\[code language="python"\]  
from sklearn.datasets import load\_boston  
housing\_data = load\_boston()  
print housing\_data.DESCR  
\[/code\]

We might want to make it a Pandas dataframe to make things easier to
handle.

\[code language="python"\]  
import pandas as pd  
df = pd.DataFrame(housing\_data.data)  
df.columns = housing\_data.feature\_names  
df\['PRICE'\] = housing\_data.target  
df.head()  
\[/code\]

![table]({filename}/images/table.png){.alignnone
.size-full .wp-image-72 width="1206" height="318"}

The goal is to predict the *PRICE* variable given the other features.
How does this variable distribute?

\[code language="python"\]  
import matplotlib.pyplot as plt  
df.PRICE.hist()  
plt.xlabel('PRICE')  
\[/code\]

![download
(8)]({filename}/images/download-8.png){.alignnone
.size-full .wp-image-74 width="378" height="271"}

Let's turn the dataframe into a ML-friendly notation.

\[code language="python"\]  
X = df.drop('PRICE', axis=1)  
y = df\['PRICE'\]  
\[/code\]

We will now define the metric that assess the accuracy of our
algorithm/pipeline. Let's use the good old cross validation.

\[code language="python"\]  
from sklearn import cross\_validation  
def evaluate\_model(X, y, algorithm):  
print 'Mean Squared Error'  
scores = cross\_validation.cross\_val\_score(algorithm, X, y,
scoring='mean\_squared\_error')  
print -scores  
print 'Accuracy: %0.2f' % -scores.mean()  
\[/code\]

So, now, we can try a bunch of algorithms and see which one works best
by calling *evaluate\_model*. It is now time to implement a first
algorithm. So, let's explore a bit the data set. Is there any pattern we
can exploit?

\[code language="python"\]

plt.figure(figsize=(10,7))  
plt.scatter(df\['RM'\], y)  
plt.xlabel('Average number of rooms')  
plt.ylabel('Housing price in \$1000\\'s')  
plt.show()

\[/code\]

![download]({filename}/images/download.png){.alignnone
.size-full .wp-image-78 width="610" height="438"}

As expected, there is a relation between the average number of rooms and
the median price. So, let's build the first algorithm.

\[code language="python"\]  
from sklearn.pipeline import make\_pipeline  
from sklearn.preprocessing import FunctionTransformer  
from sklearn.linear\_model import LinearRegression

def just\_RM\_column(X):  
RM\_col\_index = 5  
return X\[:, \[RM\_col\_index\]\]

pipe = make\_pipeline(  
FunctionTransformer(just\_RM\_column),  
LinearRegression()  
)  
\[/code\]

How well does it perform?

\[code language="python"\]  
evaluate\_model(X, y, pipe)  
'''Mean Squared Error \[ 43.19492771 41.72813479 46.89293772\] Accuracy:
43.94'''  
\[/code\]

Can we visualize what the pipeline is actually doing?

\[code language="python"\]  
def plot\_model\_RM(X, y, pipe):  
X\_train, X\_test, y\_train, y\_test =
cross\_validation.train\_test\_split(  
X,  
y,  
test\_size=0.33,  
random\_state=5  
)  
pipe.fit(X\_train, y\_train)  
fake\_X\_train = np.array(X\_train)  
fake\_X\_train\[:, 5\] = np.linspace(min(fake\_X\_train\[:, 5\]),
max(fake\_X\_train\[:, 5\]), num=len(fake\_X\_train\[:, 5\]))  
fake\_X\_test = np.array(X\_test)  
fake\_X\_test\[:, 5\] = np.linspace(min(fake\_X\_test\[:, 5\]),
max(fake\_X\_test\[:, 5\]), num=len(fake\_X\_test\[:, 5\]))  
plt.figure(figsize=(20,7))  
plt.subplot(1, 2, 1)  
plt.scatter(X\_train\['RM'\], y\_train)  
plt.scatter(fake\_X\_train\[:, 5\], pipe.predict(fake\_X\_train),
color='r')  
plt.xlabel('Average number of rooms')  
plt.ylabel('Housing price in \$1000\\'s')  
plt.title('Train Data Set')  
plt.subplot(1, 2, 2)  
plt.scatter(X\_test\['RM'\], y\_test)  
plt.scatter(fake\_X\_test\[:, 5\], pipe.predict(fake\_X\_test),
color='r')  
plt.xlabel('Average number of rooms')  
plt.ylabel('Housing price in \$1000\\'s')  
plt.title('Test Data Set')  
plt.show()

plot\_model\_RM(X, y, pipe)  
\[/code\]

![download
(1)]({filename}/images/download-1.png){.alignnone
.size-full .wp-image-84 width="1173" height="449"}

We now do a bit of feature engineering. We square the features.

\[code language="python"\]  
def add\_squared\_col(X):  
return np.hstack((X, X\*\*2))

pipe = make\_pipeline(  
FunctionTransformer(just\_RM\_column),  
FunctionTransformer(add\_squared\_col),  
LinearRegression()  
)  
\[/code\]

We evaluate this other pipeline.

\[code language="python"\]  
evaluate\_model(X, y, pipe)  
'''  
Mean Squared Error  
\[ 40.31207562 36.75642688 40.75444834\]  
Accuracy: 39.27'''  
\[/code\]

And we see how the algorithm is fitting the data set.

\[code language="python"\]  
plot\_model\_RM(X, y, pipe)  
\[/code\]

![download
(2)]({filename}/images/download-2.png){.alignnone
.size-full .wp-image-86 width="1165" height="449"}  
We now try a different model like a *decision tree*.

\[code language="python"\]  
from sklearn.tree import DecisionTreeRegressor

pipe = make\_pipeline(  
FunctionTransformer(just\_RM\_column),  
FunctionTransformer(add\_squared\_col),  
DecisionTreeRegressor(max\_depth=3)  
)  
evaluate\_model(X, y, pipe)  
'''  
Mean Squared Error  
\[ 57.28366371 61.5437311 84.32756118\]  
Accuracy: 67.72  
'''  
plot\_model\_RM(X, y, pipe)  
\[/code\]

![download
(3)]({filename}/images/download-3.png){.alignnone
.size-full .wp-image-87 width="1165" height="449"}

We now explore a second feature: *INDUS*.

\[code language="python"\]

plt.figure(figsize=(10,7))  
plt.scatter(df\['INDUS'\], y)  
plt.xlabel('Average number of rooms')  
plt.ylabel('Housing price in \$1000\\'s')  
plt.show()

\[/code\]

![download
(4)]({filename}/images/download-4.png){.alignnone
.size-full .wp-image-89 width="610" height="438"}

So, we see another relation between *INDUS* and *PRICE*. So, let's add
this second feature.

\[code language="python"\]

def RM\_and\_INDUS\_cols(X):  
RM\_col\_index = 5  
INDUS\_col\_index = 2  
return X\[:, \[RM\_col\_index, INDUS\_col\_index\]\]

pipe = make\_pipeline(  
FunctionTransformer(RM\_and\_INDUS\_cols),  
FunctionTransformer(add\_squared\_col),  
LinearRegression()  
)

evaluate\_model(X, y, pipe)  
'''  
Mean Squared Error  
\[ 32.3420789 31.4260901 35.95835866\]  
Accuracy: 33.24  
'''  
\[/code\]

Now, plotting a model in 3D needs a bit more effort.

\[code language="python"\]  
def plot\_model\_RM\_INDUS(X, y, pipe):  
X\_train, X\_test, y\_train, y\_test =
cross\_validation.train\_test\_split(  
X,  
y,  
test\_size=0.33,  
random\_state=5  
)  
pipe.fit(X\_train, y\_train)  
X\_test = np.array(X\_test)  
fig = plt.figure(figsize=(10,7))  
ax = p3.Axes3D(fig)  
x = X\_test\[:, 2\]  
y = X\_test\[:, 5\]  
z = y\_test  
ax.scatter(x, y, z, c='r', marker='o')  
x = np.arange(min(x), max(x), (max(x) - min(x)) / 100.0)  
y = np.arange(min(y), max(y), (max(y) - min(y)) / 100.0)  
X, Y = np.meshgrid(x, y)  
Z = np.zeros(X.shape)  
fake\_X = np.zeros((1, 10))  
for i in range(X.shape\[0\]):  
for j in range(X.shape\[1\]):  
fake\_X\[0, 2\] = X\[i, j\]  
fake\_X\[0, 5\] = Y\[i, j\]  
Z\[i, j\] = pipe.predict(fake\_X)\[0\]  
ax.plot\_surface(X, Y, Z, alpha=0.2)  
ax.set\_xlabel('INDUS')  
ax.set\_ylabel('RM')  
ax.set\_zlabel('Price')

plot\_model\_RM\_INDUS(X, y, pipe)  
\[/code\]

![animation]({filename}/images/animation.gif){.alignnone
.size-full .wp-image-91 width="720" height="504"}

How pretty is that?

The following step is to use all the features available. So, we move to
a 13-dimensional feature vector.

\[code language="python"\]  
pipe = make\_pipeline(  
LinearRegression()  
)  
evaluate\_model(X, y, pipe)  
'''  
Mean Squared Error  
\[ 20.50009513 22.42870192 27.88911654\]  
Accuracy: 23.61'''  
\[/code\]

The error got quite smaller. We cannot however plot the model in
13-dimensions. We will now re-use the function that adds a squared
feature.

\[code language="python"\]  
pipe = make\_pipeline(  
FunctionTransformer(add\_squared\_col),  
LinearRegression()  
)  
evaluate\_model(X, y, pipe)  
'''  
Mean Squared Error  
\[ 16.7819682 14.599869 18.17785453\]  
Accuracy: 16.52'''  
\[/code\]

Even better. Now, we will switch to a ridge-regressor (combined with a
normalization of the features).

\[code language="python"\]  
from sklearn.preprocessing import StandardScaler  
from sklearn.linear\_model import Ridge

pipe = make\_pipeline(  
StandardScaler(),  
FunctionTransformer(add\_squared\_col),  
Ridge(alpha=3)  
)  
evaluate\_model(X, y, pipe)  
'''  
Mean Squared Error  
\[ 16.4292824 14.50522561 18.27167008\]  
Accuracy: 16.40'''  
\[/code\]

 
