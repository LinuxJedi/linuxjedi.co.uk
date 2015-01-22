C Library Visibility
====================

:date: 2015-01-22 09:25
:category: Coding
:tags: HP, Advanced Technology Group, C, API, MySQL

I was surprised by the recent `announcement <http://mysqlserverteam.com/how-to-use-ssl-and-mysql-client-library-in-the-same-binary/>`_ that MySQL are going to start to conceal the hidden function calls in their C connector.  Surprised because although this is great news I had expected them to do this years ago.  Working for HP's Advanced Technology Group I realise I take such things for granted.  For this blog post I'm going to talk about why it is important and how to do it.

So, when you create a dynamic library in C the default thing that happens is every function call in that library effectively becomes a potential API call.  Whether you document every single function or not to make it official API is up to you but I suspect in 99.99% of cases there are private functions you don't want users to mess with.  Additionally holding the symbol information for every function so that you can link your application to it takes a massive amount of space, one such library I can think of is 8x bigger than it should be due to exposing every function call.

In MySQL's case and likely others this can cause a problem with collisions during linking.  MySQL can use its bundled in YaSSL library to supply SSL, and due to the functions being exposed this can cause problems if your application links to libmysqlclient and OpenSSL since they both use the same public API calls in many places.

RedHat and other distributions actually solve this in MySQL by stripping the binaries of unneeded symbols at compile time.  This is indeed one effective solution.  But I don't believe this is the correct solution.  In fact Ulrich Drepper in `How To Write Shared Libraries <https://software.intel.com/sites/default/files/m/a/1/e/dsohowto.pdf>`_ pretty much reserves this as a last resort.

Link Time Visibility
--------------------

The solution I and many others recommend is using visibility at link time.  There are three parts to applying this:

1. The compiler flag

2. An extra include file

3. Marking the functions you want to be in the API as public

I shall go through these steps for GCC, other compilers will be very similar and there is plenty of information on the internet about this.

Compiler Flag
^^^^^^^^^^^^^

You simply need to add one compiler flag which will hide all function calls by default instead of exposing them all by default::

   -fvisibility=hidden

Include File
^^^^^^^^^^^^

This is one example taken from `libAttachSQL <http://libattachsql.org/>`_ and there is an example with more platform support on the `GCC Visibility manual page <https://gcc.gnu.org/wiki/Visibility>`_.

In this example you need to change ``BUILDING_ASQL`` and ``ASQL_API`` to suit your own naming.

.. code-block:: c

   #if defined(BUILDING_ASQL)
   # if defined(HAVE_VISIBILITY) && HAVE_VISIBILITY
   #  define ASQL_API __attribute__ ((visibility("default")))
   # elif defined (__SUNPRO_C) && (__SUNPRO_C >= 0x550)
   #  define ASQL_API __global
   # elif defined(_MSC_VER)
   #  define ASQL_API extern __declspec(dllexport)
   # else
   #  define ASQL_API
   # endif /* defined(HAVE_VISIBILITY) */
   #else  /* defined(BUILDING_ASQL) */
   # if defined(_MSC_VER)
   #  define ASQL_API extern __declspec(dllimport)
   # else
   #  define ASQL_API
   # endif /* defined(_MSC_VER) */
   #endif /* defined(BUILDING_ASQL) */

Marking Public API
^^^^^^^^^^^^^^^^^^

With the above include file you need to define ``BUILDING_ASQL`` somewhere in your library compiling.  This makes sure that during the library compiling/linking all the functions can be seen but they will be hidden at link time from external applications.

Then when you are defining an API call in your .h file you can do as follows:

.. code-block:: c

   int hidden_function(int a, int b);

   ASQL_API
   int public_function(int a, int b);

You can see here I have prepended the function declaration with ``ASQL_API`` for any function I wish to be part of the public API.

Conclusion
^^^^^^^^^^

If you leave undocumented API dangling people will tend to use it, which causes all sorts of issues when you want to change some of the internal functions.  Ideally when writing an API setting the visibility should be a very early step, but thankfully it is one that can easily be added to a project at any time.
