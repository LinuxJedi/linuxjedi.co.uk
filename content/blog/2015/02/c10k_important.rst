Why The C10K Problem is Important
=================================

:date: 2015-02-14 17:49
:category: General
:tags: HP, Advanced Technology Group, Nginx, libAttachSQL

For those who are not familiar with the concept the `C10K problem <http://www.kegel.com/c10k.html>`_ is about trying to handle many simultaneous clients on a web server.  Originally written about trying to handle 10,000 clients on a Gigabit Ethernet connection back in the late 90s, but this is still a problem today (with more clients and bigger connections).

Websites are dealing with more and more traffic as not only more people every year are using the internet with more devices but they are also increasing their usage.  By this I mean not only in the amount they use the internet but higher resolution monitors and faster CPUs for interactive content means the amount of data for websites has increased too.  It has got to the point where dozens of files are needed to load a site such as Facebook or Twitter.

Faster and faster internet connections have also meant that users are far more impatient.  I first used the Internet at home in 1995 with a 33.6Kbit/sec modem.  Websites would typically take at least 10 seconds to access and load, sometimes more.  This didn't bother us back then.  A decade later Internet speeds are much faster and sites are much bigger (javascript, css, high-res/retina images, flash, etc...), but users expect load times of only a couple of seconds and access/wait times of less than a second, even on cell phones.

Although the server hardware is evolving it is difficult to keep up with client demand and thus the C10K problem is still an issue today.  One way of solving this is to have many servers or cloud instances handling the traffic.  This can cause a cost issue for many companies, especially startups.  The other solution which is gaining in popularity is event driven I/O.

Typically with event driven I/O you run the server single threaded, although you can offload onto multiple threads/processes.  A single event loop is run which listens for new events such as data in or out and reacts based on the event.  In Linux this relies heavily in ``epoll()`` and BSD based distributions ``kqueue()``.  These are edge-triggered ``poll()`` replacements which notifies the application of a transition from a socket not-ready to ready.

It does not feel natural to use a single-threaded solution in a world of multi-core CPUs but there is a wealth of evidence that this approach works very well.  It is in-general simpler to code since many of the complications of dealing with many threads such as race conditions and locking go away.  But there is the caveat that handling an event incorrectly could cause an application to hang.  The event-driven approach also typically reduces CPU usage of the application which on modern hardware can help with energy and heat savings.

`Nginx <http://nginx.com/>`_ is an example of a web/proxy server which uses event-driven design such as this.  Part of the reason Nginx is becoming so popular is that the design of it gives it the ability to scale much easier than more traditional web servers such as Apache.

With `libAttachSQL <http://libattachsql.org/>`_ we at the Advanced Technology Group are doing something very similar, but this time on the client side.  So that client applications can handle many connections to one or more servers on a single thread with ease.  We already have plans to add even more features around this for the 2.0 release.

Internally libAttachSQL uses `libuv <https://nikhilm.github.io/uvbook/introduction.html>`_ which is a high performance event driven I/O library born out of Node.js.  It also uses the event driven features of OpenSSL for SSL connections.

I have heard many times that C10K is not an issue today due to the high performance hardware at much lower prices than were previously available.  It may not be a 10K problem any more, but it is still an issue.  Even the big boys of the Internet today are using event driven solutions to help them scale and keep the running costs low.  This is evident by the increased usage of technologies such as Nginx.

In the last couple of years there is talk of the `C10M problem <http://highscalability.com/blog/2013/5/13/the-secret-to-10-million-concurrent-connections-the-kernel-i.html>`_ which suggests moving control of the TCP/IP stack completely away from the kernel to the user layer.  Personally I feel this is going a little too far for generic applications.  It could mean that your applications require specific OS/kernel and even specific hardware to run.  For people writing web servers and libraries this can easily bloat the code and by the time you have dealt with edge cases I suspect the performance increase will not be worth the extra work.
