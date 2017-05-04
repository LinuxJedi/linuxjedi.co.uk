#################################################
Reflection on integer arithmetic package problem
#################################################

:date: 2016-12-26 23:03
:category: Data Struct & Algo
:tags: software-engineering, c
:summary: Origin from MAW 3.9

This weekend, I'm working on MAW 3.9. The single problem results
in almost 500 lines of code. This is quite unexpected. The problem
is stated as the following:

  Write an arbitrary-precision integer arithmetic package. You should
  use a strategy similar to polynomial arithmetic. Compute the distribution
  of the digits :math:`0` to :math:`9` in :math:`2^{4000}`.

This post is the reflection about this problem.

*****************
Which way to go?
*****************

Since the problem states "arbitrary-precision" and "use a strategy similar to
polynomial arithmetic", then I can conclude that linked list is the best data
structure for this problem. However, the question is how we can construct the
linked list to best implement our integer arithmetic operations (i.e. addition,
mulitiplication)?

We essentially have two options:

1. We put the most significant digit as the the very first data node and
   we put the least significant digit as the last data node. For example,
   for a number :math:`123`, we will implement it like ``dummy->1->2->3``.

2. This is the exactly opposite of the first option. We put the least significant
   digit as the very first data node and we put the most significant digit as
   the last data node. Again, for :math:`123`, we will implement is like
   ``dummy->3->2->1``.

Let's evaluate these two options from two perspective:

1. Whether we can easily construct a linked list to represent arbitrary-precision integer?

2. Whether the arithmetic operations are essy to implement? 

From the first perspective, for option one, each time we add a new digit to the most significant position, we insert
a new node at the very beginning of the list (i.e. right after the header node).
On the other hand, for option two, we append a new node
at the very end of the list. Since we design our ``addDigit`` with an input of a pointer to node (i.e. to specify
where to add node), these two options work equally well.

From the second perspective, things are different. Take arithmetic addition as an example. When we try to add
two numbers, for option one, we need to walk through the whole list to begin with the very end of the node
because we want to start with unit digit. This makes our routine complex because we need to use a while loop
to walk through the list first. For second option, situation is easier becauuse the number is implemented in the
reverse order in the list. The very first data node is the unit digit and we can directly start with addition
while we move towards the end of the list. If we need to add additional node because of carry (i.e. :math:`999 + 1`
will be no longer 3-digit but 4-digit number), we can naturally pass the pointer pointing towards the current node to
the ``addDigit`` function.

So, we choose option two to implement our integer package.

************
Memory leak
************

Memory leak is a very important issue to pay attention to during the testing phase. We use `valgrind <http://valgrind.org/>`_
to help us detect if there is any leak in our code. You can reference `their quick start guide <http://valgrind.org/docs/manual/quick-start.html#quick-start.intro>`_
and `memory check user manual <http://valgrind.org/docs/manual/mc-manual.html#mc-manual.errormsgs>`_ for the commands and error shooting.

Here are the two mistakes I made (You can check out `my commit about memory leak debug <https://github.com/xxks-kkk/algo/commit/299ebb9a90791612343f194d9eec1ed3909c97b3#diff-5db0d6074a742e1a08d3bb60c69e5a21>`_):

1. Always ``free`` the chunk allocated by ``malloc`` whenever possible.

Take ``multiply`` function as an example:

.. code-block:: c
   :linenos:
                
    integerList
    multiply(integerList A, integerList B)
    {
      PtrToNode dummyA = A->NextDigit;
      PtrToNode dummyB = B->NextDigit;

      integerList tmpR = makeEmpty();
      PtrToNode dummyTmpR = tmpR;

      integerList R = makeEmpty();

      int product, carry = 0;
      int i, indent = 0;

      while (dummyA != NULL)
      {
        while (dummyB != NULL)
        {
          product = dummyA->Digit * dummyB->Digit + carry;
          carry = product / 10;
          addDigit(product % 10, dummyTmpR);
          dummyTmpR = dummyTmpR->NextDigit;
          dummyB = dummyB->NextDigit;
        }

        if (carry > 0)
        {
          addDigit(carry, dummyTmpR);
          dummyTmpR = dummyTmpR->NextDigit;
        }

        for(i = 0; i < indent; i++)
        {
          addDigit(0,tmpR);
        }

        integerList tmp = R; // prevent memory leak
        R = add(R, tmpR);
        deleteAll(tmp);

        indent ++;
        carry = 0;
        deleteIntegerList(tmpR);
        dummyTmpR = tmpR;
        dummyA = dummyA->NextDigit;
        dummyB = B->NextDigit;
      }

      deleteAll(tmpR);
      return R;
    }

We allocate ``tmpR`` through ``makeEmpty()`` in Line[7]. If we don't do anything about it
inside the function, then the memory will be lost because we have no way to reference this
chunk of memory outside the function. Local variable ``tmpR`` is the only reference to the
memory allocated on the heap. However, once the function is done, the local variable is destroyed
from the stack, and thus, we lose our only reference to the memory chunk. So, we need to free it
before we exit the function (Line[49]).

2. Be careful with a function call inside a function call.

This type of leak is much more subtle than the first one. Originally instead of

.. code-block:: c

    integerList tmp = R;
    R = add(R, tmpR);
    deleteAll(tmp);

I only have ``R = add(R, tmpR)``. This cause the leak because of the following reasoning:
Originally, we have ``R`` points to a list of nodes. When we do ``add(R,tmpR)``, we create
a new list of nodes, which hold our addition result. Then we let ``R`` points towards this newly-created
list. This makes us lose the list of nodes originally pointed by ``R``. That's why we introduce ``tmp``.
                
***************
makeEmpty ?
***************

Originally, I don't have this ``makeEmpty`` function:

.. code-block:: c

    integerList
    makeEmpty()
    {
      integerList R = malloc(sizeof(struct Node));
      R->NextDigit = NULL; // super important step
      return R;
    }

If you take a look at this function, it seems to be a wrapper around ``malloc`` operation, which
seems redundant (we could directly call ``malloc`` directly in the place that ``makeEmpty`` appears).
However, the key for this routine is ``R->NextDigit = NULL;``. This step can be easily omitted. However,
without this step, we don't have fully control on what our newly-allocated empty list (i.e. a list with only
header node) will look like. In other words, our header node will point to somewhere (i.e. ``R->NextDigit``) randomly without
our key step. This can cause serious trouble for the following routine debug. For example, we could have ``R->NextDigit``
holds some address value that happens to have a node structure there with a value in it. For instance, ``dummy->1``.
This can usually happen when you OS try to reuse the memory chunk you previously freed. For example, try the following experiment:

1. replace ``makeEmpty`` on Line[7] & line[10] in ``multiply`` function
2. ``multiply`` works fine with ``test_multiply()`` solely in the test program.
3. ``multiply`` won't work if we do ``test_intializeInteger()`` and ``test_add()`` before ``test_multiply()``
   because the integer we construct will no longer be ``342`` in the test case but something like ``3425``, where
   ``5`` is some value pointed by ``R->NextDigit``.

So, always clear out the pointer by setting it to ``NULL`` whenever we do initialization.
