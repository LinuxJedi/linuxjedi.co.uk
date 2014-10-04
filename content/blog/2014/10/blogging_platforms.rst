Blogging Platforms
==================

:date: 2014-10-04 22:16
:category: General
:tags: Blog, LinuxJedi

A couple of weeks ago I ditched Blogger as my main blogging platform.  The main reason for this was the editing tools were breaking posts containing code.  Whilst it is a great platform for basic blogging, it is not suitable for developers blogs.

So, I was on the hunt for blogging platforms that would make it easy for me to write posts that contain technical content and is not expensive to run.  I also don't want to be maintaining my own web server, I may be capable of doing this but I don't want the time overhead.

I tried several things out that met some of my requirements but many didn't fit all.  Wordpress was probably the closest, but I had trouble bending the free templates to my will.

With many on my team at HP's Advanced Technology Group using `GitHub Pages <https://pages.github.com/>`_ for blog posts I thought I would give it a try.  Most of the team are trying out Jekyll which looks really good, but isn't for me.  I prefer `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ to Markdown and use it every day for the `libAttachSQL documentation <http://docs.libattachsql.org>`_.

On my journey I came across `Tinkerer <http://tinkerer.me/>`_ which is a layer on top of `Python Sphinx <http://sphinx-doc.org/>`_ to generate a blog site from RST files.  This was great for me because Sphinx is the renderer used for libAttachSQL's docs both in the build system and `Read The Docs <https://readthedocs.org/>`_.  I created a new blog on this hosted on GitHub Pages and `Disqus <https://disqus.com/>`_ for comments.

I had several minor problems with Tinkerer, many of which I worked around, but the main flaw was no timestamp support for blog posts.  All blog posts would have a date but not a time, so in the RSS feeds it would be as if they were posted at midnight.  If you are posting at 22:00 it means in feed aggregators your post would end up below many others posted that day and multiple posts in a day could be in any order.

Today I bumped into a blogging platform called `Pelican <http://blog.getpelican.com/>`_.  It too uses RST files to generate the site, but supports metadata in the RST files to signify things such as time of post.  It was incredibly easy to port my Tinkerer posts over so I gave it a try.

I have ended up with generation scripts, RST files and a theme I have modified in a `GitHub repo <https://github.com/LinuxJedi/linuxjedi.co.uk>`_ and the generated content in my `GitHub Pages Repo <https://github.com/LinuxJedi/linuxjedi.github.io>`_.  Pelican has a built-in HTTP server which makes it easy to preview your generated HTML before it is uploaded to the site.

In conclusion, Tinkerer is a great platform, but Pelican feels more mature and it seems to have a wider community around it.  I also found its templates much easier to edit.  Both platforms have an Open Source feel to the way you create and publish content which is fantastic for my usage.  I think I have finally found a blogging platform I can settle with.
