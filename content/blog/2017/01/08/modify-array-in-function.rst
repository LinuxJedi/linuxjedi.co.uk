##################################
Modify array inside function in C
##################################

:date: 2017-01-08 09:23
:category: programming languages
:tags: c
:Status: Published
:summary: Commonly seen C usage

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

  (gdb) x/4bx array                                                                           
  0x7fffffffe050: 0x05    0x00    0x00    0x00
  
We can see that the first element of our ``test`` array becomes ``5`` and the starting address of our
``array`` is still ``0x7fffffffe050``. In other words, the only thing changed is the value that
address ``0x7fffffffe050`` holds. In addition, if you take a look at the array address output, you can see
that before the function call, during the function call, and after the function call, the array address
doesn't change at all: ``0x7fffffffe050``. This leads to our second observation:

- We can change the **contents** of array in the caller function (i.e. ``test_change()``) through callee function (i.e. ``change``)
  by passing the the value of array to the function (i.e. ``int *array``). This modification can be effective in the
  caller function without any ``return`` statement.

- However, doing so, we doesn't change the address of the array. It seems that array is a local variable inside both caller function
  and callee function. Its address is copied and passed from ``test_change`` to ``change``::

    Inside change:
    
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

    after change2:
     
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

"array on Stack" with the declaration looks like ``int test[3] = {1,2,3}`` in our test routines. The array declared like this stays on the stack and local to the
function calls. "array on heap" is the dynamic array involving ``malloc``, which I mention in the `previous post <{filename} /blog/2017/01/06/josephus-wrapup.rst>`_. When we talk about
resize the array, we mean the latter case. In other words, we can only change the array itself (number of elements) with dynamically allocated array in the heap.

Let's take a look at ``change3``:

.. code-block:: c

    void
    change3(int **array, int length)
    {
      int* tmp = calloc(length, sizeof(int));
      int i;
      for (i = 0; i < length; i++)
      {
        *(tmp+i) = 5;
      }
      free(*array);
      *array = tmp;
    }

and our corresponding test routine ``test_change3()``:

.. code-block:: c

    void test_change3()
    {
      printf("TEST: change3\n");
      int i, length = 3;
      int* test = calloc(length, sizeof(int));
      test[0] = 1;
      test[1] = 2;
      test[2] = 3;
      printf("Before:");
      print(test, length);
      printf("before change, test address: %p\n", test);
      change3(&test, length);
      printf("After:");
      print(test, length);
      printf("after change, test address: %p\n", test);
    }
                                                                        
The first task is to understand ``int **array``. There is a template sentence when comes to C type declaration: "<VariableName> is ... <typeName>". In our case,
The template sentence becomes "array is ... int". Now let's work out the "..." with "right-left" rule:

  "go right when you can, go left when you must"

In our case, we start with "array" and go right, and nothing left with declaraiton. So, we must go left. the first symbol is ``*``, which reads as "pointer to".
So now our template sentence becomes "array is pointer to ... int". Great! Let's continue to go left, we see another ``*``, which makes our sentence becomes
"array is pointer to pointer to ... int". Then we meet ``int``, which means all the symbol in the declaration is consumed and our sentence is complete:
"array is pointer to pointer to int". This means ``array`` variable itself is a pointer containing an address of a pointer, which holds an address of a int.

Let's see if this is true with gdb.::

  (gdb) p array         
  $1 = (int **) 0x7fffffffe070    

  (gdb) p/a *0x7fffffffe070
  $8 = 0x601010           

  (gdb) p *0x601010                                      
  $7 = 1                

  (gdb) p *array                  
  $2 = (int *) 0x601010           

  (gdb) p **array                 
  $3 = 1                          

The address holds by ``array`` is ``0x7fffffffe070``. We further examine the value holds by ``0x7fffffffe070`` and by our assumption, it should be another address
and it is: ``0x601010``. Then, we check the value hold by that address, which is expected ``1`` the first element of our ``test`` array.

Our goal is to let ``test`` array in ``test_change3()`` be ``5,5,5``::

    Before change3
    
                     +---+---+--+
    test  ---------> | 1 | 2 | 3|
                     +---+---+--+
    
                     +---+---+--+
    tmp   ---------> | 5 | 5 | 5|
                     +---+---+--+
 

    After change3

                           +---+---+--+
    tmp   ---------------> | 5 | 5 | 5|
                       /-> +---+---+--+
    test(array) -------
                    

From the picture we can see that we want to modify ``array`` inside ``change3`` pointing to ``5,5,5`` and this change will persist to the ``test`` array in our caller function.
In other words, we want both ``test`` and ``array`` no longer independent but want them "tie up" as the same pointer with different names. How do we do that?

The solution is given by ``change3`` but we really need to think about why it makes sense. Firstly, we want to use gdb to examine the address
of key variables::

  (gdb) p array                                                       
  $4 = (int **) 0x7fffffffe070                                        
  (gdb) p *array                     
  $5 = (int *) 0x601010
  (gdb) p (*array)+1                                             
  $14 = (int *) 0x601014                                         
  (gdb) p (*array)+2                                             
  $15 = (int *) 0x601018                                         
  (gdb) p *(*array)                                              
  $18 = 1 
  (gdb) p *(*array)+1                                            
  $16 = 2                                                        
  (gdb) p *(*array)+2                                            
  $17 = 3                                                        
  
  (gdb) p tmp                                                                 
  $7 = (int *) 0x601030                                                       
  (gdb) p tmp+1                                                               
  $8 = (int *) 0x601034                                                       
  (gdb) p tmp+2                                                               
  $9 = (int *) 0x601038                                                       
  (gdb) p *tmp                                                                
  $10 = 5                                                                     
  (gdb) p *(tmp+1)                                                            
  $11 = 5                                                                     
  (gdb) p *(tmp+2)                                                            
  $12 = 5 

We first print out the ``array`` address of each element and we print out the ``tmp`` address of each element.
With the information above, let's compose our conceptual picture::

  Before *array = tmp;
  
     4 bytes                                         4 bytes                                    
  +-----------+-----------+----------+------------+-----------+----------+--------+-------+----------+------
  |  1        | 2         | 3        |   ...      |    5      |     5    |  5     |  ...  | 0x601010 | ...
  +-----------+-----------+----------+------------+-----------+----------+--------+-------+----------+------
  ^           ^           ^                       ^           ^          ^                ^
  0x601010   0x601014     0x601018                0x601030    0x601034   0x601048         0x7fffffffe070
                                                  tmp                                     array
                                                     
Now, let's execute ``*array = tmp``, we get the following::

  (gdb) p *array                                                                             
  $19 = (int *) 0x601010                                                                     
  (gdb) p *array                                                                             
  $20 = (int *) 0x601030 

Now the picture looks like::

  After *array = tmp;
  
     4 bytes                                         4 bytes                                    
  +-----------+-----------+----------+------------+-----------+----------+--------+-------+----------+------
  |  1        | 2         | 3        |   ...      |    5      |     5    |  5     |  ...  | 0x601030 | ...
  +-----------+-----------+----------+------------+-----------+----------+--------+-------+----------+------
  ^           ^           ^                       ^           ^          ^                ^
  0x601010   0x601014     0x601018               0x601030    0x601034   0x601048        0x7fffffffe070
                                                 tmp                                    array
                                                     
We don't modify the address of the ``array`` itself (still ``0x7fffffffe070``) but the content that stored at ``0x7fffffffe070``
which is no longer ``0x601010`` but ``0x601030``, which is the starting address of the ``tmp``: ``5,5,5``.
This may seem like magic. However, in C, a variable (i.e. ``test`` in ``test_change3()``) is merely a synonym for address.
by invoking ``change3`` through ``&test``, we pass in the address ``0x601010`` via a carrier ``0x7fffffffe070``, and we modify the
address to ``0x601030`` and send the address back again through carrier.

With this understanding, we can see why the output looks like::

  TEST: change3
  Before:1 2 3
  before change, test address: 0x601010
  After:5 5 5
  after change, test address: 0x601030

Hoepfully, after our examination, we can understand ``arrayInsert`` for MAW 3.15.a proposed at the beginning of the post:

.. code-block:: c

    void
    arrayInsert(int elem, int** list, int length)
    {
      *list = realloc(*list, sizeof(int) * (length+1));
      int i;
      for (i = 0; i < length; i++)
      {
        (*list)[length - i] = (*list)[length-i-1];
      }
      *((*list)) = elem;
    }

`Get the complete source code <https://github.com/xxks-kkk/Code-for-blog/blob/master/2017/array-to-function/array-to-function.c>`_.


************
Reference
************

1. If you would like to read more about decoding C type declarations. You can read more here:

   - `Reading C type declarations <http://unixwiz.net/techtips/reading-cdecl.html>`_ 
   - `Right-left rule to understand C type declaration <http://ieng9.ucsd.edu/~cs30x/rt_lt.rule.html>`_
   - Chapter 3 in "Expert C Programming" by Peter Van Der Linden



..
   http://stackoverflow.com/questions/34844003/changing-array-inside-function-in-c

