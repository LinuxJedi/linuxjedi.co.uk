libAttchSQL Hits First GA!
==========================

:date: 2014-10-22 11:35
:category: MySQL
:tags: MySQL, libAttachSQL, HP, Advanced Technology Group

We have come a long way since the first code was put down for `libAttachSQL <http://libattachsql.org>`_ on the 4th July.  It has been a fantastic project to work on so I am very pleased to announce our first GA release.

For those who haven't seen it so far libAttachSQL is a non-blocking, lightweight C API for MySQL servers.  It is Apache 2.0 licensed so is compatible with most Open Source and commercial licensing.  HP's Advanced Technology Group saw a need in this field not just for HP itself but for other companies and projects too.

As for the GA release itself, there are not many changes over the RC release beyond stability fixes.  A full list can be seen in the `version history documentation <http://docs.libattachsql.org/en/latest/appendix/version_history.html#version-1-0>`_.

In addition to the GA release we have recently had a driver for `Sysbench <https://launchpad.net/sysbench>`_ merged into their trunk so libAttachSQL can be used for benchmarking MySQL servers.  We have also started work on a tool called `AttachBench <https://github.com/libattachsql/attachbench>`_ which when complete will run similar MySQL tests as Sysbench but will allow for multiple connections per thread (something libAttachSQL excels at).  At the moment AttachBench requires the tables from Sysbench's "Select" test already setup and I don't recommend tinkering with it yet unless you don't mind getting a bit dirty.

With the release of libAttachSQL 1.0.0 we have also launched a new website on `libattachsql.org <http://libattachsql.org>`_.  It is a basic Pelican based site (very much like this blog) but will make it much easier for anyone to add content, just like this blog all the source is in `RST files on GitHub <https://github.com/libattachsql/libattachsql.org>`_.

Download links for libAttachSQL 1.0.0 can be found on the `News section <http://libattachsql.org/posts/2014/Oct/21/version-100-ga-released/>`_ of the project website.  There is a source package as well as packages for RHEL/CentOS 6.x and 7.x.  Packages for Ubuntu 12.04 and 14.04 are waiting to be built in the PPA at time of posting.  We hope to have releases for more operating systems in the near future.

Rest assured we are not stopping here.  I already have ideas of what I want to see in 1.1 and we have some spin-off projects planned.  If you would like to learn more please come along to my talk on libAttachSQL at `Percona Live London <http://www.percona.com/live/london-2014/sessions/libattachsql-next-generation-c-connector-mysql>`_.  I'm also talking to several people outside of HP to see what they would like in libAttachSQL and am happy to talk to anyone else who wants to know more and has feedback.

Many thanks to everyone who has helped us get this far.
