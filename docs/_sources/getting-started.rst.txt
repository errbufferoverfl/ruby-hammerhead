
Getting Started
==================

Getting yourself setup with Sphinx and ablog is pretty straight-forward using this repo!

By default this installation will get you setup with a reStructuredText and Markdown parser, an extension for creating panels, grids, dropdowns and more, an extension so users can easily copy and paste your code snippets, as well as extension to generate `OpenGraph metadata <https://ogp.me/>`_. For more information about each of these components' checkout the `References </references/>`_.

The first thing you'll need to do is clone this repository locally using Git:

.. code-block::

    git clone https://github.com/errbufferoverfl/ruby-hammerhead.git


Next you'll need to install all the dependencies which are managed by Pipenv:

.. tip::

    Ruby Hammerhead uses Python 3.9, if you are using multiple versions of Python, I'd recommend checking out `asdf <https://github.com/asdf-vm/asdf>`_ an extendable version manager with support for Python, Ruby, Node.js, Elixir, Erlang & more.

.. code-block::

    pipenv install

Run the default build, which will create a website that looks exactly like `the demo site <https://errbufferoverfl.github.io/ruby-hammerhead/>`_.

.. code-block::

    ablog build && ablog serve

.. warning::

    Many of the files located in kitchen sink include broken references, citations and hyperlinks to demonstrate what things will look like if incorrectly configured. If you're running your build for the first time and haven't deleted this directory, you can expect the following errors:

    .. code-block::

        /ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:264: WARNING: Footnote [4] is not referenced.
        /ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:270: WARNING: Footnote [11] is not referenced.
        /ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:15: WARNING: Undefined substitution referenced: "problematic".
        /ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:264: WARNING: Unknown target name: "5".
        /ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:307: WARNING: Unknown target name: "body elements".
        /ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:318: WARNING: Unknown target name: "hyperlink reference without a target".
        /ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:278: WARNING: citation not found: nonexistent

Making Changes
----------------

While developing your blog & making changes, I recommend running :code:`ablog clean` before building and serving to make sure you don't accidentally capture artifacts.

.. code-block::

    ablog clean && ablog build && ablog serve

You can also run :code:`ablog clean -D` which does a deep clean, removing cached environment and doctree files.

.. code-block::

    ablog clean -D && ablog build && ablog serve