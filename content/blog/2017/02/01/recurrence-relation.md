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
    - Method 1: Characteristic equations
    - Method 2: Generating functions
    - Example
- Linear nonhomogeneous recurrence relation with constant coefficients
    - Method 1: Characteristic equations
    - Method 2: Generating functions 
    - Example

## Linear homogeneous recurrence relation with constant coefficients

Definition: Let $h_0, h_1, h_2, \dots, h_n, \dots$ be a sequence of numbers. This sequence is 
said to satisfy a **linear recurrence relation of order $k$**, provided that there
exist quantities $a_1, a_2, \dots, a_k,$ with $a_k \ne 0$, and a quantity $b_n$
(each of these quantities $a_1,a_2,\dots,a_k,b_n$ may depend on $n$) such that 

$$
\begin{equation}
h_n = a_1h_{n-1} + a_2h_{n-2} + \dots + a_kh_{n-k} + b_n, (n\ge k) \label{eq:1}
\end{equation}
$$

Example: The Fabonacci sequence $f_0, f_1, f_2, \dots, f_n, \dots$ satisfies
the linear recurrence relation

$$
\begin{equation}
f_n = f_{n-1} + f_{n-2} (n\ge 2)
\end{equation}
$$

of order 2 with $a_1 = 1, a_2 = 1,$ and $b_n = 0$.

Definition: The linear recurrence relation \ref{eq:1} is called **homogeneous** 
provided that $b_n$ is zero and is said to have **constant coefficients** provided that
$a_1, a_2, \dots, a_k$ are constants.

### Method 1: Characteristic equations

Theorem 7.4.1: Let $q$ be a nonzero number. Then $h_n = q^n$ is a solution of the
linear homogeneous recurrence relation

$$
\begin{equation}
h_n - a_1h_{n-1}-a_2h_{n-2}- \dots - a_kh_{n-k} = 0, (a_k \ne 0, n \ge k) \label{eq:2}
\end{equation}
$$

with constant coefficients iff $q$ is a root of the polynomial equation (called **characteristic equation**) 

$$
\begin{equation}
x_k-a_1x^{k-1}-a_2x^{k-2}= \dots - a_k = 0 \label{eq:3}
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

Example: Solve the Fabonacci recurrence relation

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

and its two roots are $\frac{1+\sqrt(5)}}{2}$, $\frac{1-\sqrt(5)}{2}$, and by theorem 7.4.1,

$$
\begin{equation*}
f_n = c_1 (\frac{1+\sqrt(5)}}{2})^n + c_2 (\frac{1-\sqrt(5)}{2})^n
\end{equation*}
$$

is the general solution. We now want constants c_1, and c_2 so that 

$$
\left \{
\begin{array}{ll}
(n = 1) c_1 (\frac{1+\sqrt(5)}}{2}) + c_2 (\frac{1-\sqrt(5)}{2}) = 1\\
(n = 0) c_1 + c_2 = 0 \\
\end{array}
\right \}
$$

### Method 2: Generating functions