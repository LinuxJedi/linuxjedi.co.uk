Title: MAW Chapter 6: Priority Queues (Heaps) writing questions
Date: 2017-03-24 19:45
Category: Data Struct & Algo
Tags: heaps, proof, math, maw

## Solutions

including: MAW 6.6, 6.7, 6.9

### MAW 6.6

> How many nodes are in the large heap in Figure 6.13?

This question is interesting in the sense that the algorithm of counting reflecting
the underneath implemenation structure. Since the binary heap is actually implemented 
in terms of array, we start with $i = 1$ and position at the root. We follow the path
toward the last node, doubling $i$ when taking a left child, and doubling $i$ and adding
one when taking a right child. Then, we have the following calculation:
$2(2(2(2(2(2(2i+1)+1)))))+1 = 225$.

### MAW 6.7

> b. show that a heap of eight elements can be constructed in eight comparisons between 
>    heap elements.

Thie question is interesting because it offers another method we can use when build a binary
heap with even number of elements. That is, we build binomial queue first. since the binary 
form of $8$ is $1000_2$, this means we will have only one binomial tree $B_3$ inside the binomial queue.
Once we construct this binomial tree, we need one last step to tweek the binomial tree to
follow binary heap property, namely each node has to have either zero or two children.

For this question, it takes seven comparisons to construct the binomial queue (with a solo binomial tree)
and we get the following:

<img src="/images/maw-6-7-b.PNG" alt="MAW 6.7.b" style="width: 700px;"/>

Then we need to restore the binary heap property because "a" node has three children.
This can be done by the eighth compariosn between "b" and "c". If "c" is less than "b",
then "b" is made a child of "c". Otherwise, both "c" and "d" are made children of "b".

### MAW 6.9

> a. Give an algorithm to find all nodes less than some value, X, in a binary heap.
>    Your algorithm should run in $O(K)$, where $K$ is the number of nodes output.

The big idea is that we perform a preorder traversal of the heap. In detail, we start
from the root of the heap. If value of the root is smaller than $X$, then we output
this value and call procedure recursively once for its left child and once for its right 
child. If the value of a node is bigger or equal than $X$, then the procedure halts
without printing the value. We don't need to check the children by heap definition.

The complexity of this algorithm is $O(N)$ in worst case, where $N$ is the total number
of nodes in the heap. This happens when every node in the heap is smaller than $X$, and 
the procedure has to call each node of the heap.

> b. Does your algorithm extend to any of the other heap structures dicussed in 
>    this chapter?

Yes. It works for leftist heap, skew heap, and d-heaps.