Title: Splay Tree
Date: 2017-02-13 01:12
Category: Data Struct & Algo
Tags: trees, maw
Summary: Splay tree summary

This is the summary of *Splay tree* part in MAW Chapter 4.

## Motivation

Ordinary BST has no balance conditions and thus, it is possible for a whole sequnece of $O(N)$ accesses to take place. This cumulative running time 
then becomes noticeable. So, we introduce the balance condition on BST to improve our running time. One way to do so is to enforce a balance condition
when nodes change (i.e. insert or delete) like AVL. However, this data structure is hard to code and rebalancing costs time. In addition, sometimes it is 
OK for us to have $O(N)$ operation as long as it occurs infrequently. In other words, A search data structure with $O(N)$ worst-case time, but a *guarantee*
of at most $O(M \log N)$ for any $M$ consecutive operations, is good enough. Splay tree meets our needs. It is a data structure that 
lies right in-between BST (no balance condition) and AVL (very strict balance condition).

## Concept

A splay tree is a type of balanced binary search tree. Structurally, it is identical to an ordinary binary search tree; the only difference is in the 
algorithms for finding, inserting, and deleting entries. Specifically, splay tree is a self-adjusting tree, which the structure get organized over time
as nodes are accessed (i.e., insert, delete, or find). This makes sense because if we don't re-structure the tree each time we access an node, then 
the amortized time bound should be $O(M N)$ for a sequence of $M$ accesses instead of $O(M \log N)$.

The way we restructure the tree is called *splaying*. Chapter 4 talks about bottom-up splaying algorithms. Every time a node is accessed in a splay tree,
it is moved to the root of the tree. The amortized cost of the operation is $O(\log N)$. As shown by MAW, simply moving the element to the root by
rotating it up the trees does not have this property. However, the following three structuring rules do guarantee this amortized bound.

```

                             y             x
   Zig (terminal case):     /     ====>     \               (same as AVL single rotation)
                           x                 y

                    z              z
                   /              /             x
   Zig-zag:       y     ====>    x   ====>     / \          (same as AVL double rotation)
                   \            /             y   z
                    x          y

                    z                         x
                   /            y              \
   Zig-zig:       y     ====>  / \   ====>      y
                 /            x   z              \
                x                                 z
```

In the above pictures, x is the node that was accessed (that will
eventually be at the root of the tree).  By looking at the local
structure of the tree defined by x, x's parent, and x's grandparent we
decide which of three rules to follow.  We continue to
apply the rules until x is at the root of the tree.

```
Splay(1)

              7                    7                   7               1
             /                    /                   /                 \
            6                    6                   6                   6
           /                    /                   /                   / \
          5                    5                   1                   4   7 
         /      =======>      /        =======>     \    ======>      / \
        4                    4                       4               2   5
       /                    /                       / \               \
      3                    1                       2   5               3
     /                      \                       \
    2                        2                       3
   /                          \
  1                            3
```

## Implementation details

Splay tree is really a flexible data structure in the sense that there are many options to implement 
the "splay" rules and corresponding tree operations and still have the property hold. Reference [wiki](https://en.wikipedia.org/wiki/Splay_tree)
for complete summary. Here, I only mention some of my findings. Please note that depends on how you implement your operations, the resulting tree
may be different (i.e. different insert algorithm may result in different tree structure but there root will be the same).

### Insertion (bottom-up)

There are two ways to do this. The first way is to use "split" to split the tree based upon the insertion value. By the property of splaying, 
we will either have the insertion value (already inside the tree) or the parent of the insertion point at the root. Then we can make our insertion 
value as the new root and adjust the orginal tree to form the new tree. For example,  if the insertion value ``elem`` smaller than the root, we do

```{c}
if (elem < T->Element)
{
  newT->Right = T;
  newT->Left = T->Left; // we can do this b/c the result of splaying is the parent node of where we should insert.
  T->Left = NULL;
}
```

The code is straightforward but ``newT->Left = T->Left`` is worth a remark. Here, when ``T`` is the parent of the insertion point, 
we know ``T``'s left subtree's values are smaller than ``elem`` as well. This is because 
if there is any node $x$ greater than ``elem`` but smaller than ``T``'s value, then ``T`` should be $x$ instead (by splaying), which is a contradiction.

The second way is to do BST insertion first and then splay the insertion value, which is really straightforward and easy to code. 

## Deletion (bottom-up)

Correspondingly there are two methods to deletion as well. The first way is to splay the to-be-deleted node. This puts the node at the root. If it is
deleted, we get two subtrees $T_L$ and $T_R$. If we find the largest element in $T_L$, then this element is rotated to the root of $T_L$, and 
$T_L$ will now have a root with no right child. We can finish the deletion by making $T_R$ the right child.

The second way is to do BST deletion first, and then splay the parent of the deletion point to the root. It is quite similar to BST deletion and see
the implementation [here](https://github.com/xxks-kkk/algo/blob/master/trees/splay/splay.c).

## Properties

- any $M$ consecutive tree operations starting from an empty tree take at most $O(M \log N)$ time.
- Even though the worst-case running time is $O(N)$ for operation, the amortized cost of the operation is $O(\log N)$.
- if all nodes in a splay tree are accessed in sequential order, the resulting tree consists of a chain of left children. (MAW 4.26.a)
- if all nodes in a splay tree are accessed in sequential order, then the total access time is $O(N)$, regardless of the initial tree.

## Pros & Cons of data structure

Splay tree is simpler and easier to program. Because of its implicity, splay tree insertion and deletion is typically faster in practice.
Find operation can be faster or slower, depending on circumstances. Splay trees are designed to give especially fast access to nodes that 
have been accessed recently, so they really excel in applications where a small fraction of the nodes are the targets of most of the find operation.

## Todo

This post does not cover every part of the splay tree. This post will be updated once I complete the following two parts study:

- MAW Chapter 11 gives a thorough study of the amortized cost of the splay tree operations $O( \log N)$.
- MAW Chapter 12 gives implementation details on top-down splay tree.  

## Reference

- http://www.cs.cmu.edu/afs/cs/academic/class/15859-f05/www/documents/splay-trees.txt
- http://web.stanford.edu/class/archive/cs/cs166/cs166.1146/lectures/08/Small08.pdf (proof of properties in a concise structure)
- http://digital.cs.usu.edu/~allan/DS/Notes/Ch22.pdf
- https://courses.cs.washington.edu/courses/cse373/06sp/handouts/lecture14.pdf
- https://people.eecs.berkeley.edu/~jrs/61b/lec/36