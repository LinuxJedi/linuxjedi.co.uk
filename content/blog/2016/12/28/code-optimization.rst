############################
A peek in code optimization
############################

:date: 2016-12-28 13:21
:category: Data Struct & Algo
:tags: singly-linked-list, software-engineering
:summary: MAW 3.9 solution optimization

Quite often, when I take a look at a programming
question solution, I'm amazed by how succint the provided
solution is. However, it is also known that getting an "optimized"
solution is often taking iterative approach. This is something
that I didn't realize until I start to work in the industry.

This post is mainly a reminder to keep reminding myself about this point:
We don't have to give a perfect solution right away. We can provide a
solution and gradually make it better.

The example I show here is ``integerList add(integerList A, integerList B)``,
which is part of `MAW 3.9 integer arithmetic package question <{filename}/blog/2016/12/25/integer-package.rst>`_

.. code-block:: c

    integerList
    add(integerList A, integerList B)
    {
      PtrToNode dummyA = A->NextDigit;
      PtrToNode dummyB = B->NextDigit;
      integerList R = malloc(sizeof(struct Node));
      PtrToNode dummyR = R;
      int digitSum = 0;
      int carry = 0;

      while (dummyA != NULL && dummyB != NULL)
      {
        digitSum = dummyA->Digit + dummyB->Digit + carry;
        if (digitSum < 10)
        {
          addDigit(digitSum, dummyR);
          carry = 0;
        }
        else
        {
          carry = 1;
          addDigit(digitSum-10, dummyR);
        }
        dummyA = dummyA -> NextDigit;
        dummyB = dummyB -> NextDigit;
        dummyR = dummyR -> NextDigit;
      }

      // example case: 342 + 706
      if (carry == 1 && dummyA == NULL && dummyB == NULL)
      {
        addDigit(carry, dummyR);
        dummyR = dummyR->NextDigit;
      }

      while(dummyA != NULL)
      {
        addDigit(dummyA->Digit + carry, dummyR);
        carry = 0;
        dummyA = dummyA->NextDigit;
        dummyR = dummyR->NextDigit;
      }

      while(dummyB != NULL)
      {
        addDigit(dummyB->Digit + carry, dummyR);
        carry = 0;
        dummyB = dummyB->NextDigit;
        dummyR = dummyR->NextDigit;
      }

      return R;
    }
  
The idea for this first iteration solution stems from MAW 3.5
`List unionSortedLists(List L, List P) <https://github.com/xxks-kkk/algo/blob/master/linkedList/generic/linkedList.c>`_:

  Given two sorted lists, L and P, write a procedure to compute L1 union L2 using
  only the basic list operations.

Since we put the least significant digit as the very first data node and we
put the most significant digit as the last data node, we walk through the list.
If you compare this routine with ``unionSortedLists`` routine, you can easily
find that both routine structure is composed of three while loops. This makes sense
because ``union`` and ``add`` are extremely similar mathematically.

First we start by adding the unit digit. If both numbers have the same number of digits,
then we are done afte the first while loop. There is a special case where we still have
a carry after we processed all the digits. If number of digits for two numbers are not the same,
then we just move extra digits to the result.

Let's see how we can optimize this code.

In the solution, we build the case around the number of digits that operands have.
However, this is necessary because in the case that two numbers have different number of digits,
we can add leading zeros to the beginning of the number with fewer digits. This will make
adding two numbers with different number of digits the same as adding two numbers with the same
number of digits. So, we eliminate the latter two while loops and only need to keep the first while
loop in the original solution.

Here is the final result.

.. code-block:: c

    integerList
    add(integerList A, integerList B)
    {
      PtrToNode dummyA = A->NextDigit;
      PtrToNode dummyB = B->NextDigit;
      integerList R = makeEmpty();
      PtrToNode dummyR = R;
      int digitSum = 0;
      int carry = 0;
      int x, y;

      while (dummyA != NULL || dummyB != NULL)
      {
        (dummyA != NULL) ? (x = dummyA->Digit) : (x = 0);
        (dummyB != NULL) ? (y = dummyB->Digit) : (y = 0);

        digitSum = x + y + carry;
        carry = digitSum / 10;
        addDigit(digitSum % 10, dummyR);

        if (dummyA != NULL) dummyA = dummyA -> NextDigit;
        if (dummyB != NULL) dummyB = dummyB -> NextDigit;
        dummyR = dummyR -> NextDigit;
      }

      // example case: 342 + 706
      if (carry == 1)
      {
        addDigit(carry, dummyR);
        dummyR = dummyR->NextDigit;
      }

      return R;
    }
