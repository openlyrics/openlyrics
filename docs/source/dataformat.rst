:tocdepth: 3

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
        ``<verse name="v1" lang="en">``

    translated song title
        ``<title lang="en">``

    translated theme
        ``<theme lang="en">``

    transliterated lyrics
        ``<verse name="v1" lang="en" translit="he">``

    transliterated song title
        ``<title lang="en" translit="he">``

    transliterated theme
        ``<theme lang="en" translit="he">``

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

It is recommended using `UTF-8 <http://en.wikipedia.org/wiki/Utf8>`_ encoding for the
content of xml files in OpenLyrics format. *UTF-8* is well supported among
programming libraries and allows to have text in multiple languages in one
file.

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

Description of all possible elements enclosed in tag ``<properties>``. Elements
enclosed in this tag may be any arbitrary order. For example it  doesn't matter
if tag ``<titles>`` occurs before ``<authors>``::
    
    <titles><title>Amazing Grace</title></titles>
    <authors><author>John Newton</author></authors>

Or ``<titles>`` occurs after ``<authors>``::
    
    <authors><author>John Newton</author></authors>
    <titles><title>Amazing Grace</title></titles>

**An application implementing OpenLyrics should not depend on any order of
elements enclosed in the tag ``<properties>``.**


Titles
^^^^^^

Title is a **mandatory element**. Every song must contain at least one title::

    <titles><title>Amazing Grace</title></titles>

There could be more titles::

    <titles>
      <title>Amazing Grace</title>
      <title>Amazing</title>
    </titles>

You can define attribute ``lang=""``. It says what is the language of the
title. The value of this attribute should be in the format ``xx`` or ``xx-YY``
where ``xx`` is an `ISO-639 language code <http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_
and YY is an `country code <http://en.wikipedia.org/wiki/ISO_3166-1>`_. For
more details see `bcp47 <ftp://ftp.rfc-editor.org/in-notes/bcp/bcp47.txt>`_.

It comes handy when the song is translated from one
language to another and there is a need to know the titles in other languages
or the song contains lyrics in multiple languages::

    <titles>
      <title lang="en">Amazing Grace</title>
      <title lang="de">Staunenswerte Gnade</title>
      <title lang="pl">Cudowna Boża łaska</title>
    </titles>

Additionally, it is possible use attribute ``original="true"``. This attribute
expresses that a title is the title of the original song::

    <titles>
      <title lang="en" original="true">Amazing Grace</title>
      <title lang="pl">Cudowna Boża łaska</title>
    </titles>


Authors
^^^^^^^

Authors is an optional element. When this element is present in the song,
there should be at least one subelement ``<author>``::

    <authors><author>John Newton</author></authors>

There could be more authors::

    <authors>
      <author>John Newton</author>
      <author>Johannes Newton</author>
    </authors>

Three types of authors can be distinguished:

* *author of words*::

      <author type="words">John Newton</author>

* *author of music*::

      <author type="music">John Newton</author>

* *translator*::

      <author type="translation" lang="cs">Jan Ňůtn</author>
  
  The translator type must in addition contain the attribute ``lang=""``.
  Value of this attribute should be in the format ``xx`` or ``xx-YY``.
  ``xx`` means language code and ``YY`` means country code.


Copyright
^^^^^^^^^

This element should contain copyright information. In some countries it is
necessary to display copyright information during presentation. In this
situation this comes handy.

This element could look like::

    <copyright>public domain</copyright>

Or for example::

    <copyright>1998 Vineyard Songs</copyright>


CCLI Number
^^^^^^^^^^^

`CCLI <http://www.ccli.com/>`_
stands for *Christian Copyright Licensing International*. CCLI offers
copyright licensing of songs and other resource materials for use in Christian
worship. For registered churches CCLI offers songs and other resources
for download. At CCLI an ID is assigned to every song. This element
provides integration with CCLI.

CCLI number (id) must be a positive integer::

    <ccliNo>22025</ccliNo>


Release Date
^^^^^^^^^^^^

Release date is a date/time when the song was released or published.

It can be just year::

    <releaseDate>1779</releaseDate>

year-month::

    <releaseDate>1779-09</releaseDate>

year-month-day::

    <releaseDate>1779-12-30</releaseDate>

year-month-day and time::

    <releaseDate>1779-12-31T13:15</releaseDate>


Transposition
^^^^^^^^^^^^^

This element is used when there is a need to move the key or the pitch of
chords up or down. The value must be a positive or negative integer.

The negative integer moves the pitch down by a fixed number of semitones::

    <transposition>-3</transposition>

The positive integer moves the pitch up by a fixed number of semitones::

    <transposition>4</transposition>


Tempo
^^^^^

Tempo means how the song should be played. It could be expressed in beats
per minute (bpm) or as any text value.

Tempo in bpm must be a positive integer in the range 30-250::

    <tempo type="bpm">90</tempo>

Tempo expressed as text can contain any arbitrary text. For example
``Very Fast``, ``Fast``, ``Moderate``, ``Slow``, ``Very Slow``, etc.::

    <tempo type="text">Moderate</tempo>


Key
^^^

Key determines the musical scale of a song. The value could be ``A``, ``B``,
``C#``, ``D``, ``Eb``, ``F#``, ``Ab``, etc.

Example::

    <key>Eb</key>


Variant
^^^^^^^

Variant should be used in situation, where there are 2 songs with the same
title and it is needed to distinguish those songs.

For example there could be two songs with the title *Amazing grace*. One song
published many years ago and one song published by a well known band, say
for instance *Newsboys*.

For the old song it could be::

    <variant>old hymn</variant>

For the song from a well known band::

    <variant>Newsboys</variant>


Publisher
^^^^^^^^^

Name of the publisher of the song::

    <publisher>Sparrow Records</publisher>


Custom Version
^^^^^^^^^^^^^^

Many songs aren't written at once. When a new song is written, it usually
contains just a title and lyrics. In the future the song will be updated
and more data will be added. This could help users distinguish different
versions of the same song.

This element can contain any arbitrary text which could help the user to
distinguish various song versions.

It could contain for example a version number::

    <customVersion>0.99</customVersion>

or date::

    <customVersion>2010-02-04</customVersion>

or anything else::

    <customVersion>this is previous version</customVersion>


Keywords
^^^^^^^^

Keywords are used to get more precise results when searching for a song in the
song database.

For the song *Amazing Grace* it could be::

    <keywords>amazing grace, how sweet the sound, a wretch like me</keywords>


Verse Order
^^^^^^^^^^^

Determines the order of verses in the lyrics. In lyrics part every verse is
enclosed in tag ``<verse>``. Every verse should have a different one word name.

Every word in ``<verseOrder>`` refers to name of verse in the ``<lyrics>``.
Verse name can appear in ``<verseOrder>`` multiple times.

Verse names should be in lowercase.

For example when in the lyrics part are verses with names *v1*, *v2*, and *c*,
this element could be::

    <verseOrder>v1 c v2 c v1 c</verseOrder>


Songbooks
^^^^^^^^^

If a song comes from any collection or songbook, here should be noted the name
of the songbook/collection and number of a song in that songbook.
For songbook name is used attribute ``name=""`` and for number attribute
``entry=""``. Both attributes can contain any text::

    <songbooks>
      <songbook name="Name of a songbook or collection" entry="48"/>
    </songbooks>

The attribute ``name=""`` is mandatory but ``entry=""`` is not::

    <songbooks>
      <songbook name="Name of a songbook or collection"/>
    </songbooks>

The attribute ``name=""`` is mandatory but ``entry=""`` is not::

    <songbooks>
      <songbook name="This is a Songbook Name" entry="48"/>
      <songbook name="Name of a songbook without number"/>
      <songbook name="Name of a songbook" entry="84c"/>
    </songbooks>


Themes
^^^^^^

Themes are used to categorize songs. Having songs categorized can be useful
when choosing songs for a ceremony or for a particular topic.

There can be one or more themes::

    <themes><theme>Adoration</theme></themes>

As additional attributes could be an ``id=""`` and/or ``lang=""``::

    <themes>
      <theme>Adoration</theme>
      <theme id="1" lang="en-US">Grace</theme>
      <theme id="2" lang="en-US">Praise</theme> 
      <theme id="3" lang="en-US">Salvation</theme>
      <theme id="1" lang="pt-BR">Graça</theme>
      <theme id="2" lang="pt-BR">Adoração</theme>
      <theme id="3" lang="pt-BR">Salvação</theme>
    </themes>

The ``id`` attribute should be used when using a theme from a
`standardized CCLI list <http://www.ccli.com.au/owners/themes.cfm>`_.
The list can be found in the downloadable OpenLyrics archive in
file with name ``themelist.txt``. The value of ``id`` is the line number
of a particular theme in this file. Standardized themes with id should ease
assigning translated themes to songs in an application.

``lang`` defines a language of a theme.
Value of this attribute should be in the format ``xx`` or ``xx-YY``.
``xx`` means language code and ``YY`` means country code.


Comments
^^^^^^^^

This field is for other additional unspecified user data. There can be more
items. The value can be any text::

    <comments>
      <comment>One of the most popular songs in our congregation.</comment>
      <comment>We sing this song often.</comment>
    </comments>



Song lyrics
-----------

Description of the possible syntax enclosed in tag ``<lyrics>``. This tag
contain text of a song and other stuff related to it.

Lyrics part of OpenLyrics format will mostly contain elements like 
``<verse>``, ``<lines>`` or ``<line>``. A song should contain at least
**one verse with one line**.::

    <lyrics>
      <verse name="v1">
        <lines>
          <line>This is the first line of the text.</line>
        </lines>
      </verse>
    </lyrics>

In ``<line>`` should be enclosed all text for one line. An empty line is
expressed by ``<line/>`` or ``<line></line>``. More lines of text
can be in element ``<lines>``::

    <lines>
      <line>This is the first line of the text.</line>
      <line>This is the second line of the text.</line>
    </lines>

There can be more group of lines::

    <verse name="v1">
      <lines>
        <line>This is the first line of the text.</line>
      </lines>
      <lines>
        <line>This is the second line of the text.</line>
      </lines>
    </verse>

And of course it can contain more verses::

    <lyrics>
      <verse name="v1">
        <lines><line>First line of first verse.</line></lines>
      </verse>
      <verse name="v2">
        <lines><line>First line of second verse.</line></lines>
      </verse>
    </lyrics>

The tag ``<verse>`` is meant for all song parts, not only verses but
also for *chorus*, *bridge*, *pre-chorus*, etc.

It is recommended enclose in one element ``<verse>`` text for one slide.


Verse Name
^^^^^^^^^^

For every verse an attribute ``name`` with an unique value is required.
*There shouldn't be two or more verses the same name*. (The exception is
the situation when there are present more translations of a verse.)

The recommendation for standardized verse names follows:

======================= ============================================
Name                    Description
======================= ============================================
``v1, v2, v3, ...``     first verse, second verse, third verse, ...
``c``                   chorus
``c1, c2, ...``         more choruses
``p``                   pre-chorus
``p1, p2, ...``         more pre-choruses
``b``                   bridge
``b1, b2, ...``         more bridges
``e``                   ending
``e1, e2, ...``         more endings
``v1a, v1b, v1c, ...``  this schema is for splitting verse to more parts
                        (e.g. for splitting verse over more slides)
``ca, cb, ...``         splitting chorus to more parts
``c1a, c1b, ...``       splitting chorus to more parts
``pa, pb, ...``         splitting pre-chorus to more parts
``p1a, p1b, ...``       splitting pre-chorus to more parts
``ba, bb, bc, ...``     splitting bridge to more parts
``b1a, b1b, b1c, ...``  splitting bridge to more parts
``ea, eb, ec, ...``     splitting ending to more parts
``e1a, e1b, e1c, ...``  splitting ending to more parts
======================= ============================================

In recommended naming schema are names in **lowercase**.
The value of the ``name`` attribute could be any *one word*.

Example of a song containing two verses (*v1, v2*), a chorus (*c*),
bridge (*b*) and ending (*e*). Second verse is splited into more slides::

    <lyrics>
      <verse name="v1">
        ...
      </verse>
      <verse name="v2a">
        ...
      </verse>
      <verse name="v2b">
        ...
      </verse>
      <verse name="c">
        ...
      </verse>
      <verse name="b">
        ...
      </verse>
      <verse name="e">
        ...
      </verse>
    </lyrics>

Chords
^^^^^^

OpenLyrics format allows storing chords. Having chords can be handy in
some situations. For example when printing leadsheets or when preseting
a song during band training.

The element containing a chord name looks like::

    <chord name="D7"/>

Elements ``<chord>`` are mixed with the text of a song. This element should be
placed immediately before the letters where it should be played::

    <lyrics>
      <verse name="v1">
        <lines>
          <line><chord name="D7"/>Amazing grace how 
                <chord name="E"/>sweet the sound</line>
          <line>That saved <chord name="A"/>a wretch
                <chord name="F#"/>like me.</line>
        </lines>
      </verse>
    </lyrics>

At the moment there is no a fixed notation for chords. But if you would like
to see some examples how chords can be written, see 
:ref:`chord examples <chordlist>`.

Multiple Languages (Lyrics Translations)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lyrics translation can be useful for example in situation when the worship band
is singing a song in a foreing language and wants to display translation
of the text for others to understand.

Translations are at the verse level. They can be added by translating a text of
a ``<verse>`` and by adding attribute ``lang=""`` to ``<verse>``.
The value of this attribute should be in the format ``xx`` or ``xx-YY``
where ``xx`` is an `ISO-639 language code <http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_
and YY is an `country code <http://en.wikipedia.org/wiki/ISO_3166-1>`_. For
more details see `bcp47 <ftp://ftp.rfc-editor.org/in-notes/bcp/bcp47.txt>`_.

More translations of a verse should have the same value of the attribute
``name=""`` but different values of ``lang=""``.

Example of a song containg English and German translation for the first verse::

    <lyrics>
      <verse name="v1" lang="en">
        <lines><line>This text is in English.</line></lines>
      </verse>
      <verse name="v1" lang="de">
        <lines><line>Dieses Text ist auf Deutsch.</line></lines>
      </verse>
    </lyrics>

Because translations are defined at the verse level, there can be also
situation, that some verses have translations and some do not.


Transliteration
^^^^^^^^^^^^^^^

`Transliteration <http://en.wikipedia.org/wiki/Transliteration>`_ comes handy in
situation when singing for instance a Hebrew song but the congregation is not
able read Hebrew aplhabet.

Transliteration allows to distinguish in one song:

* text written in original alphabet (e.g. Hebrew)
* pronunciation of original aplhabet mapped to requested alphabet (e.g. Hebrew
  pronunciation written in English)
* translation of the song to requested language (e.g. English translation)

Transliteration can be defined by adding attribute ``translit=""`` to
``<title>``, ``<theme>`` or ``<verse>``.
The value of this attribute should be in the format ``xx`` or ``xx-YY``
where ``xx`` is an `ISO-639 language code <http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_
and YY is an `country code <http://en.wikipedia.org/wiki/ISO_3166-1>`_. For
more details see `bcp47 <ftp://ftp.rfc-editor.org/in-notes/bcp/bcp47.txt>`_.

The attribute ``translit=""`` must be used in conjunction with attribute
``lang=""``. This is because one writting system can be transliterated
to different languages differently. For example Hebrew is transliterated
differently to English and French.

In the following example the attribute ``lang=""`` means the language of
original alphabet (Hebrew) and ``translit=""`` means the language to what
the song was transliterated (English)::

    <verse name="v1" lang="he" translit="en">
    ...
    </verse>

Example of lyrics containing original text written in Hebrew 
``<verse name="v1" lang="he">``, transliterated to English
``<verse name="v1" lang="he" translit="en">`` and translated
to English ``<verse name="v1" lang="en">``::

    <lyrics>
      <verse name="v1" lang="he">
        <lines><line>הבה נגילה</line></lines>
      </verse>
      <verse name="v1" lang="he" translit="en">
        <lines><line>Hava nagila</line></lines>
      </verse>
      <verse name="v1" lang="en">
        <lines><line>Let's rejoice</line></lines>
      </verse>
    </lyrics>


Verse Parts (Groups of Lines)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the term *verse parts* or *group of lines* could be misleading but
It was hard to find any other meaningful name for this feature.

This feature means the ability marking words for different groups of people.
For example some words should be sung by men and some by women.

This feature is the reason why there is the tag ``<lines>``. This ability is
implemented by adding attribute ``part=""`` to the element ``<lines>``.
The value of this attribute is any arbitrary text.

Example of lyrics containing one verse with some words for men and soe word
for women::

    <lyrics>
      <verse name="v1">
        <lines part="men">
          <line>First line of words sung by men.</line>
          <line>Second line of words sung by men.</line>
        </lines>
        <lines part="women">
          <line>First line of words sung by women.</line>
          <line>Second line of words sung by women.</line>
        </lines>
      </verse>
    </lyrics>

Comments in Lyrics
^^^^^^^^^^^^^^^^^^

OpenLyrics format supports adding comments. Comments must be put before
a line with text. Comments could be useful for printing leadsheets.
They can contain various information. For example it could contain information
how to play or sing any particular text.

Example::

    <lyrics>
      <verse name="v1">
        <lines>
          <comment>Singing loudly.</comment>
          <line>Text of verse.</line>
          <comment>Singing quietly.</comment>
          <line>Text of verse.</line>
        </lines>
      </verse>
      <verse name="c">
        <lines>
          <comment>Singing loudly.</comment>
          <line>Line content.</line>
          <line>Line content.</line>
        </lines>
      </verse>
    </lyrics>


Advanced Example
----------------

More song examples can be found in folder ''songs'' distributed with the
OpenLyrics ZIP archive.

Here's an example of the XML::

    <?xml version="1.0" encoding="UTF-8"?>
    <song xmlns="http://openlyrics.info/namespace/2009/song"
          version="0.7"
          createdIn="OpenLP 2.0"
          modifiedIn="ChangingSong 0.0.2"
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

