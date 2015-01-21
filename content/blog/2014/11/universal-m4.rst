Autotools and Mac Universal binaries
====================================

:date: 2014-11-25 16:38
:category: Coding
:tags: HP, Advanced Technology Group, libAttachSQL, Autotools

Recently I have been working on a Python based wrapper for `libAttachSQL <http://libattachsql.org/>`_ and found that when testing on a Mac I was having trouble compiling the wrapper.  It turns out that Python included in Mac operating systems uses a universal binary (also called fat binary) format and since libAttachSQL is not compiled that way it would not link correctly.

For those who have never come across this, Universal binaries were originally intended to contain executables for multiple platforms (such as PPC and i386) to ease hardware transition.  The OS will only load the compatible part into memory and use that.  Python as well as several other current Mac binaries are compiled to have i386 and x86_64 binaries in one package.

Compiling a Universal binary is actually relatively easy but I didn't want to put the hard work on the use who is compiling the library and I wanted something I could use in other projects in the future.  So I have created an m4 script which can be used with Autotools to build Universal binaries.  This can be found in my `m4 scripts GitHub repository <https://github.com/LinuxJedi/m4scripts>`_.

The script in question is called ``ax_mac_universal.m4`` and when the ``AX_UNIVERSAL_BINARY`` macro is used it will automatically detect if the environment supports universal binaries and add the necessary compiler flags to build them.  It also adds ``--enable-universal-binary`` to configure so that you can force this feature on/off at will.

This script will be included as part of the upcoming libAttachSQL 1.0.2 release.
