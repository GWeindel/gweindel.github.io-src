#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Gabriel Weindel'
SITETITLE = 'Gabriel Weindel\'s website'
SITENAME = 'Gabriel Weindel'
SITEURL = ''
SITEDESCRIPTION = "Blog posts and thoughts on cognitive science (under construction)."
SITESUBTITLE = "Blog posts and thoughts on cognitive science (under construction)."
THEME_COLOR = "white"
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = 'Flex'

SITELOGO = 'img/profile.png'
FAVICON = 'img/favicon.ico'

# --------------8<---------------------
# Files and content


# This will look for a directory img/ 
# inside the directory content/
# The contents of img/ will be available at 
# {{ SITEURL }}/img
STATIC_PATHS = ['img','pdfs']

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
#LINKS = (('Links you might find useful : ', '#'),
# 	 ('- Github &nbsp;&nbsp;&nbsp;&nbsp;', 'https://github.com/GWeindel'),
#         ('- ORCID &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', 'https://orcid.org/0000-0002-7592-1686'),
#         ('- GScholar', 'https://scholar.google.fr/citations?user=o_fW4gIAAAAJ&hl=fr&oi=ao'),)
#	 ('- Twitter&nbsp;', 'https://twitter.com/GWeindel'),)

# Social widget
SOCIAL = [
    ("twitter", "https://twitter.com/GWeindel"),
    ("github", "https://github.com/GWeindel"),
    ("orcid", "https://orcid.org/0000-0002-7592-1686"),
]

MAIN_MENU = True

MENUITEMS = (('About Me','pages.html'), ('Posts', 'posts.html'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GITHUB_CORNER_URL = 'https://github.com/GWeindel/'
BROWSER_COLOR = 'white'
