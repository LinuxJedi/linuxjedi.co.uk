#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Zeyuan Hu'
SITENAME = "Fluffy Stuff"
SITESUBTITLE = "A tmp place to rest"
SITEURL = 'http://zhu45.org'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_DOMAIN = SITEURL

STATIC_PATHS = ['assets', 'images']

# Blogroll
# LINKS = (('Brian Aker', 'http://krow.net/'),
#          ('Eric Gustafson', 'https://egustafson.github.io/oscon-2014-p1.html'),
#          ('Patrick Galbraith', 'http://patg.net/'),
#          ('Yazz Atlas', 'http://askyazz.com/'),
#         )

# Social widget
SOCIAL = (('GitHub', 'http://github.com/xxks-kkk'),
          ('Stack Overflow', 'http://stackoverflow.com/users/1460102/jerry'),
          ('WordPress', 'http://zeyuanhu.wordpress.com/'),
          ('LinkedIn', 'https://cn.linkedin.com/in/zhu45')
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
DEFAULT_DATE_FORMAT = '%a %d %b %Y, %H:%M'
HIDE_SIDEBAR = False
# Cleaner page links
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
# Cleaner Articles
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
DISPLAY_TAGS_INLINE = True

#################################
#
# Pelican notmyidea-lxj customization
#
#################################

#THEME='notmyidea-lxj'

#################################
#
# Pelican bootstrap3 customization
#
#################################

#THEME='pelican-bootstrap3'
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
PLUGIN_PATHS = ['plugins']
PLUGINS = ['tag_cloud', 'render_math', 'i18n_subsites']
LOCAL_CONTENT_CACHE = False
HIDE_SIDEBAR = True
DISPLAY_CATEGORIES_ON_MENU = False # disable display categories in the navbar
DISPLAY_PAGES_ON_MENU = False
PYGMENTS_STYLE = 'emacs'
BOOTSTRAP_THEME = 'lumen'

#################################
#
# Pelican cid customization
#
#################################

INDEX_URL = 'blog2'
INDEX_SAVE_AS = INDEX_URL+'/index.html'

THEME='pelican-cid'
USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('About', 'about-zack.html'),
                    ('Blog', INDEX_URL),
                    ('Quotes', 'quotes.html'),
                    ('Projects', 'projects.html')
)
SITEFOOTER = u'Zeyuan Hu &copy; 2015-2017.'

#################################


# disable category
# DIRECT_TEMPLATES = ['index', 'tags', 'archives']
#USE_FOLDER_AS_CATEGORY = False

# Archives page related setting
ARCHIVES_URL = 'archives/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Ensure the pages appear in the menu 
# Usually, pages will go to the menu by default. I use this as a safeguard.

# year archive
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/period_archives.html'
YEAR_ARCHIVE_URL = 'archives/{date:%Y}/period_archives.html'

# tag
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

# Disqus
DISQUS_SITENAME='zhu45-org'

# Google analytics
GOOGLE_ANALYTICS='UA-37565522-2'

# Exclude the draft page
ARTICLE_EXCLUDES = [ '/drafts' ]


#################################
#
# Custom Jinja Filters
#   see: http://jinja.pocoo.org/docs/templates/#filters
#  
#   format: http://strftime.org
#################################


def suffix(d, wrap=True):
    tmp = 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')
    if wrap:
        return '<span class="day_suffix">' + tmp + '</span>'
    else:
        return tmp


def tagsort(tags):
    return sorted(tags, lambda a, b: len(b[1]) - len(a[1]))


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


def month_name(month_number):
    import calendar
    return calendar.month_name[month_number]


def archive_date_format(date):
    return custom_strftime('%m.%d.%Y', date)


def sidebar_date_format(date):
    return custom_strftime('%a {S} %B, %Y', date)


def dump(thing):
    return vars(thing)

# Which custom Jinja filters to enable
JINJA_FILTERS = {
    "month_name": month_name,
    "archive_date_format": archive_date_format,
    "sidebar_date_format": sidebar_date_format,
    "tagsort": tagsort,
    "dump": dump,
}
