Title: MAW Chapter 5: Hashing writing questions
Date: 2017-03-16 17:41
Category: Data Struct & Algo
Tags: hashing, proof, math, maw
Summary: My solutions to selected problems in MAW Chapter 5

## Solutions

including: MAW 5.4, 5.5, 5.6, 5.10, 5.11

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

### MAW 5.5

> An alternative collision resolution strategy is to define a sequence, $F(i) = r_i$,
> where $r_0 = 0$ and $r_1, r_2, \dots, r_N$ is a random permutation of the first $N$
> integers (each integer appears exactly once).

> a. Prove that under this strategy, if the table is not full, then the collision can 
> always be resolved.

Since the sequence $F(i)$ is defined as a random permutation of the first $N$ integers,
then each cells of the table will be probed eventually. If the table is not full, then the 
collision can always be resolved.

> b. Would this strategy be expected to eliminate clustering?

This seems to eliminate primary clustering but not secondary clustering because
all elements that hash to some location will try the same collision resolution sequence.

> c. If the load factor of the table is $\lambda$, what is the expected time to perform
> an insert and for a successful search?

The running time is probably similar to quadratic probing. The advantage here is that 
the insertion can't fail unless the table is full.

### MAW 5.6

> What are the advantages and disadvantages of the various collision resolution strategies?

Separate chaining hashing requires the use of pointers, which costs some memory, and the 
standard method of implementing calls on memory allocation routines, which typically are
expensive. 

Linear probing is easily implemented, but performance degrades severly as the load 
factor increases because of primary clustering. 

Quadratic probing is only slightly more 
difficult to implement and gives good performance in practice. An insertion can fail 
if the table is half empty, but this is not likely. Even if it were, such an insertion 
would be so expensive that it wouldn't matter and would almost certainly point up a 
weakness in the hash function. 

Double hashing eliminates primary and secondary clustering but the computation of a second
hash function can be costly. 

### MAW 5.10

> Describe a procedure that avoids initializing a hash table (at the expense of memory).

To each hash table slot, we can add an extra field that we'll call `WhereOnStack`, and 
we can keep an extra stack. When an insertion is first performed into a slot, we push
the address (or number) of the slot onto the stack and set the `WhereOnStack` field to point
to the top of the stack. When we access a hash table slot, we check that `WhereOnStack`
points to a valid part of the stack and that the entry in the (middle of the) stack that is 
pointed to by the `WhereOnStack` field has that hash table slot as an address.


### MAW 5.11

> Suppose we want to find the first occurrence of a string $P_1P_2\dots P_k$ in a long 
> input string $A_1A_2\dots A_N$. We can solve this problem by hashing the pattern string,
> Obtaining a hash value $H_p$, and comparing this value with the hash value formed from 
> $A_1A_2\dots A_k$, $A_2A_3\dots A_{k+1}$, $A_3A_4\dots A_{k+2}$, and so on until 
> $A_{N-k+1}A_{N-k+2}\dots A_N$. If we have a match of hash values, we compare the string character
> by character to verify the match. We return the position (in A) if the strings actually 
> do match, and we continue in the unlikely event that the match is false.

> a. Show that if the hash value of $A_iA_{i+1}\dots A_{i+k-1}$ is known, then the hash 
> value of $A_{i+1}A_{i+2}\dots A_{i+k}$ can be computed in constant time.

As suggested by MAW p.151, we use $\sum_{i=0}^{KeySize-1} Key[KeySize-i-1]\cdot 32^i$
as the function to compute the hash value of a given string. Then, by this definition,
$A_iA_{i+1}\dots A_{i+k-1}$ can be computed as 

$$
H_1 = (32^0A_i + 32^1A_{i+1} + \dots + 32^{k-1}A_{i+k-1}) \bmod N
$$

similarly, $A_{i+1}A_{i+2}\dots A_{i+k}$ can be computed as 

$$
H_2 = (32^1A_{i+1} + \dots + 32^kA_{i+k}) \bmod N
$$

If we take a look at the relationship between these two equations, we can see 

$$
H_2 = H_1 - 32^0A_i \bmod N + 32^kA_{i+k} \bmod N
$$

This can be computed in constant time if $H_1$ is known.

> b. Show that the running time is $O(k+N)$ plus the time spent refuting false matches.

The pattern's hash value $H_p$ computed in $O(K)$ time. Then, $A_1A_2\dots A_k$
is computed in $O(K)$ time. Then starting with $A_2A_3\dots A_{k+1}$ and until
$A_{N-k+1}A_{N-k+2}\dots A_N$, each hash value is computed in $O(1)$ by a) above.
Since, there are $N-k+1-2+1$ terms of $O(1)$, then the total running time is
$O(K) + O(K) + O(N-K) = O(N+K)$. Of course, there is also time we spend on refuting false
matches.