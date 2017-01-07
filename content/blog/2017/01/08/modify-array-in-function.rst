##################################
Modify array inside function in C
##################################

:date: 2017-01-08 09:23
:category: programming languages
:tags: c
:Status: draft

In this post, I want to write down the lesson learned
about modifying array inside a function in C with an example
from MAW 3.15.a:

    Write an array implementation of self-adjusting lists.
    A self-adjusting list is like a regular list, except that
    all insertions are performed at the front, and when an element
    is accessed by a Find, it is moved to the front of the list
    without changing the relative order of the other items.

In general, there are two cases when we need to use functions to work with array. Let's
examine accordingly.

************************
Modify the array content
************************

Let's take a look at the following sample function first:

.. code-block:: c

    void change(int *array,int length)
    {
      printf("array address inside function: %p\n", array);
      int i;
      for(i = 0 ; i < length ; i++)
          array[i] = 5;
    }
          
and in our test function we do:

.. code-block:: c

    void test_change()
    {
      int i, length = 3;
      int test[3] = {1,2,3};

      printf("Before:");
      print(test, length);
      printf("before change, test address: %p\n", test);
      change(test, 3);
      printf("After:");
      print(test, length);
      printf("after change, test address: %p\n", test);
    }
                  
The output looks something like::

  Before:1 2 3
  before change, test address: 0x7fffffffe050
  array address inside function: 0x7fffffffe050
  After:5 5 5
  after change, test address: 0x7fffffffe050

Let's examine our ``change`` function under gdb.::

   p array                                                                                     
   $1 = (int *) 0x7fffffffe050

shows us that actually ``array`` is a pointer to int with the address ``0x7fffffffe050``.::

  (gdb) p *0x7fffffffe050                                                                              
  $3 = 1       

If we take a look at what value hold the address, we can see that it's ``1``, which is the first element of
our ``int test[3]`` array. This leads to our very first important observation:

- When pass an array to a function, it will decay to a pointer pointing to the first element of the array.
  In other words, we can do ``p *array`` in gdb and get ``1`` as well.

Since the size of int under my system is 4 bytes (check by ``p sizeof(int)`` in gdb), and let's examine the four conseuctive
bytes with starting address ``0x7fffffffe050``::

  (gdb) x/4bx array                           
  0x7fffffffe050: 0x01    0x00    0x00    0x00

As you can see, this is integer ``1``. Now, let's start with the first iteration of the loop in ``change``. Once we finish the
iteration, ``i`` becomes ``1`` and let's see what change to our ``array``::

  (gdb) p array[0]                                                                            
  $12 = 5                                                                                     

  (gdb) p array               
  $13 = (int *) 0x7fffffffe050
  
  (gdb) p *0x7fffffffe050
  $10 = 5                

  (gdb) x/4x array                                                                           
  0x7fffffffe050: 0x05    0x00    0x00    0x00
  
We can see that the first element of our ``test`` array becomes ``5`` and the starting address of our
``array`` is still ``0x7fffffffe050``. In other words, the only thing changed is the value that
address ``0x7fffffffe050`` holds. In addition, if you take a look at the array address output, you can see
that before the function call, during the function call, and after the function call, the array address
doesn't change at all: ``0x7fffffffe050``. This leads to our second observation:

- We can change the **contents** of array in the caller function (i.e. ``test_change()``) through callee function (i.e. ``change``)
  by passing the array itself to the function (i.e. ``int *array``) without any ``return`` statement, 

- However, doing so, we doesn't change the address of the array. It seems that array is a local variable inside both caller function
  and callee function. Its address is passed from ``test_change`` to ``change``::

                     +---+---+--+
    array ----->  -> | 1 | 2 | 3|
                 /-> +---+---+--+
    test --------

Let's verify above observation with another function ``change2``:

.. code-block:: c

    void change2(int *array,int length)
    {
      printf("array address inside function: %p\n", array);
      int i;
      int tmp[3] = {5,5,5};
      array = tmp;
    }
        
With the similar test program ``test_change2()`` we get the following output::

  TEST: change2
  Before:1 2 3
  before change, test address: 0x7ffda5b41bc0
  array address inside function: 0x7ffda5b41bc0
  After:1 2 3
  after change, test address: 0x7ffda5b41bc0

``change2`` is very tempting because we assign ``array`` points to ``tmp``, which let ``test`` inside ``test_change2`` points to ``tmp`` as well. However, this is wrong and
the output confirms our observation above: array is local variable to the caller function and callee function, and when we pass a array into a function, the address is
passed (copied) from caller to callee. After that, address inside callee can reassign and will have no effect on the array (address) in caller. In other words, even though
the address inside ``change2`` and ``test_change2`` are the same, but they are independent with each other::

                     +---+---+--+
    test  ---------> | 1 | 2 | 3|
                     +---+---+--+
    
                     +---+---+--+
    tmp   ----->  -> | 5 | 5 | 5|
                 /-> +---+---+--+
    array -------


What if we want to modify ``test`` itself inside ``test_change2`` beyond the content of the array. What if we want to resize the array to make it hold more values?    

***********************
Modify the array itself
***********************

Before we start to answer the above question. Let me clear out an important concept: "array on stack" and "array on heap".






..
   http://stackoverflow.com/questions/34844003/changing-array-inside-function-in-c

