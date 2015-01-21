Webserver Concealing
====================

:date: 2015-01-21 19:30
:category: Security
:tags: HP, Advanced Technology Group, Security

Right now there are bots on the internet scanning every IP possible for vulnerable servers.  This is a fact of life on the internet.  This means you need to keep any internet facing machines as secure as possible.

Whilst it is no panacea one step you can take to hide the version of the web server software you are using.  If there is a zero-day bug a bot or malicious person is scanning for and you are vulnerable this can help hide it.

I was recently looking at an SSL problem with a local high school and found the server was reporting the following::

   Server:Apache/2.2.15 (Novell)
   X-Powered-By:PHP/5.3.3

There are several problems here, all are solvable:

#. Novell is unmaintained.  There are no security updates.  This needs replacing with something such as a Linux distribution or FreeBSD which does get updates.

#. Apache 2.2.15 and PHP 5.3.3 are both around 4-5 years old.  They have dozens of known bugs and secrity flaws which are fixed in newer versions.

#. The server version is advertised.  I was able to find this information easily which means any hacker can, then he can cross-reference with known security flaws and do whatever he wants with this server.

Clearly the first thing that should be done here is to update the server and its software packages.  But in addition it is possible to hide the versions used so at least one of these three points is eliminated.

First to hide the Apache server version we simply need to add one line to the configuration file:

.. code-block:: apacheconf

   ServerTokens prod

The server will now only announce that it is running Apache but no server version or OS used.

As for PHP, you can turn the announcement off completely with the following in your php.ini file:

.. code-block:: ini

   expose_php = off

This is only one small security improvement, but having many layers of security will help dramatically to protect your servers.  I only recommend this after dealing with things like software updates, firewalls, code security audits, etc...

As a side note, if you are using PHP I highly recommend using `Suhosin <http://suhosin.org/>`_ to help secure your server installation.
