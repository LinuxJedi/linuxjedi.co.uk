Title: Skew heap
Date: 2017-04-05 23:30
Category: Data Struct & Algo
Tags: heaps, maw
Summary: Summary for skew heap

This is the summary of *skew heap* part in MAW Chapter 6.

## Motivation

Like the relation between splay trees and AVL trees, we want to have 
$O(\log N)$ amortized cost per operation. In addition, we don't want
to have any auxiliary information stored at the nodes. In this case,
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

## Runtime analysis

- `merge`, `deleteMin`, and `insert` are all running in $O(\log N)$ amortized time.

## Reference

- MAW Chapter 6
- http://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/heaps.pdf