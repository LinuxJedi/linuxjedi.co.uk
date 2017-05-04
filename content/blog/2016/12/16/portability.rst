.. _portability.rst:

############################
Lesson Learned: Portability
############################

:date: 2016-12-16 23:20
:category: misc
:tags: software-engineering, shell, AIX
:summary: Shell is not portable!

Portability is a kind of issue that people always talk about in software engineering field.
I never have been through such problem on my own probably because I don't have to port my
stuff into different platforms. However, this is not the case anymore during the work.

Recently, I revisit the first task I owned when I joined the team, which is to develop a lightweight
configuration tool to improve product usability. Lightweight is the key of this task as we originally
have a Java-based GUI setup tool involving lots of point & click. This solution is fairly unpopular among
our customers mainly because the program itself takes lots of space for DB2 image and it doesn't fit well
with his peers, which all are scripts that can be executed directly from shell.

So, in my iteration, I decide to follow the format of majority of utility tools in DB2 image - using scripting language.
The language I choose is, unfortunately, Shell. The whole task goes amazingly well. With the help of my tool, product configuration
time is reduced by 75%. Everyone in my team loves it until someone decides to run it on AIX.

The environment I develop the tool is SUSE with ``ksh`` installed. The AIX that my colleague tries to test my tool on also has ``ksh`` configured
but there are some quirky behavior difference on different platform.

For instance, when I try to split an array, say ``tmp2`` with delimiter ``:``, the following code works great on SUSE::

  saveIFS=$IFS
  IFS=":"
  local tmp2=($tmp) # split tmp with ":" and stored into tmp2 as array
  IFS=$saveIFS

However, on AIX, only the following way will work::

  #!/bin/sh
  tmp=a:b:c:d
  saveIFS=$IFS
  IFS=":"
  local tmp2
  n=0
  for i in $tmp; do tmp2[$n]=$i; ((n=n+1)); done
  IFS=$saveIFS
  echo ${tmp2[0]}
  echo ${tmp2[1]}
  echo ${tmp2[2]}
  echo ${tmp2[3]}

As you can see, I need a for loop to split the array on AIX.

For another example, when I try to increment counter inside a loop, on SUSE,
I can do ``((n++))`` but on AIX, I need to do ``((n=n+1))``.

This makes me realize why most of our development scripts (i.e. to help build the source code)
use perl instead of shell. I have to rewrite the whole script in Perl.

This is a very important lesson for a fresh college graduate by that time.
