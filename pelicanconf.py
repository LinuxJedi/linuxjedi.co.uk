#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#AUTHOR = 'Zeyuan Hu'
SITENAME = "Tech Stuff"
SITESUBTITLE = "A tmp place to rest"
SITEURL = 'http://zhu45.org'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS = (('Brian Aker', 'http://krow.net/'),
#          ('Eric Gustafson', 'https://egustafson.github.io/oscon-2014-p1.html'),
#          ('Patrick Galbraith', 'http://patg.net/'),
#          ('Yazz Atlas', 'http://askyazz.com/'),
#         )

# Social widget
SOCIAL = (('GitHub', 'http://github.com/xxks-kkk'),
#          ('Another social link', '#'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='notmyidea-lxj'
DEFAULT_DATE_FORMAT = '%a %d %b %Y, %H:%M'

# Cleaner page links
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
# Cleaner Articles
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

DISPLAY_TAGS_INLINE = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tag_cloud']
