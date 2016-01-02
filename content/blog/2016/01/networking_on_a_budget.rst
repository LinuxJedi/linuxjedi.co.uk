Multi-Gigabit Networking on a Budget
====================================

:date: 2016-01-02 14:10
:category: Nginx
:tags: Nginx, networking

I've recently acquired two "refurbished" Xeon workstations from eBay to do some `NGINX <https://www.nginx.com/>`_ testing with. These are:

* A Lenovo ThinkStation S30 - 6 core / 12 thread E5-1650v2 @3.5GHz, 4GB ECC RAM (upgraded to 12GB ECC - £10) - £650

* A Lenovo ThinkStation C20 - 2x 4 core / 8 thread (8 core / 16 thread total) E5620 @2.4GHz, 12GB ECC RAM - £200

As you can maybe tell, I'm a fan of Lenovo hardware, I use a Thinkpad x220 still as my primary laptop despite also having newer laptops.

.. image:: /images/xeon_workstations.jpg
   :alt: Lenovo ThinkStation S30 and C20
   :width: 400px

The S30 was actually brand new, still sealed in box with Lenovo tape. Both machines were in great condition and run NGINX very well... Too well... The gigabit LAN in these was easily saturated without any real effort from the rest of the machines.

I decided to look into ways of upgrading the network on these machines but without spending a fortune doing it.

Quad-port Bonded Gigabit
------------------------

First up I looked into 4-port Gigabit network cards. For £40 each I got hold of an Intel Pro 1000 ET and an Intel Pro 1000 PT. The main difference between these cards appears to be the number of interrupt channels per port. The ET has 4 per port, the PT has 1. I have an HP ProCurve 16-port Gigabit switch I luckily picked up on eBay for £10 a while back so both cards were hooked into this using lots of short runs of CAT5e cabling.

Intel Pro 1000 ET:

.. image:: /images/1000et.jpg
   :alt: Intel Pro 1000 ET
   :width: 400px

Intel Pro 1000 PT:

.. image:: /images/1000pt.jpg
   :alt: Intel Pro 1000 PT
   :width: 400px

I was using Fedora 23 in both machines, RedHat have an excellent guide on how to bond network connections using NetworkManager's CLI tool which can be seen `here <https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Networking_Guide/sec-Network_Bonding_Using_the_NetworkManager_Command_Line_Tool_nmcli.html>`_. I also installed irqbalance so that I didn't have to worry too much about pinning the network card interrupts to specific CPUs (by default they are all pinned to the first CPU). This generally isn't the recommended way of doing it, `setting RPS <http://linuxjedi.co.uk/posts/2015/Jul/06/hitting-network-limits/>`_ is considered better, but worked fine for my testing.

I used `iperf3 <http://software.es.net/iperf/>`_ for measuring the bandwidth between the cards and did no tuning apart from setting up irqbalance.

.. code-block:: bash

   $ iperf3 -Z -N -P4 -c ngx4

The result summary showed almost exactly 3GBit/sec being transferred between the cards. This tallys with what was being observed using NGINX which was peaking at around 3.5GBit/sec with a little bit of tuning. The biggest problem with these cards and NGINX was the amount of connections-per-second. Whilst the Pro 1000 ET could easily handle the number of interrupts required for a high number of Packets Per Second, the Pro 1000 PT got very saturated quickly. Having a high number of PPS is vital to handling many connections per second with small amounts of data being transferred.

10 Gigabit Ethernet
-------------------

I spent a while looking at alternative solutions for even faster networks. I looked into Inifiband, Dolphin Interconnect and other similar technologies. All designed for fast low-latency connections. I almost bought an Inifiband based solution when I stumbled across a pair of Mellanox ConnectX 2 10GbE adaptors. Ordering the pair of these came to £24.81 (plus £10.71 shipping from the US). They use SFP+ connectors so I bought a copper 1 meter SFP+ cable for £4.

Mellanox ConnectX 2:

.. image:: /images/connectx.jpg
   :alt: Mellanox ConnectX 2
   :width: 400px

I plugged them in to each and set them up with static IPs and they worked great out-the-box. The Linux driver is showing 8 interrupts for the cards and irqbalance handles these nicely. With iperf executed as before the results are 9.4GBit/sec transferred through these cards.

Summary
-------

I have learned a lot from this, especially since this is my first physical exposure to 10GBit networking (I've configured software for them, just never wired them). The 4-port Intel NICs are amazing and I would highly recommend the Intel Pro 1000 ET or VT if you are in the market for a used card, the PT cards are good too but can't handle as many PPS.

I'm extremely impressed by the performance of the 10GbE cards for such a low price and they would make great cards to do large file transfers (video work?) between machines in a home. I haven't yet found an affordable switch yet that has more than 2 SFP+ ports but I'm keeping my eye out for one. I'm also on the lookout for a cheap way of doing 40GbE connections but it may be a little too soon to do this kind of testing.

I love the Lenovo ThinkStations and would have been equally happy with HP's Z-series, but couldn't find them at the right price-point. The Ivy-Bridge based S30 would actually make an amazing gaming machine if paired with a good graphics card. For me, they are both fantastic dev/test machines (and very fast at compiling). I've already used them to debug a lot of code and I'm looking forward to testing more hardware and software with them in the future.
