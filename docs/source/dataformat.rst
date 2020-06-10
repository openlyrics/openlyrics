:tocdepth: 3

.. _dataformat:

.. highlight:: xml

Data Format
===========


Basic Structure
---------------

.. image:: /images/xmlstructure.png
   :width: 70%


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
        ``<released>``

    OpenLyrics version
        ``<song version="0.8>``

    keywords for searching
        ``<keywords>``

    last modification time
        ``<song modifiedDate="">``

    lines of text
        ``<lines>``

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

    multiple song books
        ``<songbooks>``

    song metadata
        ``<song xml:lang="">``
        ``<song version="">``
        ``<song createdIn="">``
        ``<song modifiedIn="">``
        ``<song modifiedDate="">``

    song translator
        ``<author type="translator" lang="cs">``

    song variant
        ``<variant>``

    song version
        ``<version>``

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

Here is an example of a song containing only the required XML tags::

    <song xmlns="http://openlyrics.info/namespace/2009/song"
          version="0.9">
      <properties>
        <titles>
          <title>Amazing Grace</title>
        </titles>
      </properties>
      <lyrics>
        <verse name="v1">
          <lines>
            Amazing grace how sweet the sound
          </lines>
        </verse>
      </lyrics>
    </song>

As you can see from this example, a minimal song should only contain:

* metadata
* title
* verse with one line of text

**Tags with empty values are not allowed. If a tag is empty, it should be
excluded from the XML.**


Metadata
--------

Metadata **should** be present in every song. This should ease debugging
applications using OpenLyrics.

Metadata is enclosed in the ``<song>`` tag as attributes::

    <song xmlns="http://openlyrics.info/namespace/2009/song"
          xml:lang="en"
          version="0.8"
          createdIn="OpenLP 1.9.0"
          modifiedIn="ChangingSong 0.0.1"
          modifiedDate="2010-01-28T13:15:30+01:00">

``xmlns``
    Defines an XML namespace. The value should be always
    ``http://openlyrics.info/namespace/2009/song``

``xml:lang``
    Language of the OpenLyrics document. It defines the default language for titles,
    keywords, themes, comments, lyrics, etc. The format of this attribute should be
    or ``xx-YY``, where ``xx`` is a language code from the
    `ISO-639 <http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_ standard, and
    ``YY`` is a `country code <http://en.wikipedia.org/wiki/ISO_3166-1>`_. For more
    details see `BCP 47 <http://www.rfc-editor.org/rfc/bcp/bcp47.txt>`_.
    Default language can be overwriten for a specified element, see:
    ``<title lang="">``, ``<theme lang="">``, ``<verse lang="">``.
    This element is optional. If not specified, it means document language is ``"en"``.

``version``
    Version of the OpenLyrics format used by a song. This gives applications the
    ability to notify users if the application doesn't support newer versions of
    OpenLyrics. This element is **required**.

``createdIn``
    String to identify the application where a song was created for the
    first time. This attribute should be set when a new song is
    created. It should not be changed with additional updates and
    modification to the song. Even when the song is edited in another
    application. Recommended content of this attribute is *application
    name* and *version* like ``OpenLP 1.9.0``. This element is optional.

``modifiedIn``
    String to identify the application where a song was edited for the
    last time. This attribute should be set with every modification.
    Recommended content of this attribute is *application name* and
    *version* like ``OpenLP 1.9.0``. This element is optional.

``modifiedDate``
    Date and time of the last modification. This attribute should be set with
    every modification of the song. This attribute should use the
    `ISO 8601 <http://en.wikipedia.org/wiki/ISO_8601>`_ date format, which looks
    like this::

        YYYY-MM-DDThh:mm:ss±[hh]:[mm]

    For example, the 28th of January, 2010, at 30 seconds past 1:15pm in the UTC+1
    timezone would look like this::

        2010-01-28T13:15:30+01:00

    This element is optional.


Encoding and Filenames
----------------------

Encoding
^^^^^^^^

The recommended encoding for OpenLyrics files is the ubiquitous
`UTF-8 <http://en.wikipedia.org/wiki/Utf8>`_ encoding. *UTF-8* is supported by
most programming languages, and using this encoding means that OpenLyrics files
can have more than one language per file.

File Names
^^^^^^^^^^

When creating and saving OpenLyrics files, it is recommended that the song
contained in the file should be easily identifiable by looking at the file name. A
well-named file would probably use a combination of one or more of the following
fields:

* ``<titles>``
* ``<variant>``
* ``<authors>``

In addition to this, the file extension should be ``.xml`` since OpenLyrics is an
XML format.

File name examples::

    Amazing Grace.xml
    Amazing Grace (old hymn).xml
    Amazing Grace (John Newton).xml

Additionally, file names should not contain characters which could cause issues on
any operating system. Most modern operating systems support a wide range of
characters in file names, but some of the common characters to avoid are ``/``,
``\`` and ``:``.

Compressed file formats should also be taken into consideration when naming files,
as some compression formats (most notably
`ZIP <http://en.wikipedia.org/wiki/ZIP_(file_format)>`_ files) cannot handle all
valid file name characters. It is recommended that files should be compressed
using the `7-Zip <http://en.wikipedia.org/wiki/7zip>`_ format, as this format is
known to handle non-ASCII file names well.


Song Properties
---------------

OpenLyrics songs are essentially divided into two sections. The first section,
denoted by the ``<properties>`` tag, contains the various properties of the song,
and the second section, denoted by the ``<lyrics>`` tag, contains the lyrics.

The ``<properties>`` tag groups various song property tags together. These tags
include the ``<titles>`` and ``<authors>`` tags. The order of tags within the
``<properties>`` tag is arbitrary. For example, it doesn't matter if the
``<titles>`` tag occurs before the ``<authors>`` tag::

    <titles><title>Amazing Grace</title></titles>
    <authors><author>John Newton</author></authors>

Or if the ``<titles>`` tag occurs after the ``<authors>`` tag::

    <authors><author>John Newton</author></authors>
    <titles><title>Amazing Grace</title></titles>

**An application implementing the OpenLyrics format should not depend on any order
of tags enclosed in the ``<properties>`` tag.**

Titles
^^^^^^

The ``<titles>`` tag is **mandatory**, and every song must contain at least one
title::

    <titles><title>Amazing Grace</title></titles>

However, there could be any number of titles::

    <titles>
      <title>Amazing Grace</title>
      <title>Amazing</title>
    </titles>

An optional ``lang`` attribute can be added to the ``<title>`` tag. This attribute
defines the language of the title. The format of this attribute should be ``xx``
or ``xx-YY``, where ``xx`` is a language code from the
`ISO-639 <http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_ standard, and
``YY`` is a `country code <http://en.wikipedia.org/wiki/ISO_3166-1>`_. For more
details see `BCP 47 <http://www.rfc-editor.org/rfc/bcp/bcp47.txt>`_.

The ``lang`` attribute comes in handy when the song is translated from one
language to another and it is necessary to know the translated version of the
title, or when a song contains lyrics in multiple languages::

    <titles>
      <title lang="en">Amazing Grace</title>
      <title lang="de">Staunenswerte Gnade</title>
      <title lang="pl">Cudowna Boża łaska</title>
    </titles>

An additional ``original`` attribute, containing a boolean value of either
``true`` or ``false``, can be used to indicate that the associated title is the
original title of the song::

    <titles>
      <title lang="en" original="true">Amazing Grace</title>
      <title lang="pl">Cudowna Boża łaska</title>
    </titles>


Authors
^^^^^^^

The ``<authors>`` tag is optional. When this tag is present in the song, there
should be at least one ``<author>`` sub-tag::

    <authors><author>John Newton</author></authors>

There can, of course, be more authors::

    <authors>
      <author>John Newton</author>
      <author>Johannes Newton</author>
    </authors>

Three different types of authors can be defined:

* *author of words*::

      <author type="words">John Newton</author>

* *author of music*::

      <author type="music">John Newton</author>

* *translator*::

      <author type="translation" lang="cs">Jan Ňůtn</author>

  When the ``type`` is ``translation``, a ``lang`` attribute is mandatory. The
  value of this attribute should be in the same format as the ``lang`` attribute
  of the ``<title>`` tag.


Copyright
^^^^^^^^^

The ``<copyright>`` tag contains the copyright information of the song. In some
countries it is a legal requirement to display copyright information during the
presentation of songs. The ``<copyright>`` tag has no specific format, though it
is recommended that the value contains at least the year and copyright holder of
the song.

For example::

    <copyright>Public Domain</copyright>

Or::

    <copyright>1998 Vineyard Songs</copyright>


CCLI Number
^^^^^^^^^^^

`CCLI <http://www.ccli.com/>`_ stands for *Christian Copyright Licensing
International*. CCLI is an organisation that offers copyright licensing of songs
and other resource materials to churches and Christian organisations for use in
Christian worship. For registered churches, CCLI offers songs and other resources
for download. A CCLI ID is assigned to every song. This tag provides integration
with CCLI.

The CCLI number (ID) must be a positive integer::

    <ccliNo>22025</ccliNo>


Release Date
^^^^^^^^^^^^

The ``<released>`` tag tracks the date when a song was released or published.

It can be just a year::

    <released>1779</released>

Or a year and a month::

    <released>1779-09</released>

Or a year, month and day::

    <released>1779-12-30</released>

Or even a year, month, day and time::

    <released>1779-12-31T13:15</released>


Transposition
^^^^^^^^^^^^^

The ``<transposition>`` tag is used when it is necessary to move the key or the
pitch of chords up or down. The value must be a positive or negative integer.

A negative value moves the pitch down by a fixed number of semitones::

    <transposition>-3</transposition>

A positive value moves the pitch up by a fixed number of semitones::

    <transposition>4</transposition>


Tempo
^^^^^

The tempo of a song defines the speed at which a song is to be played. It could be
expressed in beats per minute (BPM) or as any text value. The ``<tempo>`` tag has
a ``type`` attribute which defines whether the tempo is measured in BPM or by a
phrase. The ``type`` attribute therefore can be one of two possible values,
``bpm`` and ``text``.

If the tempo is measured in BPM, it must be a positive integer in the range
of 30-250::

    <tempo type="bpm">90</tempo>

If the tempo is expressed as a phrase, it can contain any arbitrary text. For
example ``Very Fast``, ``Fast``, ``Moderate``, ``Slow``, ``Very Slow``, etc.::

    <tempo type="text">Moderate</tempo>


Key
^^^

The key determines the musical scale of a song. For example, ``A``, ``B``, ``C#``,
``D``, ``Eb``, ``F#`` or ``Ab``.

Example::

    <key>Eb</key>


Variant
^^^^^^^

The ``<variant>`` tag is used to differentiate between songs which are identical,
but may be performed or sung differently.

For example, there could be two songs with the title *Amazing Grace*. One song was
published many years ago and one song was published by a well known band, say for
instance the *Newsboys*.

For the old song the ``<variant>`` could be::

    <variant>Original Hymn</variant>

While the ``<variant>`` by the well known band would list their name::

    <variant>Newsboys</variant>


Publisher
^^^^^^^^^

The ``<publisher>`` tag contains the name of the publisher of the song::

    <publisher>Sparrow Records</publisher>


Custom Version
^^^^^^^^^^^^^^

No song is ever created once, never to be edited again. Songs are updated over
time, sometimes to add additional verses, sometimes to fix spelling or grammatical
errors. OpenLyrics tries to add in some rudimentary version control in the form of
a ``<version>`` tag, which could be updated whenever a song changes
significantly.

This tag can contain any arbitrary text which could help the user to distinguish
between various versions of a song.

For example, it could contain a version number::

    <version>0.99</version>

Or a date::

    <version>2010-02-04</version>

Or almost anything else::

    <version>this is previous version</version>


Keywords
^^^^^^^^

Keywords are used for more precise results when searching for a song in a song
database. These keywords are stored in the ``<keywords>`` tag.

For example, in *Amazing Grace*::

    <keywords>amazing grace, how sweet the sound, God's grace</keywords>


Verse Order
^^^^^^^^^^^

The verse order of a song defines the order in which the verses are typically sung
or performed. The verse order is denoted by the ``<verseOrder>`` tag.

The verse order is a space-separated string of verse names (which are defined in
the ``<lyrics>`` section of the file). Verse names can appear multiple times, and
should be lowercase. See the ``<verse>`` section for more information on verse
names.

For example::

    <verseOrder>v1 c v2 c v1 c</verseOrder>


Song Books
^^^^^^^^^^

Most songs come from some sort of collection of songs, be it a book or a folder of
some sort. It may be useful to track where the song comes from, and for this can
be done through the ``<songbook>`` tag.

Because songs are often found in more than one song book, multiple ``<songbook>``
tags can be defined. For this reason, ``<songbook>`` tags are wrapped in a
``<songbooks>`` tag.

Each ``<songbook>`` tag contains two attributes:

    ``name``
        The name of a song book is stored in the ``name`` attribute.
    ``entry``
        As songs are normally indexed in song books, the index of the song is
        stored in the ``entry`` attribute.

Both attributes can contain any text::

    <songbooks>
      <songbook name="Name of a songbook or collection" entry="48"/>
    </songbooks>

The ``name`` attribute is mandatory but ``entry`` is optional::

    <songbooks>
      <songbook name="Name of a songbook or collection"/>
    </songbooks>


Themes
^^^^^^

Themes are used to categorize songs. Having songs categorized can be useful when
choosing songs for a ceremony or for a particular sermon topic. A theme is defined
by a ``<theme>`` tag. A song can have multiple themes, so any ``<theme>`` tags
are wrapped in a ``<themes>`` tag::

    <themes><theme>Adoration</theme></themes>

A ``<theme>`` tag has an optional ``lang`` attribute, which defines the language
of the theme. The value of this attribute should be in the same format as the
``lang`` attribute of the ``<title>`` tag.

Some examples::

    <themes>
      <theme>Adoration</theme>
      <theme lang="en-US">Grace</theme>
      <theme lang="pt-BR">Graça</theme>
      <theme lang="en-US">Praise</theme>
      <theme lang="pt-BR">Adoração</theme>
      <theme lang="en-US">Salvation</theme>
      <theme lang="pt-BR">Salvação</theme>
    </themes>

It is highly recommended that themes should come from the list of themes on the
CCLI web site: `<http://www.ccli.co.za/owners/themes.cfm>`_


Comments
^^^^^^^^

The ``<comment>`` tag is used to store any additional, unspecified user data in
a free-form text field. A song can contain multiple ``<comment>`` tags, and thus
they are wrapped in a ``<comments>`` tag.

An example::

    <comments>
      <comment>One of the most popular songs in our congregation.</comment>
      <comment>We sing this song often.</comment>
    </comments>


Song Lyrics
-----------

The second section of an OpenLyrics song is defined by the ``<lyrics>`` tag. This
tag contains words of a song and other data related to it.

The ``<lyrics>`` tag contains one or more ``<verse>`` tags. Each ``<verse>`` tag
defines a verse or stanza of a song, and contains a single mandatory attribute,
``name``. Each verse can contain one or more ``<lines>`` tags, which holds a
logical grouping of words.

A song should contain at least **one verse**::

    <lyrics>
      <verse name="v1">
        <lines>
          This is the first line of the text.
        </lines>
      </verse>
    </lyrics>

There can be multiple ``<lines>`` tags::

    <verse name="v1">
      <lines>
        This is the first line of the text.
      </lines>
      <lines>
        This is the second line of the text.
      </lines>
    </verse>

And of course, a song can contain multiple verses::

    <lyrics>
      <verse name="v1">
        <lines>First line of first verse.</lines>
      </verse>
      <verse name="v2">
        <lines>First line of second verse.</lines>
      </verse>
    </lyrics>

The ``<verse>`` tag is not only used for verses, but also choruses, bridges, etc.


Line Breaks
^^^^^^^^^^^

Within a ``<lines>`` tag, a ``<br/>`` tag is used to define breaks between lines.

For example::

    <lines>
      Amazing grace, how sweet the sound<br/>
      That saved a wretch like me!</br>
      I once was lost, but now am found,<br/>
      Was blind but now I see.<br/>
    </lines>


Split Verse
^^^^^^^^^^^

Use the ``break="optional"`` attribute on the ``<lines>`` tag to tell the application
about an optional split for a long verse.
The application then can decide to break the verse in two slides if it
doesn't fit on one screen::

    <verse name="v1">
      <lines break="optional">
        Amazing grace, how sweet the sound<br/>
        That saved a wretch like me!</br>
      </lines>
      <lines>
        I once was lost, but now am found,<br/>
        Was blind but now I see.<br/>
      </lines>
    </verse>

This tells the application that it can split the verse after the
line "That saved a wretch like me!"

Verse Name
^^^^^^^^^^

As previously mentioned, every ``<verse>`` tag has a mandatory ``name`` attribute.
Verse names should be unique, written in **lower case**, a single word, and should
follow the naming convention as laid out in the table below:

======================= ==========================================================
Name                    Description
======================= ==========================================================
``v1, v2, v3, ...``     first verse, second verse, third verse, ...
``v1a, v1b, v1c, ...``  first verse part 1, first verse part two, ...
``c``                   chorus
``c1, c2, ...``         first chorus, second chorus, ...
``c1a, c1b, ...``       first chorus part 1, first chorus part 2, ...
``p``                   pre-chorus
``p1, p2, ...``         first pre-chorus, second pre-chorus, ...
``p1a, p1b, ...``       first pre-chorus part 1, first pre-chorus part 2, ...
``b``                   bridge
``b1, b2, ...``         first bridge, second bridge, ...
``b1a, b1b, b1c, ...``  first bridge part 1, first bridge part 2, ...
``e``                   ending
``e1, e2, ...``         first ending, second ending, ...
``e1a, e1b, e1c, ...``  first ending part 1, first ending part 2, ...
======================= ==========================================================

According to the table above, a song containing two verses (*v1, v2*), a chorus
(*c*), a bridge (*b*) and an ending (*e*) would look like this::

    <lyrics>
      <verse name="v1">
        ...
      </verse>
      <verse name="v2">
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

The OpenLyrics format also provides the ability to include chords in the lyrics of
songs. The tag containing a chord name looks like this::

    <chord name="D7"/>

The ``<chord>`` tags are mixed in with the lyrics of a song. This tag should be
placed immediately before the letters where it should be played::

    <lyrics>
      <verse name="v1">
        <lines>
          <chord name="D7"/>Amazing grace how <chord name="E"/>sweet the sound<br/>
          That saved <chord name="A"/>a wretch <chord name="F#"/>like me.
        </lines>
      </verse>
    </lyrics>

Chords should be written according to this :ref:`list of chords <chordlist>`.

Multiple Languages (Lyrics Translations)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The translation of lyrics can be useful for situations where a song is written in
a language that the majority of the congregation does not know. A translation of
the song can be displayed in a language common to most of the congregation.

OpenLyrics supports the translation of verses by adding a ``lang`` attribute to
``<verse>`` tags. To add translations to a particular verse, the ``<verse>`` tag
should be repeated, with the same ``name`` attribute value as the verse to be
translated, and with ``lang`` attribute set to the language of the translation.
The value of the ``lang`` attribute should be in the same format as the ``lang``
attribute used in other tags.

Multiple translations of a verse should have the same value of the ``name``
attribute but different values of ``lang``.

For example, this song is written in English and has a German translation for the
first verse::

    <lyrics>
      <verse name="v1" lang="en">
        <lines>This text is in English.</lines>
      </verse>
      <verse name="v1" lang="de">
        <lines>Dieser Text ist auf Deutsch.</lines>
      </verse>
    </lyrics>


Transliteration
^^^^^^^^^^^^^^^

`Transliteration <http://en.wikipedia.org/wiki/Transliteration>`_ is the process
whereby words from one writing system are converted to another writing system. For
instance there might be a Hebrew song, written in the Hebrew alphabet, which is
then rewritten into the English alphabet (but not into English) so that it is
easier for the congregation to pronounce the Hebrew words.

Transliteration can be defined by adding a ``translit`` attribute to the
``<title>``, ``<theme>`` or ``<verse>`` tags. The value of this attribute should
be the same format as the ``lang`` tags.

The ``translit`` attribute must be used in conjunction with the ``lang``
attribute. This is because one writing system can be transliterated into different
languages in different ways. For example, Hebrew is transliterated into English a
different way than when it is transliterated into French.

In the following example the ``lang`` attribute defines the language of original
alphabet (Hebrew) and ``translit`` defines the language into which the song was
transliterated (English)::

    <verse name="v1" lang="he" translit="en">
    ...
    </verse>

As an example, here is a song which was originally written in Hebrew, then
transliterated to the English alphabet, and then finally translated into English::

    <lyrics>
      <verse name="v1" lang="he">
        <lines>הבה נגילה</lines>
      </verse>
      <verse name="v1" lang="he" translit="en">
        <lines>Hava nagila</lines>
      </verse>
      <verse name="v1" lang="en">
        <lines>Let's rejoice</lines>
      </verse>
    </lyrics>


Verse Parts (Groups of Lines)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In some songs, certain lines or sections of the song may be sung by a particular
group of people. For example, some songs contain sections where only the men or
only the women sing. The ``part`` attribute, attached to the ``<lines>`` tag,
marks these different sections (or parts) of songs. The value of this attribute is
can be any arbitrary text.

For example, a song containing one verse with some words for men and some words
for women::

    <lyrics>
      <verse name="v1">
        <lines part="men">
          First line of words sung by men.<br/>
          Second line of words sung by men.
        </lines>
        <lines part="women">
          First line of words sung by women.<br/>
          Second line of words sung by women.
        </lines>
      </verse>
    </lyrics>


Comments in Lyrics
^^^^^^^^^^^^^^^^^^

The OpenLyrics format also supports comments within lyrics. Comments are useful
for adding non-visible information. For example, a comment could contain the style
in which to play or sing any particular set of lyrics. Once again, comments are
defined by the ``<comment>`` tag.

For example::

    <lyrics>
      <verse name="v1">
        <lines>
          <comment>Singing loudly.</comment>
          Text of verse.<br/>
          <comment>Singing quietly.</comment>
          Text of verse.
        </lines>
      </verse>
      <verse name="c">
        <lines>
          <comment>Singing loudly.</comment>
          Line content.<br/>
          Line content.
        </lines>
      </verse>
    </lyrics>


Advanced Example
----------------

More song examples can be found in the ``songs`` directory distributed with the
OpenLyrics archive.

Here's an advanced example of the XML::

    <?xml version="1.0" encoding="UTF-8"?>
    <song xmlns="http://openlyrics.info/namespace/2009/song"
          version="0.8"
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
        <released>1779</released>
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
            Amazing grace how sweet the sound<br/>
            That saved a wretch like me.<br/>
            I once was lost, but now am found,<br/>
            Was blind but now I see.
          </lines>
        </verse>
        <verse name="v2">
          <lines>
            'Twas grace that taught my heart to fear,<br/>
            And grace my fears;<br/>
            How precious did that grace appear<br/>
            The hour I first believed.
          </lines>
        </verse>
        <verse name="v3">
          <lines>
            Through many dangers, toil and snares,<br/>
            I have already come;<br/>
            'Tis grace has brought me safe thus far,<br/>
            And grace will lead me home.
          </lines>
        </verse>
        <verse name="v4">
          <lines>
            When we've been there ten thousand years<br/>
            Bright shining as the sun,<br/>
            We've no less days to sing God's praise<br/>
            Than when we've first begun.
          </lines>
        </verse>
      </lyrics>
    </song>

