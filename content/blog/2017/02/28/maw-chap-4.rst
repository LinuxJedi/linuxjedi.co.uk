##########################
MAW: Chapter 4 Reflection
##########################

:date: 2017-03-12 10:45
:category: misc
:tags: meta, maw
:summary: An overview summary of MAW Chapter 4

***********
Reflection
***********

In Chapter 4, we learn about the tree data structure. If we take a look from ADT
perspective, the ADT we learn about is called Dictionary (a.k.a Map) ADT, which 
represented by a set of (key, value) pairs that support insert, find, delete operations.
The core idea for this ADT, as you can imagine, is to store information according to 
some key and be able to retrieve it efficiently. Now our big picture becomes:

.. raw:: html

    <img src="/images/maw-chap4.PNG" alt="predecessor-successor" style="width: 700px;"/>

Implementing dictionary ADT with tree structure brings following advantages:

- Trees reflect structural relationships in the data
- Trees are used to represent hierarchies
- Trees provide an efficient insertion and searching
- Trees are very flexible data, allowing to move subtrees around with minumum effort

Many different tree structures get presented in this chapter. Most fundamental ones are:

- `Binary Search Tree <{filename}/blog/2017/01/28/binary-tree.md>`_
- `AVL tree <{filename}/blog/2017/02/05/avl.md>`_
- `Splay tree <{filename}/blog/2017/02/11/splay.md>`_
- `B-tree <{filename}/blog/2017/02/19/b-tree.md>`_

Some variations to the above structures are Order Statistic Tree (MAW 4.44), Threaded Tree (MAW 4.45),
k-d Tree (MAW 4.46), and B*-tree (MAW 4.38).

**********
Left Out
**********

Some material I left out when I work through this chapter:

- 4.11 (cursor implementation of trees is not top priority)
- 4.33, 4.34 (Form a nice tree drawing project; don't have time to do them now)
- 4.12, 4.13, 4.14, 4.26.b, 4.37.b;c, 4.38 (interesting but may require too much effort)

**********
Reference
**********

- https://courses.cs.washington.edu/courses/cse332/10sp/lectures/lecture6.pdf