Title: MAW Chapter 7: Sorting writing questions
Date: 2017-04-15 23:54
Category: Data Struct & Algo
Tags: sorting, proof, math, maw
Summary: My solutions to selected problems in MAW Chapter 7

## Solutions

including: MAW 7.1, 7.2, 7.3, 7.4

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