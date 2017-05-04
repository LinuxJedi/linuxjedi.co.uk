.. _polynomial-multiply.rst:

##########################
Polynomial Multiplication
##########################

:date: 2016-12-18 18:53
:category: Data Struct & Algo
:tags: singly-linked-list, maw
:summary: Origin from MAW 3.7

I finally got time to continue working through MAW. The problem 3.7 relates to polynomial multiplication.

*******
Problem
*******

Write a function to multiply two polynomials, using a linked list implementation. You must make sure that
the output polynomial is sorted by exponent and has at most one term of any power.

  a. Give an algorithm to solve this problem in :math:`O(M^2N^2)` time.
  b. Write a program to perform the multiplication in :math:`O(M^2N)` time, where :math:`M` is the number
     of terms in the polynomiial of fewer terms.
  c. Write a program to perform the multiplication in :math:`O(MNlog(MN))` time.
  d. Which time bound above is the best?

**********
Solution
**********

==========
Question 1
==========

The first question is quite straightforward. We keep the result in a linked list with
exponent sorted in descending order. Each time a multiply is performed, we search through
the result linkedlist for the term with the same exponent as ours. If so, we simply add 
coefficients together. If not, we add our product as a new term.

.. code-block:: c

    Polynomial
    multiply1(Polynomial A, Polynomial B)
    {
    Polynomial R = malloc(sizeof(struct Node));
    PtrToNode dummyRPrev = R;
    PtrToNode dummyR = R;
    PtrToNode dummyA = A->Next;
    PtrToNode dummyB = B->Next;

    int tmpExponent, tmpCoefficient;
    
    while (dummyA != NULL)
    {
        while (dummyB != NULL)
        {
          tmpExponent = dummyA->exponent + dummyB->exponent;
          tmpCoefficient = dummyA->coefficient * dummyB->coefficient;

          // we go through the output polynomial to see if there is
          // a term with the same exponent as our tmpExponent.
          while (dummyR != NULL)
          {
            if (dummyR->exponent == tmpExponent)
            {
              dummyR->coefficient = dummyR->coefficient + tmpCoefficient;
              break;
            }
            else
            {
              dummyRPrev = dummyR;
              dummyR = dummyR->Next;
            }
          }

          // We couldn't find the term with the same exponent, so we create
          // a new term in our output polynomial.
          if (dummyR == NULL)
          {
            insert(tmpCoefficient, tmpExponent, dummyRPrev);
          }
        
          dummyR = R;
          dummyB = dummyB->Next;
        }
        dummyB = B->Next;
        dummyA = dummyA->Next;
      }

      return R;
    }

The total running time is :math:`O(M*N)`. We start from the inner most loop. We
go through the result linkedList to search for the duplicate exponent term. The running
time depends on the length of the linkedList. The result linkedList can have at most
:math:`M*N` terms. Then, for the middle loop, we iterate through :math:`N` times and 
for the outer most loop, we iterate through :math:`M` times. So, the total running time
is :math:`O(M*N*MN) = O(M^2N^2)`.

==========
Question 2
==========

We can certainly do better than :math:`O(M^2N^2)`. 

.. code-block:: c

    Polynomial
    multiply2(Polynomial A, Polynomial B)
    {
      int lenA = 0, lenB = 0;
      PtrToNode dummyA = A->Next;
      PtrToNode dummyB = B->Next;
      Polynomial R = malloc(sizeof(struct Node));
      PtrToNode dummyTmp, dummyShort, dummyLong, Long;
      Polynomial Tmp = malloc(sizeof(struct Node));  

      while(dummyA != NULL)
      {
        lenA++;
        dummyA = dummyA->Next;
      }

      while(dummyB != NULL)
      {
        lenB++;
        dummyB = dummyB->Next;
      }

      if (lenA < lenB)
      {
        dummyShort = A->Next;
        dummyLong = B->Next;
        Long = B;
      }
      else
      {
        dummyShort = B->Next;
        dummyLong = A->Next;
        Long = A;
      }

      while(dummyShort != NULL)
      {
        dummyTmp = Tmp;
        while(dummyLong != NULL)
        {
          int coefficient = dummyShort->coefficient * dummyLong->coefficient;
          int exponent = dummyShort->exponent + dummyLong->exponent;
          insert(coefficient, exponent, dummyTmp);
          dummyTmp = dummyTmp->Next;
          dummyLong = dummyLong->Next;
        }
        R = add(R, Tmp);
        dummyLong = Long->Next;
        deletePolynomial(Tmp);
        dummyShort = dummyShort->Next;
      }

      return R; 
    }

Suppose polynomials :math:`A` has :math:`M` terms, and polynomials
:math:`B` has :math:`N` terms. :math:`M < N`.
Instead of updating the result after each multiply, we multiply one term
from :math:`A` (the polynomials with fewer terms) by all the terms from 
:math:`B` (the polynomials with more terms). Then we add this with the output
linkedList using ``Polynomial add(...)`` function I implemented (can be found under
`polynomial.c <https://github.com/xxks-kkk/algo/blob/master/linkedList/polynomial/polynomial.c>`_).
The ``add`` function has a runtime :math:`O(max(M,N))` and thus we can get our runtime for ``multiply2``:

.. math::

    O(max(N,0)) + O(max(N,N)) + O(max(N,2N)) + ... + O(max(N, N(M-1))) = O(M^2N)

Also, we calculate the length of :math:`A` taking :math:`O(M)`; we calculate the length of :math:`B`
taking :math:`O(N)`; and we do ``deleteList`` during the while loop taking :math:`O(MN)`. So, the total runtime is:

.. math::

    O(M^2 N) + O(M) + O(N) + O(MN) = O(M^2 N) 

.. note::

    For this implementation, I kind of using an interface within the function. The logic
    begins with ``while (dummyShort != NULL)`` are the same for both :math:`M<N` and :math:`M>N`.
    So, there is potential to write the same logic twice for these two cases respectively. The solution 
    I use is to provide an interface using ``dummyLong`` and ``dummyShort`` variables.

    Please note we need to multiply one term from the polynomials with fewer terms by all the terms from
    the polynomial with more terms. If we do the other way around, the runtime will be :math:`O(MN^2)`.

===============
Question 3 & 4
===============

I haven't coded up for question 3 because I want to wait for finishing sorting chapter. However, I can see how we
can get :math:`O(MNlog(MN))`. This solution is very similar to Question 1. We first multiply all terms out using 
:math:`O(MN)`. Then, we sort resulting :math:`MN` terms by exponent. Then, we run through the linked list merging any
summing any terms with the same exponent (which will be contiguous). The sort takes :math:`O(MNlog(MN))` time. 
The multipies and the merging of duplicates can be performed in :math:`O(MN)` time.
So, we have:

.. math::

    O(MN) + O(MNlog(MN)) + O(MN) = O(MNlog(MN))

When we actually compare the runtime of three solutions, we can see 1st one is the worst among the three. However,
for 2nd one and 3rd one, the comparison result depends on the size of :math:`M` and :math:`N`. If :math:`M` and 
:math:`N` are close in size, then :math:`O(MNlog(MN))\approx O(MNlog(M^2))=O(MNlog(M))`, which is better than :math:`O(M^2N)`.
However, if :math:`M` is very small in comparison to :math:`N`, then :math:`M` is less than :math:`log(MN)` and in this case,
2nd one is better than 3rd one.
