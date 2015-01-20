The Pointer Corruption Bug
==========================

:date: 2015-01-20 09:16
:category: General
:tags: HP, Advanced Technology Group, C, Python, API, Documentation, libAttachSQL

Or an alternative name for this post...

Why API Docs Should Have Examples
---------------------------------

As part of my continuation of libAttachSQL for HP's Advanced Technology Group I have recently been focusing on a Python based wrapper called pyAttachSQL.  This is currently at an alpha level of release with no package builds yet.

Today I want to talk about one (silly on my part) very frustrating bug I found whilst working on pyAttachSQL and why this means API docs should have examples for every call.

The Crash
---------

Whilst writing the group connection functions I was using a `Py_BuildValue <https://docs.python.org/2/c-api/arg.html#c.Py_BuildValue>`_ call to generate parameters to use in a callback `PyObject_CallObject <https://docs.python.org/2/c-api/object.html#c.PyObject_CallObject>`_.  So the code looked a little like this:

.. code-block:: c

   cbargs= Py_BuildValue("iOOO", &events, &pycon, &pycon->query, &self->cb_args);
   ...
   PyObject_CallObject(self->cb_func, cbargs);
   Py_DECREF(cbargs);

Those who are Python API veterans will be able to see straight away where I went wrong but I am quite new to the API.  The code was segfaulting on ``PyObject_CallObject``.

My Big Dumb Mistake
-------------------

.. image:: /images/droids.jpg

Whilst debugging this I found the problem was in ``cbargs``, for some reason the pointers to ``pycon`` and alike were slightly different to when they were set.  After some time going over it again and again in GDB and watching the pointers get incremented it suddenly hit me.  The incrementation was happening during reference increment functions inside ``Py_BuildValue``.  Which makes sense because the one first items in a ``PyObject`` structure is the reference count.  I was supposed to pass pointers, not pointers to pointers.  The ``Py_BuildValue`` function has no type checking so was taking whatever you passed to it as a pointer to a structure.

So the question many of you would be asking is: why did you pass pointers to pointers?  That is easy to answer...  Earlier in the code I have been using the `PyArg_ParseTuple <https://docs.python.org/2/c-api/arg.html#c.PyArg_ParseTuple>`_ and similar functions which are on the same documentation page, using a similar API and I assumed the API was consistent with no examples to show me otherwise.  The fix was to simply remove the ``&`` symbols from the above code.

Lessons Learnt
--------------

I guess there is two lessons I have learnt from this:

1. Don't assume that an API is consistent
2. Add examples for every API call in the documentation

I'll shortly be opening a ticket for libAttachSQL and pyAttachSQL to implement the second item.
