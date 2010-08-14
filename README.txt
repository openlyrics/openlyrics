Open Lyrics
===========

OpenLyrics is a free, open XML standard for Christian worship songs.
The goal of OpenLyrics is to provide an application-independant and
operating system-independant song format for interoperability between
applications.

For more details see:

http://sourceforge.net/apps/trac/changingsong/wiki/DevOpenLyrics

or

http://openlyrics.info


Files
-----

example_simple.xml       minimalist song example
example_complex.xml      complex song example

openlyrics_schema.rng    RelaxNG XML Schema for a song
validate.py              python script to validate xml using RelaxNG schema

chords.txt               examples of chord notation
themelist.txt            standardized song themes (from www.ccli.com)


Folders
-------

songs                    several song examples
tools                    additional tools


Validation
===========


Online Validator
----------------

http://validator.nu/


Other RelaxNG Software
----------------------

http://relaxng.org/#software


Included Validator
------------------

validate.py  for validating xml documents
with given RelaxNG schema.

To use this python script you need:

- python >=2.4 
- python library lxml:

http://pypi.python.org/pypi/lxml

Usage:

$ python validate.py  openlyrics_schema.rng  any_song.xml
