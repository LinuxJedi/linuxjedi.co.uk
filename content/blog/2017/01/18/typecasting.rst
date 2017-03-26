################
Typecasting in C
################

:date: 2017-01-19 00:53
:category: programming languages
:tags: c, pointer
:summary: A study of typecasting in C

This post covers the typecasting in C with the aim to get a clear understanding
of the most commonly-seen C manipulation. This writeup is adapted from
"Hacking - the Art of Exploitation".

******
TL;DR
******

- Typecasting change a variable into a different type just for that operation.
- Pointer type determines the size of the data it points to. In other words, when you
  do pointer arithemetic (i.e ``+``), the number of bytes change (i.e increase) in terms of memory
  address is determined by the pointer type.
- ``void`` pointer is a generic pointer and we need to cast them to the proper data type in order to
  de-reference it.
- Pointer is merely a memory address. With typecasting, any type with enough size to hold
  the memory address can work like a pointer.

********
Details
********

Typecasting is simply a way to temporarily change a variable's data type,
despite how it was originally define. When a variable is typecast into a different type, 
the compiler is basically told to treat that variable as if it were the new data type,
but *only for that operation*.

Typecasting is mostly used with pointers. Before we jump into typecasting, let's take a look
why we need to define type for pointer (pointer is just a memory address). One reason for this
is to try to limit programming errors. An integer pointer should only point to integer data, while
a character pointer should only point to character data. Another reason is for pointer arithmetic.
An integer is four bytes in size, while a character only takes up a single byte.

.. code-block:: c

    #include <stdio.h>

    int main()
    {
      int i;

      char char_array[5] = {'a', 'b', 'c', 'd', 'e'};
      int int_array[5] = {1, 2, 3, 4, 5};

      char *char_pointer;
      int *int_pointer;

      char_pointer = char_array;
      int_pointer = int_array;

      for(i = 0; i < 5; i++)
      {
        printf("[integer pointer] points to %p, which contains the integer %d\n", int_pointer, *int_pointer++);
      }

      for(i = 0; i < 5; i++)
      {
        printf("[char pointer] points to %p, which contains the char '%c'\n", char_pointer, *char_pointer++);
      }
    }

The program itself is pretty straightforward. Here is the output::

  [integer pointer] points to 0x7ffd90db45a4, which contains the integer 1
  [integer pointer] points to 0x7ffd90db45a8, which contains the integer 2
  [integer pointer] points to 0x7ffd90db45ac, which contains the integer 3
  [integer pointer] points to 0x7ffd90db45b0, which contains the integer 4
  [integer pointer] points to 0x7ffd90db45b4, which contains the integer 5
  [char pointer] points to 0x7ffd90db45c1, which contains the char 'a'
  [char pointer] points to 0x7ffd90db45c2, which contains the char 'b'
  [char pointer] points to 0x7ffd90db45c3, which contains the char 'c'
  [char pointer] points to 0x7ffd90db45c4, which contains the char 'd'
  [char pointer] points to 0x7ffd90db45c5, which contains the char 'e'
  
Even though the same value of 1 is added to ``int_pointer`` and ``char_pointer``
in their respective loops, the compiler increments the pointer's addresses by different
amounts. Since a char is only 1 byte, the pointer to the next char would naturally also be 1 byte over.
But since an integer is 4 bytes, a pointer to the next integer has to be 4 bytes over.

.. code-block:: c
                
    #include <stdio.h>

    int main()
    {
      int i;

      char char_array[5] = {'a', 'b', 'c', 'd', 'e'};
      int int_array[5] = {1, 2, 3, 4, 5};

      char *char_pointer;
      int *int_pointer;

      // The char_pointer and int_pointer now point to incompatible data types.
      char_pointer = int_array; 
      int_pointer = char_array;

      for(i = 0; i < 5; i++)
      {
        printf("[integer pointer] points to %p, which contains the integer %c\n", int_pointer, *int_pointer++);
      }

      for(i = 0; i < 5; i++)
      {
        printf("[char pointer] points to %p, which contains the char '%d'\n", char_pointer, *char_pointer++);
      }
    }
  
The output is::

   $ gcc pointer_types2.c
   pointer_types2.c: In function ‘main’:
   pointer_types2.c:13: warning: assignment from incompatible pointer type
   pointer_types2.c:14: warning: assignment from incompatible pointer type
   
Here, the compiler and the programmer are the only ones that care about a pointer's type.
In the compiled code, a pointer is nothing more than a memory address, so the compiler
will still compile the code if a pointer points to an incompatible data type - it simply warns us
to anticipate unexpected results.::

  [integer pointer] points to 0x7ffe2d481324, which contains the integer a
  [integer pointer] points to 0x7ffe2d481328, which contains the integer e
  [integer pointer] points to 0x7ffe2d48132c, which contains the integer ▒
  [integer pointer] points to 0x7ffe2d481330, which contains the integer
  [integer pointer] points to 0x7ffe2d481334, which contains the integer
  [char pointer] points to 0x7ffe2d481301, which contains the char '1'
  [char pointer] points to 0x7ffe2d481302, which contains the char '0'
  [char pointer] points to 0x7ffe2d481303, which contains the char '0'
  [char pointer] points to 0x7ffe2d481304, which contains the char '0'
  [char pointer] points to 0x7ffe2d481305, which contains the char '2'

Even though ``int_pointer`` points to character data that only contains 5 bytes of data, it is still
typed as an integer. This means that adding 1 to the pointer will increment the address by 4 each time.
Similarly, the ``char_pointer``'s address is only incremented by 1 each time, stepping through the 20 bytes
of integer data, one byte at a time. So, we need to make sure that pointer type is correct. This is the place where
we need typecasting.

.. code-block:: c
      
    #include <stdio.h>

    int main()
    {
      int i;

      char char_array[5] = {'a', 'b', 'c', 'd', 'e'};
      int int_array[5] = {1, 2, 3, 4, 5};

      char *char_pointer;
      int *int_pointer;

      char_pointer = (char *) int_array;
      int_pointer = (int *) char_array;

      for(i = 0; i < 5; i++)
      {
        printf("[integer  pointer] points to %p, which contains the integer %c\n", int_pointer, *int_pointer);
        int_pointer = (int *)((char *)int_pointer + 1);
      }

      for(i = 0; i < 5; i++)
      {
        printf("[char pointer] points to %p, which contains the char '%d'\n", char_pointer, *char_pointer);
        char_pointer = (char *)((int *)char_pointer + 1);
      }
    }
                                          
Typecasting is just a way to change the type of a variable on the fly. In the above code, when the pointers
are initially set, the data is typecast into the pointer's data type. This will prevent the C compiler from complaining
about the conflicting data types; however, any pointer arithmetic will still be incorrect (because typecasting is just
for that one operation). To fix that, when 1 is added to the pointers, they must first be typecast into the correct data type
so the address is incremented by the correct amount. Then this pointer needs to be typecast back into the pointer's data type
once again. It works but in a not beautiful way.::

  [integer pointer] points to 0x7ffd484ac470, which contains the integer a
  [integer pointer] points to 0x7ffd484ac471, which contains the integer b
  [integer pointer] points to 0x7ffd484ac472, which contains the integer c
  [integer pointer] points to 0x7ffd484ac473, which contains the integer d
  [integer pointer] points to 0x7ffd484ac474, which contains the integer e
  [char pointer] points to 0x7ffd484ac450, which contains the char '1'
  [char pointer] points to 0x7ffd484ac454, which contains the char '2'
  [char pointer] points to 0x7ffd484ac458, which contains the char '3'
  [char pointer] points to 0x7ffd484ac45c, which contains the char '4'
  [char pointer] points to 0x7ffd484ac460, which contains the char '5'

Sometimes, we probably want to use a generic, typeless pointer. In C, a void pointer is a typeless pointer, defined by the ``void`` keyword.
Here are two things we need to note:

  - pointers cannot be de-referenced unless they have a type. In order to retrieve the value stored in the pointer's memory address, the
    compiler must first know what type of data it is.
  - void pointers must also be typecast before doing pointer arithmetic, which indicates that a void pointer's main purpose is to simply hold a
    memory address.

Let's rewrite our program.

.. code-block:: c

    #include <stdio.h>

    int main()
    {
      int i;

      char char_array[5] = {'a', 'b', 'c', 'd', 'e'};
      int int_array[5] = {1, 2, 3, 4, 5};

      void *void_pointer;

      void_pointer = (void *)char_array;

      for(i = 0; i < 5; i++)
      {
        printf("[char pointer] points to %p, which contains the char %c\n", void_pointer, *((char *)void_pointer));
        void_pointer = (void *)((char *)void_pointer + 1);
      }

      void_pointer = (void *)int_array;

      for(i = 0; i < 5; i++)
      {
        printf("[integer pointer] points to %p, which contains the integer %d\n", void_pointer, *((int *)void_pointer));
        void_pointer = (void *)((int *) void_pointer + 1);
      }
    }

The output is::

  [char pointer] points to 0x7fff06cf8de0, which contains the char a
  [char pointer] points to 0x7fff06cf8de1, which contains the char b
  [char pointer] points to 0x7fff06cf8de2, which contains the char c
  [char pointer] points to 0x7fff06cf8de3, which contains the char d
  [char pointer] points to 0x7fff06cf8de4, which contains the char e
  [integer pointer] points to 0x7fff06cf8dc0, which contains the integer 1
  [integer pointer] points to 0x7fff06cf8dc4, which contains the integer 2
  [integer pointer] points to 0x7fff06cf8dc8, which contains the integer 3
  [integer pointer] points to 0x7fff06cf8dcc, which contains the integer 4
  [integer pointer] points to 0x7fff06cf8dd0, which contains the integer 5

The void pointer is really just holding the memory addresses, while the hard-coded typecasting
is telling the compiler to use the proper types whenever the pointer is used. Since the type is
taken care of by the typecasts, the void pointer is truly nothin more than a memory address.
With the data types defined by typecasting, anything that is big enough to hold a four-byte or eight-byte value can
work the same way as a void pointer.

.. code-block:: c

    #include <stdio.h>

    int main()
    {
      int i;

      char char_array[5] = {'a', 'b', 'c', 'd', 'e'};
      int int_array[5] = {1, 2, 3, 4, 5};

      unsigned long int hacky_nonpointer;

      hacky_nonpointer = (unsigned long int)char_array;

      for(i = 0; i < 5; i++)
      {
        printf("[hacky_nonpointer] points to %p, which contains the char %c\n", hacky_nonpointer, *((char *)hacky_nonpointer));
        hacky_nonpointer = hacky_nonpointer + sizeof(char);
      }

      hacky_nonpointer = (unsigned long int)int_array;

      for(i = 0; i < 5; i++)
      {
        printf("[hacky_nonpointer] points to %p, which contains the integer %d\n", hacky_nonpointer, *((int *)hacky_nonpointer));
        hacky_nonpointer = hacky_nonpointer + sizeof(int);
      }
    }

Note that I use ``unsigned long int`` because I'm on a 64-bit system. ``unsigned int`` is enough for 32-bit system.::

  [hacky_nonpointer] points to 0x7fff3e378360, which contains the char a
  [hacky_nonpointer] points to 0x7fff3e378361, which contains the char b
  [hacky_nonpointer] points to 0x7fff3e378362, which contains the char c
  [hacky_nonpointer] points to 0x7fff3e378363, which contains the char d
  [hacky_nonpointer] points to 0x7fff3e378364, which contains the char e
  [hacky_nonpointer] points to 0x7fff3e378340, which contains the integer 1
  [hacky_nonpointer] points to 0x7fff3e378344, which contains the integer 2
  [hacky_nonpointer] points to 0x7fff3e378348, which contains the integer 3
  [hacky_nonpointer] points to 0x7fff3e37834c, which contains the integer 4
  [hacky_nonpointer] points to 0x7fff3e378350, which contains the integer 5

The important thing to remember about variables in C is that the compiler is the
only thing that care about a variable's type. In the end, after the program has been compiled,
the variables are nothing more than memory addresses. This means that variables of one type can easily be coerced into
behaving like another type by telling the compiler to typecast them into the desired type.
