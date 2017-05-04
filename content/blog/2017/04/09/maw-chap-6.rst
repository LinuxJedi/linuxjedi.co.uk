##########################
MAW: Chapter 6 Reflection
##########################

:date: 2017-04-09 10:45
:category: misc
:tags: meta, maw, heaps
:summary: An overview summary of MAW Chapter 6

***********
Reflection
***********

In chapter 6, we learn about the priority queue ADT. We assume each item has 
a "priority" and the ADT allows us to insert the element into the queue and 
get the element with "highest" priority from the queue. The model looks like

.. raw:: html

    <img src="/images/priority-queue-ADT.PNG" alt="priority queue ADT"/>

and the big picture we have studied so far becomes:

.. raw:: html

    <img src="/images/ADT.PNG" alt="ADT overview"/>

In order to support two operations required by the model, we propose four new 
implmentations. `Binary heap <{filename}/blog/2017/03/31/binary-heap.md>`_ is 
the most commonly-seen one. Insert can be done in :math:`O(\log N)` in the worst
case and constant on average. DeleteMin can be done in :math:`O(\log N)`. However,
it has natural drawback in supporting merge operation, which is needed when we 
want to merge two heaps into one. This leads to the 
`leftist heap <{filename}/blog/2017/04/03/leftist-heaps.md>`_. Leftist heap
supports all three operations (insert, DeleteMin, merge) efficiently but we
needs to maintain extra information in the node and we need to do extra test 
during merge in order to maintain the leftist heap property. 
To better solve these two little disadvantages, we propose 
`skew heap <{filename}/blog/2017/04/04/skew-heap.md>`_, which has 
no restriction on the tree structure at all while still enjoying the efficiency of operations
in amortized time. However, there is still room for improvement because
both leftist heap and skew heap cannot support constant on average insertion like
binary heap does. This is why we propose a new structure called 
`binomial queue <{filename}/blog/2017/04/08/binomial-queue.md>`_.

There are many applications of priority queues:

- Operating system task scheduler
- Forward network packets in order of urgency
- Select most frequent symbols for data compression
- Sorting
- Implementation for greedy algorithms

**********
Left Out
**********

Some material I left out when I work through this chapter:

- 6.9.c, 6.10, 6.12, 6.20, 6.21, 6.30, 6.32, 6.33, 6.34, 6.35, 6.36

**********
Reference
**********

- MAW Chapter 6
- https://courses.cs.washington.edu/courses/cse332/10sp/lectures/lecture4.pdf