Title: Sorting prelim
Date: 2017-04-18 10:03
Category: Data Struct & Algo
Tags: sorting, maw
Summary: Prelim for sorting

Chapter 7: Sorting will have some rigorous analysis of the sorting algorithms
(no wonder as suggested by the title of the book). Some meta-concepts related with
sorting appeard at the very beginning of the chapter. I usually push them to the
end-chapter summary post but this time I decide to do a writeup beforehand because 
I find it is really hard to talk about various sorting schemes without setting up some
ground concepts first.

## Definitions

- Sorting problem: Given an array $A$, output $A$ such that: 
  For any $i$ and $J$, if $i < j$, then $A[i] \le A[j]$.

\* ---- Note ---- *

> Here, for the input, we are given an array $A$ of data records, each with
> a key (which can be an integer, character, string, etc) as long as the following
> condition can be met:
>
> - There is an ordering on the set of possible keys
> - We can compare any two keys using $<, >, =$

- Sorting algorithm using comparison operators (i.e $<, >, =$) is known as
**comparison-based sorting**. Another major type is called **counting sort** (i.e. Radix sort).

- If the entire sort can be done in main memory (i.e number of elements is relatively small, usually less than a million), we call it **internal sorting**. By the contrast,
if the data is on the disk, we call it **external sorting**.

- An algorithm requires $O(1)$ extra space is known as an **in place** sorting algorithm.

\* ---- Note ---- *

> Under the context of the sorting, we may ask: Does the sorting algorithm require extra
> memory to sort the collection of items? Do we need to copy and temporarily store some 
> subset of the keys/data records?

- A sorting algorithm is **stable** if elements with equal keys are left in the same
order as they occur in the input. In other words, we can ask ourself the question:
Does it rearrange the order of input data records which have the same key value
(duplicates)? If the answer is No, then the sorting algorithm is *stable*.
One example is that Phone book is sorted by name. 
Now let's sort the book by country - is the list still sorted by name within each country?
As you can tell, it is an extremely important property for databases.

\* ---- Note ---- *

> When we evaluate the performance of a sorting algorithm, we usually evaluate it
> from three perspectives: *running time*, *memory requirements (aka space)*, 
> and *stability*.

- There will be three kinds of running time mentioned in the sorting analysis:

    - *average case time*: given an arbitrary input, what do we expect the running time
    to be.
    - *worst case time*: for a particular degenerate case, how bad will the algorithm
    perform.
    - *best case time*: for a particularly benevolent input case, what is the best case 
    performance.

## Reference

- MAW Chapter 7
- https://www.cs.duke.edu/courses/fall01/cps100/notes/sorting_cheat.txt
- https://courses.cs.washington.edu/courses/cse373/01sp/Lect15.pdf
- http://web.mit.edu/1.124/LectureNotes/sorting.html