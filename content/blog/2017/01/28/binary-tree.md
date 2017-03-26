Title: Binary Tree & Binary Search Tree
Date: 2017-01-29 13:20
Category: Data Struct & Algo
Tags: trees, maw
Summary: Binary tree and binary search tree summary

This is the summary of *binary tree* and *binary search tree* part in MAW Chapter 4.

## Concept

- A *binary tree* is a tree in which no node can have more than two children. 
- An important application of binary trees is *binary search tree*: for every node,
  $X$, in the tree, the values of all the keys in its left subtree are smaller than
  the key value in $X$, and the values of all the keys in its right subtree are larger
  than the key value in $X$ (*BST-property*).

## Classification of binary trees

- A *full* binary tree (proper binary tree or 2-tree) is a binary tree in which each node
  has exactly zero or two children.

\* ---- Note ---- *

> A *full node* in a binary tree is a node that has exactly two non-null children.

- A *complete* binary tree is a binary tree, which is completely filled, with the possible
  exception of the bottom level, which is filled from left to right.

![full-complete-binary-tree]({filename}/images/full-complete-binary-tree.PNG)

- A *perfect* binary tree: A binary tree in which all internal nodes have exactly two children 
  and all leaves are at the same level. It has property: each level has exactly twice as many 
  nodes as the previous level (since each internal node has exactly two children).

![perfect-binary-tree]({filename}/images/perfect-binary-tree.png)

- A *balance* binary tree: a binary tree structure in which the left and right 
  subtrees of every node differ in height by no more than 1. Yes, [AVL tree]({filename}/blog/2017/02/05/avl.md)
  definition.

## Properties

- The average depth of binary tree is $O(\sqrt{n})$
- A binary tree of $N$ nodes, there are $N+1$ `NULL` pointers representing children (MAW 4.4)
- The maximum number of nodes in a binary tree of height $H$ is $2^{H+1}-1$ (MAW 4.5)
- The number of full nodes plus one is equal to the number of leaves in a nonempty binary tree
- The average depth of a node in a binary search tree constructed from random data is $O(\log n)$
- The average of height of a random binary search tree is $O(\log n)$ (i.e., $E[h] = O(\log n)$) (MAW 4.14)
- All the basic operations `find`, `findMin`, `findMax`, `insert`, and `delete`
  $O(H)$ time, where $H$ is the height of the tree.
    - worst case: height $H = n - 1$
    - base case: height $H = \log N$, where the tree is a complete binary tree.
- Randomly built binary search trees:
    - The *average height* is much closer to the best case.
    - Little is known about the average height when *both insertion and deletion* are used.
    - characteristics
        - Keys inserting in *random order* into an initially empty tree.
        - Each of the $n!$ *permutations* of the input keys is *equally likely*.

## Reference

- MAW Chapter 4
- https://en.wikipedia.org/wiki/Binary_tree
- https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html
