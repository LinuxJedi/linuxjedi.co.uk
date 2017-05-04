Title: MAW Chapter 7: Sorting writing questions
Date: 2017-04-15 23:54
Category: Data Struct & Algo
Tags: sorting, proof, math, maw
Summary: My solutions to selected problems in MAW Chapter 7

## Solutions

including: MAW 7.1, 7.2, 7.3, 7.4, 7.5.a, 7.9, 7.10, 

### MAW 7.1

> Sort the sequence 3,1,4,1,5,9,2,6,5 using insertion sort.

```
| index    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| original | 3 | 1 | 4 | 1 | 5 | 9 | 2 | 6 | 5 |
|----------|---|---|---|---|---|---|---|---|---|
| pass 1   | 1 | 3 | 4 | 1 | 5 | 9 | 2 | 6 | 5 |
| pass 2   | 1 | 3 | 4 | 1 | 5 | 9 | 2 | 6 | 5 |
| pass 3   | 1 | 1 | 3 | 4 | 5 | 9 | 2 | 6 | 5 |
| pass 4   | 1 | 1 | 3 | 4 | 5 | 9 | 2 | 6 | 5 |
| pass 5   | 1 | 1 | 3 | 4 | 5 | 9 | 2 | 6 | 5 |
| pass 6   | 1 | 1 | 2 | 3 | 4 | 5 | 9 | 6 | 5 |
| pass 7   | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 9 | 5 |
| pass 8   | 1 | 1 | 2 | 3 | 4 | 5 | 5 | 6 | 9 |
```

### MAW 7.2

> What is the running time of insertion sort if all keys are equal?

If you take a look at the code on p. 220, you can see that inner for loop checks
`A[j-1] > tmp` and it will fail immediately. Thus, the running time is $O(N)$.

### MAW 7.3

> Suppose we exchange elements $A[i]$ and $A[i+k]$, which were originally
> out of order. Prove that at least 1 and at most $2k-1$ inversions are removed.

The inversion that existed between $A[i]$ and $A[i+k]$ is removed. This shows 
at least one inversion is removed. Now let's consider $A[i], A[i+1], \dots, A[i+k-1], A[i+k]$,
Suppose $A[i]$ is greater than $A[i+1], \dots, A[i+k]$ and $A[i+k]$ is smaller than
$A[i], \dots, A[i+k-1]$. In this case, by swapping $A[i]$ and $A[i+k]$, we fix 
$2k-1$ inversions ($-1$ is that $A[i]$ greater than $A[i+k]$ and $A[i+k]$ smaller
than $A[i]$ points to the same inversion).

Another way to think about $2k-1$ is that for each of the $k-1$ elements 
$A[i+1], A[i+2], \dots, A[i+k-1]$, at most two inversions can be removed by exchange.
For instance, for $A[i+1]$, two inversions are $A[i]$ and $A[i+1]$, and $A[i+1]$ and
$A[i+k]$ (i.e. for sequence 10,4,3, by swapping 10 and 3, we remove inversion {10,4}
and {4,3}). Thus, a maximum of $2(k-1)+1 = 2k-1$.

### MAW 7.4

> Show the result of running Shellsort on the input 9,8,7,6,5,4,3,2,1 using the
> increments {1,3,7}

```
| index        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| original     | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|--------------|---|---|---|---|---|---|---|---|---|
| after 7-sort | 2 | 1 | 7 | 6 | 5 | 4 | 3 | 9 | 8 |
| after 3-sort | 2 | 1 | 4 | 3 | 5 | 7 | 6 | 9 | 8 |
| after 1-sort | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
```

### MAW 7.5.a

> What is the running time of Shellsort using the two-increment sequence {1,2}?

The answer is $\Theta(N^2)$. Let's first show the lower bound. By the conclusion
of 7.3, we know that The 2-sort removes at most only three (i.e. $k=2$) inversions
at a time. In addition, a pass with increment $h_k$ consists of $h_k$ insertion sorts
of about $N/h_k$ elements. Then, by theorem 7.2, we know that the algorithm 
is $\Omega(N^2)$. By the same argument, the 2-sort is two insertion sorts of size $N/2$,
so the cost of that pass is $O(N^2)$. The 1-sort is also $O(N^2)$, so the upper bound
for the algorithm is $O(N^2)$. 

### MAW 7.9

> Determine the running time (i.e. number of swaps) of Shellsort for 

> a. sorted input

$O(N \log N)$. No exachanges acutally done in each each pass but we will still
need to go through the second for loop, which indicates that each pass takes 
$O(N)$. There are total $O(\log N)$ passes and the answer follows.

> b. reverse-ordered input

$O(N \log N)$. It is easy to show that after an $h_k$ sort, no element is farther
than $h_k$ from its rightful position. Thus, if the increments satisfy $h_{k+1} \le ch_k$
for a constant $c$, which implies $O(\log N)$ increments, then the bound follows.

However, one cannot talk about shellsort without specifying the increment sequence.
If we assume the shell sequence (i.e. $N/2, N/4, \dots, 2, 1$), then the running time
is $O(N^2)$ as suggested by [this answer](https://www.cs.rochester.edu/~brown/172/exams/2ndmidterm_ans_13.pdf),
which I'll copy below for future reference.

Shellsort is just a bunch of insertion sorts. For a given increment $I$, there will
be $I$ subarrays to sort by insertion, each of length $N/I$. We know that insertion
sort requires time $O(m^2)$ to sort a reverse-sorted array of length $m$. Here, $m$
will be ($N/I$) for each subarray. Thus one subarray will cost $(N/I)^2$ to sort. 
There are $I$ subarrays, so the total cost will be $I * (N/I)^2 = N^2/I$. But that 
is the cost just for a single increment. The total time for all of the iterations must be
$N^2/(N/2) + N^2/(N/4) + N^2/(N/8) + \dots + N^2/2 + N^2/1 = 2N + 4N + \dots + N^2/2 + N^2/1$ .
If we factor out an $N$, we get $N(2+4+\dots+N/2+N)$ . In parenthesis is the sum of powers of 
2 from 2 to $N$, which is approximately equalt to $2N$. Therefore, the total cost
is $N(2N) = 2N^2 = O(N^2)$.

### MAW 7.10

> Do either of the following modifications to the Shellsort routine coded in 
> Fig. 7.4 affect the worst case running time?

> a. Before line 2, subtract one from `Increment` if it is even.

The key improvement in terms of the worst case running time lies in the increment
sequence. As suggested on p.224,225, we improve the worst time running time from
$O(N^2)$ to $O(N^{3/2})$ by changing the increment sequence into the sequence that
consecutive increments have no common factors. 

If we follow the modification indicated by this question, it is still possible
to have a case that we will have consecutive increments to share a common factor.
For instance, if we sort an array with size $N = 45$, then with the modification,
the increment sequence will be $45, 21 (22-1), 9, 3, 1$.

> b. Before line 2, add one to `Increment` if it is even.

In this case, conseuctive increments are relatively prime and by the argument in 
the proof of theorem 7.4, we can have the worst case running time $O(N^{3/2})$.