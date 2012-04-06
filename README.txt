OpenLyrics
===========

OpenLyrics is a free, open XML standard for Christian worship songs.
The goal of OpenLyrics is to provide an application-independant and
operating system-independant song format for interoperability between
applications.

For more details see:

http://openlyrics.info


Files
-----

openlyrics_0.8_schema.rng    RelaxNG XML Schema for a song
validate.py                  python script to validate xml using RelaxNG schema

chords.txt               examples of chord notation
themelist.txt            standardized song themes (from www.ccli.com)


Folders
-------

examples                          song examples
examples/example_simple.xml       minimalistic song example
examples/example_complex.xml      complex song example
examples/example_format.xml       example with formatting tags
examples/example_format_2.xml     more complex song with formatting tags

songs                             several song examples
tools                             additional tools


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
