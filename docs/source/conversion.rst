:tocdepth: 2

.. _conversion:

Conversion from other formats
=============================

Conversion of songs from other format is necessary for migration to 
OpenLyrics format and for compatibility with other applications.

OpenSong
--------

This section describes how to convert OpenSong songs into OpenLyrics format.
The conversion process should work in most situation. However, it is 
recommended to ensure that the conversion was successfull. For the conversion
will be used a script in command prompt.

Prerequisites
^^^^^^^^^^^^^

Before using the script for conversion please ensure that the following
is available in your system:

* `Python <http://www.python.org/>`_ >= 2.5
* `lxml <http://codespeak.net/lxml/>`_

Usage
^^^^^

To execute the scrit use the following command::

    python ./opensong2openlyrics.py opensong_file  openlyrics_file.xml

where ``opensong_file`` is the original song in OpenSong format and
``openlyrics_file.xml`` is the name of the song in OpenLyrics format.


Other formats
------------------

Conversion to Other formats is not currently supported. It will follow.

