Title: Skew heap
Date: 2017-04-05 23:33
Category: Data Struct & Algo
Tags: heaps, maw
Summary: Summary for skew heap

This is the summary of *skew heap* part in MAW Chapter 6.

## Motivation

Like the relation between splay trees and AVL trees, we want to have 
$O(\log N)$ amortized cost per operation. In addition, we don't want
to have any auxiliary information stored at the nodes. In other words,
we want to trade strict $O(\log N)$ operation for less space we need 
to use for the data structure. In this case,
like splay trees to AVL trees, we have Skew heaps to leftist heaps.

## Concept

Skew heaps are binary trees with heap order, but there is no structural constraint
on these trees. This means that we don't need the binary tree to be complete 
(i.e. binary heap) or left heavy (i.e. leftist heap).

In addition, we don't store $Npl$ information in the node.

## Properties

- A perfectly balanced tree forms if the keys $1$ to $2^k-1$ are inserted in order
into an initially empty skew heap.

## Operations

Skew heap is extremely similar with leftist heap in terms of `merge` operation. 
There is only one difference: for leftist heap, we check to see whether the 
left and right children satisfy the leftist heap order property and swap them
if they do not. However, for skew heaps, the swap is unconditional. In other words,
we **always** swap the left & right subtrees at each step of merge. 

In the below example, we want to merge two skew heaps $H_1$ and $H_2$:

<img src="/images/skew-heap-01.PNG" alt="skew heap 01" style="width: 700px;"/>

Then, we get the following result of merging $H_2$ with $H_1$'s right subheap:

<img src="/images/skew-heap-02.PNG" alt="skew heap 02" style="width: 700px;"/>

and this is the final merge result:

<img src="/images/skew-heap-03.PNG" alt="skew heap 03" style="width: 700px;"/>

\* ---- Note ---- *

> The end result is actually leftist heap but there is no guaranteed that this is
> always the case. If you take a look, $H_1$ is not lefist heap.

## Runtime analysis

- `merge`, `deleteMin`, and `insert` are all running in $O(\log N)$ amortized time.

## Reference

- MAW Chapter 6
- http://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/heaps.pdf