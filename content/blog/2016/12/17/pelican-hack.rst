.. _pelican-hack.rst:

##################
Pelican Hack Day
##################

:date: 2016-12-17 22:44
:category: tools
:tags: pelican, Jinja

I have been using Sphinx since 2012 and I spend quite a amount of time to customize
my old Sphinx-based websites 
(`This article revisits all my past website construction effort <https://zeyuanhu.wordpress.com/2016/11/24/under-construction-part-12/>`_).
However, most of the time I'm tweaking the CSS and content organization of the site.
I never get my hands on a serious template customization. The reason is quite simple,
I have limited knowledge how Sphinx interact with Jinja template engine and Jinja
language itself just looks really bizzare to me. 

Now, since I start a new blog, I decide to give Jinja a chance and customize 
`my archive page <{filename}/archives/index.html>`_ a little bit.

Here is what I want my archive page to look like:

    - Don't display post content. Only the title itself.
    - Display archives by year and archives by tags within the same page at the same time.
    - Display the number of posts for each year, and for each tag.
    - Show the time only in "month.day.year". I don't need the hours and minutes.

****************
First Iteration
****************

If you have read about `Creating themes section in Pelican doc <http://docs.getpelican.com/en/3.6.3/themes.html#templates-and-variables>`_,
you will see that we have to work with ``archives.html``. Pelican will use the layout
specified in this file to generate our archive page.