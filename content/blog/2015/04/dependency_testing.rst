Why Dependency Testing is Important
===================================

:date: 2015-04-23 22:27
:category: General
:tags: Testing, Parallels

Or...

Why I'm Ditching Parallels
--------------------------

I've been using Parallels quite successfully for several months now and I must admit it is a great way to run all my various Linux distros that I work with on my Mac.

One of my main VMs is the latest Fedora release (currently Fedora 21). Fedora can be quite bleeding edge and in recent releases they have had a policy of a rolling kernel release inside the fixed twice-annual releases.

A few weeks ago my Fedora VM ran an update which included an update to a 3.19 Kernel release. After a reboot my Fedora VM didn't start Xorg and was stuck at a service startup messages.

I wasn't getting much response from Parallels support so I dug in to debug what had happened. It turns out that the Parallels tools had attempted to rebuild and failed. This meant that the required kernel modules were missing and a full boot could not happen. My Parallels had also updated so I could not switch to an older kernel, because this required a module rebuild and there development packages for the older kernels were not available.

I ended up creating a quick temporary patch to fix this and `posted it on Parallels forum <https://forum.parallels.com/threads/temporary-fix-for-kernel-3-19.328277/>`_. I eventually got a response from Parallels support stating they are working on the problem and to this day (now nearly 2 weeks after I created the patch) the problem has still not officially fixed by Parallels.

Now, I understand that Parallels needs time to fix these things. But, this problem could have easily been resolved months ago, before it was even a problem to the users that have needed my patch.

It comes down to a type of continuous integration that is relatively easy to set up. That is to test with new versions of your dependencies when they are upgraded.

In the case of Linux this could be done by having a script that updates Arch Linux or similar daily, tries to install Parallels Tools and reports on failure. If Parallels had used this process with Arch Linux the problem would have been automatically detected in early February and they would have had time to fix it before it affected the bigger distros.

This would cause a few false failures but those would be easy to weed out. They could even take a Fedora release and build a new kernel and other dependencies for it daily which will probably reduce the false failures.

Today we are at a point where Ubuntu 15.04 has been released. The kernel with that distro is not compatible and there is no update to the proprietary Xorg driver that comes with Parallels for Xorg 1.17 that comes with this release. Making it completely unusable with Parallels.

I need to use virtual machines for my day job at Nginx as I did in HP, so this problem is a real productivity killer and has meant I've had to finally give up and ditch Parallels. Today I've been trying VMWare Fusion instead and so far it is working great with every distro I need to use, even with updated kernel and Xorg.
