Title: Solving recurrence relations in a nutshell
Date: 2017-02-02 01:05
Category: Mathematics
Tags: recursion, combinatorics, math
Summary: MATH475 methods to solve recurrence relation

Able to solve recurrence relation is a very important skill when we study data structures
and algorithm. This is a ability that I used to be familar with when I took combinatorics
class when I was an undergraduate. However, by that time, I didn't realize how important 
this skill is from computer science point of view. But, thanks to MAW, I do now.

This post is a study summary note on this very important subject. The aim of this note 
is to help at least me quickly solve any types of recurrence relation in the future.
The content closely follows Chapter 7
"Recurrence Relations and Generating Functions" of 
["Introductory Combinatorics"](https://www.amazon.com/Introductory-Combinatorics-5th-Richard-Brualdi/dp/0136020402),
which is the textbook I used.

\* ---- Note ---- *

> This note is practical-oriented. I will skip the proof of the theorem whenever possible.
> If you are interested in the proof side of the universe, please read the book.

## TOC

The post will be organized in the following format:

- Linear homogeneous recurrence relation with constant coefficients
    - Method 1: Characteristic equation
        - distinct roots (theorem 7.4.1)
        - roots with multiplicities (theorem 7.4.2)
    - Method 2: Generating function
- Linear nonhomogeneous recurrence relation with constant coefficients
    - Method 1: Characteristic equation
    - Method 2: Generating functions

## Linear homogeneous recurrence relation with constant coefficients

*Definition:* Let $h_0, h_1, h_2, \dots, h_n, \dots$ be a sequence of numbers. This sequence is 
said to satisfy a **linear recurrence relation of order $k$**, provided that there
exist quantities $a_1, a_2, \dots, a_k,$ with $a_k \ne 0$, and a quantity $b_n$
(each of these quantities $a_1,a_2,\dots,a_k,b_n$ may depend on $n$) such that 

$$
\begin{equation}
h_n = a_1h_{n-1} + a_2h_{n-2} + \dots + a_kh_{n-k} + b_n, (n\ge k) \label{eq:1}
\end{equation}
$$

*Example:* The Fabonacci sequence $f_0, f_1, f_2, \dots, f_n, \dots$ satisfies
the linear recurrence relation

$$
\begin{equation}
f_n = f_{n-1} + f_{n-2} (n\ge 2)
\end{equation}
$$

of order 2 with $a_1 = 1, a_2 = 1,$ and $b_n = 0$.

*Definition:* The linear recurrence relation \ref{eq:1} is called **homogeneous** 
provided that $b_n$ is zero and is said to have **constant coefficients** provided that
$a_1, a_2, \dots, a_k$ are constants.

### Method 1: Characteristic equation

*Theorem 7.4.1:* Let $q$ be a nonzero number. Then $h_n = q^n$ is a solution of the
linear homogeneous recurrence relation

$$
\begin{equation}
h_n - a_1h_{n-1}-a_2h_{n-2}- \dots - a_kh_{n-k} = 0, (a_k \ne 0, n \ge k) \label{eq:2}
\end{equation}
$$

with constant coefficients iff $q$ is a root of the polynomial equation (called **characteristic equation**) 

$$
\begin{equation}
x_k-a_1x^{k-1}-a_2x^{k-2}- \dots - a_k = 0 \label{eq:3}
\end{equation}
$$

If the polynomial equation has $k$ *distinct* roots $q_1, q_2, \dots, q_k$, then

$$
\begin{equation}
h_n = c_1q_1^{n}+c_2q_2^n+ \dots + c_kq_k^n \label{eq:4}
\end{equation}
$$

is the general solution of \ref{eq:2} in the following sense: No matter what initial
values for $h_0, h_1, \dots, h_{k-1}$ are given, there are constants $c_1, c_2, \dots, c_k$
so that \ref{eq:4} is the unique sequence which satisfies both the recurrence relation 
\ref{eq:2} and the initial values.

*Example:* Solve the Fabonacci recurrence relation

$$
\begin{equation*}
f_n = f_{n-1} + f_{n-2} (n\ge 2)
\end{equation*}
$$

subject to the initial values $f_0 = 0$, and $f_1$ = 1.

We rewrite reccurrence relation into $f(n) - f(n-1) - f(n-2) = 0$ and the characteristic 
equation of this recurrence relation is

$$
\begin{equation*}
x^2 - x - 1 = 0
\end{equation*}
$$

and its two roots are $\frac{1+\sqrt 5}{2}$, $\frac{1-\sqrt 5}{2}$, and by theorem 7.4.1,

$$
\begin{equation*}
f_n = c_1 \Big(\frac{1+\sqrt 5}{2}\Big)^n + c_2 \Big(\frac{1-\sqrt 5}{2}\Big)^n
\end{equation*}
$$

is the general solution. We now want constants c_1, and c_2 so that 

$$
\begin{equation*}
\begin{cases}
c_1 \Big(\frac{1+\sqrt 5}{2}\Big) + c_2 \Big(\frac{1-\sqrt 5}{2}\Big) &=& 1 \qquad (n=1)\\
c_1 + c_2 &=& 0 \qquad (n=0)\\
\end{cases}
\end{equation*}
$$

and we have $c_1 = \frac{1}{\sqrt 5}$, and $c_2 = -\frac{1}{\sqrt 5}$. Thus,

$$
\begin{equation*}
f_n = \frac{1}{\sqrt 5}\Big(\frac{1+\sqrt 5}{2}\Big)^n - \frac{1}{\sqrt 5}\Big(\frac{1-\sqrt 5}{2}\Big)^n
\end{equation*}
$$

is the solution of the Fabonacci recurrence relation.

\* ---- Note ---- *

> As you might notice, theorem 7.4.1 explicitly requires that the roots of the characteristic equation have 
> to be distinct. However, that's not always the case and theorem 7.4.1 will not work (see book for an example).
> That's why we need theorem 7.4.2.

*Theorem 7.4.2:* Let $q_1, q_2, \dots, q_n$ be the distinct roots of the following characteristic equation of the 
linear homogeneous recurrence relation with constant coefficients:

$$
\begin{equation}
h_n = a_1h_{n-1}+a_2h_{n-2}+ \dots + a_kh_{n-k}, a_k \ne 0, \qquad (n \ge k) \label{eq:5}
\end{equation}
$$

If $q_i$ is an $s_i$-fold root fo the characteristic equation of \ref{eq:5}, the part of the general solution of this recurrence 
relation corresponding to $q_i$ is 

$$
\begin{equation*}
H_{n}^{(i)} = c_1q_i^n + c_2nq_i^n + \dots + c_{s_i}n^{s_i-1}q_i^n
\end{equation*}
$$

The general solution of the recurrence relation is 

$$
\begin{equation*}
h_n = H_n^{(1)} + H_n^{(2)} + \dots + H_n^{(t)}
\end{equation*}
$$

*Example:* Solve the recurrence relation

$$
\begin{equation*}
h_n = -h_{n-1} + 3h_{n-2}+5h_{n-3}+2h_{n-4} \qquad (n \ge 4)
\end{equation*}
$$

subject to the initial values $h_0=1$, $h_1 = 0$, $h_2 = 1$, and $h_3 = 2$.

The characteristic equation of this recurrence relation is $x^4 + x^3 -3x^2 - 5x - 2 = 0$, which has roots $-1$, $-1$, $-1$, $-2$.
Thus, the part of the general solution corresponding to the root $-1$ is

$$
\begin{equation*}
H_n^{(1)} = c_1(-1)^n + c_2n(-1)^n + c_3n^2(-1)^n
\end{equation*}
$$

while the part of a general solution corresponding to the root $2$ is $H_n^{(2)} = c_42^n$. The general solution is 

$$
\begin{equation*}
h_n = H_n^{(1)} + H_n^{(2)} = c_1(-1)^n + c_2n(-1)^n + c_3n^2(-1)^n + c_42^n
\end{equation*}
$$

Then we can use initial values to determine $c1$, $c2$, $c3$, $c4$ and we have $h_n = \frac{7}{9} (-1)^n - \frac{3}{9}n(-1)^n + \frac{2}{9}2^n$.

<!--\* ---- Note ---- *

> You probably already notice from the previous example that "characteristic equation" method really depends on the diffculty in finding all roots
> of a polynomial equation. Sometimes finding the roots of characteristic equation can be quite diffcult. That's what second method tries to address.
> If you find out that characteristic equation is really diffcult to solve, you can always use "generating function" method.-->

### Method 2: Generating function

*Definition:* Let $h_0, h_1, h_2, \dots, h_n, \dots$ be an infinite sequence of numbers. Its **generating function** is defined to be the infinite
series

$$
\begin{equation}
g(x) = h_0 + h_1x + h_2x^2 + \dots + h_nx^n + \cdots
\end{equation}
$$

The coefficient of $x^n$ in $g(x)$ is the general solution to $h_n$. As you can see, generating functions are Taylor series (power series expansion)
of infinitely differentiable functions. If we can find the function (i.e. $g(x)$) and its Taylor series, then the coefficients of the Taylor series give the solution 
to the problem.

Let's illustrate this method using an example.

*Example:* Solve the recurrence relation 

$$
\begin{equation*}
h_n = 5h_{n-1} - 6h_{n-2} \qquad (n \ge 2) 
\end{equation*}
$$

subject to the initial values $h_0 = 1$ and $h_1 = -2$.

We first rewrite the recurrence relation into $h_n -5h_{n-1} + 6h_{n-2} = 0 \quad (n \ge 2)$. Let $g(x) = h_0 + h_1x + h_2x^2 + \dots + h_nx^n + \cdots$
be the generating function for the sequence $h_0, h_1, \dots, h_n, \dots$. We then form the following system of equations with the multipliers chosen based 
upon our rewritten recurrence relation initially.

$$
\begin{eqnarray*}
g(x) &=& h_0 + h_1x + h_2x^2 + \dots + h_nx^n + \cdots \\
-5xg(x) &=&   -5h_0x - 5h_1x^2 - \dots - 5h_{n-1}x^n - \cdots \\
6x^2g(x) &=&         6h_0x^2 + \dots + 6h_{n-2}x^n + \cdots
\end{eqnarray*}
$$

If you look at the coefficients of $x^n$ term vertically of all these three equations, you can see that they match our recurrence relation exactly.
Now, we add these three equations together, we obtain

$$
\begin{equation*}
(1-5x+6x^2)g(x) = h_0 + (h_1-5h_0)x + (h_2 - 5h_1 + 6h_0)x^2 + \dots + (h_n - 5h_{n-1} + 6h_{n-2})x^n + \cdots .
\end{equation*}
$$

since $$h_n - 5h_{n-1} + 6h_{n-2} = 0 \quad (n \ge 2)$ and our initial condition, we have

$$
\begin{equation*}
(1-5x+6x^2)g(x) = h_0 + (h_1 - 5h_0)x = 1 -7x
\end{equation*}
$$

Thus,

$$
\begin{equation*}
g(x) = \frac{1-7x}{1-5x+6x^2}
\end{equation*}
$$

Now, we need to expand $g(x)$ in order to get the coefficient of $h_n$. Since $1-5x+6x^2 = (1-2x)(1-3x)$, we can write

$$
\begin{equation*}
\frac{1-7x}{1-5x+6x^2} = \frac{c_1}{1-2x} + \frac{c_2}{1-3x}
\end{equation*}
$$

for some constants $c1$ and $c2$. We can determine $c1$ and $c2$ by multiplying both sides of this equation by $1-5x+6x^2$ to get

$$
\begin{equation*}
1 - 7x = (c_1 + c_2) + (-3c_1 -2c_2)x
\end{equation*}
$$

We can get $c_1 = 5$ and $c_2 = -4$. Since 

$$
\begin{equation*}
\frac{1}{(1-rx)^n} = \sum_{k=0}^\infty\dbinom{n+k-1}{k}r^kx^k \qquad \Big(|x| < \frac{1}{|r|}\Big)
\end{equation*}
$$

We have 

$$
\begin{equation*}
\frac{1}{1-2x} = 1 + 2x + 2^2x^2 + \dots + 2^nx^n + \cdots
\end{equation*}
$$

$$
\begin{equation*}
\frac{1}{1-3x} = 1 + 3x + 3^2x^2 + \dots + 3^nx^n + \cdots
\end{equation*}
$$

So

$$
\begin{eqnarray*}
g(x) &=& 5(1 + 2x + 2^2x^2 + \dots + 2^nx^n + \cdots) -4(1 + 3x + 3^2x^2 + \dots + 3^nx^n + \cdots) \\
&=& 1 + (-2)x + (-15)x^2 + \dots + (5\times2^n - 4\times3^n)x^n + \cdots
\end{eqnarray*}
$$

Thus, $h_n = 5\times2^n - 4\times3^n$.

\* ---- Note ---- *

> Getting the polynomial expansion of $g(x)$ is the hardest part of this method. For instance, factoring the 
> denominator of $g(x)$ can be tricky for high degree polynomials. I need more practice on solving recurrence
> relation to decide which method is superior under what kind of situation.

## Linear nonhomogeneous recurrence relation with constant coefficients

**nonhomogeneous** means $b_n$ in \ref{eq:1} is no longer zero constant.

### Method 1: Characteristic equation

*Steps:*

1) Find the general solution of the homogeneous relation.

2) Find a particular solution of the nonhomogeneous relation.
     
- If $b_n$ is a polynomial of degree $k$ in $n$, then look for a particular solution $h_n$ that is also a polynomial of degree $k$ in $n$. Thus, try 
    - $h_n = r$ (a constant) if $b_n = d$ (a constant)
    - $h_n = rn + s$ if $b_n = dn + e$
    - $h_n = rn^2 + sn + t$ if $b_n = dn^2 + en + f$
- If $b_n$ is an exponential, then look for a particular solution that is also an exponential. Thus, try $h_n = pd^n$ if $b_n = d^n$ or $h_n = pnd^n$ if 
  the first try doesn't work.

3) Combine the general solution and the particular solution so that the combined solution satisfies the initial conditions.

*Example:* Solve 

$$
\begin{eqnarray*}
h_n &=& 3h_{n-1} - 4n, \qquad (n \ge 1) \\
h_0 &=& 2
\end{eqnarray*}
$$

We first consider corresponding homogeneous recurrence relation $h_n = 3h_{n-1}$ and its characteristic equation is $x - 3 = 0$. and thus
we have the general solution $h_n = c3^n, \quad (n \ge 1)$.

Now we seek a particular solution of the nonhomogeneous recurrence relation $h_n = 3h_{n-1}-4n, \quad (n \ge 1)$. We try to find a solution of the 
form $h_n = rn + s$ for some constant number $r$ and $s$. We plug in our conjecture into the recurrence relation and get

$$
\begin{equation*}
rn + s = 3(r(n-1)+s) - 4n = (3r-4)n + (-3r+3s)
\end{equation*}
$$

Thus, $r = 2$ and $s = 3$ and $h_n = 2n + 3$. Now, we combine the general solution of the homogeneous relation with the particular solution 
of the nonhomogeneous relation to obtain

$$
\begin{equation*}
h_n = c3^n + 2n + 3
\end{equation*}
$$

Now, let's use inital condition to solve for $c$ and we have $c = -1$. So, $h_n = -3^n + 2n + 3$.

\* ---- Note ---- *

> As you can see, solving recurrence relation using characteristic equation has strong connection with solving differential equations (both homogeneous and
> nonhomogeneous). 

### Method 2: Generating function

There is nothing difference in using "generating function" method to solve nonhomogeneous than solve homogeneous recurrence relation. That's actually 
a beauty of this method: nothing needs to tweak in order to work under different situation.

\* ---- Note ---- *

> Certainly, not all recurrence relation appeard in computer science can be easily solved by the method described in this post. For instance,
> inside [Josephus problem]({filename}/blog/2016/12/31/josephus-problem.md), recurrence relation may depend on whether $n$ is odd or even and 
> methods may not apply nicely. This implies another type of technique to solve recurrence relation is to guess the solution and prove it by induction.
> Also, in the book, solving $h_n = h_{n-1} + n^3$ on p. 250 is not standard as well.