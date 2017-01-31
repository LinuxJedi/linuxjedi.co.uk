Title: MAW Chapter 4: Tree proof questions
Date: 2017-01-26 17:41
Category: Data Struct and Algo Analysis in C
Tags: trees, proof

There are a lot of written proof questions in Chapter 4. Those questions offer
great insights on the general techniques in solving algorithmatic proving questions.
So, I decide to record them in this single post. Of course, this post will be continually
updated as I work through the chapter.

## Insights

- Recursive tree definition is a natural fit with induction (i.e., MAW 4.5, 4.6, 4.7).
- Usually there are two ways to prove a problem in tree, one direction is from induction
  and the other one is from basic tree property (i.e., MAW 4.4, 4.6).
- Combinatorics (relating to binomials) and Probability theory (discrete part) are important to look at (i.e., MAW 4.14)

## Solutions

### MAW 4.4

> Show that in a binary tree of $N$ nodes, there are $N + 1$ `NULL` pointers
> representing children.

**Proof:**
For a binary tree with $N$ nodes, there are two types of edges (pointers): 

1. edges that are doesn't exist (`NULL` pointers).
2. edges that exist to connect nodes (not `NULL` pointers).

Let's first calculate the number of pointers in total, regardless whether the pointer
is `NULL` or not. Since each node has $2$ outgoing pointers, 
there are $2N$ pointers in total. Next, we need to calculate the number of edges that actuall
exist. Since each edge connects some node to its parent, and every node except 
the root has one parent. In other words, each node, except the root node, has one incoming
pointer from its parent. So, we have $N-1$ edges existing. Thus the remaining
$2N - (N-1) = N+1$ edges are actually non-existing. Thus, we have $N+1$ `NULL` pointers.

### MAW 4.5

> Show that the maximum number of nodes in a binary tree of height $H$ is $2^{H+1}-1$.

**Proof:** 
Let's prove this by induction.

*Base case:* $H = 0$. A binary tree of height $0$ has only one node, root. $2^{H+1}-1$ equals
one for $H = 0$. Therefore ture for $H = 0$.

*Inductive Hypothesis:* Assume that the maximum number of nodes in a binary tree of height $H$ is
$2^{H+1}-1$ for $H = 1, 2, ..., k$. Consider a tree $T$ of height $k+1$. The root of $T$ has 
a left subtree and a right subtree each of which has height at most $k$. These can have
at most $2^{k+1}-1$ nodes each by the inductive hypothesis. Adding the root node gives the 
maximum number of nodes in a binary tree of height $k+1$, 

$$
\begin{equation} 
2(2^{k+1} - 1) + 1 = 2^{(k+1)+1} - 1 
\end{equation}
$$

Remarks:

The maximum condition achieves when we have *perfect binary tree*.

$$
\begin{equation}
n = \sum_{i=0}^{h} 2^i = 2^{h+1} - 1 \text{where n is the number of nodes} 
\end{equation}
$$

### MAW 4.6

> A *full node* is a node with two children. Prove that the number of full nodes
> plus one is equal to the number of leaves in a nonempty binary tree.

Let's use two methods to prove this question.

*Method 1:*

**Proof:**
Let's use the following notation for our proof:

$$
\begin{eqnarray*}
N & = & \text{number of nodes in a nonempty binary tree} \\
F & = & \text{number of full nodes} \\
H & = & \text{number of nodes with one child} \\
L & = & \text{number of leaves}
\end{eqnarray*}
$$

Then, we have $N = F + H + L \label{eq:1}$. We can get another equation based on the number of 
edges: $N - 1 = 2F + H \label{eq:2}$. $N-1$ is the number of edges for a $N$ node binary tree 
and $2F + H$ is another way to calculate the number of edges. Now based on these 
two euqations we have:

$$
\begin{eqnarray*}
2F + H + 1 & = & F + H + L \\
F + 1 & = & L
\end{eqnarray*}
$$

*Method 2:*

**Proof:**
Let's prove by induction. If there are $N$ full nodes in a non-empty binary tree
then there are $N+1$ leaves.

*Base case:* $N = 0$ This is ture because the tree has one node and the root is 
a leaf.

*Inductive hypothesis:* Suppose the theorem holds for $N = 1, 2, ..., k$. Then we 
want to show that if there are $k+1$ full nodes in a non-empty binary tree then there 
are $k+2$ leaves. Pick a leaf node and keep removing its parent recursively 
(i.e., remove its parent and then parent's parent and so on) until a full node
is reached. That is, you are traversing from a leaf along the path towards the root,
while removing the nodes along the path before a full node is reached. This full node
becomes a non-full node because one of its child node is removed. At this point the
tree will have one less leaf and one less full node.

![]({filename}/images/maw-4-6.PNG)

Therefore, the tree has $k$ full nodes after the nodes are removed. By the inductive
hypothesis there are $k+1$ leaves. Add all the nodes that were removed back into the 
tree the same way to create the original tree. We are adding one full node and 
one leaf node. Therefore, we have $k+1$ full nodes with $k+2$ leaves.

### MAW 4.7

> Suppose a binary tree has leaves $l_{1}, l_{2}, ..., l_{M}$ at depths
> $d_{1}, d_{2}, ...,d_{M}$, repectively. Prove that $\sum_{i=1}^M 2^{-d_{i}} \leq 1$
> and determine when the quality is true.

**Proof:**
Let's prove this by induction. 

*Base case:* when $M = 1$, there is one node: the root is a leaf wit depth zero. Then
the sum is one, and claim holds.

*Inductive hypothesis:* Suppose the theorem is true for all trees with at most $k$ nodes.
Consider any tree with $k+1$ nodes. Such a tree consists of an $i$ node left subtree and 
a $k-i$ node right subtree. By the inductive hypothesis, the sum for the left subtree
leaves is at most one with respect to the left tree root. Because all leaves are one deeper
with respect to the original tree than with respect to the subtree, the sum is at
most $1/2$ with respect to the root. Similar logic implies that the sum for leaves 
in the right subtree is at most $1/2$ proving the theorem.

The equality is true if and only if every internal node is a full node. In other words,
no nodes have one child. Suppose there is a node with one child, and the equality still
holds. Each time we remove two nodes to create a new tree that has a node with no child.
This new tree has the same property has the previous one, and by the statement we proved
above, we should have the same sum as the old, which is one. Eventually, we are left
with two node, one of them is root. Now, we calculate the sum, which gives $1/2$. This 
is contradiction to the equality.

\* ---- Note ---- *

> This problem is called [Kraft–McMillan inequality](https://en.wikipedia.org/wiki/Kraft%E2%80%93McMillan_inequality),
  which is one of fundamental theorem in Information theory. I find [this youtube playlist about information theory](https://www.youtube.com/playlist?list=PLE125425EC837021F)
  is really good as an intro to the field because it doesn't make the material look very daunting and super technical,
  which some [lecture note](http://circuit.ucsd.edu/~yhk/ece154c-spr16/pdfs/LectureNotes01.pdf) manages to achieve.

### MAW 4.14

> Prove that the depth of a random binary search tree (depth of the deepest node) is $O(\log N)$, on average.

This question can be restated like the following: suppose that we insert $n$ distinct elements into an 
initially empty tree. Assuming that the $n!$ permutations are equally likely to occur, then show that
the average height of the tree is $O(\log N)$.

Before we dive into the proof, let's think about how we can construct a random binary search tree.
We construct a tree $T$ by inserting in order randomly selected $n$ distinct elements into an 
initially empty tree. Here the actual values of the elements do not matter. What matters is the position
of the inserted element in the $n$ elements. Thus, we construct a random binary search tree as the following:

An element $i$ from the $n$ elements is selected uniformly ar random and is inserted to the empty tree. Then all 
the other elements are inserted. Here all the elements greater than $i$ go into the right subtree of $i$
and all the elements smaller than $i$ go into the left subtree. Thus, the height of the tree constructed
is one plus the larger of the height of the left subtree and the height of the right subtree.

**Proof:**
Following our construction process above, if we randomly choose the $i^{th}$ key, the left
subtree has $i-1$ elements and the right subtree has $n-i$ elements. Let $h_{n}$ be the
height of a randomly built binary search tree on $n$ keys. Then we have

$$
\begin{equation} 
h_{n} = 1 + max(h_{i-1}, h_{n-i}) \label{eqn:1}
\end{equation}
$$

Now, let's define $Y_{n} = 2^{h_n}$. If we can show 
that $E[Y_n]$ is polynomial in $n$, we then have $E[h_n] = O(\log n)$. Again, $Y_n$ 
depends on $i$ not $n$. Let's represent \ref{eqn:1} in terms of $Y_n$:

$$
\begin{eqnarray*}
h_{n} &=& 1 + max(h_{i-1}, h_{n-i}) \\
2^{h_n} &=& 2^{1 + max(h_{i-1}, h_{n-i})} \\
        &=& 2 \cdot 2^{max(h_{i-1}, h_{n-i})} \\
        &=& 2 \cdot max(2^{h_{i-1}}, 2^{h_{n-i}}) \\
Y_n     &=& 2 \cdot max(Y_{i-1}, Y_{n-i}) 
\end{eqnarray*}
$$

Now, let's calculate $E[Y_n]$. Here, $I=i$ means we pick $i_{th}$ element as our 
first element inserting into the empty tree.Since, we pick the first insertion element equally
likely, then $P(I=i) = \frac{1}{n}$.

$$
\begin{eqnarray*}
E[Y_n] &=& \sum_{i=1}^n E[Y_n|I=i]P(I=i) \\
       &=& \sum_{i=1}^n E[Y_n|I=i]\frac{1}{n} \\
       &=& \frac{2}{n}\sum_{i=1}^n E[max(Y_{i-1},Y_{n-i})] \\
       &\le& \frac{2}{n}\sum_{i=1}^n (E[Y_{i-1}] + E[Y_{n-i}])
\end{eqnarray*}
$$

Now we expand the last summation as

$$
\begin{equation}
(E[Y_0] + E[Y_{n-1}]) + \dots + (E[Y_{n-1}] + E[Y_0]) = 2\sum_{i=0}^{n-1}E[Y_i]
\end{equation}
$$

Thus, we have

$$
\begin{equation}
E[Y_n] \le \frac{4}{n}\sum_{i=0}^{n-1}E[Y_i]
\end{equation}
$$

Then, we will show that for all integers $n>0$, 

$$
\begin{eqnarray*}
E[Y_n] &\le& \frac{1}{4}\dbinom{n+3}{3} \\
       &=& \frac{1}{4}\cdot\frac{(n+3)(n+2)(n+1)}{6} \\ 
       &=& O(n^3)
\end{eqnarray*}
$$

Then, we use *Jensen's inequality*, which states that $f(E[X]) \le E[f(X)]$ provided
the expectations exist and are finite, and f(x) is convex. Let this $X$ be $h_n$ and
$f(x) = 2^x$, then $E[f(X)] = E[Y_n]$. So, we have

$$
\begin{equation}
2^{E[h_n]} \le \frac{1}{4}\dbinom{n+3}{3} = O(n^3)
\end{equation}
$$

By taking the log of both sides, we have $E[h_n] = O(\log n)$

**Remarks:**

- Let's first prove $\sum_{i=0}^{n-1}\dbinom{i+3}{3} = \dbinom{n+3}{4}$

**Proof:** Use *Pascal's identity:* $\dbinom{n}{k} = \dbinom{n-1}{k-1} + \dbinom{n-1}{k}$
Also using the simple identity $\dbinom{4}{4} = 1 = \dbinom{3}{3}$. We have:

$$
\begin{eqnarray*}
\dbinom{n+3}{4} &=& \dbinom{n+2}{3} + \dbinom{n+2}{4} \\
                &=& \dbinom{n+2}{3} + \dbinom{n+1}{3} + \dbinom{n+1}{4} \\
                &=& \dbinom{n+2}{3} + \dbinom{n+!}{3} + \dbinom{n}{3} + \dbinom{n}{4} \\
                &\vdots& \\
                &=& \dbinom{n+2}{3} + \dbinom{n+!}{3} + \dbinom{n}{3} + \dots + \dbinom{4}{3} + \dbinom{4}{4} \\
                &=& \sum_{i=0}^{n-1}\dbinom{i+3}{3}
\end{eqnarray*}
$$

- Let's prove $E[Y_n] \le \frac{1}{4}\dbinom{n+3}{3}$ by induction.

**Proof:** *Base case:* $n=1$. 

$$
\begin{equation}
1 = Y_1 = E[Y_1] \le \frac{1}{4}\dbinom{1+3}{3} = 1.
\end{equation}
$$

*Inductive Hypothesis:* Assume that $E[Y_i]\le\frac{1}{4}\dbinom{i+3}{3}$ for all $i<n$. Then,

$$
\begin{eqnarray*}
E[Y_n] &\le& \frac{4}{n}\sum_{i=0}^{n-1}E[Y_i] \\
       &\le& \frac{1}{4}\dbinom{i+3}{3} \\
       &=&   \frac{1}{n}\sum_{i=0}^{n-1}\dbinom{i+3}{3} \\
       &=&   \frac{1}{n}\dbinom{n+3}{4} \\
       &=&   \frac{1}{n}\frac{(n+3)!}{4!(n-1)!} \\
       &=&   \frac{1}{4}\frac{(n+3)!}{3!n!} \\
       &=&   \frac{1}{4}\dbinom{n+3}{3}
\end{eqnarray*}
$$

\* ---- Note ---- *

> I [reference this lecture note](https://www.cs.bgu.ac.il/~fds112/wiki.files/P05.pdf) when I try to develop the proof. 
> Overall, I share the similar proof with this one. However, we have slightly difference in terms of how we 
> define $E[Y_n]$. The note defines an indicator random variables $Z_{n,i} = I\{I=i\}$, where $I=i$ means we pick $i_{th}$ element as our 
> first element inserting into the empty tree. Since, we pick the first insertion element equally
> likely, then $P(I=i) = \frac{1}{n}$, and thus, $E[Z_{n,i}] = \frac{1}{n}$ by $E[I_A] = P(A)$. Then, he defines $Y_n = \sum_{i=1}^nZ_{n,i} \cdot (2 \cdot max(Y_{i-1}, Y_{n-i}))$
> because only one $Z_{n,i}$ can be $1$ and all others are $0$. It seems right but when he calculates the $E[Y_n]$, he states that
> $Z_{n,i}$ is independent of $Y_{i-1}$ and $Y_{n-i}$. However, I don't think so as the height of the tree $h_n$, which $Y_n$ is constructed from 
> depends on which element we pick first. I tend to think about $E[Y_n]$ as expectation of the conditional expectation.

[//]: # (https://www.cs.rochester.edu/~gildea/csc282/slides/C12-bst.pdf)
[//]: # (http://cs.stackexchange.com/questions/6342/proof-that-a-randomly-built-binary-search-tree-has-logarithmic-height)