Title: Josephus Problem
Date: 2016-12-31 20:24
Category: Data Struct and Algo Analysis in C
Tags: Algorithm, double-linked-list, dynamic-programming

### Preface

This is actually MAW 3.10. I gradually realize how dense MAW is.
In the [previous problem](http://zhu45.org/posts/2016/Dec/26/reflection-on-integer-arithmetic-package-problem/),
I almost write up 500 lines of code. For this one, I need to a bit of research in order to learn fully from this question.

Let's start to dive in.


### Problem

The *Josephus problem* is the following game: $N$ people, numbered $1$ to $N$, are
sitting in a circle. Starting at person 1, a hot potato is passed. After $M$ passes,
the person holding the hot potato is eliminated, the circle closes ranks, and the
game continues with the person who was sitting after the eliminated person picking
up the hot potato. The last remaining person wins. Thus, if $M = 0$ and $N = 5$, players
are eliminated in order, and player 5 wins. If $M = 1$ and $N = 5$, the order of elimination
is 2,4,1,5.

### Solution


### Implementation


### Reference

- https://en.wikipedia.org/wiki/Josephus_problem
- Graham, R.L.; Knuth, D.E.; Patashnik, O. (1989), Concrete Mathematics: A Foundation for Computer Science, Addison Wesley, p. 8, ISBN 978-0-201-14236-5