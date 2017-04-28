OpenLyrics
===========

OpenLyrics is a free, open XML standard for Christian worship songs.  The
goal of OpenLyrics is to provide an application-independant and operating
system-independant song format for interoperability between applications.

For more details see:

  http://openlyrics.org


Files
-----

openlyrics-0.8.rng	- RelaxNG XML Schema for a song
validate.py		- Python script to validate XML using RelaxNG schema

chords.txt		- examples of chord notation
themelist.txt		- standardized song themes (from www.ccli.com)


Folders
-------

examples		- song examples
examples/simple.xml	-   minimalistic song example
examples/complex.xml	-   complex song example
examples/format.xml	-   example with formatting tags
examples/format2.xml	-   more complex song with formatting tags

songs			- several song examples
tools			- additional tools


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

validate.py - for validating xml documents with given RelaxNG schema.

To use this python script you need:

  * python >=2.4
  * python library lxml:
      http://pypi.python.org/pypi/lxml

Usage:
  python validate.py openlyrics-0.8.rng any_song.xml
