YubiKey NEO with GnuPG
======================

:date: 2015-01-28 10:24
:category: Security
:tags: YubiKey, Security, HP, Advanced Technology Group

Last week I published a blog post on using `YubiKey for OS Logins <http://linuxjedi.co.uk/posts/2015/Jan/19/yubikey-for-os-logins/>`_.  Since then I've had a request from inside HP to create a blog post on using the YubiKey NEO with GnuPG which is another thing I have done with my NEO.

The YubiKey NEO has a built-in CCID smartcard interface which is disabled by default.  GnuPG can use this instead of a passphrase for your keys.  This blog post will give some indication on how to do this.  It is assuming you have some experience of using gpg, I wanted to keep this as short as possible and it can be a complex topic.  As with any process I highly recommend backing up your existing gpg keys if you have any:

.. code-block:: bash

   $ gpg -o key-backup.key --armour --export-secret-keys email@address.com

Before we start you will need to enable CCID on the YubiKey NEO, it is disabled by default.  The easiest way to do this is to use the `YubiKey NEO Manager <https://developers.yubico.com/yubikey-neo-manager/>`_.  In this tool click on *Change connection mode* and tick the CCID box.

First of all the YubiKey's CCID needs initializing.  The following enables the admin commands and starts the generation of new keys.  If you want to use the YubiKey with your old key then Ctrl-C out when it asks about the expiry.  Otherwise go through the prompts and make sure to use the ``save`` command afterwards:

.. code-block:: bash

   $ gpg --card-edit

   gpg/card> admin

   gpg/card> generate

Now, every time you use it you will be asked for the PIN or admin PIN.  These are set to some basic defaults ('123456' and '12345678' respectively) so it would be a good idea to change these:

.. code-block:: bash

   $ gpg --change-pin

Option 1 is to change the access PIN and option 3 is to change the admin PIN.

Using an existing key
---------------------

If you have followed the steps above you have a primed smart card on your YubiKey ready to load your key onto.  Before we do this you need a total of three subkeys, one for encryption (you likely already have), one for signing and one for authentication.  We need to enter the key editor mode of gpg to look at this and add these:

.. code-block:: bash

   $ gpg --expert --edit-key email@address.com

You should get a list of your key and subkeys straight away.  The *Usage* column is the one we are looking for here.  You need an ``E`` for Encryption, ``A`` for Authentication and ``S`` for Signing.  If you are missing any of these:

.. code-block:: bash

   gpg> addkey

Select option 8 (RSA) and then add whatever you need.  Repeat the process until you have one of each.

You are now ready to move the keys to the YubiKey:

.. code-block:: bash

   gpg> key 1
   gpg> keytocard
   gpg> key 2
   gpg> keytocard
   gpg> key 3
   gpg> keytocard
   gpg> save

Your secret subkeys are now on the YubiKey which can be verified using:

.. code-block:: bash

   $ gpg --card-status

