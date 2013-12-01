#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'marshtrm'
SITENAME = u'Tom R. Marsh'
SITEURL = ''
SITEROOT = '/'
DEPLOYED_SITEURL = "http://www.tomrmarsh.com"
DISPLAY_PAGES_ON_MENU = True

PATH = 'content' # Path to content
PAGE_DIR = 'pages'  # Directory for pages, relative to PATH.
OUTPUT_PATH = 'public'
TYPOGRIFY = True

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
THEME = os.path.join(os.environ.get('HOME'), 'websites', 'code',
  '/Users/pmarshwx/websites/code/pelican-elegant')
STATIC_PATHS = ['downloads']
PLUGIN_PATH = os.path.join(os.environ.get('HOME'), 'websites',
                           'code', 'pelican-plugins')
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.literal',
           'liquid_tags.notebook',]


# Elegant Theme Variables
FAPPID = 1426827610867639
HIDE_CATEGORIES = True
HIDE_TAGS = True
USE_FAVICON = True
PLUGINS += ['sitemap', 'extract_toc', 'tipue_search']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS += ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
LANDING_PAGE_ABOUT = {
    'title': """
    Chief Compliance Officer By Day<br /> Amateur Musician By Night
    """,
    'details': """
     <p>Over the years, I have enjoyed playing music for my family and friends.
     A few years ago my daughter, Nikki, asked me to create a CD of instrumental Christmas music so she could share it with her students, as well enjoy it while decorating her home for Christmas.
     I enthusiastically welcomed the opportunity and created my CD, "<a href="/the-joy-of-christmas.html" title="The Joy of Christmas">The Joy of Christmas</a>".
     Three years have come and gone since that first CD and Nikki thought it was time for another.
     So I immediately began applying my unique style to some traditional Christmas classics.
     The result is a new CD, "<a href="/celebrate-the-season.html" title="Celebrate the Season">Celebrate the Season</a>".</p>

    <p>I hope this music inspires you to celebrate the season. If it does, please consider making a donation to support my musical endeavors.</p>

    <center><section style="padding:0em 0em 1em 0em;"><form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
    <input type="hidden" name="cmd" value="_s-xclick">
    <input type="hidden" name="hosted_button_id" value="WNK3UW2S6X99E">
    <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
    </form></section></center>
    """
    }

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
