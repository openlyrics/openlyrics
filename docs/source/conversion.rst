:tocdepth: 2

.. _conversion:

Conversion From Other Formats
=============================

Being able to convert songs from other formats to OpenLyrics is necessary to
speed up the adoption of the OpenLyrics format and for compatibility with
other applications which already support OpenLyrics.


OpenSong
--------

One of the tools bundled with the OpenLyrics source documents is a command
line tool to convert `OpenSong <http://www.opensong.org/>`_ song files to
OpenLyrics. The conversion script should work in most situations, but do
make sure that the conversion was successful before removing the old files.

Prerequisites for conversion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before using the script for conversion please ensure that the following
is available in your system:

* `Python <http://www.python.org/>`_ >= 2.5
* `lxml <http://codespeak.net/lxml/>`_

Application
^^^^^^^^^^^

To execute the script use the following command::

    python ./opensong2openlyrics.py opensong_file  openlyrics_file.xml

Where ``opensong_file`` is the original song in OpenSong format and
``openlyrics_file.xml`` is the name of the song in OpenLyrics format.


Other Formats
-------------

`OpenLP <http://openlp.org/>`_ supports importing from a wide range of other formats.
So you can use it to convert your songs to the OpenLyrics format. See
`<http://manual.openlp.org/songs.html#song-importer>`_ for more information.
