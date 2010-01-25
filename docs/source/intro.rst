.. _intro:

Introduction
============

OpenLyrics is an open standard for storing songs for
interoperability between Church Presentation applications.

Brief Introduction
------------------

OpenLyrics is a free, open XML standard for Christian worship songs. The goal of
OpenLyrics is to provide an application-independant and operating
system-independant song format for interoperability between applications.

Download
--------

`OpenLyrics 0.6 archive`_ contains several song examples and `RelaxNG`_ xml schema.

.. _OpenLyrics 0.6 archive:
   http://openlyrics.info/files/openlyrics-0.6.zip
.. _RelaxNG:
   http://en.wikipedia.org/wiki/RelaxNG


Example
-------

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
