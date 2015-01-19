YubiKey for OS Logins
=====================

:date: 2015-01-19 16:14
:category: General
:tags: YubiKey, Security, HP, Advanced Technology Group

I have mentioned a few times in this blog that HP takes security very seriously and HP's Advanced Technology Group is always looking into new ways of making things secure.  Recently the team all got a `YubiKey Neo <https://www.yubico.com/products/yubikey-hardware/yubikey-neo/>`_ to use.  The initial idea was we would be trying the FIDO U2F with Google accounts but several of us went much further.

Yazz Atlas from our team has been working on getting his SSH key into the NEO with some success.  I initially got my GPG key to work with the smart card feature in the NEO and have since been tinkering with a couple of other things.

I happened to find an original YubiKey in a drawer which was used for OTP two-factor authentication to a server I no longer have access to.  I wanted to use this as a way of two-factor authentication for my computers.  Unfortunately there is no good way of doing this on the Mac at the moment so I came up with a different way of doing a less secure two-factor authentication with it (but more secure than a fixed password).

The original YubiKey's have two "slots" in them.  Each slot can store either an OTP two-factor authentication identity or a static password.  You can tap a YubiKey to get the first slot and hold for around 3 seconds for the second slot.  The way I'm using this is to have the slots store static passwords, I then have a hand typed part of my password and a second static part stored on the YubiKey.  This means that if the YubiKey is stolen/used it is useless without my hand typed-part.  I have a backup of the YubiKey's static password in my `LastPass <https://lastpass.com/>`_ account (which incidentally uses two-factor authentication).

There was a minor snag in this to begin with, my Macs are encrypted with FileVault which has a known login problem.  If you type a password too quickly it actually drops some of characters that you have typed.  The YubiKey is a virtual keyboard and although it deliberately doesn't type too quickly, it is too fast for FileVault.  If your YubiKey is a version 2.3 or higher this is easy to fix.  In the `YubiKey Personalization Tool <https://www.yubico.com/products/services-software/personalization-tools/>`_ you can go to settings and change the output frequency, this setting change can then be used to update a slot.  But if like me your original YubiKey is an older version you cannot do this.  There is a way around this by generating a new key, but it requires the command line (the GUI doesn't have the options to change the delay whilst generating a new key).

First of all you need the command line YubiKey Personalization Tool.  There are `Linux, Mac and Windows versions available <https://yubico.github.io/yubikey-personalization/releases.html>`_ and some Linux distros have it in their repository.  Using this tool you can generate a new random static password with a typing delay as follows:

.. code-block:: bash

   ykpersonalize -2 -opacing-20ms -ostrong-pw2 -ostrong-pw1 -ostatic-token

You can change the ``-2`` to ``-1`` if you wish to program slot 1 instead.  The typing delay is added using the ``pacing-20ms`` option.  Unfortunately this flag doesn't quite match the GUI, if you want to match the GUI options here is what you need to use:

* 20ms Delay - ``pacing-10ms``
* 40ms Delay - ``pacing-20ms``
* 60ms Delay - ``pacing-20ms`` and ``pacing-10ms``

For FileVault it is recommended you using the 40ms delay as a minimum.  The 20ms delay works most of the time but can still fail.

So, now to log into my machines I type in the part of the password I have remembered and then press the YubiKey to fill in the rest of the password.
