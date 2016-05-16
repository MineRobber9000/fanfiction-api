# FanFiction.net API

Based on [jabagawee's fanfiction api][source].

[source]: https://github.com/jabagawee/FanFiction.Net-API

Had big problems with git, then ended up with me losing all history, until I find my other machine. 

## Features
* Gather story, chapter and user information
* Download stories to pdf, epub, mobi and txt
* Gather stories, favourites, and favourite authors of a user.
* Login Sessions
* Full command line functionality
  * Help file
  * Download multiple stories
  * Download from file(s)
  * Download to different formats
  * Specify output directory

## Bugs
* Printing to pdf, generates a weird format. Also doesn't work without X interface.

## Planned features
* Filter and search effectively

### Setup
To setup, clone or download the zip, then run `python setup.py install`, from the root directory.

Alternatively the package is available at [pypi](https://pypi.python.org/pypi/fanfiction-api).
To install run `pip install  fanfiction-api`

If authentication is going to be used, the program expects to see the file `$HOME/.ffconf.yaml`, which should contain your fanfiction.net details. If no config file is specified, and this one does not exist, it will be created.
```
  #$HOME/.ffconf.yaml
  username:
  email:
  password:
```

### Dependencies
* [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/)
* [PyYAML](http://pyyaml.org/wiki/PyYAMLDocumentation)
* [pdfkit](https://pypi.python.org/pypi/pdfkit)
* [ebooklib](https://pypi.python.org/pypi/EbookLib/0.15)
* [requests](https://pypi.python.org/pypi/requests)
* [KindleGen](http://www.amazon.com/gp/feature.html?docId=1000765211)
