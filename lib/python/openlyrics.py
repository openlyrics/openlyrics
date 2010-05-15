#! /usr/bin/env /usr/bin/python
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#  
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
from datetime import datetime
from xml.etree import cElementTree as etree

u"""
Provides a module to access OpenLyrics data type.

Usage:
from openlyrics import Song
s = Song('song.xml')
"""

# A few 

def fromstring(text):
    u"Read from a string."
    tree = etree.fromstring(text)
    song = Song()
    if tree:
        song.from_xml(tree)
    return song

def tostring(song):
    u"Convert to a file."
    tree = song.to_xml()
    return etree.tostring(tree.getroot(), encoding=u'UTF-8')

def parse(filename):
    u"Read from the file."
    tree = etree.parse(filename)
    song = Song(tree)
    return song

class Song(object):
    u"""
    Definition of an song.
    
    titles:        A list of Title (class) objects.
    authors:       A list of Author (class) objects.
    songbooks:     A list of Songbook (class) objects, with a name and entry.
    themes:        A list of Theme (class) objects.
    comments:       A list of string comments
    release_date:   The date, in the format of yyyy-mm-ddThh:mm.
    ccli_no:        The CCLI number. Numeric or string value.
    tempo:          Numeric value of speed.
    tempo_type:     Unit of measurement of tempo. Example: "bpm".
    key:            Key of a string. Example: "Eb".
    transposition:  Key adjustment up or down. Integer value.
    verse_order:    The verse names in a specific order.
    variant:        A string describing differentiating it from other songs
                    with a common title.
    keywords:       
    copyright:      A copyright string.
    publisher:      A string value of the song publisher.
    custom_version: 
    """
    
    def __init__(self, filename = None):
        u"Create the instance."
        self.__ns = u''
        self._version = u'0.7'
        
        self.titles = []
        self.authors = []
        self.songbooks = []
        self.themes = []
        self.comments = []
        self.verses = []
        
        # String Types
        self.release_date = u''
        self.ccli_no = u''
        self.tempo = u''
        self.tempo_type = u''
        self.key = u''
        self.transposition = u'0'
        self.verse_order = u''
        self.variant = u''
        self.keywords = u'' # Should keywords be a list?
        self.copyright = u''
        self.publisher = u''
        self.custom_version = u''
        
        self.createdIn = u''
        self.modifiedIn = u''
        self.modifiedDate = u''

        if filename:
            self.parse(filename)
    
    def parse(self, filename):
        u"Read from the file."
        tree = etree.parse(filename)
        self.from_xml(tree)
    
    def write(self, filename):
        u"Save to a file."
        tree = self.to_xml()
        # lxml implements pretty printing
        # argument 'encoding' adds xml declaration:
        # <?xml version='1.0' encoding='UTF-8'?>
        try:
            tree.write(filename, encoding=u'UTF-8', pretty_print=True)
        except TypeError:
            # TODO: implement pretty_print for other ElementTree API
            # implementations
            tree.write(filename, encoding=u'UTF-8')
    
    def from_xml(self, tree):
        u"Read from XML."
        if isinstance(tree, etree.ElementTree):
            root = tree.getroot()
        else:
            root = tree
        
        if u'}' in root.tag:
            self.__ns = root.tag.split(u'}')[0].lstrip(u'{')
        self.createdIn = root.get(u'createdIn', u'')
        self.modifiedIn = root.get(u'modifiedIn', u'')
        self.modifiedDate = root.get(u'modifiedDate', u'')
        
        self.titles = []
        elem = tree.findall(_path(u'properties/titles/title',self.__ns))
        for el in elem:
            title = Title(el.text, el.get(u'lang',None))
            self.titles.append(title)
        
        self.authors = []
        elem = tree.findall(_path(u'properties/authors/author',self.__ns))
        for el in elem:
            author = Author(el.text, el.get(u'type',None),
                            el.get(u'lang',None))
            self.authors.append(author)
        
        self.songbooks = []
        elem = tree.findall(_path(u'properties/songbooks/songbook',self.__ns))
        for el in elem:
            songbook = Songbook(el.get(u'name',None), el.get(u'entry',None))
            self.songbooks.append(songbook)
        
        self.themes = []
        elem = tree.findall(_path(u'properties/themes/theme',self.__ns))
        for el in elem:
            theme = Theme(el.text, el.get(u'id',None), el.get(u'lang',None))
            self.themes.append(theme)
        
        self.comments = []
        elem = tree.findall(_path(u'properties/comments/comment',self.__ns))
        for el in elem:
            self.comments.append(el.text)
        
        elem = tree.find(_path(u'properties/copyright',self.__ns))
        if elem != None:
            self.copyright = elem.text
        
        elem = tree.find(_path(u'properties/ccliNo',self.__ns))
        if elem != None:
            self.ccli_no = elem.text
        
        elem = tree.find(_path(u'properties/releaseDate',self.__ns))
        if elem != None:
            self.release_date = elem.text
        
        elem = tree.find(_path(u'properties/tempo',self.__ns))
        if elem != None:
            self.tempo_type = elem.get(u'type',None)
            self.tempo = elem.text
        
        elem = tree.find(_path(u'properties/key',self.__ns))
        if elem != None:
            self.key = elem.text
        
        elem = tree.find(_path(u'properties/verseOrder',self.__ns))
        if elem != None:
            self.verse_order = elem.text
        
        elem = tree.find(_path(u'properties/keywords',self.__ns))
        if elem != None:
            self.keywords = elem.text
        
        elem = tree.find(_path(u'properties/transposition',self.__ns))
        if elem != None:
            self.transposition = elem.text
        
        elem = tree.find(_path(u'properties/variant',self.__ns))
        if elem != None:
            self.variant = elem.text
        
        elem = tree.find(_path(u'properties/publisher',self.__ns))
        if elem != None:
            self.publisher = elem.text
        
        elem = tree.find(_path(u'properties/customVersion',self.__ns))
        if elem != None:
            self.custom_version = elem.text
        
        self.verses = []
        for verse_elem in tree.findall(_path(u'lyrics/verse',self.__ns)):
            verse = Verse()
            name = verse_elem.get(u'name', None)
            lang = verse_elem.get(u'lang', None)
            translit = verse_elem.get(u'translit', None)
            for lines_elem in verse_elem.findall(_path(u'lines', self.__ns)):
                lines = Lines()
                lines.part = lines_elem.get(u'part', None)
                for line_elem in lines_elem.findall(_path(u'line', self.__ns)):
                    # TODO: This returns the outer element, but it should not.
                    lines.lines.append( Line(etree.tostring(line_elem)) )
                verse.lines.append(lines)
            self.verses.append(verse)
    
    def to_xml(self):
        u"Convert to XML."
        root = etree.Element(u'song')
        root.set(u'xmlns', self.__ns)
        root.set(u'version', self._version)
        root.set(u'createdIn', self.createdIn)
        root.set(u'modifiedIn', self.modifiedIn)
        root.set(u'modifiedDate', datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))
        
        props = etree.Element(u'properties')
        
        if len(self.titles):
            elem1 = etree.Element(u'titles')
            for t in self.titles:
                elem2 = etree.Element(u'title')
                if t.lang:
                    elem2.set(u'lang',t.lang)
                elem2.text = t.title
                elem1.append(elem2)
            props.append(elem1)
        
        if len(self.authors):
            elem1 = etree.Element(u'authors')
            for a in self.authors:
                elem2 = etree.Element(u'author')
                if a.type:
                    elem2.set(u'type',a.type)
                    if a.type == u'translator' and a.lang:
                        elem2.set(u'lang',a.lang)
                elem2.text = a.author
                elem1.append(elem2)
            props.append(elem1)
        
        if len(self.songbooks):
            elem1 = etree.Element(u'songbooks')
            for s in self.songbooks:
                elem2 = etree.Element(u'songbook')
                if s.entry:
                    elem2.set(u'entry',s.entry)
                elem2.text = s.name
                elem1.append(elem2)
            props.append(elem1)
        
        if len(self.themes):
            elem1 = etree.Element(u'themes')
            for t in self.themes:
                elem2 = etree.Element(u'theme')
                if t.id:
                    elem2.set(u'id',t.id)
                if t.lang:
                    elem2.set(u'lang',t.lang)
                elem2.text = t.theme
                elem1.append(elem2)
            props.append(elem1)
        
        if len(self.comments):
            elem1 = etree.Element(u'comments')
            for c in self.comments:
                elem2 = etree.Element(u'comment')
                elem2.text = str(c)
                elem1.append(elem2)
            props.append(elem1)
        
        if self.copyright:
            elem1 = etree.Element(u'copyright')
            elem1.text = str(self.copyright)
            props.append(elem1)
        
        if self.ccli_no:
            elem1 = etree.Element(u'ccliNo')
            elem1.text = str(self.ccli_no)
            props.append(elem1)
        
        if self.release_date:
            elem1 = etree.Element(u'releaseDate')
            elem1.text = str(self.release_date)
            props.append(elem1)
        
        if self.tempo:
            elem1 = etree.Element(u'tempo')
            if self.tempo_type:
                elem1.set(u'type',self.tempo_type)
            elem1.text = self.tempo
            props.append(elem1)
        
        if self.key:
            elem1 = etree.Element(u'key')
            elem1.text = self.key
            props.append(elem1)
        
        if self.verse_order:
            elem1 = etree.Element(u'verseOrder')
            elem1.text = self.verse_order
            props.append(elem1)
        
        if self.keywords:
            elem1 = etree.Element(u'keywords')
            elem1.text = self.keywords
            props.append(elem1)
        
        if self.transposition:
            elem1 = etree.Element(u'transposition')
            elem1.text = self.transposition
            props.append(elem1)
        
        if self.variant:
            elem1 = etree.Element(u'variant')
            elem1.text = self.variant
            props.append(elem1)
        
        if self.publisher:
            elem1 = etree.Element(u'publisher')
            elem1.text = self.publisher
            props.append(elem1)
        
        if self.custom_version:
            elem1 = etree.Element(u'customVersion')
            elem1.text = self.custom_version
            props.append(elem1)
        
        root.append(props)
        
        #TODO: Verses
        
        tree = etree.ElementTree(root)
        return tree
    

# Property elements

class Title(object):
    u"""
    A title for the song.
    
    title: The title as a string.
    lang:  A language code, in the format of "xx", or "xx-YY".
    """
    title = None
    lang = None
    
    def __init__(self, title = None, lang = None):
        u"Create the instance."
        self.title = title
        self.lang = lang
    
    def __str__(self):
        u"Return a string representation."
        return self.title
    
    def __unicode__(self):
        u"Return a unicode representation."
        return self.title


class Author(object):
    u"""
    An author of words, music, or a translation.
    
    author: Author's name as a string.
    type:   One of "words", "music", or "translation". This module will throw
            ValueError if one of these is found to be incorrect.
    lang:   A language code, in the format of "xx", or "xx-YY".
    """
    author = None
    type = None
    lang = None
    
    def __init__(self, author = None, type = None, lang = None):
        u"Create the instance. May return `ValueError`."
        self.author = author
        if type not in (u'words',u'music',u'translation', None):
            raise ValueError(u'`type` must be one of "words", "music", or\
                    "translator".')
        self.type = type
        self.lang = lang
    
    def __str__(self):
        u"Return a string representation."
        return self.author
    
    def __unicode__(self):
        u"Return a unicode representation."
        return self.author


class Songbook(object):
    u"""
    A songbook/collection with an entry/number.
    
    name:  The name of the songbook or collection.
    entry: A number or string representing the index in this songbook.
    """
    name = None
    entry = None
    
    def __init__(self, name = None, entry = None):
        u"Create the instance."
        self.name = name
        self.entry = entry
    
    def __str__(self):
        u"Return a string representation."
        return u'%s #%s' % (self.name, self.entry)
    
    def __unicode__(self):
        u"Return a unicode representation."
        return u'%s #%s' % (self.name, self.entry)


class Theme(object):
    u"""
    A category for the song.
    
    theme: The name of the song.
    id:    A number from the standardized CCLI list.
                 http://www.ccli.com.au/owners/themes.cfm
    lang:  A language code, in the format of "xx", or "xx-YY".
    """
    theme = None
    id = None
    lang = None
    
    def __init__(self, theme = None, id = None, lang = None):
        u"Create the instance."
        self.theme = theme
        self.id = id
        self.lang = lang
    
    def __str__(self):
        u"Return a string representation."
        return self.theme
    
    def __unicode__(self):
        u"Return a unicode representation."
        return self.theme

    
# Verse element and subelements

class Verse(object):
    u"""
    A verse for a song.
    """
    name = None
    lang = None
    translit = None
    lines = None
    
    def __init__(self):
        u"Create the instance."
        self.lines = []
    

class Lines(object):
    u"""
    A group of lines in a verse.
    """
    lines = None
    part = None
    
    def __init__(self):
        u"Create the instance."
        self.lines = []
    
    def __str__(self):
        u"Return a string representation."
        return u'\n'.join(str(l) for l in self.lines)
    
    def __unicode__(self):
        u"Return a unicode representation."
        return u'\n'.join(unicode(l) for l in self.lines)

class Line(object):
    u"""
    A single line in a group of lines.
    """
    markup = u''
    
    def __init__(self, markup):
        self.markup = markup
        self.__chords_regex = re.compile(u'<chord[^>]>')
    
    def _get_text(self):
        u"Get the text for this line."
        return self.__chords_regex.sub(u'',self.markup)
    
    def _set_text(self, value):
        u"Set the text for this line. This removes all chords."
        self.markup = value
    
    text = property(_get_text, _set_text)
    
    # Chords property
    def _get_chords(self):
        u"Get the chords for this line."
        self.__chords_regex.findall(self.markup)
    chords = property(_get_chords)
    
    def __str__(self):
        u"Return a string representation."
        return str(self.text)
    
    def __unicode__(self):
        u"Return a unicode representation."
        return self.text


# Various functions

def _path(tag, ns = None):
    u"""
    If a namespace is on a document, the XPath requires {ns}tag for every
    tag in the path. This assumes that only one namespace for the document
    exists.
    """
    if ns == None or len(ns) == 0:
        return tag
    else:
        return u'/'.join(u'{%s}%s' % (ns, t) for t in tag.split(u'/'))
