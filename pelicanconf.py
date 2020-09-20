#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys

sys.path.append("plugins/pelican-jupyter-reader/pelican")

AUTHOR = "Jason Ross"
SITENAME = "Jason Ross's Blog"
# SITEURL = "https://jason-s-ross.github.io"

PATH = "content"

TIMEZONE = "PST8PDT"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# Social widget
SOCIAL = (("LinkedIn", "https://www.linkedin.com/in/jason-ross-80b962b2/"),)

DEFAULT_PAGINATION = False

THEME = "./themes/pelican-blueidea"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKUP = ("ipynb",)

from plugins import pelican_jupyter_reader

PLUGIN_PATHS = ["./plugins/"]
PLUGINS = [pelican_jupyter_reader, "pelican-md-metayaml"]
IPYNB_MARKUP_USE_FIRST_CELL = True
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_EXPORT_TEMPLATE = "templates/base.html.j2"
