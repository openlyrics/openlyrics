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
        ``<chord root="D">``

    beats
        ``<beat><chord root="D"></beat>``

    comments in lyrics
        ``<verse><lines><comment/></lines></verse>``

    date of song release
        ``<released>``

    OpenLyrics version
        ``<song version="0.9>``

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
        ``<timeSignature>``

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
        ``<song chordNotation="">``
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

    instrumental parts without lyrics
        ``<instrument name="i1">``

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
          xml:lang="de"
          chordNotation="german"
          version="0.9"
          createdIn="OpenLP 1.9.0"
          modifiedIn="ChangingSong 0.0.1"
          modifiedDate="2010-01-28T13:15:30+01:00">

``xmlns``
    Defines an XML namespace. The value should be always
    ``http://openlyrics.info/namespace/2009/song``

``xml:lang``
    Language of the OpenLyrics document. It defines the default language for titles,
    keywords, themes, comments, lyrics, etc. The format of this attribute should be
    ``xx`` or ``xx-YY``, where ``xx`` is a language code from the
    `ISO-639 <http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_ standard, and
    ``YY`` is a `country code <http://en.wikipedia.org/wiki/ISO_3166-1>`_. For more
    details see `BCP 47 <http://www.rfc-editor.org/rfc/bcp/bcp47.txt>`_.
    Default language can be overwriten for a specified element, see:
    ``<title lang="">``, ``<theme lang="">``, ``<verse lang="">``.
    This element is optional. If not specified, it means document language is ``"en"``.

``chordNotation``
    A string to idetify the preferred notation of the chords. Supported values are
    ``english`` (default), ``english-b``,  ``german``, ``dutch``, ``hungarian``, ``neolatin``.
    This element is optional.

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

Processing Instructions
-----------------------

OpenLyrics, like all XML files, can contain `processing instructions <https://www.w3.org/TR/REC-xml/#sec-pi>`_.
With the ``xml-stylesheet`` attribute it is possible to `associate <https://www.w3.org/TR/xml-stylesheet/>`_
CSS or XSLT style sheets with an OpenLyrics document. For example::

    <?xml-stylesheet href="ol.css" type="text/css"?>
    <song xmlns="http://openlyrics.info/namespace/2009/song" version="0.9">

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

Like the lyrics, the title can be :ref:`transliterated<Transliteration>` with an
optional ``translit`` attribute alongside ``lang`` attribute::

    <titles>
      <title lang="he">הבה נגילה</title>
      <title lang="he" translit="en">Hava Nagila</title>
      <title lang="en">Let Us Rejoice</title>
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

Four different types of authors can be defined:

* *author of words*::

      <author type="words">John Newton</author>

* *author of music*::

      <author type="music">John Newton</author>

* *translator*::

      <author type="translation">Csiszér László</author>
      <author type="translation" lang="cs">Jan Ňůtn</author>

  When the ``type`` is ``translation``, a ``lang`` attribute can be added. The
  value of this attribute should be in the same format as the ``lang`` attribute
  of the ``<title>`` tag. It is not mandatory, because the translation normally
  matches the language of the document, stored in ``<song xml:lang="">``, but
  it can be useful for bilingual documents to indicate precisely the translator.

* *arranger*, a person, who produces an alternate version, arrangement of a song,
  who rewrites, alters, reworks a song or adopts a song to another language::

      <author type="arrangement">John Newton</author>

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
pitch of chords up or down. The value must be an integer between -11 and 11.

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

The key determines the musical scale of a song. It can be determined with the
following major or minor values:

============== ====== ======
Key signature  Major  Minor
============== ====== ======
10♯            A#     Fxm
9♯             D#     B#m
8♯             G#     E#m
7♯             C#     A#m
6♯             F#     D#m
5♯             B      G#m
4♯             E      C#m
3♯             A      F#m
2♯             D      Bm
1♯             G      Em
0              C      Am
1♭             F      Dm
2♭             Bb     Gm
3♭             Eb     Cm
4♭             Ab     Fm
5♭             Db     Bbm
6♭             Gb     Ebm
7♭             Cb     Abm
============== ====== ======

Example::

    <key>Eb</key>


Time Signature
^^^^^^^^^^^^^^

The ``timeSignature`` tag is used to define the time signature::

    <timeSignature>3/4</timeSignature>

Its value must be a fraction: an integer between 1 and 63, a slash (/), and one of
the following integers: 1, 2, 4, 8, 16, 32, 64. For example: 2/2, 4/4, 3/4, 7/8, 12/8.


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

The verse order of a song defines the order in which the verses and instrumental parts
are typically sung or performed. The verse order is denoted by the ``<verseOrder>`` tag.

The verse order is a space-separated string of verse and instrumental names (which are defined in
the ``<lyrics>`` section of the file). Verse names can appear multiple times, and
should be lowercase. See the ``<verse>`` section for more information on verse
names.

For example::

    <verseOrder>i v1 c v2 c v1 c o</verseOrder>


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

Like title and the lyrics, the theme can be :ref:`transliterated<Transliteration>` with an
optional ``translit`` attribute alongside ``lang`` attribute::

    <themes>
      <theme>Peace</theme>
      <theme lang="he">שָׁלוֹם</theme>
      <theme lang="he" translit="en">Shalom</theme>
    </themes>

It is highly recommended that themes should come from the list of themes on the
CCLI web site: `<https://songselect.ccli.com/search/themes>`_


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

The ``<lyrics>`` tag contains one or more ``<verse>`` or ``<instrument>`` tags.
Each ``<verse>`` tag defines a verse or stanza of a song, and contains a single
mandatory attribute, ``name``. Each ``<instrument>`` tag defines an instrumental
part (without lyrics) of a song, and contains a single mandatory attribute, ``name``.
Each verse and istreumental part can contain one or more ``<lines>`` tags, which holds a
logical grouping of words and chords.

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

Verse/Instrumental Name
^^^^^^^^^^^^^^^^^^^^^^^

OpenLyrics supports these verse and instrumental types:

+------------+------------+-------+------------+
| Name       | Short code | Type               |
+============+============+=======+============+
| intro      | i          | verse | instrument |
+------------+------------+-------+------------+
| verse      | v          | verse |            |
+------------+------------+-------+------------+
| pre-chorus | p          | verse |            |
+------------+------------+-------+------------+
| chorus     | c          | verse |            |
+------------+------------+-------+------------+
| solo       | s          |       | instrument |
+------------+------------+-------+------------+
| bridge     | b          | verse |            |
+------------+------------+-------+------------+
| middle     | m          |       | instrument |
+------------+------------+-------+------------+
| other      | o          | verse |            |
+------------+------------+-------+------------+
| ending     | e          | verse | instrument |
+------------+------------+-------+------------+


As previously mentioned, every ``<verse>`` or ``<instrument>`` tag has a mandatory ``name`` attribute.
They should be unique, written in **lower case**, a single word, and should
follow the naming convention as laid out in the table below:

+-------------------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+
|                         | i          | v          | p          | c          | s          | b          | m          | o          | e          |
+=========================+============+============+============+============+============+============+============+============+============+
| section                 | ``i``      |            | ``p``      | ``c``      | ``s``      | ``b``      | ``m``      | ``o``      | ``e``      |
+-------------------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+
| | section part A        | | ``ia``   |            | | ``pa``   | | ``ca``   | | ``sa``   | | ``ba``   | | ``ma``   | | ``oa``   | | ``ea``   |
| | section part B        | | ``ib``   |            | | ``pb``   | | ``cb``   | | ``sb``   | | ``bb``   | | ``mb``   | | ``ob``   | | ``eb``   |
| | section part C…       | | ``ic``…  |            | | ``pc``…  | | ``cc``…  | | ``sc``…  | | ``bc``…  | | ``mc``…  | | ``oc``…  | | ``ec``…  |
+-------------------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+
| | first section         | | ``i1``   | | ``v1``   | | ``p1``   | | ``c1``   | | ``s1``   | | ``b1``   | | ``m1``   | | ``o1``   | | ``e1``   |
| | second section        | | ``i2``   | | ``v2``   | | ``p2``   | | ``c2``   | | ``s2``   | | ``b2``   | | ``m2``   | | ``o2``   | | ``e2``   |
| | third section…        | | ``i3``…  | | ``v3``…  | | ``p3``…  | | ``c3``…  | | ``s3``…  | | ``b3``…  | | ``m3``…  | | ``o3``…  | | ``e3``…  |
+-------------------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+
| | first section part A  | | ``i1a``  | | ``v1a``  | | ``p1a``  | | ``c1a``  | | ``s1a``  | | ``b1a``  | | ``m1a``  | | ``o1a``  | | ``e1a``  |
| | first section part B  | | ``i1b``  | | ``v1b``  | | ``p1b``  | | ``c1b``  | | ``s1b``  | | ``b1b``  | | ``m1b``  | | ``o1b``  | | ``e1b``  |
| | first section part C… | | ``i1c``… | | ``v1c``… | | ``p1c``… | | ``c1c``… | | ``s1c``… | | ``b1c``… | | ``m1c``… | | ``o1c``… | | ``e1c``… |
+-------------------------+------------+------------+------------+------------+------------+------------+------------+------------+------------+

According to the table above, a song containing an instrumental intro (*i*) two verses (*v1, v2*), a chorus
(*c*), a bridge (*b*) and an ending (*e*) would look like this::

    <lyrics>
      <instrument name="i">
        ...
      </instrument>
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

The OpenLyrics format also provides the ability to include chords in the lyrics and instrumental part of
songs. The tag containing a chord name looks like these::

    <chord root="C" structure="dom7">lyrics...</chord>
    <chord root="D" bass="F#">lyrics...</chord>
    <chord root="C" structure="min" bass="Eb"/>lyrics
    <chord root="E" structure="3-5-m7-13">lyrics...</chord>

The root note
"""""""""""""

The ``root`` attribute describes the root note of the chord. The values should marked
with English notation:

======= ========= ====== ===== ========= ========
english english-b german dutch hungarian neolatin
======= ========= ====== ===== ========= ========
**C**   C         C      C     C         Do
**C#**  C#        Cis    Cis   Cisz      Do#
**Db**  Db        Des    Des   Desz      Reb
**D**   D         D      D     D         Re
**D#**  D#        Dis    Dis   Disz      Re#
**Eb**  Eb        Es     Es    Esz       Mib
**E**   E         E      E     E         Mi
**F**   F         F      F     F         Fa
**F#**  F#        Fis    Fis   Fisz      Fa#
**Gb**  Gb        Ges    Ges   Gesz      Solb
**G**   G         G      G     G         Sol
**G#**  G#        Gis    Gis   Gisz      Sol#
**Ab**  Ab        As     As    Asz       Lab
**A**   A         A      A     A         La
**A#**  A#        Ais    Ais   Aisz      La#
**Bb**  B         B      Bes   B         Sib
**B**   H         H      B     H         Si
======= ========= ====== ===== ========= ========

The preferred notation for displaying can be marked with ``chordNotation`` attribute on root element.

For supporting diatonic transposition and theoretical keys the following notes are valid also:

======= ========= ====== ===== ========= ========
english english-b german dutch hungarian neolatin
======= ========= ====== ===== ========= ========
**E#**  E#        Eis    Eis   Eisz      Mi#
**B#**  H#        His    Bis   Hisz      Si#
**Fx**  Fx        Fisis  Fisis Fiszisz   Fax
**Cx**  Cx        Cisis  Cisis Ciszisz   Dox
**Gx**  Gx        Gisis  Gisis Giszisz   Solx
**Cb**  Cb        Ces    Ces   Cesz      Dob
**Fb**  Fb        Fes    Fes   Fesz      Fab
======= ========= ====== ===== ========= ========

The bass
""""""""

The optional ``bass`` attribute describes the foreign bass of the chord if any. The values should marked
with English notation.

The chord structure
"""""""""""""""""""
The ``structure`` attribute describes the kind of the chord. This element is optional,
if not present, the default value is the ``major``. It can be marked

- with a sorthand code, or
- with a chord formula (for experts).

These are the built-in **sorthand codes**:

============ =================================== ========
Shortcode    Chord Name                          Notation
============ =================================== ========
**power**    perfect 5th; power chord            5
             major
**min**      minor                               m
**aug**      augmented                           \+
**dim**      diminished                          m,5♭
**dom7**     dominant 7th                        7
**maj7**     major 7th                           Δ
**min7**     minor 7th                           m7
**dim7**     diminished 7th                      ⵔ
**halfdim7** half-diminished 7th                 ⵁ
**minmaj7**  minor major 7th                     mΔ
**augmaj7**  augmented major 7th                 +Δ
**aug7**     dominant 7th sharp 5; augmented 7th +7
**maj6**     major 6th                           6
**maj6b**    (major minor 6th)                   6♭
**min6**     minor 6th                           m6
**min6b**    (minor minor 6th)                   m6♭
**dom9**     (dominant) 9th                      9
**dom9b**    dominant minor 9th                  7,9♭
**maj9**     major 9th                           Δ9
**min9**     minor (dominant)Í 9th               m9
**minmaj9**  minor major 9th                     mΔ9
**aug9**     augmented (dominant) 9th            +9
**halfdim9** half-diminished 9th                 ⵁ9
**sus4**     major/minor suspended 4th           4
**sus2**     major/minor suspended 2nd           2
**add9**     major added 9th                     add9
============ =================================== ========

Other chords can be noted with **chord formulas**. OpenLyrics has 85 built-in chords defined by a formula.
Using chord formulas, an author can write additional custom chords. Chord formulas are described
in :ref:`chord formulas <chordlist>`.

To display root+structure+bass
""""""""""""""""""""""""""""""

The processors should display chords:

- First display the ``root`` according to ``chordNotation``.
- Immediately followed by the notation for the marked chord.
- If there is a bass: immediately followed by a slash (/) and the ``root`` according to ``chordNotation``.

Examples:

=============================================== =========
XML                                             Displayed
=============================================== =========
``<chord root="C" structure="dom7"/>``          C7
``<chord root="D" bass="F#"/>``                 D/F♯
``<chord root="C" structure="min" bass="Eb"/>`` Cm/E♭
``<chord root="E" structure="3-5-m7-13"/>``     E7,6
=============================================== =========

Mixing lyrics and chords
""""""""""""""""""""""""

The ``<chord>`` tags are mixed in with the lyrics of a song::

    <lyrics>
      <verse name="v1">
        <lines>
          <chord root="D" structure="dom7"/>Amazing grace
          how</chord> <chord root="E">sweet the sound</chord><br/>
          That saved <chord root="A">a wretch</chord>
          <chord root="F#"/>like me.</chord>
        </lines>
      </verse>
    </lyrics>

This tag can be normal and empty.

Normal tags:

- Can mark normal chords with lyrics. They should be placed on the lyrics (syllables), to which the chord applies. With
  this syntax overlapping can avoided::

    Ho<chord root="E" bass="G#">san</chord><chord root="A">na,
    ho</chord><chord root="B">san<chord root="C#" structure="min">na,<br/>
    Ho</chord><chord root="A">sanna in the <chord root="C#"
    structure="min">high</chord><chord root="B">est.</chord>

      E/G# A     B  C#m
    Hosan__na, hosanna,
      A            C#m B
    Hosanna in the highest.

- Can mark upbeats using an optional ``upbeat`` attribute, when a chord starts with a music pause::

    <chord root="D" upbeat="true">You are my
    pas</chord><chord root="D" structure="sus2" bass="C#">sion</chord><br/>
    <chord root="B" structure="min7" upbeat="true">Love of my</chord>
    <chord root="G">life</chord>

      D              D2 /C♯
       You are my passion
    Bm7           G
       Love of my life

- Can mark more that one chord on one syllable (nested tag)::

    <chord root="A"><chord root="G"><chord root="D">Al</chord></chord></chord>
    le<chord root="D">luja,</chord>

    DGA    D
    Al__leluja

Empty tags:

- Can mark chords without lyrics (chords on music pause). Example::

    Aunque mis <chord root="E">ojos<br/>
    no te puedan</chord> <chord root="C#" structure="min">ver,
    te puedo sent<chord root="A">ir,<br/>
    Sé que estás a</chord><chord root="E">quí.</chord><chord root="B"/>

               E
    Aunque mis ojos
                 C#m               A
    no te puedan ver, te puedo sentir,
                   E  B
    Sé que estás aquí.

- Can mark chords without time specification like in version 0.8. They should be places immediately before the letters where it should be
  played. (With this syntax chords can overlap.)::

    A<chord root="G"/>mazing <chord root="G" structure="dom7" />Grace!
    how <chord root="C"/>sweet the <chord root="G">sound.

     G      G7         C         G
    Amazing Grace! how sweet the sound.

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

In parallel to the lyrics, titles and themes can be transliterated.


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

Line repeat
^^^^^^^^^^^

In some songs not only the verses but also the lines may be repeated. Repeated verse can be managed
with the ``<verseOrder>`` tag::

    <verseOrder>v1 v1 c v2 v2 c</verseOrder>

Repeating lines can be described with an optional attribute for lines::

    <lines repeat="2">O my Jesus.</lines>

The value of this attribute should be an integer with a value of 2 or more.

Lyrics projectors and processors can display the above example like this::

    𝄆 O my Jesus. 𝄇×2

Or simply::

    O my Jesus.
    O my Jesus.

Instrumental parts
^^^^^^^^^^^^^^^^^^

In some songs there are parts without lyrics, instrumental sections, etc.
OpenLyrics supports describing these parts, very similar to ``<verse>`` tags::

    <lyrics>
      <instrument name="i">
        <lines>
          <beat><chord root="B" structure="m3-5" /><chord root="A" bass="C#" /></beat>
          <beat><chord root="D" /></beat>
          <beat><chord root="A" /></beat>
          <beat><chord root="G" /></beat>
        </lines>
      </instrument>
    </lyrics>

<instrument> tags are siblings to <verse> tags. They can be in any order
(described in ``<verseOrder>``). The name of an instrumental part can be intro (``name="i"``),
middle (``name="m"``), outro (``name="o"``) or solo (``name="s"``), and can named similar to other
verse names (``i, i1, i2, i1a, i1b``). Instrumental part can't contain lyrics, only ``<chord>`` and
``<beat>`` tags. A <beat> represents a beat in the music. A <beat> tag can contains only <chord> tags.
But it is not mandatory to separate beats, instrumental parts can contain chords only::

    <instrument name="i">
      <lines>
        <chord root="D" /><chord root="A" /><chord root="G" />
      </lines>
    </instrument>

If a lyrics projector supports chords it can display instrumental
parts as a verse without lyrics. If a lyrics projector does not support
chords, can simply omit instrumental parts.

The example above should be displayed like so::

    {Intro} h A/C# | D | A | G

Formatting extensions
---------------------

Formatting options for OpenLyrics can be extended. There is a possibility to define and apply
custom tags for formatting lyrics or chords. The extensions can be defined in ``format`` section
which can be placed between the ``properties`` and ``lyrics`` tags.

Formatting tags
^^^^^^^^^^^^^^^

OpenLyrics is quite solid in lyrics formatting options. If the author needs additional formatting
options, they can define a formatting dictionary and apply the defined tags in the lyrics. The
formatting dictionary should be placed in ``<tags>`` tag and should have a ``target`` application or processor identifier attribute, which supports these custom tags. A tag consists of the definition of an opening and a closing element. Closing element is not mandatory (empty XML element). They can be included in the lyrics as XML elements and a ``name`` attribute points to its custom tag name::

  <song xmlns="http://openlyrics.info/namespace/2009/song" version="0.9">
    <properties>
      <titles>
        <title>Amazing Grace</title>
      </titles>
    </properties>
    <format>
      <tags application="MyHTMLExporter">
        <tag name="red">
          <open><![CDATA[<span style="color:red">]]></open>
          <close><![CDATA[</span>]]></close>
        </tag>
        <tag name="strong">
          <open><![CDATA[<strong>]]></open>
          <close><![CDATA[</strong>]]></close>
        </tag>
      </tags>
    </format>
    <lyrics>
      <verse name="v1">
        <lines>
          Amazing <tag name="red">grace!</tag> How sweet the sound<br/>
          That saved a wretch <tag name="strong">like</tag> me.
        </lines>
      </verse>
    </lyrics>
  </song>

This method allows custom formatting tags to be saved in OpenLyrics files and load them without
loss of data.

It should be noted that:

- Support for formatting tags is not mandatory for OpenLyrics processors.

- Formatting tags are not interpreted elements, they have no common meaning. Their name is just a
  name that carries no standardized meaning (e.g., "red" can mean red text, but it can also mean
  anything else, e.g., black text). A formatting only carries a meaningful definition for the user
  and processor of the formatting in some descriptive language that makes sense to them (e.g.,
  HTML, HTML+CSS, PostScript, ...)::

    <tags application="OpenLP">
      <tag name="r">
        <open>&lt;span style="-webkit-text-fill-color:red"&gt;</open>
        <close>&lt;/span&gt;</close>
      </tag>
    </tags>

- Different programs that import or export OpenLyrics may use quite different formatting tags, or
  may simply ignore those belonging to other programs and even if they use the same names, may
  associate a whole different meaning with them (e.g. "red" may be a fill color or a background
  color in another case.)



Advanced Example
----------------

More song examples can be found in the ``songs`` directory distributed with the
OpenLyrics archive.

Here's an advanced example of the XML::

  <?xml version="1.0" encoding="UTF-8"?>
  <?xml-stylesheet href="ol.css" type="text/css"?>
  <song xmlns="http://openlyrics.info/namespace/2009/song"
   version="0.9"
   createdIn="OpenLP 2.0"
   modifiedIn="ChangingSong 0.0.2"
   modifiedDate="2009-12-22T21:24:30+02:00"><!-- date format: ISO 8601 -->
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
      <verseOrder>i v1 v2 v3 v4 v5 v6</verseOrder>
      <themes>
        <theme>Assurance</theme>
        <theme>Grace</theme>
        <theme>Praise</theme>
        <theme>Salvation</theme>
      </themes>
    </properties>
    <lyrics>
      <verse name="i">
        <lines>
          <chord root="E" structure="min" /><chord root="D"/><chord root="G"/>
        </lines>
      </verse>
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
