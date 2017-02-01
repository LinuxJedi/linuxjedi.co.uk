Title: Solving recurrence relations in a nutshell
Date: 2017-02-01 23:21
Category: Mathematics
Tags: recursion, combinatorics, math

Able to solve recurrence relation is a very important skill when we study data structures
and algorithm. This is a ability that I used to be familar with when I took combinatorics
class when I was an undergraduate. However, by that time, I didn't realize how important 
this skill is from computer science point of view. But, thanks to MAW, I do now.

This post is a study summary note on this very important subject. The aim of this note 
is to help at least me quickly solve any types of recurrence relation in the future.
The content closely follows Chapter 7
"Recurrence Relations and Generating Functions" of 
["Introductory Combinatorics"](https://www.amazon.com/Introductory-Combinatorics-5th-Richard-Brualdi/dp/0136020402),
which is the textbook I used when I took combinatorics class.

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
H_{n}^{(i)} = c_1q_i^n + c2nq_i^n + \dots + c_{s_i}n^{s_i-1}q_i^n
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

\* ---- Note ---- *

> You probably already notice from the previous example that "characteristic equation" method really depends on the diffculty in finding all roots
> of a polynomial equation. Sometimes finding the roots of characteristic equation can be quite diffcult. That's what second method tries to address.
> If you find out that characteristic equation is really diffcult to solve, you can always use "generating function" method.

### Method 2: Generating function