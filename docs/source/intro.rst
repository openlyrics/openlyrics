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

The first version of OpenLyrics was created in 2008, when the openlp.org project
leader came up with a proposal for cooperation between OpenLP and ChangingSong.
We agreed that it would be great to create at least a data format to allow
song exchange between our presentation applications. We started discussing what
this should look like.

My experience with ChangingSong made me aware that a new data format was
necessary  to implement some of the more advanced features that were being
requested. During the planning stages of creating OpenLyrics, we asked, "Why not
do it well?" Our goal from the start was to create a format that could be shared
across multiple platforms and applications.

To that end, OpenLyrics uses XML for data format definition. XML is a well
established standard with solid support in many programming languages. Numerous
libraries exist to aid in working in it.

The current design of OpenLyrics is based on the OpenSong data format along with
some features suggested by users, particularly the ability to use
`multiple languages for a song (forum) <http://sourceforge.net/projects/changingsong/forums/forum/770759/topic/1983107>`_
.


Release Numbering
-----------------

OpenLyrics uses the following release numbering scheme::

    X.X_pX

where ``X.X`` is the major release number, indicating the data format version
and ``pX`` is the optional minor release number, used when incidental files
(documentation, examples, and the like) are updated.

Therefore, this would be a valid release number, indicating a new data format::

    0.6

And this would be the minor release made when we correct typos in documentation,
add an example song, etc::

    0.6_p1


