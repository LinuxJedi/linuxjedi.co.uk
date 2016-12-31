Title: Josephus Problem
Date: 2016-12-31 20:24
Category: Data Struct and Algo Analysis in C
Tags:double-linked-list, recursion, dynamic-programming

## Preface

This is actually MAW 3.10. I gradually realize how dense MAW is.
In the [previous problem](http://zhu45.org/posts/2016/Dec/26/reflection-on-integer-arithmetic-package-problem/),
I write almost 500 lines of code. For this one, the problem is not really diffcult to solve if we implement a program 
that follows the game rule exactly. However, I figure it is a good chance to dig a little deeper to learn somewhat
fully from the question.

Let's start to dive in.

## Overview

I first describe the *Josephus problem* in general. Then, I present a closed form solution to 
solve a special case of the original problem.
Afterwards, I present a recurrence solution to solve the general problem. 

## Josephus problem

The *Josephus problem* is the following game: $N$ people, numbered $1$ to $N$, are
sitting in a circle. Starting at person 1, a hot potato is passed. After $M$ passes,
the person holding the hot potato is eliminated, the circle closes ranks, and the
game continues with the person who was sitting after the eliminated person picking
up the hot potato. The last remaining person wins. Thus, if $M = 0$ and $N = 5$, players
are eliminated in order, and player 5 wins. If $M = 1$ and $N = 5$, the order of elimination
is $2$,$4$,$1$,$5$.

## Josephus problem with $M = 2$

Let's first discuss a special case of the Josephus Problem: $M = 2$.

In the following, $n$ denotes the number of 
people in the initial circle, and $m$ denotes the count for each step. In other words, $m-1$ people
are skipped and the $m$-th is eliminated. The people in the circle are numbered from $1$ to $n$. Our goal
is to find $J(n,m)$, which denotes the survivor's number (i.e. $J(5,1) = 3$). For simplicity, let $F(n) = J(n,2)$.

![]({filename}/images/josephus-1.png) 

One quick observation is that after the first go-round, we are left with the same problem but for a different
number of people. For instance, when $n = 10$, after the first go-round, we eliminate $2$, $4$, $6$, $8$, $10$
and then we go to the second-round beginning with $3$, which is the same problem as the original one. 
The only difference is that the person with number $3$ in the first-round now becomes number $2$ in the second-round.

*Case 1: When $n$ is even ...*

Let $n = 2k$. After the first-round we are left with $k$ people, and we try to find out what is $F(k)$. In addition, by
our observation, the numbering of people is changed. If $3$ is actually the answer (i.e. $F(2k) = 3$), then in the second-round
the original person with $3$ now becomes $2$ (i.e. $F(k) = 2$). So, we have

$$
\begin{equation}
F(2k) = 2F(k) - 1, \text{ for } k >= 1 \label{eq:1}
\end{equation}
$$

*Case 2: When $n$ is odd ...*

Let $n = 2k+1$. By the same reasoning as case 1, after the first-round, we still eliminate $k$ people. For instance, when $n = 9$,
after the first-round, we elminate $2$, $4$, $6$, $8$, $1$. In other words, $1$ is eliminate just after person number $2k$. So, we 
have

$$
\begin{equation}
F(2k+1) = 2F(k) + 1, \text{ for } k >= 1\label{eq:2}
\end{equation}
$$

So now our goal is to solve the recurrence equations \ref{eq:1} and \ref{eq:2} given $F(1) = 1$ to find a closed form. Let's do
this by building a table of small values:

```text
| n    | 1 | 2   3 | 4   5   6   7 | 8   9   10   11   12   13   14   15 | 16 |
|------|---|-------|---------------|-------------------------------------|----|
| F(n) | 1 | 1   3 | 1   3   5   7 | 1   3   5    7    9    11   13   15 | 1  |
```

We can group the columns by powers of $2$ (marked by vertical lines in the table); Inside each group,
$F(n)$ is always $1$ at the beginning and then it increases by $2$ until the next group, which is 
the next power of $2$. So, for every number $n$, there exists an integer $a$ such that $2^a <= n < 2^{a+1}$.
For some $0 <= l <= 2^a$, then $n = 2^a + l$. In other words, $2^a$ is the largest power of 2 not exceeding $n$
and $l$ is what's left. Then, from the table above, we may have the formula:

$$
\begin{equation}
F(n) = F(2^a + l) = 2l + 1 \label{eq:3}
\end{equation}
$$

Now, let's prove equation \ref{eq:3} by induction on $a$.

- *Base case.* When $a = 0$, we must have $l = 1$; thus we have $F(1) = 1$, which is true.
- *Induction.* We use [strong induction](https://en.wikipedia.org/wiki/Mathematical_induction#Complete_induction) by
assuming that the equation holds for all $a$ up to certain value. Let's consider this value of $a$. The induction 
steps has two parts, depending on whether $n$ (and thus $l$) is even or odd.
    + If $2^a + l = 2k$, then

        $$
        \begin{align*}
        F(2^a + l) &= 2F(2^{a-1} + l/2) - 1 &&\text{(by equation 1)} \\
                &= 2(2l/2 + 1) - 1      &&\text{(by induction hypothesis)} \\
                &= 2l + 1
        \end{align*}
        $$

    + If $2^a + l = 2k+1$, then

        $$
        \begin{align*}
        F(2^a + l) &= 2F(2^{a-1} + (l-1)/2) + 1 &&\text{(by equation 2)} \\
                &= 2(2(l-1)/2 + 1) + 1      &&\text{(by induction hypothesis)} \\
                &= 2l + 1
        \end{align*}
        $$

This completes induction step.

Let's revisit our closed form solution \ref{eq:3} again. Let's rewrite it into the form:

$$F(n) = 2 (n - 2^a) + 1$$

$n - 2^a$ is the same as zeroing the most significant bit of $n$. Then, we multiply the result
with $2$, which is the same as shifting left one place, and adding $1$ is the same as setting the lowest
bit to $1$. In other words, equation \ref{eq:3} is essentially do a one-bit cyclic shift left. Let's try to write this 
out formally. Let $n = (b_ab_{a-1}..b_1b_0)_2$, then we have:

$$ F(n) = F((b_ab_{a-1}..b_1b_0)_2) = (b_{a-1}...b_1b_0b_a)_2 \text{ and } b_a = 1$$

For a more rigorous derivation of this cyclic shift property, please reference *Concrete Mathematics: A Foundation for Computer Science*.

The way we solve Josephus problem with $M = 2$ is unlikely to be generalized for arbitrary $m$. Let's take $n = 10$, $m = 2$ example again. The
reason we can derive the nice recurrence equations \ref{eq:1} and \ref{eq:2} is because our observation. Let's present our
observation is a different way. $F(2k)$ denotes the old numbering before the first-round. $F(k)$ denotes the new numbering 
after the first-round.

```text
      m = 2               m = 3
+-------+------+    +-------+------+
| F(2k) | F(k) |    | F(2k) | F(k) |
+-------+------+    +-------+------+
| 1     | 1    |    | 1     | 1    |
+-------+------+    +-------+------+
| 3     | 2    |    | 2     | 2    |
+-------+------+    +-------+------+
| 5     | 3    |    | 4     | 3    |
+-------+------+    +-------+------+
| 7     | 4    |    | 5     | 4    |
+-------+------+    +-------+------+
| 9     | 5    |    | 7     | 5    |
+-------+------+    +-------+------+
                    | 8     | 6    |
                    +-------+------+
                    | 10    | 7    |
                    +-------+------+
``` 

By looking at the table on the left, we can easily see that $F(2k) = 2F(k) - 1$. 
However, there is no nice clean linear relation that we can get between $F(2k)$ and $F(k)$ 
when $n = 10$, $m = 3$.

\* ---- Note ---- *

> Inside *Concrete Mathematics: A Foundation for Computer Science*, after talking about the
solution to the Josephus problem, the author shift their focus to solve a generalized
recurrence of \ref{eq:1} and \ref{eq:2}, which is (1.11) in the book. This has nothing to do
with the Josephus problem and I'm guessing the reason why the author want to talk about 
the solution to the generalized recurrence is to illustrate dynamic programming philosophy.

## General solution

The general solution utilitizes the dynamic programming paradigm by performing the first step
and using the solution of the subproblem we create to solve the initial problem. 
In terms of the solution, there is a difference when we start with the first person as $1$ or $0$.

### Starting from 0

We still use the re-numbering philosophy like we use for the $M=2$ case. However, this time,
we immediately do the re-numbering once we eliminate a person. For instance, let $n = 10$, $m = 2$.
We start from $1$ and the first person we eliminate is $2$. According to the rule, we should start to
pass potato from $3$. Before we doing so, we immediately re-number $3$ into $1$, and do so for the following
numbers (i.e. $3$, $4$, ..., $10$ are renumbered as $1$, $2$, $3$, ..., $8$).
Then, we start to pass potato again. By doing so, we make a original $n = 10$, $m = 2$ problem into 
a $n = 9$, $m = 2$ problem. The following picture illustrates this point:

```text

Initial:                          1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
right after eliminate 2:                    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 
right after eliminate 4:                              1 -> 2 -> 3 -> 4 -> 5 -> 6
...
```

Now, let $J(n,m)$ to denote the old number (position) and let $J(n-1, m)$ denote the new number (posiiton).
Then we can build the following equation based upon the above insight:

$$J(n,m) = (J(n-1,m) + m) \bmod n \text{; with }  J(1,m) = 0$$

### Starting from 1

The key insight is the following: the result of $J(n,m)$ is best NOT thought of as the *number* that is the 
Josephus survivor, but rather as the *index* of the number that is the Josephus survivor. 

Let



For example, $J(5,2)$
will tell you the *index* of the person out of a ring of five that ends up surviving.

With this intuition in mind, let's take a look at an example. Suppose we want to know $J(n,2)$. You can imagine 
we have $n$ people lined up like this: 

```
1 2 3 4 5 ... n
```

The first thing that happens is that person $2$ get eliminated, as shown here:

```
1 X 3 4 5 ... n
```

Now, we are left with a subproblem of the following form: there are $n - 1$ people remaining, every other
person is going to be eliminated, and the first person who will start to pass potato is person $3$. In other 
words, the subproblem $J(n-1, 2)$ now looks like:

```
3 4 5 ... n 1
```

$J(n-1, 2)$ will be the *index* of who survives in a line of $n - 1$ of people. Given that we have the *index*
of the person who will survive, and we also know who the starting person is, we can determine which person 
will be left. Here's how we'll do it.

The starting person in this line is the person who comes right after the person who was last executed. This will 
be person $3$. The 1-indexed position in the ring of $n-1$ people is given by $J(n-1, 2)$. We can then walk 
forward $J(n-1, 2)$ positions, wrapping around the ring if necessary, to get our final position. In other words, the 
survivor is given by position

$$(3 + J(n-1,2) - 1) \bmod n $$


### Implementation



#### Brutal Force


#### Mathematically


### What's left out


### Reference

- https://en.wikipedia.org/wiki/Josephus_problem
- Graham, R.L.; Knuth, D.E.; Patashnik, O. (1989), Concrete Mathematics: A Foundation for Computer Science, Addison Wesley, p. 8, ISBN 978-0-201-14236-5
- http://www.cut-the-knot.org/recurrence/r_solution.shtml
- http://www.exploringbinary.com/powers-of-two-in-the-josephus-problem
- http://www.math.northwestern.edu/~mlerma/problem_solving/solutions/josephus.pdf
- http://blue.butler.edu/~phenders/InRoads/MathCounts8.pdf
