# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Sphinx configuration ---------------------------------------------------

# General information about the project.
project = "Ruby Hammerhead"
copyright = "2021, errbufferoverfl"
author = "errbufferoverfl"

# The full version, including alpha/beta/rc tags
release = '1.1.0'

html_baseurl = "https://errbufferoverfl.github.io/"
html_title = "Ruby Hammerhead"
timezone = "Melbourne/Australia"

# -- Ablog configuration ---------------------------------------------------
ablog_builder = "dirhtml"

# Base URL for the website, required for generating feeds.
# e.g. blog_baseurl = "http://example.com/"
blog_baseurl = "https://errbufferoverfl.github.io/"

# A path relative to the configuration directory for posts archive pages.
blog_path = "posts"

# The "title" for the posts, used in active pages.  Default is ``'Blog'``.
blog_title = "Ruby Hammerhead"

# The path that you store your content in, this will be used for the browsing path
# on your published website
# e.g. blog_post_pattern = "blog/*/*"
blog_post_pattern = "posts/*/*"

# -- Blog Post Related --------------------------------------------------------

# Format date for a post.
post_date_format = "%b %d, %Y"

# Number of paragraphs (default is ``1``) that will be displayed as an excerpt
# from the post. Setting this ``0`` will result in displaying no post excerpt
# in archive pages.  This option can be set on a per post basis using
post_auto_excerpt = 1

# Index of the image that will be displayed in the excerpt of the post.
# Default is ``0``, meaning no image.  Setting this to ``1`` will include
# the first image, when available, to the excerpt.  This option can be set
# on a per post basis using :rst:dir:`post` directive option ``image``.
post_auto_image = 0

# Number of seconds (default is ``5``) that a redirect page waits before
# refreshing the page to redirect to the post.
post_redirect_refresh = 1

# -- Blog Feed Options --------------------------------------------------------
# Turn feeds by setting :confval:`blog_baseurl` configuration variable.
# Choose to create feeds per author, location, tag, category, and year,
# default is ``False``.
blog_feed_archives = False

# Choose to display full text in posts feeds, default is ``False``.
blog_feed_fulltext = True

# -- Font-Awesome Options -----------------------------------------------------

# Sphinx_ theme already links to `Font Awesome`_.  Default: ``False``
fontawesome_included = True

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "ablog",
    "myst_parser",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinxext.opengraph",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["README.md", "Pipfile", "Pipfile.lock", "Makefile", "make.bat", "logo.gif", "conf.py"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "github_url": "https://github.com/errbufferoverfl/",
    "twitter_url": "https://twitter.com/errbufferoverfl",
    "search_bar_text": "Search...",
    "show_prev_next": False,
    "navbar_center": [],
    "footer_items": ["copyright", "sphinx-version", "last-updated"],
}

# HTML Sidebar configuration -- options available depend on ablog & the Sphinx theme you use.
# The following additional sidebars are provided by ablog:
# * postcard.html provides information regarding the current post
# * recentposts.html lists most recent five posts.
# * authors.html, languages.html, and locations.html sidebars link to author and location archive pages.
# * tagcloud.html provides a tag cloud for post tags
# * categories.html shows categories that you have created for posts
# You can create/include additional pages, by saving them in the _templates directory and including them
# below. See _templates/sidebar-nav.html for an example

html_sidebars = {
    "*": ["search-field.html", "sidebar-nav.html"],
    "posts": ["search-field.html", "sidebar-nav.html", "recentposts.html", "archives.html"],
    "posts/**": ["search-field.html", "sidebar-nav.html", "postcard.html"],
    "kitchen-sink/**": ["search-field.html", "sidebar-nav.html", "postcard.html"],
}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "favicon.ico"

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = ["robots.txt"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# A list of JavaScript filename. The entry must be a filename string or a tuple containing the filename string and the
# attributes dictionary. The filename must be relative to the html_static_path, or a full URI with scheme like
# https://example.org/script.js. The attributes is used for attributes of <script> tag. It defaults to an empty list.
html_js_files = ["js/rubyhammerhead.js"]

# A list of CSS files. The entry must be a filename string or a tuple containing the filename string and the attributes
# dictionary. The filename must be relative to the html_static_path, or a full URI with scheme like
# https://example.org/style.css. The attributes is used for attributes of <link> tag. It defaults to an empty list.
html_css_files = ["css/rubyhammerhead.css"]

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
html_search_language = 'en'

# If true (and html_copy_source is true as well), links to the reST sources will be added to the sidebar.
# The default is True.
html_show_sourcelink = True

# -- Opengraph configuration ---------------------------------------------------
ogp_site_url = "https://errbufferoverfl.github.io/"
ogp_image = "https://errbufferoverfl.github.io/_static/opengraph.png"
ogp_use_first_image = True
ogp_image_alt = ""
ogp_description_length = 200
ogp_type = "article"

# -- sphinx-sitemap configuration ---------------------------------------------------
sitemap_filename = "sitemap.xml"
sitemap_locales = ['en']
