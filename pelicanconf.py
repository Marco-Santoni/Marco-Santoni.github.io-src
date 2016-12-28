#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marco Santoni'
SITENAME = 'Marco Santoni'
SITESUBTITLE = 'Data Scientist'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['lib/pelican-plugins', 'lib']
PLUGINS = ['render_math', 'pelican-ipynb.markup']

THEME = 'lib/pelican-clean-blog'
HEADER_COLOR = '#1a1a1a' # from pelican-clean-blog theme
SOCIAL = (
    ('linkedin', 'https://linkedin.com/in/msantoni'),
    ('twitter', 'https://twitter.com/mrsantoni')
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
