################################################
Environment variable substitution using ``Sed``
################################################

:date: 2016-12-21 12:07
:category: tools
:tags: sed, shell
:summary: A ``sed`` example

Suppose we have a text file ``config.ini`` looks something like this::

  [MSSQLSERVER]
  Driver=INSTHOME/foo/foo.so

  [SYBASE]
  Driver=INSTHOME/bar/bar.so

  ...

We want to replace all the appearance of ``INSTHOME`` with the
value we hold in ``$HOME``. Here is what I do initially:

.. code-block:: shell

     sed -i -e "s/INSTHOME/$HOME/g" config.ini

- ``s`` is used to replace the found expression ``INSTHOME`` with ``$HOME``
- ``g`` stands for "global", which means to do this find & replace
  for the whole line. If you leave off the ``g`` and ``INSTHOME`` appears
  twice on the same line, only the first ``INSTHOME`` is changed to ``$HOME``
- ``-i`` is used to edit in place on filename
- ``-e`` is to indicate the expression/command to run

.. note::

     I use double quotes ``"`` to expand any variable appeard
     inside ``"``. In this case, ``$HOME``.

However, when I type this in and I got the following error::

  sed: -e expression #1, char 13: unknown option to `s'

Why did this error happen? That confused me for a while. Then, I try to
simulate what the program will do for the above expression:

.. code-block:: shell

     sed -i -e "s/INSTHOME//home/iidev20/g" config.ini

Ah! This expansion result doesn't make sense at all because ``sed`` expression
inside ``"`` needs to follow::

  "s/[target_expression]/[replace_expression/g"

So, the first thought comes to me is to escape all ``/`` in the expression:

.. code-block:: shell

     sed -i -e "s/INSTHOME/\/home\/iidev20/g" config.ini

This can work but it has two severe drawbacks:

- I'm hardcoding the value. If ``$HOME`` no longer holds ``/home/iidev20``,
  then my command breaks again, and this hinders portability.

- The readability of this code is too bad. Probably okay for Perl programmer but
  still, not quite friendly.

To address these two issues, I find the following about `GNU sed <https://www.gnu.org/software/sed/manual/html_node/Addresses.html#Addresses>`_:

    \%regexp%
        (The % may be replaced by any other single character.)

            This also matches the regular expression regexp, but allows one to use a different delimiter than /. This is particularly useful if the regexp itself contains a lot of slashes, since it avoids the tedious escaping of every /. If regexp itself includes any delimiter characters, each must be escaped by a backslash (\).

Essentially, we don't have to use ``/`` as our delimiter for the expression, especially when the pattern itself contains a lot of slashes (i.e. file path in my case).

so, I decide to use ``|`` as the delimiter:

.. code-block:: shell

    sed -i "s|INSTHOME|$HOME|g" config.ini

.. note::

    I can also use single quote ``'`` but the command should be modified like the below
    by leaving out to-be-expanded variable name outside of single quotes.

    .. code-block:: shell

           sed -i 's|INSTHOME|'$HOME'|g' config.ini
    
Now, everything works nice and clean.
