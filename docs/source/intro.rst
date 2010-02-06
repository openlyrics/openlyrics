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

The first version of OpenLyrics was created in 2008 when, the openlp.org project
leader came up with a proposal about cooperation between OpenLP and
ChangingSong. We agreed that it would be great to create at least a data format
to allow exchange songs between our presentation applications.

My experience with ChangingSong made me aware that a new data format was
necessary  to implement some of the more advanced features that were being
requested. During the planning stages of creating OpenLyrics, we asked, "Why not
do it well?" Our goal from the start was to create a format that could be shared
across multiple platforms and applications.

OpenLyrics uses XML for data format definition. XML is a well established
standard with solid support in programming libraries.

The current design of OpenLyrics is based on the OpenSong data format and
on some features suggested by users, especially the ability to use
`multiple languages for a song (forum) <http://sourceforge.net/projects/changingsong/forums/forum/770759/topic/1983107>`_
.


Release Numbering
-----------------

OpenLyrics release numbering is in the format::

    X.X_pX

where ``X.X`` means the data format version and ``pX`` is used only, when
additionally files were updated. Additional files could be for instance
documentation, song examples, etc.

When also data format is changed, the numbering could be as follows::

    0.6

Only documentation is updated or anything else without changing data format::

    0.6_p1


