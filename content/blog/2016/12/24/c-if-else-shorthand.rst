###############################
A small C trick I learned today
###############################

:date: 2016-12-24 23:11
:category: programming languages
:tags: c
:summary: A C one-liner

Today I learned a C trick. Here is my original ``printList``:

.. code-block:: c

    void
    printList(List L)
    {
      Pos dummy; // creates a dummy node to traverse the list

      dummy = L->Next;
      
      while (dummy != NULL)
      {
        printf("%d->", dummy->Element);
        dummy = dummy->Next;
      }
    }

It works but there is a small caveat in this routine. This is
part of print out for the ``linkedListTestMain``:: 

  TEST: printList
  23->44->45->57->89->-1->

As you can see, there is a little ``->`` at the end of linked list, which
is not supposed to be there because there is no next element after ``-1``.

I try to solve this problem but the solution is not succint and I don't want to
do complicated stuff just to remove this ``->``. Howver, I finally get a solution
today that is very clean to eliminate ``->`` without adding additional complexity to
the routine.

In C, we know we can use if-else shorthand likes the following:

.. code-block:: c

     int x;           
     if (dummyA != NULL)
     {
       x = dummyA->Digit;
     }
     else
     {
       x = 0;
     }

is equivalent with

.. code-block:: c

     int x;
     (dummyA != NULL) ? (x = dummyA->Digit) : (x = 0);

We can use this shorthand inside our routine ``printf`` statement to solve our problem:

.. code-block:: c

    void
    printList(List L)
    {
      Pos dummy; // creates a dummy node to traverse the list

      dummy = L->Next;

      while (dummy != NULL)
      {
        printf("%d%s", dummy->Element, (dummy->Next) ? ("->") : (""));
        dummy = dummy->Next;
      }
    }



As you can see, inside ``printf`` statement, we don't printout ``->`` by default, we check
if ``dummy->Next`` is ``NULL``, then that means we are at the last element of the list, and
we don't append anything (i.e. ``("")``). However, if this is not the case, we print ``->``.
