#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican_jupyter import markup as nb_markup

import re
import os
import shutil

AUTHOR = 'GABRIEL WEINDEL'
AUTHOR_LOWER = 'Gabriel Weindel'
AUTHOR_SHORTENED = 'Gabriel'
AUTHOR_SUBTITLE = 'Cognitive Scientist'


SITENAME = 'Gabriel Weindel\'s webage'
SITESUBTITLE = u'Blog posts and thoughts on cognitive science (under construction).'
SITE_DESCRIPTION = 'Blog posts and thoughts on cognitive science (under construction).'
SITEURL = ''
FAVICON = 'favicon.ico'


# Regional Settings
TIMEZONE = 'Europe/Paris'
DATE_FORMATS = {'en': '%d %b, %Y'}
DEFAULT_LANG = u'en'
	
# Plugins and extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {
            'permalink': 'true'
        },
        'markdown.extensions.meta': {},
        'markdown.extensions.admonition': {},
    }
}

MARKUP = ['md']
PLUGIN_PATHS = ['/home/gabriel/pelican-plugins/']
PLUGINS = ['sitemap',
           'extract_toc',
           'neighbors',
           'render_math',
           'related_posts',
           'share_post',
           'series',
           'tipue_search',
           'summary',       # auto-summarizing articles
           'feed_summary',  # use summaries for RSS, not full articles
           'ipynb.liquid',  # for embedding notebooks
           'liquid_tags.img',  # embedding images
           'liquid_tags.video',  # embedding videos
           'liquid_tags.include_code',  # including code blocks
           'liquid_tags.literal',
           'tag_cloud',
           ]
IGNORE_FILES = ['.ipynb_checkpoints']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'hourly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Appearance
THEME = 'pelican-aegis-jupyter-theme'
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

#CLAIM_GOOGLE = "ZsWFnpirKDgtbmwb1YRymDnSfvnUrpzCbf6LD1F_4TY"
#CLAIM_BING = "8FF1B025212A47B5B27CC47163A042F0"

STATIC_PATHS = ['images', 'downloads']
DIRECT_TEMPLATES = (('index', 'archives', 'search', '404', 'about'))
AUTHOR_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Labels
RELATED_POSTS_LABEL = 'Related Posts'       # articles that share common tags
SHARE_POST_INTRO = 'Share This Post :'

# SMO
FEATURED_IMAGE = SITEURL + '/img/stone.png'

ENABLE_MATHJAX = True

# files are actually saved in /aegis-jupyter/static/img/, but its copied to /output/theme/img/.
# just store any meta files in /aegis-jupyter/static/, and you are good.
PROFILE_PHOTO_FOOTER = "theme/img/profile.png"
PROFILE_PHOTO_ABOUT = "theme/img/profile.png"
INDEX_BANNER_IMAGE = "theme/img/stone.png"
LOGO_WITH_SUBTITLE = "theme/img/logo.png"  # logo created at "https://vectr.com/"

# actually located in 'content/downloads/misc/'. Files in 'content/downloads' will be copied into 'output/downloads' to
# auto-generate html href link.
RESUME_PDF_LINK = 'downloads/CV_GW.pdf'
RESUME_BUTTON_TEXT = 'Download CV'

GITHUB_LINK = 'https://github.com/GWeindel'
#LINKEDIN_LINK = 'https://www.linkedin.com/in/eric-kim-34318811b/'

ABOUT_PAGE = 'about.html'
ARCHIVE_PAGE = 'archives.html'

# when developing offline, set it as False.
USE_CDN = False

########################### Jupyter Notebook related ########################

# for liquid tags
#CODE_DIR = 'downloads/code'
#NOTEBOOK_DIR = 'downloads/notebooks'
#MISC_DIR = 'downloads/misc'

# copies files that are used when writing jupyter notebook to output directory
#JUPYTER_IMAGES_DIR = 'content/downloads/notebooks/jupyter_images'


#def copy_jupyter_images_to_output(dir):
#    jupyter_image_dir = re.split('\\\\|\\/|\\/\\/', dir)[-1]

#    if not os.path.exists(os.path.join('output', jupyter_image_dir)):
#        os.makedirs(os.path.join('output', jupyter_image_dir))

#    for file in os.listdir(dir):
#        shutil.copy2(os.path.join(dir, file), os.path.join('output', jupyter_image_dir))


#copy_jupyter_images_to_output(JUPYTER_IMAGES_DIR)

############################ Social Media Shares ############################

# About Page
ABOUT_PAGE_TITLE = 'About me'
#ABOUT_PAGE_DESCRIPTION = 'Pythonic Thinker & Solver, Petroleum Engineer'

# Archive Page
ARCHIVE_PAGE_TITLE = 'Archive'
#ARCHIVE_PAGE_DESCRIPTION = 'Full Archives of Pythonic Excursions'

# landing(index) page description
INDEX_PAGE_TITLE = 'Index'
#INDEX_PAGE_DESCRIPTION = u'Stories About Python and Data Science | by Eric Kim'

### social media share debugger
# Twitter: https://twitter.com/validator
# Facebook: https://developers.facebook.com/tools/debug/


##############################################################################

FOOTER_TITLE = 'ABOUT GABRIEL'
TEXT_FOOTER = 'My name is Gabriel Weindel and I am a cognitive scientist currently working at Aix Marseille Université in the Laboratoire de Psychologie Cognitive and Laboratoire de Neurosciences Cognitives. As a researcher my interest goes to the test and application of mathematical cognitive models to the general population or to populations with cognitive deficits. See the About page for my resume.'
EMAIL = 'firstname.lastname[at]gmail.com'
LOCATION = 'Marseille, France'
COPYRIGHT_NOTICE = 'Website powered by Pelican, theme created by Eric Kim (https://aegis4048.github.io/) @2018'

INCLUDE_PROGRESSBAR = True
PROGRESSBAR_COLOR = '#24292e'

# turn off typografy. otherwise the codes in Jupyter won't properly be highlighted

##############################################################################

# code snippet for processing variables for auto-generation of Tech Stacks
NUM_MAX_STAR = 5
TECH_STACKS = {'Python': 5,
               'Bootstrap': 4,
               'HTML': 4,
               'Django': 4,
               'jQuery': 4,
               'CSS': 4,
               }

def process_techstacks(tech_dict, num_max_star):
    num_stacks = len(tech_dict)
    tech_stacks_list = [{key: {'filled_star': value, 'empty_star': num_max_star - value }} for key, value in tech_dict.items()]
    tech_stacks_left = tech_stacks_list[:num_stacks // 2 + num_stacks % 2]
    tech_stacks_right = tech_stacks_list[num_stacks // 2 + num_stacks % 2:]
    return tech_stacks_left, tech_stacks_right


TECH_STACKS_LEFT, TECH_STACKS_RIGHT = process_techstacks(TECH_STACKS, NUM_MAX_STAR)

##################################################################################################################

PORT = 8090

# rmdir pelican-aegis-jupyter-theme
# git rm --cached pelican-aegis-jupyter-theme -r
# git submodule add https://github.com/aegis4048/pelican-aegis-jupyter-theme.git pelican-aegis-jupyter-theme

# rmdir output
# git rm --cached output -r
# git submodule add https://github.com/aegis4048/aegis4048.github.io.git output




# git submodule add https://github.com/aegis4048/aegis4048.github.io.git output
# git rm --cached pelican-aegis-jupyter-theme -r
# rm -rf .git/modules/pelican-aegis-jupyter-theme

# git remote show origin * remote origin             --- check the connected repo
# git submodule update --init --recursive
# git submodule update --init

# pelican content -s publishconf.py


# Javascript function for estimating reading time. Run this on an article, and set the 'readingTime' variable in .md files.
"""
var count_p = 0
$('article').find('p').each(function(){
    count_p += 1
});

var count_word = 0
for (i = 0; i < count_p; i++) {
    Countable.count($('article p')[i], function(counter) {
        count_word += counter.words;
    });
}

var wpm = 200,
    estimatedTimeMin = Math.round(count_word / wpm)
    
console.log(estimatedTimeMin)
"""


"""
$('.disqus-comment').each(function(){
    var numCommentText = $(this).text(),
        num = numCommentText.match(/\d+/g)
    $(this).text(num)
});
"""