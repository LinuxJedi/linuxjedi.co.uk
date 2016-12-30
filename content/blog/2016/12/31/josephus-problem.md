Title: Josephus Problem
Date: 2016-12-31 20:24
Category: Data Struct and Algo Analysis in C
Tags:double-linked-list, dynamic-programming, recurrence

## Preface

This is actually MAW 3.10. I gradually realize how dense MAW is.
In the [previous problem](http://zhu45.org/posts/2016/Dec/26/reflection-on-integer-arithmetic-package-problem/),
I write almost 500 lines of code. For this one, the problem is not really diffcult to solve if we implement a program 
that follows the game rule exactly. However, I figure it is a good chance to dig a little deeper to learn somewhat
fully from the question.

Let's start to dive in.

## Problem

The *Josephus problem* is the following game: $N$ people, numbered $1$ to $N$, are
sitting in a circle. Starting at person 1, a hot potato is passed. After $M$ passes,
the person holding the hot potato is eliminated, the circle closes ranks, and the
game continues with the person who was sitting after the eliminated person picking
up the hot potato. The last remaining person wins. Thus, if $M = 0$ and $N = 5$, players
are eliminated in order, and player 5 wins. If $M = 1$ and $N = 5$, the order of elimination
is $2$,$4$,$1$,$5$.

## Solution

In the following, $n$ denotes the number of 
people in the initial circle, and $m$ denotes the count for each step. In other words, $m-1$ people
are skipped and the $m$-th is eliminated. The people in the circle are numbered from $1$ to $n$. Our goal
is to find $J(n,m)$, which denotes the survivor's number (i.e. $J(5,1) = 3$)

### Solution 1

Let's first take a look at a special case $m = 2$ and then try to generalize the solution for arbitrary $m$. 
For simplicity, let $F(n) = J(n,2)$.

One quick observation is that after the first go-round, we are left with the same problem but for a different
number of people. For instance, when $n = 10$, after the first go-round, we eliminate $2$, $4$, $6$, $8$, $10$
and then we go to the second-round beginning with $3$, which is the same problem as the original one. 
The only difference is that the person with number $3$ in the first-round now becomes number $2$ in the second-round.

**Case 1: When $n$ is even ...**

Let $n = 2k$. After the first-round we are left with $k$ people, and we try to find out what is $F(k)$. In addition, by
our observation, the numbering of people is changed. If $3$ is actually the answer (i.e. $F(2k) = 3$), then in the second-round
the original person with $3$ now becomes $2$ (i.e. $F(k) = 2$). So, we have

$$
\begin{equation}
F(2k) = 2F(k) - 1, \text{ for } k >= 1 \label{eq:1}
\end{equation}
$$

**Case 2: When $n$ is odd ...**

Let $n = 2k+1$. By the same reasoning as case 1, after the first-round, we still eliminate $k$ people. For instance, when $n = 9$,
after the first-round, we elminate $2$, $4$, $6$, $8$, $1$. In other words, $1$ is eliminate just after person number $2k$. So, we 
have

$$
\begin{equation}
F(2k+1) = 2F(k) + 1, \text{ for } k >= 1\label{eq:2}
\end{equation}
$$

So now our goal is to solve the recurrence equations \ref{eq:1} and \ref{eq:2} given $F(1) = 1$.

### Implementation



#### Brutal Force


#### Mathematically


### What's left out


### Reference

- https://en.wikipedia.org/wiki/Josephus_problem
- Graham, R.L.; Knuth, D.E.; Patashnik, O. (1989), Concrete Mathematics: A Foundation for Computer Science, Addison Wesley, p. 8, ISBN 978-0-201-14236-5



<!-- ![]({filename}/images/josephus-1.png) -->