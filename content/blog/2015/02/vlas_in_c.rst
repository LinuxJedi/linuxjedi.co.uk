Variable Length Arrays in C
===========================

:date: 2015-02-24 13:25
:category: Coding
:tags: HP, Advanced Technology Group, C

In a bid to aim this blog at multiple levels I'm going to talk today about Variable Length Arrays (VLAs) in C.  I'm covering this topic in particular because a friend who is a Harvard CS50 student recently asked me about them.

As many people know, C is my favourite programming language to work in (several have questioned my sanity thanks to this).  It isn't always the right programming language for every project and where it is appropriate I will use an alternative language.  But it is my favourite to work with and HP's Advanced Technology Group allows me to do a lot of work in it.

In a previous post on my old blog `I discussed why VLAIS (Variable Length Arrays In Structs) is a bad idea <http://thelinuxjedi.blogspot.co.uk/2014/02/why-vlais-is-bad.html>`_.  Put simply this is a GCC only feature which can cause a lot of problems.  Unfortunately they are used a lot in the Linux kernel but this is being improved as part of the work to port the kernel to work with the CLang compiler.

VLAs themselves are not as bad.  For those who don't know what they are, here is an example:

.. code-block:: c

   int main(int argc, char* argv[])
   {
       char name[]= "fred";
       printname(name, 5); // 4 chars + nul terminator
   }

   void printname(char *name, int length)
   {
       char name_copy[length];
       memcpy(name_copy, name, length);
       printf("Name is: %s\n", name_copy);
   }

The bit I'm referring to is "``char name_copy[length];``".  Normally array sizes are fixed at compile time but with the C99 standard VLAs were introduced.  They were in several compilers before that but it was not a standard.  The compiler will turn this into code which allocates ``name_copy`` to the correct size when the function is entered and frees the memory when the function returns.

This is incredibly useful but is not without problems:

#. You need to make sure that the application doesn't try to use ``free()`` on the VLA.  This will likely end very badly
#. If you have a pointer to a VLA you need to make sure you don't try to access it when the function has returned (just like accessing memory that has been freed)
#. Many implementations allocate this memory on the stack instead of the main pool of memory

This last one could be a problem because most platforms at least have a soft limit on stack size.  The default for the machine I'm typing on for example is 8MiB.  This sounds a lot but with recursion it is possible to easily blow this, especially with large arrays.  Ideally VLAs should be used just for allocations you know are going to be quite small and predictable.  If it is a user input without sanitation you could be opening yourself up to an attack vector.

In summary, VLAs are useful, they make allocation and freeing much easier, especially for multi-dimension arrays.  But you need to be very careful using them and only for small allocations.
