<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/errbufferoverfl/ruby-hammerhead">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">Ruby Hammerhead</h3>
<p align="center">
A template repository for setting up your own Sphinx/ablog website using the Pydata Sphinx Theme.
    <br/>
    <a href="https://github.com/errbufferoverfl/ruby-hammerhead"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://errbufferoverfl.github.io/ruby-hammerhead/">View Demo</a>
    ·
    <a href="https://github.com/errbufferoverfl/ruby-hammerhead/issues">Report Bug</a>
    ·
    <a href="https://github.com/errbufferoverfl/ruby-hammerhead/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Making Changes](#making-changes)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
# About the Project
[![Product Name Screen Shot][product-screenshot]](https://errbufferoverfl.github.io/ruby-hammerhead/)

Getting yourself setup with Sphinx and ablog is pretty straight-forward using this repo!

By default this installation will get you setup with a reStructuredText and Markdown parser, an extension for creating panels, grids, dropdowns and more, an extension so users can easily copy and paste your code snippets, as well as extension to generate `OpenGraph metadata <https://ogp.me/>`_. For more information about each of these components' checkout the `References </references/>`_.

## Built With

* [Sphinx Documentation](https://www.sphinx-doc.org/en/master/index.html)
* [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
* [ablog Documentation](https://ablog.readthedocs.io/)
* [Pydata Documentation](https://pydata-sphinx-theme.readthedocs.io/en/latest/)
* [Sphinx Design Documentation](https://sphinx-design.readthedocs.io/)

<!-- GETTING STARTED -->
# Getting Started

The first thing you'll need to do is clone this repository locally using Git:

```shell
git clone https://github.com/errbufferoverfl/ruby-hammerhead.git
```

Next you'll need to install all the dependencies which are managed by Pipenv.

**Tip:** Ruby Hammerhead uses Python 3.9, if you are using multiple versions of Python, I'd recommend checking out [asdf](https://github.com/asdf-vm/asdf) an extendable version manager with support for Python, Ruby, Node.js, Elixir, Erlang & more.

```sh
pipenv install
```

Run the default build, which will create a website that looks exactly like [the demo site](https://errbufferoverfl.github.io/ruby-hammerhead/).

```sh
ablog build && ablog serve
```

**Warning:** Many of the files located in kitchen sink include broken references, citations and hyperlinks to demonstrate what things will look like if incorrectly configured. If you're running your build for the first time and haven't deleted this directory, you can expect the following errors:

```text
/ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:264: WARNING: Footnote [4] is not referenced.
/ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:270: WARNING: Footnote [11] is not referenced.
/ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:15: WARNING: Undefined substitution referenced: "problematic".
/ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:264: WARNING: Unknown target name: "5".
/ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:307: WARNING: Unknown target name: "body elements".
/ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:318: WARNING: Unknown target name: "hyperlink reference without a target".
/ruby-hammerhead/kitchen-sink/paragraph-level-markup.rst:278: WARNING: citation not found: nonexistent
```

<!-- MAKING CHANGES -->
## Making Changes

While developing your blog & making changes, I recommend running `ablog clean` before building and serving to make sure you don't accidentally capture artifacts.

```shell
ablog clean && ablog build && ablog serve
```

You can also run `ablog clean -D` which does a deep clean, removing cached environment and doctree files.

```shell
ablog clean -D && ablog build && ablog serve
```

<!-- ACKNOWLEDGEMENTS -->
# Acknowledgements

* [Chris Holdgraf](https://github.com/choldgraf)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/errbufferoverfl/ruby-hammerhead.svg?style=flat-square
[contributors-url]: https://github.com/errbufferoverfl/ruby-hammerhead/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/errbufferoverfl/ruby-hammerhead.svg?style=flat-square
[forks-url]: https://github.com/errbufferoverfl/ruby-hammerhead/network/members
[stars-shield]: https://img.shields.io/github/stars/errbufferoverfl/ruby-hammerhead.svg?style=flat-square
[stars-url]: https://github.com/errbufferoverfl/ruby-hammerhead/stargazers
[issues-shield]: https://img.shields.io/github/issues/errbufferoverfl/ruby-hammerhead.svg?style=flat-square
[issues-url]: https://github.com/errbufferoverfl/ruby-hammerhead/issues
[license-shield]: https://img.shields.io/github/license/errbufferoverfl/ruby-hammerhead.svg?style=flat-square
[license-url]: https://github.com/errbufferoverfl/ruby-hammerhead/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/errbufferoverfl
[product-screenshot]: images/screenshot.png