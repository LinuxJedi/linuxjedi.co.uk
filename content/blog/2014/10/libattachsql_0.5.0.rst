libAttachSQL Second Beta, After the Sledgehammer
================================================

:date: 2014-10-08 20:52
:category: MySQL:
:tags: MySQL, libAttachSQL, HP, Advanced Technology Group

Last week I `blogged about getting sysbench working with libAttachSQL <http://linuxjedi.co.uk/posts/2014/Oct/03/libattachsql-benchmarks-with-sysbench/>`_.  This was not only an exercise in performance but also the first real test for `libAttachSQL <http://libattachsql.org/>`_.

Before I had done this testing the most the early Alpha and Beta releases of libAttachSQL had gone through is a few basic queries.  So, the first thing I did when I got the sysbench driver working was slap it with 1,000,000 queries.  It pretty much exploded instantly on that.  Over the course of this release I have probably hit it with over 100,000,000 queries and things run a lot smoother.

This has led to today's release of libAttachSQL 0.5.0.  As far as changes go this release has the `biggest changelog so far <http://docs.libattachsql.org/en/latest/appendix/version_history.html#version-0-5>`_.  Here is a summary of the major points:

* 11 major bugs fixes, most of them crashing bugs
* Lots more documentation and examples
* More tests
* A couple of minor features
* A new semi-blocking mode
* A more consistent API for error handling

These last two points I should talk about a bit more.  The semi-blocking mode lets the networking code block until data is received (but not until it is all received).  For applications which access using one connection per thread this will increase performance, but will decrease performance for many connections per thread (which is what libAttachSQL was originally designed for).

The error handling has moved from a user accessible struct to a type which is used in function calls.  In addition the way this is returned to the user application has been made consistent across the whole API.  This means that the API is not backwards compatible with 0.4.0.

For those wishing to try out the connector the 0.5.0 beta source release `can be found on GitHub <https://github.com/libattachsql/libattachsql/releases/tag/v0.5.0>`_.  The documentation is on `Read The Docs <http://docs.libattachsql.org/en/latest/>`_.

This will be the last beta for libAttachSQL.  The next release will be 0.9.0 RC which will hopefully be a short cycle to our first GA release.  We have many more goodies planned after GA.  Watch this space!

As always if you have any questions please get in touch either via. the comments below, the `#libAttachSQL Freenode channel <irc://chat.freenode.net/libAttachSQL>`_ or any other means.
