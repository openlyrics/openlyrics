:tocdepth: 2

.. _dataformat:

.. highlight:: xml

Data Format
===========

Basic Structure
---------------

.. image:: /images/xmlstructure.png


Features
--------

.. glossary::

    categories
        ``<theme>``

    CCLI support
        ``<ccliNo>``

    chords
        ``<chord name="D">``

    comments in lyrics
        ``<verse><lines><comment/></lines></verse>``

    date of song release
        ``<releaseDate>``

    format version
        ``<song version="0.6>``

    keywords for searching
        ``<keywords>``

    last modification time
        ``<song modifiedDate="">``

    lines of text
        ``<line>``

    multiple authors
        ``<authors>``

    multiple categories
        ``<themes>``
        
    multiple song titles
        ``<titles>``

    multiple user-defined items
        ``<comments>``

    music properties
        ``<transposition>``
        ``<tempo>``
        ``<key>``

    namespace
        ``<song xmlns="http://openlyrics.info/namespace/2009/song">``

    parts
        ``<lines part="men">``

    slides
        ``<verse>``

    song book
        ``<collection>``
        ``<trackNo>``

    song metadata
        ``<song version="">``
        ``<song createdIn="">``
        ``<song modifiedIn="">``
        ``<song modifiedDate="">``

    song translator
        ``<author type="translator" lang="cs">``

    song variant
        ``<variant>``

    song version
        ``<customVersion>``

    tagging verse type
        ``<verse name="v1">``

    translated lyrics
        ``<verse name="v1" xml:lang="en">``

    translated song title
        ``<title xml:lang="en">``

    transposition
        ``<transposition>``

    user-defined item
        ``<comment>``

    verse order
        ``<verseOrder>``


Required Data Items
-------------------

The song, containing only necessary data items, follows::

    <song xmlns="http://openlyrics.info/namespace/2009/song"
          version="0.6"
          createdIn="OpenLP 1.9.0"
          modifiedIn="ChangingSong 0.0.1"
          modifiedDate="2010-01-28T13:15:30+01:00">
      <properties>
        <titles>
          <title>Amazing Grace</title>
        </titles>
      </properties>
      <lyrics>
        <verse name="v1">
          <lines>
            <line>Amazing grace how sweet the sound</line>
          </lines>
        </verse>
      </lyrics>
    </song>

As you can see from the previous example, a minimalistic song should contain
only:

* metadata
* title
* verse with one line of text

**Elements with empty values aren't allowed. If a data item is not present
in the song, the tag, where the data would be put, should not be in xml.**


Metadata
--------

Metadata are **required** to be present in every song. They should ease debugging
of of applications using OpenLyrics.

Metadata are enclosed in tag ``<song>`` as its attributes::

    <song xmlns="http://openlyrics.info/namespace/2009/song"
          version="0.6"
          createdIn="OpenLP 1.9.0"
          modifiedIn="ChangingSong 0.0.1"
          modifiedDate="2010-01-28T13:15:30+01:00">

xmlns
    Defines a xml namespace. The value should be always
    ``http://openlyrics.info/namespace/2009/song``

version
    Version of the OpenLyrics format used by a song. This allows applications
    to notify users, if the application doesn't support newer versions of
    OpenLyrics.

createdIn
    String to identify the application where a song was created for the first
    time. This
    attribute should be set when a new song is created. It should not be
    changed with additional updates and modification to the song. Even when
    the song is edited in another application. Recommended content of this
    attribute is *application name* and *version* like ``OpenLP 1.9.0``.

modifiedIn
    String to identify the application where a song was edited for the last time.
    This attribute should be set with every modification. Recommended content
    of this attribute is *application name* and *version* like ``OpenLP 1.9.0``.

modifiedDate
    Date and time of last modification. This attribute should be set with every
    modification. The used format of date is `ISO 8601
    <http://en.wikipedia.org/wiki/ISO_8601>`_. It should be in the format
    ``YYYY-MM-DDThh:mm:ss±[hh]:[mm]``.


Encoding and Filenames
----------------------

Encoding
^^^^^^^^

I recommend using `UTF-8 <http://en.wikipedia.org/wiki/Utf8>`_ encoding for the
content of xml files in OpenLyrics format. *UTF-8* is well supported among
programming libraries.

Filenames
^^^^^^^^^

In regards to filenames, the recommendation is to use such a name which will
well identify the song just by looking at the filename. For the file could be
used a combination of fields ``<titles>``, ``<variant>`` and/or ``<authors>``.
Since OpenLyrics is a xml based format, filenames should contain the extension
``.xml``

Examples::

    Amazing Grace.xml
    Amazing Grace (old hymn).xml
    Amazing Grace (John Newton).xml

It would be nice, if songs containing non ASCII characters in its title, use
also nos ASCII characters in filenames. These days all major operating systems
should support localized characters in filenames. However, there are some
limitation in this approach. Not all archive formats handle localized filenames
well. For example, one of most used archive formats, `ZIP
<http://en.wikipedia.org/wiki/ZIP_(file_format)>`_. On the other hand, the format
`7-Zip <http://en.wikipedia.org/wiki/7zip>`_ handles it well.


Song Properties
---------------

Titles
^^^^^^

There could be more titles.

Authors
^^^^^^^

Copyright
^^^^^^^^^

CCLI Number
^^^^^^^^^^^

Release Date
^^^^^^^^^^^^

Transposition
^^^^^^^^^^^^^

Tempo
^^^^^

Key
^^^

Variant
^^^^^^^

Publisher
^^^^^^^^^

Custom Version
^^^^^^^^^^^^^^

Keywords
^^^^^^^^

Verse Order
^^^^^^^^^^^

Collection
^^^^^^^^^^

Track Number
^^^^^^^^^^^^

Themes
^^^^^^

Comments
^^^^^^^^



Song lyrics
-----------


Chords
------


Advanced Example
----------------

Here's an example of the XML::

    <?xml version="1.0" encoding="UTF-8"?>
    <song xmlns="http://openlyrics.info/namespace/2009/song"
          version="0.6"
          createdIn="OpenLP 1.9.0"
          modifiedIn="ChangingSong 0.0.1"
          <!-- date format: ISO 8601 -->
          modifiedDate="2009-12-22T21:24:30+02:00">
      <properties>
        <titles>
          <title>Amazing Grace</title>
        </titles>
        <authors>
          <author>John Newton</author>
        </authors>
        <copyright>Public Domain</copyright>
        <ccliNo>2762836</ccliNo>
        <releaseDate>1779</releaseDate>
        <tempo type="text">moderate</tempo>
        <key>D</key>
        <verseOrder>v1 v2 v3 v4 v5 v6</verseOrder>
        <themes>
          <theme>Assurance</theme>
          <theme>Grace</theme>
          <theme>Praise</theme>
          <theme>Salvation</theme>
        </themes>
      </properties>
      <lyrics>
        <verse name="v1">
          <lines>
            <line>Amazing grace how sweet the sound</line>
            <line>That saved a wretch like me.</line>
            <line>I once was lost, but now am found,</line>
            <line>Was blind but now I see.</line>
          </lines>
        </verse>
        <verse name="v2">
          <lines>
            <line>T'was grace that taught my heart to fear,</line>
            <line>And grace my fears;</line>
            <line>How precious did that grace appear</line>
            <line>The hour I first believed.</line>
          </lines>
        </verse>
        <verse name="v3">
          <lines>
            <line>Through many dangers, toil and snares,</line>
            <line>I have already come;</line>
            <line>'Tis grace has brought me safe thus far,</line>
            <line>And grace will lead me home.</line>
          </lines>
        </verse>
        <verse name="v4">
          <lines>
            <line>When we've been there ten thousand years</line>
            <line>Bright shining as the sun,</line>
            <line>We've no less days to sing God's praise</line>
            <line>Than when we've first begun.</line>
          </lines>
        </verse>
      </lyrics>
    </song>

