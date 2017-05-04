Title: Andrew Ng's ML Week 01 - 03
Date: 2017-05-04 23:48
Category: Machine Learning
Tags: ml, coursera
Summary: ML overview, Linear regression, Logistic regression, Regularization 

In my [introducing post]({filename}/blog/2017/04/20/andrew-ml-00.md), I mention that
I decide to write summary post weekly for the course. However, in practice, I find
it is very hard to do. This is mainly because I want to keep the progress in MAW 
reading while meet the coursework deadlines. So, I decide to do the summary post
based upon the module of the material itself.

In addition, like MAW reading posts, I will focus on the reflection and the post itself
may not be self-contained. However, this may happen rarely.

## ML overview

### What is ML?

The biggest take-away for me is that ML is to solve the problems that
cannot be easily solved by the programming. As mentioned by Prof. Andrew, we
know how to program the shortest path from A to B but we may have hard time
to program a solution to do image tagging, email spam checking, and so on.
The way we solve those problems is by teaching computers to do things like us
through learning algorithms.

There are a lot of examples about ML mentioned in the video:

- Database mining: large datasets from growth of automation/web (i.e. web click data,
medical records, biology, engineering)

- Applications can't program by hand. (i.e. autonomous helicopter, 
handwriting recognition, most of NLP, CV)

- Self-customizing programs (i.e. Amazon, Netflix product recommendations)

- Understanding human learning (brain, real AI)

There are two definitions for ML: 

- Arthur Samuel: the field of study that gives computers the ability to learn
without being explicitly programmed. (older, informal definition)

- Tom Mitchell: A computer program is said to learn from experience $E$ with respect
to some class of tasks $T$ and performance measure $P$, if its performance at tasks in $T$,
as measured by $P$, improves with experience $E$.

Take playing checkers as an example. $E = \text{the experience of playing many games of checkers}$;
$T = \text{the task of playing checkers}$; $P = \text{the probability that the program will win the next game}$.

### Types of ML problems

There are two general types:  Supervised learning and Unsupervised learning.

- Supervised learning: 'right' answer given

    - Regression: predict continuous valued output
        
        - EX1: given data about the size of houses on the real estate market, try to predict their price.
        - EX2: given a picture of a person, we predict their age on the basis of the given picture.
      
    - Classification: predict results in a discrete output (categories)

        - EX1: predict whether the house sells for more or less than the asking price.
        - EX2: given a patient with a tumor, we predict whether the tumor is malignant or benign.

- Unsupervised learning: little or no idea what our resuls should look like. We can
derive structure from data where we don't necessarily know the effect of the variables.

    - Clustering: take a collection of 1,000,000 different genes, and find a way to automatically group
    these genes into groups that are somehow similar or related by different variables (i.e. lifespan, location, roles)

    - Non-clustering: the "cocktail party algorithm" allows you to find structure in a 
    chaotic environment (i.e. identifying individual voices and music from a mesh of sounds at a cocktail party)

    - Other application fields: organize computing clusters, social network analysis, market segmentation, 
    astronomical data analysis

## Linear regression

### In theory

A few notation used throughout the course:

- $n = \text{number of features}$
- $m = \text{number of training examples}$
- $x^{(i)} = \text{input (features) of }i\text{th training example}$
- $x_j^{(i)} = \text{value of feature }j \text{ in }i\text{th training example}$

For linear regression, our hypothesis is 

$$
h_\theta(x) = \theta_0 x_0 + \theta_1 x_1 + \dots + \theta_n x_n = \theta^T x 
$$

where $\theta$ is a $n+1$ vector and $x$ is a $n+1$ vector as well.

$$
\left[
\begin{matrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{matrix}
\right]$$


### In practice


## Logistic regression
