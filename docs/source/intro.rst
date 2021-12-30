.. _intro:

Introduction
============

About
-----

OpenLyrics is a free, open XML standard for Christian worship songs. The goal of
OpenLyrics is to provide an application-independent and operating
system-independent song format for interoperability between applications.


History
-------

The first version of OpenLyrics was created in 2008, when the `OpenLP <https://openlp.org/>`_ project
leader approached the `ChangingSong <https://sourceforge.net/projects/changingsong/>`_ project leader, and proposed cooperation
between OpenLP and ChangingSong to improve data exchange between the two
projects. They agreed that a good first step would be to create an independent
interoperable data format to provide better song exchange between the two
applications.

Furthermore, experiences the leader of the ChangingSong had with the `OpenSong <http://www.opensong.org/>`_
project's XML format for songs made him aware that the OpenSong format was not
sufficient for the proposed features in ChangingSong, and thus a new format
would be necessary in order to implement many of the more advanced features
the project planned to develop.

Upon planning the OpenLyrics format, the two leaders decided to make the
format as open and inclusive as possible so that other presentation projects,
both open source and proprietary, could use this new format as well.

To that end, they decided to make OpenLyrics an XML format. XML is a well
established standard with solid support in many programming languages, and
there are a plethora of XML libraries for manipulating XML.

The current design of OpenLyrics is based on the OpenSong data format along with
some features suggested by users, particularly the ability to use
`multiple languages for a song (forum) <https://sourceforge.net/projects/changingsong/forums/forum/770759/topic/1983107>`_
and the possibility of using them as `single source <https://github.com/openlyrics/openlyrics/issues/29>`_
to provide various outputs including printed hymnbooks.


Release Numbering
-----------------

OpenLyrics uses the following release numbering scheme::

    X.X_pX

where ``X.X`` is the major release number, indicating the data format version
and ``pX`` is the optional minor release number, used when incidental files
(documentation, examples, and the like) are updated.

Therefore, this would be a valid release number, indicating a new data format::

    0.7

And this would be the minor release made when we correct typos in documentation,
add an example song, etc::

    0.7_p1


