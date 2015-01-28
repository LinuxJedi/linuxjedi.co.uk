Working With Git
================

:date: 2015-01-25 16:33
:category: Coding
:tags: HP, Advanced Technology Group, Git

At a recent meeting HP's Advanced Technology Group has been agreeing on standards for working with git, covering mainly the collaboration and versioning aspects.  Today I will share with you how I do this in my Open Source projects which has some crossover with the group's work.

Versioning
----------

I use `Semantic Versioning <http://semver.org/>`_ everywhere I can.  In fact I used to pretty much use it everywhere before I knew it was a standard.  This means that I have my GitHub trees layed out so that 'master' is the latest stable code, v1.0 branch is the latest stable v1.0 code, v1.1 branch is the latest in v1.1 and so on.  I then create GPG signed tags from these branches to create releases as follows:

.. code-block:: bash

   $ git checkout v1.1
   $ git tag -s v1.1.2 -m 'Version 1.1.2 release'
   $ git push --tags

Forking
-------

Even if it is just me working on a particular project I will always use forks and pull requests to work on code.  This model works well with `Travis CI <http://semver.org/>`_ because it can test code prior to merging and give feedback in the pull request.

For this example I'm assuming you are using SSH keys and two-factor authentication with Git, if you aren't you need to do this ASAP.  Instructions can be found on `GitHub's blog <https://github.com/blog/1614-two-factor-authentication>`_.

A fork is typically created as follows:

1. Create a fork in GitHub, you can do this by clicking the fork button on a project.

2. Grab a local copy of your fork to work with (replacing `USERNAME` and `Repository` with whatever is applicable to you):

   .. code-block:: bash

      $ git clone git@github.com:USERNAME/Repository

3. Then you should set the upstream remote so that you can easily grab the latest code as needed.  I've used HTTPS here because you don't need to be authenticated to do this unless it is a private repository:

   .. code-block:: bash

      $ git remote add upstream https://github.com/PROJECT/Repository

Starting a New Branch
---------------------

Whenever you are starting a new group of work, create a new branch.  This holds true for features or just basic one line fixes.  In your fork:

.. code-block:: bash

   $ git checkout master
   $ git pull --ff-only upstream master
   $ git push
   $ git checkout -b my_feature

This pulls the latest code from the upstream master to your master, pushes that to your fork and then creates a new checkout based on that code.

Syncing Fork
------------

If you have worked on some code and at the same time someone else has merged code that may conflict (a pull request will tell you this straight away) you can merge upstream with your commits as follows:

.. code-block:: bash

   $ git fetch upstream
   $ git merge upstream/master

This fetches the upstream code into a local cache and then will merge it.  If there are conflicts they will be flagged for you to resolve.

Pull Requests
-------------

When your code is good and ready you can send it up as a pull request.  To do this you first need to push it up to your local repository:

.. code-block:: bash

   $ git push --set-upstream origin my_feature

Then when you go to the project's repository you will see a button to file a pull request.  If you are using continuous integration such as Travis CI you should wait for that to give a green result and preferably peer review too before clocking the merge button.
