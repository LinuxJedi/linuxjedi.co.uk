Live Kernel Patching - Why You Should *NOT* Use It
==================================================

:date: 2015-02-14 22:00
:modified: 2015-02-14 23:11
:category: General
:tags: HP, Advanced Technology Group, Kernel

Just under a year ago on my old blog I `discussed <http://thelinuxjedi.blogspot.co.uk/2014/03/live-kernel-patching.html>`_ and even `demoed <http://thelinuxjedi.blogspot.co.uk/2014/06/live-kernel-patching-video-demo.html>`_ the new Linux live kernel patching solutions.  I was reviewing these technologies out of my own curiosity as well as HP's Advanced Technology Group having an interest.  I think these technologies are great, I am personally more of a fan of the user experience of RedHat's kpatch solution but any solution is a great technical achievement.

Having said this I believe that the use case for this technology is quite narrow.  Last time I looked into these technologies only patches that affected the code of functions could be modified.  Changing structs and data definitely didn't work and I suspect that changing function declarations was also dangerous.  There is also a performance overhead.  If you are replacing functions that are called many times a second the additional overhead of a jump to the replaced function will cause a performance hit.

Where I can see live patching to be useful is on desktop machines that need critical patching but rebooting will cause losses in productivity or in science/academia where there are often long-running applications that cannot be paused for a reboot.

The only place where I do not think it should be used and unfortunately I fear it will be the main place it is used is for Internet and network services.  Everyone should strive for 100% uptime, this is something I do not dispute.  But the 100% uptime should be for the *application*, not necessarily the underlying hardware.

100% uptime of hardware is not a possible reality.  Moving parts such as fans and hard disks fail, components degrade over time, power can fail along with redundancies and at some point you may need to upgrade or move hardware.  The solution to this is the same as the solution to kernel upgrades: multiple active servers.

For web servers, have multiple servers load balanced, you can have multiple load balancers too.  Even multiple active MySQL servers are possible thanks to technologies such as `Galera Cluster <http://galeracluster.com/>`_.  When the kernel needs updating you can apply a rolling reboot.  Technologies such as `Ansible <http://www.ansible.com/>`_ will even help you do this by making sure only a certain amount of servers from each tier of your architecture is updated at any time.

I commend SUSE and RedHat in helping to replace a technology that otherwise was long since dead in the Open Source world.  Oracle seemingly killing the development of the Open Source KSplice was an annoyance to many.  But in today's world, is a technology we really need?

I would be interested to hear in the comments if there is a use case I have missed.

Update
------
2015-02-14 23:11

Robert Collins pointed out on Facebook that the overhead for the jump is likely to be too minimal to cause a performance issue and anything that is called too often is not worth patching (I am inclined to agree).

Robert also points out that there is a cost involved in migrating many VMs when the hosts need upgrading for a zero-day.  I sort-of agree with this scenario.  For public cloud this is a problem, although I believe typically the rolling upgrade is performed by pausing VMs and resuming rather than migration.  With public cloud I feel this is acceptable with a short notice period.

For private cloud there are ways around this issue, typically VMs are throw-away in private cloud so it is easy to just blow them away and recreate them in an already updated part of the data centre rather than migrate.

