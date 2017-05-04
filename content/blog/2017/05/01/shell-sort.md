Title: Shell sort
Date: 2017-05-01 21:33
Category: Data Struct & Algo
Tags: sorting, maw
Summary: summary for shell sort

Per the final paragraph of the [last post]({filename}/blog/2017/04/17/insertion-sort.md),
the algorithm needs to avoid doing adjacent swap (in other words, comparing elements that are distant) 
so that we can have the opportunity to remove more than one inversion for each swap, which
can break $O(N^2)$ barrier. This is exactly what shellsort tries to achieve. 

## Concept

Shellsort is referred as *diminishing increment* sort: it works by swapping
non-adjacent elements; the distance between comparisons decreases as the 
algorithm runs until the last phase, in which adjacent elements are compared.

Concretely, shellsort uses an increment sequence $h_1, h_2, \dots, h_t$:

- We start with $k=t$

- Sort all subsequences of elements that are $h_k$ apart so that $A[i] \le A[i+h_k]$ for all i.
In other words, all elements spaced $h_k$ apart are sorted. ($h_k$-sort)

- Go to the next smaller increment $h_{k-1}$ and repeat until $k = 1$

\* ---- Note ---- *

> Any increment sequence will do as long as the last increment is 1 (i.e. $h_1 = 1$).
> However, choosing the increment is a practice of art: some choices dominate others.

A popular but poor choice for incremenet sequence is: $h_t = \lfloor{N/2}\rfloor$ and
$h_k = \lfloor{h_{k+1}/2}\rfloor$ proposed by shell. 

Here is the shellsort using Shell's increments:

```{c}
void
shellSort(int A[], int N)
{
  int i, j, increment, tmp;
  for (increment = N/2; increment > 0; increment /= 2)
    for(i = increment; i < N; i++)
    {
      tmp = A[i];
      for(j = i; j >= increment; j -= increment)
        if (tmp < A[j-increment])
          A[j] = A[j-increment];
        else
          break;
      A[j] = tmp;
    }
}
```

\* ---- Note ---- *

> As suggested by the algorithm above, the general strategy to $h_k$-sort is
> for each position, $i$, in $h_k, h_k+1, \dots, N-1,$ place the element in 
> the correct spot among $i, i-h_k, i-2h_k$, etc.

Here is an example of the algorithm in action (using Shell's increment sequence):

```
| index        | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 |
| original     | 81 | 94 | 11 | 96 | 12 | 35 | 17 | 95 | 28 | 58 | 41 | 75 | 15 |
|--------------|----|----|----|----|----|----|----|----|----|----|----|----|----|
| After 6-sort | 15 | 94 | 11 | 58 | 12 | 35 | 17 | 95 | 28 | 96 | 41 | 75 | 81 |
| After 3-sort | 15 | 12 | 11 | 17 | 41 | 28 | 58 | 94 | 35 | 81 | 95 | 75 | 96 |
| After 1-sort | 11 | 12 | 15 | 17 | 28 | 35 | 41 | 58 | 75 | 81 | 94 | 95 | 96 |
```

## Analysis

The running time of shellsort depends on how we pick the increment sequence. MAW gives 
running time for two commonly-seen increment sequences:

- The worst-case running time of Shellsort, using Shell's increments, is $\Theta(N^2)$.
- The worst-case running time of Shellsort, using Hibbard's increments ($1,3,7, \dots, 2^k-1$), is $\Theta(N^{3/2})$.

\* ---- Note ---- *

> The key difference between Hibbard's increments and Shell's increments is the adjacent
> increments have no common factors. The problem with Shell's increments is that
> we keep comparing the same elements over and over again. We need to increment
> so that different elements are in different passes.

The average case time is $O(N^{3/2})$ by using Hibbard's increments. The worst case time
is the sequence when smallest elements in odd positions, largest in even positions (i.e. 2,11,4,12,6,13,8,14)
when we use shell's sequence. Only last pass (i.e. $h_1 = 1$) will do the work and it becomes 
an insertion sort with $O(N^2)$. The best case can happen when we set the increment sequence to be 1
for any pass and we have a sorted array. In this case, we have $O(N)$.

Shellsort is good for up to $N \approx 10000$ and its simplcity makes it a favorite.

## Properties

- an $h_k-sorted$ array that is then $h_{k-1}$ sorted remains $h_k$ sorted (why algorithm works).
- the action of an $h_k$-sort is to perform an insertion sort on $h_k$ independent subarrays with size about $N/h_k$ elements
(i.e. $h_k = 6$ then there are 6 subarrays(by index): {0,6,12}, {1,7}, {2,8}, {3,9}, {4,10}, {5,11}).
- a larger increment swaps more distant pairs (natural derivation of the above property).

## Reference

- MAW Chapter 7
- https://www.cs.duke.edu/courses/fall01/cps100/notes/sorting_cheat.txt
- https://www.cs.rochester.edu/~brown/172/lectures/12_sort1/12sort1.html
- https://courses.cs.washington.edu/courses/cse373/01sp/Lect15.pdf
- https://courses.cs.washington.edu/courses/cse373/01sp/Lect16_2up.pdf
- http://web.mit.edu/1.124/LectureNotes/sorting.html
