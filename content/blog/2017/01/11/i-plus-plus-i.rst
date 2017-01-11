########################################
Difference between ``i++`` and ``++i``
########################################

:date: 2017-01-11 22:39
:category: programming languages
:tags: c

I'm starting to read through `Hacking: The Art of Exploitation <https://www.amazon.com/Hacking-Art-Exploitation-Jon-Erickson/dp/1593271441>`_ on
my way to work to keep honing C. I resolve a puzzle I have about C, as shown in the title.

- ``i++`` means increment the value of ``i`` by ``1`` *after* evaluating the arithmetic operation.

.. code-block:: c

     int a, b;
     a = 5;
     b = a++ * 6;

``b`` will contain ``30`` and ``a`` will contain ``6``, since the shorthand of ``b = a++ * 6``;
is the equivalent to the following statements:

.. code-block:: c

    b = a * 6;
    a = a + 1;

- ``++i`` means increment the value of ``i`` by ``1`` *before* evaluating the arithmetic operation.

.. code-block:: c

     int a, b;
     a = 5;
     b = ++a * 6;

``b`` will contain ``36`` and ``a`` wil contain ``6``, since the shorthand of ``b = ++a * 6``; is the
equivalent to the following statement:

.. code-block:: c

    a = a + 1;
    b = a * 6;
    
In fact, the two principles mentioned above apply more than "evaluating the arithmetic operation".
For example, in the stack ``push`` operation:

.. code-block:: c

     /* Push an element on the Stack
      */
     void
     push (ET elem, Stack S)
     {
       if (isFull(S))
       {
         resizeStack(S);
       }
       S->Array[++S->TopOfStack] = elem;
     }

we can do ``S->Array[++S->TopOfStack] = elem;``, which is equivalent with the following, a nice short verison:

.. code-block:: c

   S->Array[S->TopOfStack] = elem;
   S->TopOfStack = S->TopOfStack + 1;

Another example is stack ``topAndPop``:

.. code-block:: c

     /* Check the top element and pop it out of Stack
      */
     ET
     topAndPop(Stack S)
     {
       return S->Array[S->TopOfStack--];
     }
   
In this case, we essentially do:

.. code-block:: c

   ET a = S->Array[S->TopOfStack];
   S->TopOfStack = S->TopOfStack - 1;
   return a;

Look how clean I can make my code is if I can understand the difference between ``++i`` and ``i++``.
