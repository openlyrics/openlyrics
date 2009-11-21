Open Lyrics
===========

For more details see:

http://sourceforge.net/apps/trac/changingsong/wiki/DevOpenLyrics


Files
-----

example_simple.xml       minimalist song example
example_complex.xml      fairly complex song example

openlyrics.0.3.xsd       old W3C XML Schema for songs
openlyrics.0.4.rng       RelaxNG XML Schema for songs
validate.py              python script to validate xml with rng (RelaxNG xml) file


Validation
----------

There is a python script  validate.py  for validating xml documents
with given xml schema.

To use this python script you need python library lxml:

http://pypi.python.org/pypi/lxml

Usage:

$ python validate.py  openlyrics.0.4.rng  any_song.xml

