#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Gabriel Weindel'
SITENAME = 'Personal Website'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = 'Flex'

SITELOGO = 'img/profile.png'

# --------------8<---------------------
# Files and content


# This will look for a directory img/ 
# inside the directory content/
# The contents of img/ will be available at 
# {{ SITEURL }}/img
STATIC_PATHS = ['img']

# If we want to create static pages,
# we should put them in content/pages
PAGE_PATHS = ['pages']

# If we want to create blog posts (articles),
# we should put them in content/posts
ARTICLE_PATHS = ['posts']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True