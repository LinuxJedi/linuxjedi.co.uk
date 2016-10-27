MariaDB ColumnStore
===================

:date: 2016-10-27 19:35
:category: MariaDB
:tags: MySQL, MariaDB

In August of this year I was offered a change of career to work on a interesting project called MariaDB ColumnStore. The bulk of my career has been working on database software, especially MySQL based and this project intrigued me, so I took the offer.

Until a couple of years ago there was a product being developed called InfiniDB. This was an analytics database that stored using columns instead of rows and was built on top of MySQL 5.1. Unfortunately the company behind that no longer exists but MariaDB sees the value of this product. The MariaDB ColumnStore project was started as a continuation of the development of InfiniDB.

The initial goal is to take InfiniDB and modify it to work with MariaDB 10.1 whilst fixing bugs found along the way. Whilst I have only been a part of the project for a couple of months we have come a long way in that time. I can't take the all credit for that, we have a great hard-working team behind the project. I've had quite a few conversations with members of the community about the project and the feedback has been very positive. It definitely fills a gap in the MySQL/MariaDB world and I'm proud that MariaDB have invested resources into making this a successful product.

MariaDB ColumnStore is an Open Source project the source code `server <https://github.com/mariadb-corporation/mariadb-columnstore-server>`_ and `engine <https://github.com/mariadb-corporation/mariadb-columnstore-engine>`_ are available on GitHub and bugs are tracked on `Jira <https://jira.mariadb.org/projects/MCOL/issues/>`_. We also have a `public mailing list/forum <https://groups.google.com/d/forum/mariadb-columnstore>`_ to discuss the project and answer any questions. With the GitHub trees the *master* branch contains the latest release and *develop* contains the code going into the next release.

Today we are announcing the first beta release containing all our efforts so far, MariaDB ColumnStore 1.0.4. This release is our easiest ever to install, a lot cleaner and integrates better with the operating system than before.

Beta Release
------------

This first beta release contains a modified version of MariaDB 10.1.18. The modifications are required to support some of the more unique features of ColumnStore such as Window Functions. Queries are processed using external processes that can be run on multiple servers making this a distributed engine similar to map/reduce systems.

It does not yet support all the data types the MariaDB supports but for large analytics data sets it should support everything you need.

You can read about the beta `here <https://mariadb.com/blog/invitation-join-mariadb-columnstore-104-beta>`_ and download it from `MariaDB's Download Page <https://mariadb.com/downloads/columnstore>`_. There is also a follow up blog-post with `more information <https://mariadb.com/blog/getting-know-mariadb-columnstore>`_.

The Future
----------

As we head towards GA we are aiming to fix bugs found during the beta period and add a few utilities that are not yet present. We also plan to support more Linux distributions that we do at present.

From there we will be working on more enhancements and features including adding support for data types that are currently missing.

This is an exciting project with a complex codebase and it is a lot of fun to work on. I'm looking forward to the adventure ahead.
