USB Flash Drives - Trimming the FAT
===================================

:date: 2015-01-05 22:34
:category: General
:tags: USB, Flash, Filesystems, HP, Advanced Technology Group

As with most of you who read this blog I carry USB flash drives around with me all the time.  Right now I have 3 Kingston DTSE9 sticks on my keyring of various sizes each with a different purpose.  Whilst these drives are nowhere near the fastest out there they are the only ones I have had so far that don't snap off keyrings.

.. image:: /images/king16GB_DTSE9_2.jpg

For this blog post I'll be talking about data where security is not a priority.  My encrypted flash drives are currently using `VeraCrypt <https://veracrypt.codeplex.com/>`_ but that is beyond the scope of this blog post.

FAT32 woes
----------

The largest one I have is 64GB and due to some of the work I do for HP's Advanced Technology Group this often needs to have large files on it.  Traditionally FAT32 has been used as a file system for memory cards and flash drives, one of the biggest reasons for this is that it is compatible with pretty much every computer operating system out there.  But FAT32 has many flaws:

* it has a single file limit of 4GB.  That may sound huge but this rules out DVD images and large databases.
* it does not support POSIX based permissions which anyone who uses Linux is used to.
* it doesn't support journalling so with a removable drive data corruption is very common.
* as a minor issue it is also designed for spinning disks with many more write cycles than flash.

What I needed was something that fixes as many of those problems as possible but is also compatible with Linux, Mac OS X and Windows.

Alternatives
------------

I looked into several alternatives to FAT32 and summarised my findings below.  I'm primarily looking for out-of-box support, I know there are paid third-party add-ons to operating systems to add support.

exFAT
^^^^^

A company looked into all the problems with FAT and created a filesystem designed for use with flash drives, they called this *exFAT*.  Unfortunately that company is Microsoft and what they created is not an open standard and is full of patents.

This means that only people who have paid licenses can use exFAT.  This includes Mac OS X and digital camera manufacturers but unfortunately means Linux support is very limited.

exFAT is therefore thrown out.

HFS+
^^^^

HFS+ is the primary file system used by Mac OS X.  There is good support for this in Macs (obviously) and Linux, but no support in Windows.

Unfortunately that means HFS+ is out.

NTFS
^^^^

NTFS is Microsoft's primary file system in NT based operating systems (for most people this means Windows XP onwards).  Like HFS+ it isn't a bad file system for flash drives and in recent Linux distributions has very good support.  Unfortunately in Mac OS X it can only be used in read-only mode.

Another Microsoft FS thrown out.

UDF
^^^

Yes, you read that correctly, UDF.  It is a filesystem which was originally designed for use with optical media.  But, it has since been adapted for use with hard drives and flash drives!

The maximum file size is 16EB (actually bigger than the maximum volume size).  It supports POSIX file system permissions.  But most importantly, it works with Linux, Mac OS X and Windows (Vista onwards) out of the box!

In addition the UDF format was designed for packet writing so it works by appending on the end of data on the file system and expiring the old data.  In theory this could lead to less wear of the drive.  Flash drives typically use dynamic wear leveling which is similar to the static wear leveling used in SSDs but less complex.  The algorithm used may mean that the packet writing has no real advantage on the wear of the drive.  I don't have enough data to say for certain.

The file system itself works like a journal.  It appends new data to the end of the log with a new version of the file table.  So, if a write was not completed successfully it will use the previous version of the log.  This also means recovery of deleted files is possible by traversing previous versions of the data log.

For me this ticks all the boxes so I am using it with a 64GB UDF formatted flash.

Making a UDF flash drive
------------------------

Mac OS X
^^^^^^^^

Unfortunately Disk Utility doesn't let you format a flash drive as UDF but you can use the command line to do it.

First of all you need to figure out the drive path for your flash drive.  It will be in the format ``/dev/disk{drive_no}`` where drive_no is the drive number, if it is followed by the letter *s* and another number then that is a partition and not what we need at this stage:

.. code-block:: bash

   diskutil list

Now you need to find out the block size (it is typically 512).  Make a note of this number because you will need it later:

.. code-block:: bash

   diskutil info /dev/disk{drive_no} | grep "Block Size"

The drive can't be changed until we unmount the partitions so run this for every partition that is currently in-use for your drive:

.. code-block:: bash

   diskutil unmount /dev/disk{drive_no}s{partition_no}

Due to the nature of the UDF format it is possible that the operating system would still detect the drive as FAT32 afterwards so we need to blank the drive with zeros.  This could take some time:

.. code-block:: bash

   diskutil secureErase 0 /dev/disk{drive_no}

Now the drive can be formatted, replace *block_size* with the number you wrote down above:

.. code-block:: bash

   sudo newfs_udf -b {block_size} /dev/disk{drive_no}

Finally the drive can be mounted again for use as normal:

.. code-block:: bash

   diskutil mount /dev/disk{drive_no}

Linux
^^^^^

In Linux things get a little easier.  First of all unmount the partitions on the drive and then we need the block size, write this one down:

.. code-block:: bash

   sudo blockdev --getbsz /dev/sd{drive_letter}

We then need to zero out the drive so that it isn't incorrectly detected:

.. code-block:: bash

   sudo dd if=/dev/zero of=/dev/sd{drive_letter} bs=1M count=1

Then we need to make the UDF format, replacing *block_size* with the number noted above:

.. code-block:: bash

   sudo mkudffs -b {block_size} --media-type=hd /dev/sd{drive_letter}
