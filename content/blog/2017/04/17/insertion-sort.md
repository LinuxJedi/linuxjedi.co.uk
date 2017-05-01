Title: Simple sorting algorithms
Date: 2017-04-24 21:33
Category: Data Struct & Algo
Tags: sorting, maw
Summary: bubble sort, selection sort, and insertion sort

This post summarizes three typical simple sorting algorithms: *bubble sort*, 
*selection sort*, and *insertion sort*. In chapter 7, MAW mainly talks about 
*insertion sort* but for the sake of completeness, I will include the other two as
well.

## Bubble sort

### Concept

The idea for the bubble sort is to "bubble" larger elements to the end of array
by comparing $i$ and $i+1$, and swapping if $A[i] > A[i+1]$. We repeat this 
from the first to the end of unsorted part of the array.

The following code demonstrates the actual algorithm

```{c}
#define SWAP(a,b)  {int t; t = a; a = b; b = t;}
void bubbleSort(int A[], int n)
{
  int i, j;
  for(i = 0; i < n; i++) // n passes thru the array
    for(j = 1; j < (n-i); j++) // from start to the end of unsorted part
      if(A[j-1] > A[j]) SWAP(A[j-1], A[j]); 
}
```

The key for the alogorithm is that we only do the "bubble up" operation for the
unsorted part. The following gives an example of the algorithm in action:

```
| index    | 0  | 1  | 2  | 3  | 4  | 5  |
| original | 34 | 8  | 64 | 51 | 32 | 21 |
|----------|----|----|----|----|----|----|
| pass 0   | 8  | 34 | 51 | 32 | 21 | 64 |
| pass 1   | 8  | 34 | 32 | 21 | 51 | 64 |
| pass 2   | 8  | 32 | 21 | 34 | 51 | 64 |
| pass 3   | 8  | 21 | 32 | 34 | 51 | 64 |
| pass 4   | 8  | 21 | 32 | 34 | 51 | 64 |
| pass 5   | 8  | 21 | 32 | 34 | 51 | 64 |
```

### Analysis

Bubble sort is stable and in place. The running time is $O(N^2)$, which is true
for both worst case and average case. $O(N)$ can be achieved in the best case, where
the array is sorted or mostly sorted (possible a few elements a place or two
away from their correct spots).

## Selection sort

### Concept

The idea for selection sort is to scan array and select small key and swap it with 
the first element of the array (i.e. $A[0]$); scan remaining keys, select the smallest
and swap with the second element (i.e. $A[1]$); repeat the whole process until last 
element is reached. In other words, after $i$th pass, first $i$ elements are sorted and 
in proper position.

Like the bubble sort, we divide the whole array into sorted part
and unsorted part: we start with unsorted array and keep the sorted array at the beginning.
Each time we scan the unsorted part of the array and decide which element should go next
into the sorted part. However, unlike bubble sort, we build the sorted part from the
beginning of the array (in bubble sort, we start with moving the largest element to 
the end of array).

The following code demonstrates the actual algorithm

```{c}
void
selectionSort(int A[], int N)
{
  int i, j, min;
  j = min = i = 0;
  for(; i < N-1; i++)
  {
    for(j = i; j < N; j++)
      if(A[j] < A[min])
        min = j;
    swap(&A[min], &A[i]);
  }
}   
```

Here is an example of the algorithm in action:

```
| index    | 0  | 1  | 2  | 3  | 4  | 5  |
| original | 34 | 8  | 64 | 51 | 32 | 21 |
|----------|----|----|----|----|----|----|
| pass 0   | 8  | 34 | 64 | 51 | 32 | 21 |
| pass 1   | 8  | 21 | 64 | 51 | 32 | 34 |
| pass 2   | 8  | 21 | 32 | 51 | 64 | 34 |
| pass 3   | 8  | 21 | 32 | 34 | 64 | 51 |
| pass 4   | 8  | 21 | 32 | 34 | 51 | 64 |
```

### Analysis

The selection sort is NOT STABLE but in place. Selection sort is not sensitive
to the input and thus running time should be the same in best, average, and worst cases:
We go through $N-1$ passes with $N-1, \dots, 1$ comparisons, which is $O(N^2)$.

Since selection sort is insensitive to the data, it's good if we want to have our
sort routine always take the same time.

## Insertion sort

### Concept

The idea for insertion sort is that we insert an as-yet-unprocessed record
int a sorted list of the records processed so far. In details, insertion sort
consists of $N-1$ passes. For pass $P = 1$ through $N-1$, insertion sort ensures
that the elements in positions $0$ through $p$ are in sorted order. In pass $P$,
we move the element in position $P$ left until its correct place is found among
the first $P+1$ elements.

The following code demonstrates the actual algorithm

```{c}
void
insertionSort(int A[], int N)
{
  int j, P;
  int tmp;
  for(P = 1; P < N; P++)
  {
    tmp = A[P];
    for(j = P; j > 0 && tmp < A[j-1]; j--)
      A[j] = A[j-1];
    A[j] = tmp;
  }
}
```
Here is an example of the algorithm in action:

```
| index    | 0  | 1  | 2  | 3  | 4  | 5  |
| original | 34 | 8  | 64 | 51 | 32 | 21 |
|----------|----|----|----|----|----|----|
| pass 1   | 8  | 34 | 64 | 51 | 32 | 21 |
| pass 2   | 8  | 34 | 64 | 51 | 32 | 21 |
| pass 3   | 8  | 34 | 51 | 64 | 32 | 21 |
| pass 4   | 8  | 32 | 34 | 51 | 64 | 21 |
| pass 5   | 8  | 21 | 32 | 34 | 51 | 64 |
```

### Analysis

Due to the nested loops, the running time is $O(N^2)$, which can be achieved
when the input array is in reverse sorted order. In the best case, where 
the input array is already sorted, the running time is $O(N)$. For the average
case, the running time is $O(N^2)$. In fact, the bound is tight for both average case
and worst case: $\Theta (N^2)$.

In addition, insertion sort is stable and in place. Insertion sort is the most 
effectively used on input array with roughly $N < 20$ and for almost sorted array.

\* ---- Note ---- *

> [bubble sort video](https://youtu.be/8Kp-8OGwphY), 
> [selection sort video](https://youtu.be/f8hXR_Hvybo), 
> [insertion sort video](https://youtu.be/DFG-XuyPYUQ) and 
> [this animation](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)
> can help you understand the concept.

## A Lower Bound for Simple Sorting Algorithms

- An **inversion** is a pair of elements in wrong order (i.e. $i < j$ but $A[i] > A[j]$).

- Simple sorting algorithms presented in this post swap adjacenet elements
(explicitly or implicitly) removes one inversion per swap. This makes the running
time proportional to number of inversions in array.

- The average number of inversions in an array of $N$ distinct numbers is $N(N-1)/4$.

- Any algorithm that sorts by exchanging adjacent elements requires $\Omega (N^2)$ time
on average. This is due to the fact that each adjacent swap removes only one inversion.

As you can tell, to break $O(N^2)$ barrier, we must remove more than one inversion
for each swap. Adjacent elements swap will certainly not help us to achieve this goal.
The idea is that we try to swap the elements that are far apart and hopefully we can 
remove more than one inversion for each swap. Shell sort is the first algorithm
to break $O(N^2)$ running time. I'll talk about it in my next post.

## Reference

- MAW Chapter 7
- https://www.cs.duke.edu/courses/fall01/cps100/notes/sorting_cheat.txt
- https://www.cs.rochester.edu/~brown/172/lectures/12_sort1/12sort1.html
- https://courses.cs.washington.edu/courses/cse373/01sp/Lect15.pdf
- http://web.mit.edu/1.124/LectureNotes/sorting.html
