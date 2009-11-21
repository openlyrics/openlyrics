Open Lyrics
===========

For more details see:

http://sourceforge.net/apps/trac/changingsong/wiki/DevOpenLyrics


Files
-----

example_simple.xml       minimalist song example
example_complex.xml      fairly complex song example

openlyrics.rng       RelaxNG XML Schema for songs
validate.py              python script to validate xml with rng (RelaxNG xml) file


Validation
----------

There is a python script  validate.py  for validating xml documents
with given xml schema.

To use this python script you need python library lxml:

http://pypi.python.org/pypi/lxml

Usage:

$ python validate.py  xml_schema.rng  xml_file.xml

$ python validate.py  openlyrics.rng  any_song.xml

