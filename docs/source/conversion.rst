:tocdepth: 2

.. _conversion:

Converting OpenLyrics
=====================

Conversion From Other Formats
-----------------------------

Being able to convert songs from other formats to OpenLyrics is necessary to
speed up the adoption of the OpenLyrics format and for compatibility with
other applications which already support OpenLyrics.

OpenSong
^^^^^^^^

One of the tools bundled with the OpenLyrics source documents is a command
line tool to convert `OpenSong <http://www.opensong.org/>`_ song files to
OpenLyrics. The conversion script should work in most situations, but do
make sure that the conversion was successful before removing the old files.

Prerequisites
  Before using the script for conversion please ensure that the following
  is available in your system:

  * `Python <https://www.python.org/>`_ >= 2.5
  * `lxml <https://lxml.de/>`_

Usage
  To execute the script use the following command:

  .. code-block:: console

    python tools/opensong2openlyrics.py opensong_file openlyrics_file.xml

  Where ``opensong_file`` is the original song in OpenSong format and
  ``openlyrics_file.xml`` is the name of the song in OpenLyrics format.


Other Formats
^^^^^^^^^^^^^

`OpenLP <https://openlp.org/>`_ supports importing from a wide range of other formats.
So you can use it to convert your songs to the OpenLyrics format. See
`<https://manual.openlp.org/songs.html#song-importer>`_ for more information.

Converting OpenLyrics schema
----------------------------

Converting old schemas to version 0.8
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Theres is a bundled script to convert old 0.6 or 0.7 OpenLyrics files to 0.8 schema.

Prerequisites
  Before using the script for updating schema please ensure that the following
  is available in your system:

  * `Python <https://www.python.org/>`_ >= 2.5

Usage
  To execute the script use the following command:

  .. code-block:: console

    python tools/convert-schema.py old_olpenlyrics_file.xml new_olpenlyrics_file.xml

  Where ``old_olpenlyrics_file.xml`` is the original song with OpenLyrics 0.6 or 0.7 format and
  ``new_olpenlyrics_file.xml`` is the name of the song with OpenLyrics 0.8 schema.

Converting schema version 0.8 to 0.9
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is a new method to convert 0.8 schema to 0.9 using XSLT.

Prerequisites
  Use an `XSLT processor <https://en.wikipedia.org/wiki/XSLT#Processor_implementations>`_.
  We recommend libxslt's ``xsltproc``.

Usage
  Execute this command:

  .. code-block:: console

    xsltproc --output new_olpenlyrics_file.xml tools/convert-schema-0.8-to-0.9.xsl old_olpenlyrics_file.xml

  Where ``old_olpenlyrics_file.xml`` is the original song with OpenLyrics 0.8 format and
  ``new_olpenlyrics_file.xml`` is the name of the song with OpenLyrics 0.9 schema.

  The XSL is able to receive these options:

  * ``--param empty-chords``: Specifies the format for converting: ``"<chord/>text"`` or ``"<chord>text</chord>"``. Boolean: ``true()``, ``false()``. Dafault is ``true()``.
  * ``--stringparam chord-notation``: Specifies input chord notation. Used during chord processing. Possible values: ``english``, ``english-b``, ``german``, ``dutch``, ``hungarian``, ``neolatin``. Default is ``english``.
  * ``--stringparam xmllang``: Language for ``xml:lang``. Possible values: IETF BCP 47. Default is ``en``.
  * ``--param remove-optional``: Option to remove optional attributes in 0.9 (``createdIn``, ``modifiedIn`` and ``modifiedDate``). Boolean: ``true()``, ``false()``. Default is ``true()``.
  * ``--param update-meta``: Option to update ``modifiedIn`` and ``modifiedDate`` during convertion or not. Boolean: ``true()``, ``false()``. Default is ``false()``. 
  * ``--param add-pi``: Option to add CSS processing intruction: ``href="../stylesheets/openlyrics.css" type="text/css"``. Boolean: ``true()``, ``false()``. Default is ``false()``.

  A complex example:

  .. code-block:: bash

    xsltproc \
      --output new_olpenlyrics_file.xml \
      --param empty-chords "true()" \
      --stringparam chord-notation english \
      --stringparam xmllang en \
      --param remove-optional "true()" \
      --param update-meta "false()" \
      --param add-pi "false()" \
      tools/convert-schema-0.8-to-0.9.xsl \
      old_olpenlyrics_file.xml

Converting schema version 0.9 to 0.8
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If a program does not support the latest 0.9 schema, it may be necessary to convert the file back to 0.8.
There is another XSLT for this case.

Prerequisites
  Use an `XSLT processor <https://en.wikipedia.org/wiki/XSLT#Processor_implementations>`_.
  We recommend libxslt's ``xsltproc``.

Usage
  Execute this command:

  .. code-block:: console

    xsltproc --output openlyrics_0.8_file.xml tools/convert-schema-0.9-to-0.8.xsl openlyrics_0.9_file.xml

  Where ``openlyrics_0.9_file.xml`` is the original song with OpenLyrics 0.9 format and
  ``openlyrics_0.8_file.xml`` is the name of the song exported to OpenLyrics 0.8 schema.
