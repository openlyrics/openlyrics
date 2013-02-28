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

Prerequisites
^^^^^^^^^^^^^

Before using the script for conversion please ensure that the following
is available in your system:

* `Python <http://www.python.org/>`_ >= 2.5
* `lxml <http://codespeak.net/lxml/>`_

Usage
^^^^^

To execute the script use the following command::

    python ./opensong2openlyrics.py opensong_file  openlyrics_file.xml

Where ``opensong_file`` is the original song in OpenSong format and
``openlyrics_file.xml`` is the name of the song in OpenLyrics format.


OpenLP
------

`OpenLP <http://openlp.org/>`_ already supports the OpenLyrics format via
both importing and exporting. Simply choose "OpenLyrics" from the list when
importing songs.


Other Formats
-------------

Conversion to other formats is not currently supported.
