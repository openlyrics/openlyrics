# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4
#
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

__version__ = '0.2'
__all__ = ['fromstring', 'tostring', 'parse', 'Song', 'Properties',
        'Title', 'Author', 'Songbook', 'Theme', 'Verse', 'Lines', 'Line']

"""
Provides a module to access OpenLyrics data type.

Usage:
from openlyrics import Song
s = Song('song.xml')
"""

import re
from datetime import datetime
from xml.etree import cElementTree as etree


OLYR_NS = u'http://openlyrics.info/namespace/2009/song'
OLYR_VERSION = u'0.8'
OLYR_CREATED_IN = u'OpenLyrics Python Library %s' % __version__
OLYR_MODIFIED_IN = u'OpenLyrics Python Library %s' % __version__


# TODO revise creating openlyrics Objects - add more arguments to contructor

def fromstring(text):
    """
    Read from a string.
    """
    # unicode string must be passed as byte string encoded in utf-8
    if type(text) is unicode:
        text = text.encode('UTF-8')
    tree = etree.fromstring(text)
    song = Song()
    if tree:
        song._from_xml(tree)
    return song


def tostring(song, pretty_print=True, update_metadata=True):
    """
    Convert to a file.
    """
    tree = song._to_xml(pretty_print=pretty_print, update_metadata=update_metadata)
    text = etree.tostring(tree.getroot(), encoding='UTF-8')
    return unicode(text, 'UTF-8') # convert to unicode string


def parse(filename):
    """
    Read from the file.
    """
    tree = etree.parse(filename)
    song = Song(tree)
    return song


class Song(object):
    """
    Definition of an song.
    """
    
    def __init__(self, filename=None):
        """
        Create the instance.
        """
        self.__ns = OLYR_NS
        self._version = OLYR_VERSION
        
        self.verses = []
        self.props = Properties(self)
        
        self.createdIn = OLYR_CREATED_IN
        self.modifiedIn = OLYR_MODIFIED_IN
        self.modifiedDate = u''

        if filename:
            self.parse(filename)
    
    def parse(self, filename):
        """
        Read from the file.
        """
        tree = etree.parse(filename)
        self._from_xml(tree)
    
    def write(self, filename, pretty_print=True, update_metadata=True):
        """
        Save to a file.
        """
        tree = self._to_xml(pretty_print, update_metadata)
        # argument 'encoding' adds xml declaration:
        # <?xml version='1.0' encoding='UTF-8'?>
        tree.write(filename, encoding=u'UTF-8', xml_declaration=True)
    
    def get_verse(self, verse_name, lang=None, translit=None):
        """
        Returns a Verse object that matches verse_name and lang and translit when given.
        If lang and translit is not specified, it returns the first verse
        that matches verse_name.
        If not matching Verse is found, None is returned.
        """
        for verse in self.verses:
            if verse.name == verse_name and\
                            (lang is None or verse.lang==lang) and\
                            (translit is None or verse.translit==translit):
                return verse
        return None
    
    def add_verse(self, verse_name, markup, lang=None, translit=None):
        # Create Line objects
        verse_ = Verse(verse_name, lang=lang, translit=translit)
        lines = Lines()
        for cur_line in markup.split("\n"):
            lines.lines.append(Line(cur_line))
        verse_.lines = [lines]
        self.verses.append(verse_)
    
    def get_version(self):
        return self._version
    
    def _from_xml(self, tree):
        """
        Read from XML.
        """
        if isinstance(tree, etree.ElementTree):
            root = tree.getroot()
        else:
            root = tree
        
        if u'}' in root.tag:
            self.__ns = root.tag.split(u'}')[0].lstrip(u'{')
        else:
            self.__ns = ''
        self.createdIn = root.get(u'createdIn', u'')
        self.modifiedIn = root.get(u'modifiedIn', u'')
        self.modifiedDate = root.get(u'modifiedDate', u'')
        self._version = root.get(u'version', u'')
        
        self.props._from_xml(tree, self.__ns)
        
        self.verses = []
        for verse_elem in tree.findall(_path(u'lyrics/verse',self.__ns)):
            verse = Verse()
            verse._from_xml(verse_elem, self.__ns)
            self.verses.append(verse)
    
    def _to_xml(self, pretty_print=True, update_metadata=True):
        """
        Convert to XML.
        """
        # for unit tests it's helpful to not update following items
        if update_metadata:
            self.modifiedDate = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            self._version = OLYR_VERSION
        root = etree.Element(u'song')

        # attributes are sorted in alphabetic order by ElementTree
        root.set(u'createdIn', self.createdIn)
        root.set(u'modifiedDate', self.modifiedDate)
        root.set(u'modifiedIn', self.modifiedIn)
        root.set(u'version', self._version)
        root.set(u'xmlns', self.__ns)
        
        props = self.props._to_xml()
        root.append(props)
        
        lyrics_elem = etree.Element(u'lyrics')
        for verse in self.verses:
            lyrics_elem.append(verse._to_xml())
        root.append(lyrics_elem)
        
        #TODO: Verses

        if pretty_print:
            self._indent(root)
        
        tree = etree.ElementTree(root)
        return tree

    # http://infix.se/2007/02/06/gentlemen-indent-your-xml
    def _indent(self, elem, level=0):
        """
        Format the XML (prettyprint).
        """

        i = '\n' + level*'  '
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + '  '
            for e in elem:
                self._indent(e, level+1)
                if not e.tail or not e.tail.strip():
                    e.tail = i + '  '
            if not e.tail or not e.tail.strip():
                e.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
    
    def __len__(self):
        # Verses in different languages exist twice, but have the same name
        # Use a set to count them only once.
        s = set()
        for verse in self.verses:
            s.add(verse.name)
        return len(s)

class Properties(object):
    """
    Stores Song property elements.
    
    titles:         A list of Title (class) objects.
    authors:        A list of Author (class) objects.
    songbooks:      A list of Songbook (class) objects, with a name and entry.
    themes:         A list of Theme (class) objects.
    comments:       A list of string comments
    
    released:       The song release date, in the format of yyyy-mm-ddThh:mm.
    ccli_no:        The CCLI number. Numeric or string value.
    tempo:          Numeric value of speed.
    tempo_type:     Unit of measurement of tempo. Example: "bpm".
    key:            Key of a string. Example: "Eb".
    transposition:  Key adjustment up or down. Integer value.
    verse_order:    The verse names in a specified order.
    variant:        A string describing differentiating it from other songs
                    with a common title.
    keywords:       
    copyright:      A copyright string.
    publisher:      A string value of the song publisher.
    version:        A custom song version, can be any arbitrary text
    """
    
    def __init__(self, parent=None):
        self.parent_song = parent
        # List types
        self.titles = []
        self.authors = []
        self.songbooks = []
        self.themes = []
        self.comments = []
        self.verse_order = []
        
        # String Types
        self.released = u''
        self.ccli_no = u''
        self.tempo = u''
        self.tempo_type = u''
        self.key = u''
        self.transposition = u'0'
        self.variant = u''
        self.keywords = u''
        self.copyright = u''
        self.publisher = u''
        self.version = u''
        
    def get_titles_by_lang(self, lang, translit=None):
        ret_titles = []
        for title in self.titles:
            if title.lang == lang and (translit is None or title.translit==translit):
                ret_titles.append(title)
        return ret_titles
    
    def get_themes_by_lang(self, lang, translit=None):
        ret_themes = []
        for theme in self.themes:
            if theme.lang == lang and (translit is None or theme.translit==translit):
                ret_themes.append(theme)
        return ret_themes
    
    def get_raw_verse_order(self):
        verses = []
        for verse in self.parent_song.verses:
            if verse.name not in verses:
                verses.append(verse.name)
        return verses
        
    def _from_xml(self, tree, namespace):
        """
        Load xml into the properties.
        """
        self.titles = []
        elem = tree.findall(_path(u'properties/titles/title',namespace))
        for el in elem:
            title = Title(_get_text(el), el.get(u'lang',None), el.get(u'translit',None))
            self.titles.append(title)
        
        self.authors = []
        elem = tree.findall(_path(u'properties/authors/author',namespace))
        for el in elem:
            author = Author(_get_text(el), el.get(u'type',None),
                            el.get(u'lang',None))
            self.authors.append(author)
        
        self.songbooks = []
        elem = tree.findall(_path(u'properties/songbooks/songbook',namespace))
        for el in elem:
            songbook = Songbook(el.get(u'name',None), el.get(u'entry',None))
            self.songbooks.append(songbook)
        
        self.themes = []
        elem = tree.findall(_path(u'properties/themes/theme',namespace))
        for el in elem:
            theme = Theme(_get_text(el), el.get(u'lang',None), el.get(u'translit',None))
            self.themes.append(theme)
        
        self.comments = []
        elem = tree.findall(_path(u'properties/comments/comment',namespace))
        for el in elem:
            self.comments.append(_get_text(el))
        
        elem = tree.find(_path(u'properties/copyright',namespace))
        if elem != None:
            self.copyright = _get_text(elem)
        
        elem = tree.find(_path(u'properties/ccliNo',namespace))
        if elem != None:
            self.ccli_no = _get_text(elem)
        
        elem = tree.find(_path(u'properties/released',namespace))
        if elem != None:
            self.released = _get_text(elem)
        
        elem = tree.find(_path(u'properties/tempo',namespace))
        if elem != None:
            self.tempo_type = elem.get(u'type',None)
            self.tempo = _get_text(elem)
        
        elem = tree.find(_path(u'properties/key',namespace))
        if elem != None:
            self.key = _get_text(elem)
        
        elem = tree.find(_path(u'properties/verseOrder',namespace))
        if elem != None:
            self.verse_order = _get_text(elem).strip().split()
        
        elem = tree.find(_path(u'properties/keywords',namespace))
        if elem != None:
            self.keywords = _get_text(elem)
        
        elem = tree.find(_path(u'properties/transposition',namespace))
        if elem != None:
            self.transposition = _get_text(elem)
        
        elem = tree.find(_path(u'properties/variant',namespace))
        if elem != None:
            self.variant = _get_text(elem)
        
        elem = tree.find(_path(u'properties/publisher',namespace))
        if elem != None:
            self.publisher = _get_text(elem)
        
        elem = tree.find(_path(u'properties/version',namespace))
        if elem != None:
            self.version = _get_text(elem)
    
    def _to_xml(self):
        """
        Convert the properties to XML.
        """
        props = etree.Element(u'properties')
        
        if len(self.titles):
            elem1 = etree.Element(u'titles')
            for t in self.titles:
                elem1.append(t._to_xml())
            props.append(elem1)
        
        if len(self.authors):
            elem1 = etree.Element(u'authors')
            for a in self.authors:
                elem1.append(a._to_xml())
            props.append(elem1)
        
        if len(self.songbooks):
            elem1 = etree.Element(u'songbooks')
            for s in self.songbooks:
                elem1.append(s._to_xml())
            props.append(elem1)
        
        if len(self.themes):
            elem1 = etree.Element(u'themes')
            for t in self.themes:
                elem1.append(t._to_xml())
            props.append(elem1)
        
        if len(self.comments):
            elem1 = etree.Element(u'comments')
            for c in self.comments:
                elem2 = etree.Element(u'comment')
                elem2.text = c
                elem1.append(elem2)
            props.append(elem1)
        
        if self.copyright:
            elem1 = etree.Element(u'copyright')
            elem1.text = self.copyright
            props.append(elem1)
        
        if self.ccli_no:
            elem1 = etree.Element(u'ccliNo')
            elem1.text = self.ccli_no
            props.append(elem1)
        
        if self.released:
            elem1 = etree.Element(u'releaseDate')
            elem1.text = self.released
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
            elem1.text = ' '.join(self.verse_order)
            props.append(elem1)
        
        if self.keywords:
            elem1 = etree.Element(u'keywords')
            elem1.text = self.keywords
            props.append(elem1)
        
        if self.transposition and not self.transposition == u'0':
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
        
        if self.version:
            elem1 = etree.Element(u'customVersion')
            elem1.text = self.version
            props.append(elem1)
        
        return props
    

class Title(object):
    """
    A title for the song.
    
    text:     The title as a string.
    lang:     A language code, in the format of "xx", or "xx-YY".
    translit: The language code that the Title is transliterated in
    """
    
    def __init__(self, text=u'', lang=None, translit=None):
        """
        Create the instance.
        """
        self.text = text
        self.lang = lang
        self.translit = translit
    
    def _to_xml(self):
        """
        Create the XML element.
        """
        elem = etree.Element(u'title')
        if self.lang:
            elem.set(u'lang', self.lang)
        if self.translit:
            elem.set(u'translit', self.translit)
        elem.text = self.text
        return elem
    
    def __str__(self):
        """
        Return a string representation.
        """
        return unicode(self).encode('UTF-8') 
    
    def __unicode__(self):
        """
        Return a unicode representation.
        """
        return self.text


class Author(object):
    """
    An author of words, music, or a translation.
    
    name:   Author's name as a string.
    type:   One of "words", "music", or "translation". This module will throw
            ValueError if one of these is found to be incorrect.
    lang:   A language code, in the format of "xx", or "xx-YY".
    """
    
    def __init__(self, name=u'', type_=None, lang=None):
        """
        Create the instance. May return `ValueError`.
        """
        self.name = name
        if type_ and type_ not in (u'words',u'music',u'translation'):
            raise ValueError(u'`type` must be one of "words", "music", or' +
                    '"translation".')
        self.type = type_
        self.lang = lang
    
    def _to_xml(self):
        """
        Convert the XML element.
        """
        elem = etree.Element(u'author')
        if self.type:
            elem.set(u'type',self.type)
            if self.type == u'translation' and self.lang:
                elem.set(u'lang',self.lang)
        elem.text = self.name
        return elem
    
    def __str__(self):
        """
        Return a string representation.
        """
        return unicode(self).encode('UTF-8') 
    
    def __unicode__(self):
        """
        Return a unicode representation.
        """
        return self.name


class Songbook(object):
    """
    A songbook/collection with an entry/number.
    
    name:  The name of the songbook or collection.
    entry: A number or string representing the index in this songbook.
    """
    
    def __init__(self, name=u'', entry=None):
        """
        Create the instance.
        """
        self.name = name
        self.entry = entry
    
    def _to_xml(self):
        """
        Create the XML element.
        """
        elem = etree.Element(u'songbook')
        if self.entry:
            elem.set(u'entry', self.entry)
        if self.name:
            elem.set(u'name', self.name)
        return elem
    
    def __str__(self):
        """
        Return a string representation.
        """
        return unicode(self).encode('UTF-8') 
    
    def __unicode__(self):
        """
        Return a unicode representation.
        """
        return u'%s #%s' % (self.name, self.entry)


class Theme(object):
    """
    A category for the song.
    
    theme: The name of the theme.
    lang:  A language code, in the format of "xx", or "xx-YY".
    """
    
    def __init__(self, name=u'', lang=None, translit=None):
        """
        Create the instance.
        """
        self.name = name
        self.lang = lang
        self.translit = translit
    
    def _to_xml(self):
        """
        Create the XML element.
        """
        elem = etree.Element(u'theme')
        if self.lang:
            elem.set(u'lang',self.lang)
        if self.translit:
            elem.set(u'translit',self.translit)
        elem.text = self.name
        return elem
    
    def __str__(self):
        """
        Return a string representation.
        """
        return unicode(self).encode('UTF-8') 
    
    def __unicode__(self):
        """
        Return a unicode representation.
        """
        return self.name

    
# Verse element and subelements

class Verse(object):
    """
    A verse for a song.
    """
    
    def __init__(self, name=None, lang=None, translit=None):
        """
        Create the instance.
        """
        self.lang = lang
        self.translit = translit
        self.name = name
        self.lines = [] #When I add this as argument to the constructor too,
                        #all Lines are in all verses. Don't know why.
    
    def _from_xml(self, tree, namespace):
        """
        Convert from XML.
        """
        self.name = tree.get(u'name', None)
        self.lang = tree.get(u'lang', None)
        self.translit = tree.get(u'translit', None)
        ct = 0
        for lines_elem in tree.findall(_path(u'lines', namespace)):
            ct +=1
            lines_ = Lines()
            lines_._from_xml(lines_elem, namespace)
            self.lines.append(lines_)
    
    def _to_xml(self):
        """
        Create the XML element.
        """
        verse = etree.Element('verse')
        if self.name:
            verse.set(u'name', self.name)
        if self.lang:
            verse.set(u'lang', self.lang)
        if self.translit:
            verse.set(u'translit', self.translit)
        lines_found = 0
        for lin in self.lines:
            verse.append(lin._to_xml())
            lines_found +=1
        return verse

    def __str__(self):
        return unicode(self).encode('UTF-8')

    def __unicode__(self):
        """
        Return a unicode representation.
        """
        return u''.join(unicode(l) for l in self.lines)
    
    def __len__(self):
        'Number of Lines'
        try:
            return len(self.lines[0].lines)
        except IndexError:
            return 0 #No Lines


class Lines(object):
    """
    A group of lines in a verse.
    """
    
    def __init__(self):
        """
        Create the instance.
        """
        self.lines = []
        self.part = u''
    
    def _from_xml(self, elem, namespace):
        """
        Convert from XML.
        """
        self.part = elem.get(u'part', u'')
        #self.lines.append(Line(elem.text)) #First line
        ct=1
        cur_line = elem.text
        for child in elem:
            ct+=1
            if child.tag == "{%s}br"%OLYR_NS: #Line break
                self.lines.append(Line(cur_line))
                cur_line = child.tail
            elif child.tail: # Skip <chord> and custom tags for now
                cur_line += child.tail
        
        self.lines.append(Line(cur_line)) #Create Line object for the last line
    
    def _to_xml(self):
        """
        Create the XML element.
        """
        lines_elem = etree.Element('lines')
        if self.part:
            lines_elem.set('part', self.part)
        ct = 0
        for line in self.lines:
            ct += 1
            if ct == 1: #First line
                lines_elem.text = line.markup
            else: # <br/> + next line
                br = etree.Element('br')
                br.tail = line.markup
                lines_elem.append(br)
        return lines_elem
    
    def __str__(self):
        """
        Return a string representation.
        """
        return unicode(self).encode('UTF-8')
    
    def __unicode__(self):
        """
        Return a unicode representation.
        """
        return u'\n'.join(unicode(l) for l in self.lines)
    
    def __len__(self):
        return len(self.lines)


# TODO add chords handling
class Line(object):
    """
    A single line in a group of lines.
    """
    
    def __init__(self, markup):
        """
        Create a line element.
        
        markup      A String containing the Line markup
        """
        self.markup = markup
    
    def _get_text(self):
        """
        Get the text for this line.
        """
        return self.markup.strip()
    
    def _set_text(self, value):
        """
        Set the text for this line. This removes all chords.
        """
        self.markup = value
    
    text = property(_get_text, _set_text)
    
    def __str__(self):
        """
        Return a string representation.
        """
        return unicode(self).encode('UTF-8')
    
    def __unicode__(self):
        """
        Return a unicode representation.
        """
        return self.text


# Various functions

def _path(tag, ns=None):
    """
    If a namespace is on a document, the XPath requires {ns}tag for every
    tag in the path. This assumes that only one namespace for the document
    exists.
    """
    if ns:
        return u'/'.join(u'{%s}%s' % (ns, t) for t in tag.split(u'/'))
    else:
        return tag


# FIXME simplify handling mixed content of XML
def _element_contents_to_string(elem):
    """
    Get a string representation of an XML Element, excluding the tag of the
    element itself.
    """
    s = u""
    if elem.text:
        s += _get_text(elem)
    if s == None:
        s = u""
    for sub in elem.getchildren():
        # Strip the namespace
        if sub.tag.partition("}")[2]:
            tag = sub.tag.partition("}")[2]
        else:
            tag = sub.tag
        subtag = ' '.join((tag,) + tuple('%s="%s"' % i for i in sub.items()))
        subtext = _element_contents_to_string(sub)
        if subtext:
            s += '<%(tag)s>%(text)s</%(tag)s>' % \
                    {"tag": subtag, 'text': subtext}
        else:
            s += "<%(tag)s />" % {'tag': subtag}
        if sub.tail:
            s += sub.tail
    return unicode(s)

def _get_text(elem):
    """
    Strip whitespace and return the element
    """
    if not elem.text:
        return ''
    return re.sub('\s+',' ',elem.text.strip())

