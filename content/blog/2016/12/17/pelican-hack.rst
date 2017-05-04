.. _pelican-hack.rst:

##################
Pelican Hack Day
##################

:date: 2016-12-17 22:44
:category: tools
:tags: pelican, Jinja
:summary: Design log for Pelican website

I have been using Sphinx since 2012 and I spend quite a amount of time to customize
my old Sphinx-based websites 
(`This article revisits all my past website construction effort <https://zeyuanhu.wordpress.com/2016/11/24/under-construction-part-12/>`_).
However, most of the time I'm tweaking the CSS and content organization of the site.
I never get my hands on a serious template customization. The reason is quite simple,
I have limited knowledge how Sphinx interact with Jinja template engine and Jinja
language itself just looks really bizzare to me. 

Now, since I start a new blog, I decide to give Jinja a chance and customize 
`my archive page </archives/index.html>`_ a little bit.

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

For the first iteration, my ``archives.html`` looks something like this

.. code-block:: rst
   :linenos:

    {% extends "base.html" %}
    {% block content %}
    <section id="content" class="body">
    <h1>Archives for {{ SITENAME }}</h1>

    {# based on http://stackoverflow.com/questions/12764291/jinja2-group-by-month-year #}

    {% for year, year_group in dates|groupby('date.year')|reverse %}
    {% for month, month_group in year_group|groupby('date.month')|reverse %}
        <h4 class="date">{{ (month_group|first).date|strftime('%b %Y') }}</h4>
        <div class="post archives">
        <ul>
            {% for article in month_group %}
                <li><a href="{{ SITEURL }}/{{ article.url }}">{{ article.title }}</a></li>
            {% endfor %}
        </ul>
        </div>
    {% endfor %}
    {% endfor %}
    </section>
    {% endblock %}

Let's first take a look at what archive page we can get from this code.

.. image:: /images/pelican-hack-1.png

Line[1],[2] illustrates how usually template file get organized. Usually, we create
a basic html file that specifies the layout of our site, which is ``base.html`` in my case.
Then, we want to extends this basic html to tailor to different needs. Inside ``base.html``,
we will place a placeholder, which will be replaced by the content of each child html page::

      {% block content %}
      {% endblock %}

In my case, I extends ``base.html`` to make an archive page. The content enclosed between 
``{% block content %}`` and ``{% endblock %}`` will replace the placeholder inside ``base.html``.

Line[4] ``{{ SITENAME }}`` is very similar to shell expansion. We will expand the variable ``SITENAME``
with its content. ``SITENAME`` is the same variable we specify in ``pelicanconf.py`` and the expanded
result will be the value we assign to ``SITENAME`` variable in config file. In my case, the expansion
result will be "Tech Stuff".

Starts from Line[8], things start to get interesting:: 

  {% for year, year_group in dates|groupby('date.year')|reverse %}
  ...
  {% endfor %}

Jinja itself is based on Python. So, we can borrow some knowledge from our Python realm. As you can tell,
``{% for ... %} ... {% endfor %}`` is what for loop looks like in Jinja. 

``dates`` itself is a list of articles ordered by date, with each element is an *article* object. Here is what 
``dates`` looks like in my mind::

      dates = [ article1, article2, article2, ... ]

and each *article* looks like::

      article = [ title, summary, author, date, ... ]

Let's put the following code in our ``archives.html`` to better understand the structure of ``dates``::

    {% for year in dates %}
    <h1>{{ year }}</h4>
    {% endfor %}

The output looks like::

    /Users/zeyuan/Documents/projects/linuxjedi.co.uk/content/blog/2016/12/17/pelican-hack.rst
    /Users/zeyuan/Documents/projects/linuxjedi.co.uk/content/blog/2016/12/16/portability.rst
    /Users/zeyuan/Documents/projects/linuxjedi.co.uk/content/blog/2016/12/03/maw-003.rst
    /Users/zeyuan/Documents/projects/linuxjedi.co.uk/content/blog/2016/11/28/maw-002.rst
    ...

.. note::

    I would highly recommend to read through the 
    `Creating themes section in Pelican doc <http://docs.getpelican.com/en/3.6.3/themes.html#templates-and-variables>`_ page,
    they describe those objects in word.

``groupby`` is a `Jinja filter which can group a sequence of objects by a common attribute <http://jinja.pocoo.org/docs/dev/templates/>`_
In our case, we want to group the info based on year. In other words, *article* with the same year should be in the same group.
Let's experiment with the following code::

    {% for year, year_group in dates|groupby('date.year') %}
        <h1>{{ year }} {{ year_group }}</h4>
    {% endfor %}

The output looks like::

    2015 []
    2016 [, , , , , , ]

Then, we apply ``reverse`` filter to make ``2016`` on top of ``2015``. The reset of the code shouldn't be hard to decode.

.. note::

    ``|`` is pipe, which is used to separate filters. It works like pipe in shell.

************
Count posts
************

This is what my current archive page layout looks like::

    {% extends "base.html" %}
    {% block content %}
    <section id="content" class="body">
    <h1>Archives for {{ SITENAME }}</h1>

    <p>
    <h2>Archives by year</h2>

    {% for year, numposts in articles|groupby('date.year') %}
    <li><a href="{{ SITEURL }}/archives/{{ year }}/period_archives.html">{{ year }} ({{ numposts|count }})</a></li>
    {% endfor %}
    </p>

    <p>
    <h2>Archives by tag</h2>

    {% for tag, articles in tags %}
    <li><a href="{{ SITEURL }}/tag/{{ tag }}.html">{{ tag }} ({{ articles|count }})</a></li>
    {% endfor %}
    </p>
    </section>
    {% endblock %}

If you understand previous sections, this code chunk should have no problem to you. I should point out that ``count``
is the filter we use to count the number of *articles*.

*********
The rest
*********

For "Archive by year", I use another template "period_archives.html" to specify the layout. It looks pretty straightforward.
However, there is a problem takes me a while to figure out:

    When I click on certain year, I jump to the archive page for that year. In that year, I want to have
    the page display "Archives for 2016". "2016" can be replaced based on the year I actually click initially.
    This leads to a problem to me: how do I know which year the user click? In other words, how do I pass the information
    to "period_archives.html"?

I couldn't find a nice way to solve this problem. Here is what I do::

    {% for year, null in dates|groupby('date.year') %}
        <h1>Archives for {{ year }}</h1>
    {% endfor %}

Since each articles under a certain year archive should have the same year value, I need to take a look at one of them
to find out the year value and put the value to the heading. However, I don't have to do this trick for tag. I can somehow
magically reference the value::

    <h1>Archives by tag '{{ tag }}'</h1>

Last point I want to point out is that you can define your own Jinja filter under ``pelicanconf.py``.
  