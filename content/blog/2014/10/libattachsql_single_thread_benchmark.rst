libAttachSQL Single Thread vs. libmysqlclient Multi Thread
==========================================================

:date: 2014-10-15 20:01
:category: MySQL
:tags: MySQL, libAttachSQL, HP, Advanced Technology Group


I have recently `posted up benchmarks <http://linuxjedi.co.uk/posts/2014/Oct/03/libattachsql-benchmarks-with-sysbench/>`_ of `libAttachSQL <http://libattachsql.org>`_ vs. libmysqlclient using sysbench.  Whilst these are great and shows the results I hoped for, this isn't what we designed libAttachSQL for.  It was designed for non-blocking many connections per thread.

With this in mind I spent today knocking up a quick benchmark tool which replicates the Sysbench "Select" test but using libAttachSQL's connection groups on a single thread.  The code for this can be seen in the new `AttachBench <https://github.com/libattachsql/attachbench>`_ GitHub tree.  Of course the secondary reason for this is to try and hammer the connection groups feature, which of course did find a bug when I scaled to around 32 connections.  This has been fixed in libAttachSQL's master ready for the next release and is what I am using for these benchmarks.

The Test
--------

I used the exact same test rig and configuration as the previous Sysbench tests and as before the test was run with 1,000,000 queries.  The AttachBench tool executed was as follows:

.. code-block:: bash

   attachbench --db=sbtest --user=test --pass=test --db=testdb --queries=1000000 --connections=32 --host=/tmp/mysql.sock --port=0

I've added the results to the previous select test to the graph for comparison.  The two "Select" result sets are for Sysbench with one connection per thread.  The third is with AttachBench running the same queries, just with many connections in a single thread.

.. image:: /images/select_single_thread.png

This exceeded my expectations.  Having many connections in a single thread actually outperforms many threads with one connection.  It is early days and there is much more testing and improvement that can be done.  But I'm very encouraged by these results.

I'll be talking more about libAttachSQL and these results at `Percona Live London next month <http://www.percona.com/live/london-2014/sessions/libattachsql-next-generation-c-connector-mysql>`_ so please come along if you are in the area.
