Title: MAW Chapter 6: Priority Queues (Heaps) writing questions
Date: 2017-03-24 19:45
Category: Data Struct & Algo
Tags: heaps, proof, math, maw

## Solutions

including: MAW 6.6

### MAW 6.6

> How many nodes are in the large heap in Figure 6.13?

This question is interesting in the sense that the algorithm of counting reflecting
the underneath implemenation structure. Since the binary heap is actually implemented 
in terms of array, we start with $i = 1$ and position at the root. We follow the path
toward the last node, doubling $i$ when taking a left child, and doubling $i$ and adding
one when taking a right child. Then, we have the following calculation:
$2(2(2(2(2(2(2i+1)+1)))))+1 = 225$.

### MAW 6.7

> Prove that for binary heaps, `BuildHeap` does at most $2N-2$ comparisons between elements.



