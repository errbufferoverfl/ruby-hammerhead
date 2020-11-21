<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/errbufferoverfl/ruby-hammerhead">
    <img src="imgs/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Ruby Hammerhead</h3>

  <p align="center">
A template repo for setting up your own Sphinx/ablog website using the Pydata Sphinx Theme.
    <br />
    <a href="https://github.com/errbufferoverfl/ruby-hammerhead"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://www.errbufferoverfl.me">View Demo</a>
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
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->

[![Product Name Screen Shot][product-screenshot]](https://errbufferoverfl.me)

A template repo for setting up your own Sphinx/ablog website using the Pydata Sphinx Theme.

This repo was made so people could easily get started using Sphinx and ablog to hot their own website, on GitHub pages,
Azure Storage, or a static hosting service of their choice. This repo is part of a series of blog posts I wrote on how to build your website and publish it using Azure DevOps and Azure Storage.

<!-- GETTING STARTED -->

To get a local copy up and running follow these simple steps.

This is an example of how to list things you need to use the software and how to install them.

1. Clone the repo
```sh
git clone https://github.com/errbufferoverfl/ruby-hammerhead.git
```
2. Install pip packages
```sh
pipenv install
```
3. Run the default installation
```sh
ablog build && ablog serve
```
4. Customise the `about.html` file located in `_templates` directory and replace the `logo.png` file with a picture you
like. If the name is different make sure to update this in the `about.html` file as well!

5. While developing your website, I recommend running `ablog clean` before building and serving to make sure you don't accidentally capture artifacts.
```sh
ablog clean && ablog build && ablog serve
```
6. Once you're happy with everything you can safely remove the following files and directories:
* imgs/
* README.md

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
[product-screenshot]: imgs/screenshot.png