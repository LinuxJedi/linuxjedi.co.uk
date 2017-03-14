Title: MAW Chapter 5: Hashing writing questions
Date: 2017-03-13 17:41
Category: Data Struct & Algo
Tags: hashing, proof, math, maw

## Solutions

including: MAW 5.4

### MAW 5.4

> A large number of deletions in a separate chaining hash table can cause the 
> table to be fairly empty, which wastes space. In this case, we can rehash to 
> a table half as large. Assume that we rehash to a larger table when there are 
> twice as many elements as the table size. How empty should the table be before
> we rehash to a smaller table?

We must be careful not to rehash too often. Let $p$ be the threshold (fraction of table
size) at which we rehash to a smaller table. Then, if the new table has size $N$, 
it contains $2Np$ elements. This table will require rehashing after either 
$2N-2Np$ insertions or $pN$ deletions. Then, we don't want to do rehashing either 
after a few insertion or a few deletions. A good strategy is to set $2N-2Np$ equals to $pN$
and we get $p = \frac{2}{3}$. For instance, suppose we have a table of size 300.
If we rehash at 200 elements, then the new table size is $N = 150$, and we can do 
either 100 insertions or 100 deletions until a new rehash is required. 

If we know that insertions are more frequent than deletions, then we might choose $p$
to be somewhat larger. All in all, we play around the relation between $2N-2Np$ and 
$pN$ depends on which operation we favorite.