OpenLyrics
===========

OpenLyrics is a free, open XML standard for Christian worship songs.  The
goal of OpenLyrics is to provide an application-independant and operating
system-independant song format for interoperability between applications.

For more details see:

  https://openlyrics.org


Files
-----

openlyrics-0.9.rng	- RelaxNG XML Schema for a song

chords.txt		- examples of chord notation
themelist.txt		- standardized song themes (from www.ccli.com)


Folders
-------

examples		- song examples
songs			- several song examples
stylesheets			- reference style implementation using purse CSS or XSLT/HTML/CSS
tools			- additional tools for validation and conversion


Validation
===========

Recommended method:
  xmllint --noout --relaxng openlyrics-0.9.rng any_song.xml

Included Validator
------------------

tools/validate.py - for validating xml documents with given RelaxNG schema.

To use this python script you need:

  * python >=3.6
  * python library lxml:
      https://pypi.org/project/lxml/

Usage:
  python3 tools/validate.py openlyrics-0.9.rng any_song.xml

Conversion from 0.8 to 0.9
==========================

To use this command you need libxslt's xsltproc.

Usage:
  xsltproc --output new_olpenlyrics_file.xml tools/convert-schema-0.8-to-0.9.xsl old_olpenlyrics_file.xml
