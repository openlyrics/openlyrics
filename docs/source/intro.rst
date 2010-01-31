.. _intro:

Introduction
============

About
-----

OpenLyrics is a free, open XML standard for Christian worship songs. The goal of
OpenLyrics is to provide an application-independant and operating
system-independant song format for interoperability between applications.


History
-------

The first version of OpenLyrics was created in 2008. Back in 2008, the
openlp.org project leader came up with a proposal about cooperation between
OpenLP and ChangingSong. We agreed that it would be great to create at least
a data format to allow exchange songs between our presentation applications.
One day he suggested the name **openlyrics**. Thus the data format is named
using that name.

In the beginning with ChangingSong I was aware that a new data format is
necessary, if I would like to implement some more advanced features, requested
by users of other applications.
During designing openlyrics I realized why not to do it well? In order to
be used by more applications.

OpenLyrics uses XML for data format definition. XML is a well established
standard with solid support in programming libraries.

The current design of OpenLyrics is based on the OpenSong data format and
on some features suggested by users, especially the ability using
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


