Title: Num of function calls in recursive Fibonacci routine
Date: 2017-01-22 23:12
Category: Data Struct & Algo
Tags: math, call-stack, recursion, maw
Summary: Origin from MAW 3.24

This is MAW 3.24: 

> If the recursive rotuine in Section 2.4 used to computeFibonacci numbers is run for N = 50, is stack space likely to run out?Why or why not?

```{c}
unsigned long
Fib(int N)
{
  if (N <= 1)
    return 1;
  else
    return Fib(N-1) + Fib(N-2);
}
```

Let's first do an empirical experimentation. By running [our test program numCalls](https://github.com/xxks-kkk/Code-for-blog/blob/master/2017/numCalls/numCalls.c)
and we can get the following output:

```
    i               Fib(i)          numCalls
    i = 0           1               1
    i = 1           1               1
    i = 2           2               3
    i = 3           3               5
    i = 4           5               9
    i = 5           8               15
    i = 6           13              25
    i = 7           21              41
    i = 8           34              67
    i = 9           55              109
    i = 10          89              177
    i = 11          144             287
    i = 12          233             465
    i = 13          377             753
    i = 14          610             1219
    i = 15          987             1973
    i = 16          1597            3193
    i = 17          2584            5167
    i = 18          4181            8361
    i = 19          6765            13529
    ... snip ...
    i = 50          20365011074     40730022147
```

We know that the Fibonacci numbers are defined by the following recurrence relation:

$$
\begin{equation}
F(n) = F(n-1) + F(n-2), \text{ for }n = 2, 3, ... \label{eq:1}
\end{equation}
$$

We define $F(0) = F(1) = 1$. Now, we want to find out the number of recursive calls made to calculate $F(n)$. We use $G(n)$ to denote the number of calls made by the recursive program in calculating $F(n)$. Let's examine the output above. We see that $G(0) = G(1) = 1$ and to compute $G(n)$ for arbitrary $n$, we'll make an initial call, and then $G(n-1)$ calls to calculate $F(n-1)$ and $G(n-2)$ calls to calculate $F(n-2)$. Thus, we have the following recurrence relation for $G(n)$:
$$
\begin{equation}
G(n) = G(n-1) + G(n-2) + 1 \label{eq:2}
\end{equation}
$$
Let's solve this recurrence relation by establish the relationship between $F(n)$ and $G(n)$ and then, we can get the closed form based upon the closed form of $F(n)$. 

Let's suppose that $G(n)$ depends on $F(n)$ in some way. In other words, $G(n)$ is a function of $F(n)$. Let's try linear form first:
$$
\begin{equation}
G(n) = a F(n) + b \text{ where a, b are unknown constants}  \label {eq:3}
\end{equation}
$$
Since we know that $G(0) = G(1) = 1​$ and $F(0) = F(1) = 1​$, then \ref{eq:3} becomes 

$$
\begin{eqnarray*}
G(1)  & = & a F(1) + b \\
1 & = & a + b
\end{eqnarray*}
$$

Now let's plugin \ref{eq:3} into \ref{eq:2} and using the \ref{eq:1} and we have:

$$
\begin{eqnarray*}
G(n) & = & G(n-1) + G(n-2) + 1 \\
a F(n) + b & = & G(n-1) + G(n-2) + 1 \\
a (F(n-1) + F(n-2)) + b & = & G(n-1) + G(n-2) + 1 \\
a (F(n-1) + F(n-2)) + b & = & a F(n-1) + b + a F(n-2)) + b + 1 \\
b & = & -1
\end{eqnarray*}
$$

Now, our \ref{eq:3} becomes $G(n) = 2F(n) - 1$. That is, the number of function calls
to calculate a Fibonacci number $F(n)$ is $2F(n) - 1$.

Then the question asks about "is the stack space likely to run out?". This actually confuses
me because it seems like the author tries to indicate that there is a relationship between
the number of recursive calls and the actual space the program is going to take in call stack.
I have no clue so far. But, maybe we can find out the space of our `Fib` routine
is going to take in call stack and how large the system call stack and we can compare the two
to get some insights.

We can use `ulimit -a` or `ulimit -s` to find out the size of stack that system allows:

```{shell}
$ ulimit -a
... snip ...
stack size              (kbytes, -s) 10240
... snip ...
```

As you can see, the default stack size is `10 MB`. Let's see how large space our `Fib`
is going to use on stack: as of `gcc 4.6`, there is an option `-fstack-usage` to allow
us check the function max amount of stack use. [Read more info here](https://gcc.gnu.org/onlinedocs/gnat_ugn/Static-Stack-Usage-Analysis.html>).

```
numCalls.c:17:1:Fib     48      static
numCalls.c:27:1:main    64      static
```

As you can see, `Fib` only uses `48 bytes` and it's quite unlikely to drain out our stack space. 
But, of course, the runing time is another thing. I mean it's going to be very slow to get the output
for $N = 50$.


## Future work

- [This paper](http://vulms.vu.edu.pk/Courses/CS201/Downloads/p60-robertson.pdf) mentions that 
  \ref{eq:1} and \ref{eq:2} with their initial conditions respectively form second-order 
  Discrete Dynamical System (DDS). This offers some more mathematical insights. This actually reminds
  me equation 1.11 in *Concrete Mathematics: A Foundation for Computer Science* working on 
  a generalized Josephus problem recurrence relation with a system of three equations and three unknown
  constant coefficients. In fact, this way of solving problem seems anywhere like differential equations,
  calculating moments in statistics, and so on. Quite interesting.

- Lots of things can be said about call stack. In addition, "determine the amount of stack a program uses" is an interesting
  question that I may dig in the future.

