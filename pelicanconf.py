#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
import os.path
from traitlets.config import Config

sys.path.append("plugins/pelican-jupyter-reader/pelican")

from plugins import pelican_jupyter_reader

AUTHOR = "Jason Ross"
SITENAME = "Jason Ross's Blog"
# SITEURL = "https://jason-s-ross.github.io"

PATH = "content"

TIMEZONE = "PST8PDT"

DEFAULT_LANG = "en"

STATIC_PATHS = ["images", "css"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CUSTOM_CSS = "css/custom.css"

# Blogroll

# Social widget
SOCIAL = (("LinkedIn", "https://www.linkedin.com/in/jason-ross-80b962b2/"),)

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ["./plugins/", "./plugins/pelican-plugins/"]

PLUGINS = [pelican_jupyter_reader, "pelican-md-metayaml", "i18n_subsites", "render_math", "pelican-js"]

THEME = "./themes/my-bootstrap3"
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
PYGMENTS_STYLE = "tango"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKUP = ("ipynb",)


IPYNB_MARKUP_USE_FIRST_CELL = True
IGNORE_FILES = [".ipynb_checkpoints"]

NBCONVERT_CONFIG = Config()
NBCONVERT_CONFIG.HTMLExporter.exclude_input_prompt = True
NBCONVERT_CONFIG.HTMLExporter.exclude_output_prompt = True
