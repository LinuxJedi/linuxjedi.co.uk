########################################################################
What's the difference between sourcing a script and executing a script?
########################################################################

:date: 2016-12-20 21:49
:category: tools
:tags: shell
:summary: Amusing question in shell

I run across the question in the title when I take a break from the work
today. Then I did a little bit googling, and the explanation is not quite satisfying
to me. So, I decide to answer this question by a simplied example from my work.

For me, this question appears frequently when you try to install some software.
Some software, like the product I'm working on, depends on a set of environment variables
in order to setup itself properly. Usually, this may inovlve manual editing of the environment
variables in order to make the product work. However, we can do much better.
We can somehow let a setup program to edit the environment variable for the user and finish
the whole product setup process automatically.

Suppose a software relies on an environment variable ``TEST_SOURCE`` and
we don't have such an environment variable initially.

.. code-block:: shell

      $ echo $TEST_SOURCE
      $

If we create a test script ``test.sh`` like the following:

.. code-block:: shell

     #!/bin/sh

     export TEST_SOURCE=HELLO
     
Then we can have two way to execute this script: either by ``./test.sh`` or
by ``source test.sh`` and they two have different outcome:

.. code-block:: shell

     $ ./test.sh
     $ echo $TEST_SOURCE
     $
     $ source test.sh
     $ echo $TEST_SOURCE
     HELLO

So, the conclusion is that when we execute in ``source``, we actually run program
in the current shell. However, if we execute in ``./``, then we run the program
in a separately shell and the execution (i.e. modify environment variable) doesn't
impact our current shell.

















..
   http://www.theeggeadventure.com/wikimedia/index.php/Interview_Questions




      
