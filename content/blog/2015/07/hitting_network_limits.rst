Hitting Network Limits
======================

:date: 2015-07-06 18:10
:category: Nginx
:tags: Nginx, networking

I recently wrote a high-level blog post for NGINX `outlining the new SO_REUSEPORT feature in NGINX <https://www.nginx.com/blog/socket-sharding-nginx-release-1-9-1/>`_. One of the problems I was having whilst doing the benchmarks for this was that I was hitting some kind of bottleneck before hitting the limit of what NGINX could process. This meant that it was difficult to get useful benchmarks.

The main reason was down to hitting a limit on the maximum number of interrupts per second that could be processed. Despite the evidence staring me in the face it didn't click with me that all the interrupts were being processed on just one CPU.

::

    PID   USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
    3     root      20   0       0      0      0 R  95.4  0.0   0:10.28 ksoftirqd/0 
    21076 nobody    20   0   57208  31140   2272 S  26.5  1.0   9:41.90 nginx       
    21075 nobody    20   0   57164  31200   2376 S  26.2  1.0   9:47.15 nginx       
    21078 nobody    20   0   57236  31272   2376 S  25.8  1.0   9:40.71 nginx       
    21077 nobody    20   0   57184  31112   2268 R  25.2  1.0   9:40.94 nginx 

This is an example on my home test rig. The server is based on a Core2Quad CPU, nothing special but it helps pin bottlenecks a lot of the time. NGINX in this example has been configured with ``SO_REUSEPORT`` enabled and we are returning just a very small packet response. The thing to notice here is that each NGINX worker is only using around 25-26% CPU (theoretically this machine has 400% CPU possible), and 95% CPU is being used for ``ksoftirqd``. This last part is the key, it basically means that CPU 0 is being used up nearly 100% dealing with network interrupts, hitting a limit of what the machine can process. Whilst I very quickly figured that network interrupts were the bottleneck the above didn't click with me at the time to be the issue.

It turns out in Linux there is a way to spread these interrupts across all CPUs, I stumbled upon it by accident earlier today (and am kicking myself that I wasn't aware of it before). It is called **Receive Packet Steering** (RPS). `RedHat's Performance Tuning Guide <https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Performance_Tuning_Guide/network-rps.html>`_ has a good description of what it does and how to use it. To enable it on a quad-core machine simply do:

.. code-block:: bash

   $ echo f > /sys/class/net/eth0/queues/rx-0/rps_cpus

Obviously replacing *eth0* with the name of your network card. Once enabled I was getting much better results::

    PID   USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND     
    21076 nobody    20   0   56140  29988   2272 R  93.8  1.0   9:12.14 nginx       
    21075 nobody    20   0   56152  30008   2376 R  92.9  1.0   9:17.54 nginx       
    21077 nobody    20   0   55996  29844   2268 R  92.4  1.0   9:11.67 nginx       
    21078 nobody    20   0   56160  30196   2376 R  91.7  1.0   9:11.85 nginx

The client machine (which was also configured with this parameter) was reading 2.5x the traffic and nearly half the latency. In addition there is `Receive Flow Steering (RFS) <https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Performance_Tuning_Guide/network-rfs.html>`_ which can reduce latency when RPS is used, in my testing the average latency was the same but the standard deviation was reduced.

Network cards that can spread the hardware interrupts and stacks using DPDK or similar probably won't have this issue. But for cloud environments I suspect this option will help a great deal. As always "Your Mileage May Vary".

If you have any tips for increasing performance please feel free to leave them in the comments.
