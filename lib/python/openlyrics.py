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
        'Title', 'Author', 'Songbook', 'Theme', 'Verse', 'Language', 'Line']

'''
Provides a module to access OpenLyrics data type.

Usage:
from openlyrics import Song
s = Song('song.xml')
'''

import re
from datetime import datetime
from xml.etree import cElementTree as etree
from StringIO import StringIO


OLYR_NS = u'http://openlyrics.info/namespace/2009/song'
OLYR_VERSION = u'0.7'
OLYR_CREATED_IN = u'OpenLyrics Python Library %s' % __version__
OLYR_MODIFIED_IN = u'OpenLyrics Python Library %s' % __version__


# TODO revise creating openlyrics Objects - add more arguments to contructor

# A few 

def fromstring(text):
    'Read from a string.'
    # unicode string must be passed as byte string encoded in utf-8
    if type(text) is unicode:
        text = text.encode('UTF-8')
    tree = etree.fromstring(text)
    song = Song()
    if tree:
        song._from_xml(tree)
    return song


def tostring(song, pretty_print=True, update_metadata=True):
    'Convert to a file.'
    tree = song._to_xml(pretty_print, update_metadata)
    text = etree.tostring(tree.getroot(), encoding='UTF-8')
    return unicode(text, 'UTF-8') # convert to unicode string


def parse(filename):
    'Read from the file.'
    tree = etree.parse(filename)
    song = Song(tree)
    return song


class OrderedDict(dict):

    def __init__(self, *args):
        self._keys = []
        super(OrderedDict, self).__init__(*args)

    def __delitem__(self, key):
        super(OrderedDict, self).__delitem__(key)
        self._keys.remove(key)

    def __setitem__(self, key, item):
        super(OrderedDict, self).__setitem__(key, item)
        if key not in self._keys: self._keys.append(key)

    def clear(self):
        super(OrderedDict, self).clear()
        self._keys = []

    def copy(self):
        dict_copy = super(OrderedDict, self).copy()
        dict_copy._keys = self._keys[:]
        return dict_copy

    def items(self):
       return zip(self._keys, self.values())

    def keys(self):
        return self._keys

    def pop(self):
        return self._keys

    def popitem(self):
        try:
            key = self._keys[-1]
        except IndexError:
            raise KeyError('dictionary is empty')

        val = self[key]
        del self[key]

        return (key, val)

    def setdefault(self, key, failobj = None):
        super(OrderedDict, self).setdefault(key, failobj)
        if key not in self._keys: self._keys.append(key)

    def update(self, d):
        super(OrderedDict, self).update(dict)
        for key in d.keys():
            if key not in self._keys: self._keys.apend(key)

    def values(self):
        return map(self.get, self._keys)


class Song(OrderedDict):
    '''
    Definition of an song. Song is an ordered dictionary with Verse objects.

    verse_order:      The verse names in a specified order.
    raw_verse_order:  The verse names in order as in XML file.
    '''
    
    def __init__(self, filename=None):
        'Create the instance.'
        super(Song, self).__init__()
        self.__ns = OLYR_NS
        self._version = OLYR_VERSION
        self.createdIn = OLYR_CREATED_IN
        self.modifiedIn = OLYR_MODIFIED_IN
        self.modifiedDate = u''

        self.verse_order = []
        
        self.props = Properties()

        if filename:
            self.parse(filename)

    def __setitem__(self, key, value):
        # new verse can be created from multiple types
        if type(value) in (str, unicode, list):
            value = Verse(value)
        super(Song, self).__setitem__(key, value)
    
    def parse(self, filename):
        'Read from the file.'
        tree = etree.parse(filename)
        self._from_xml(tree)
    
    def write(self, filename, pretty_print=True, update_metadata=True):
        'Save to a file.'
        tree = self._to_xml(pretty_print, update_metadata)
        # argument 'encoding' adds xml declaration like:
        # <?xml version='1.0' encoding='UTF-8'?>
        tree.write(filename, encoding=u'UTF-8')

    @property
    def raw_verse_order(self):
        'Read verse order as in XML'
        return self.keys()
    
    def _from_xml(self, tree):
        'Read from XML.'
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
        
        elem = root.find(_path(u'properties/verseOrder', self.__ns))
        if elem != None:
            self.verse_order = _get_text(elem).strip().split()
        
        for verse_elem in tree.findall(_path(u'lyrics/verse',self.__ns)):
            self._verse_from_xml(verse_elem)
    
    def _to_xml(self, pretty_print=True, update_metadata=True):
        'Convert to XML.'

        # for unit tests it's helpful to not update following items
        if update_metadata:
            self.modifiedIn = OLYR_MODIFIED_IN
            self.modifiedDate = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            self._version = OLYR_VERSION

        root = etree.Element(u'song')

        # attribuses are sorted in alphabetic order by ElementTree
        root.set(u'createdIn', self.createdIn)
        root.set(u'modifiedDate', self.modifiedDate)
        root.set(u'modifiedIn', self.modifiedIn)
        root.set(u'version', self._version)
        root.set(u'xmlns', self.__ns)
        
        props = self.props._to_xml()

        if self.verse_order:
            elem = etree.SubElement(props, u'verseOrder')
            elem.text = ' '.join(self.verse_order)
        
        root.append(props)
        
        # convert Verses
        lyrics_elem = etree.SubElement(root, u'lyrics')
        for n in self.raw_verse_order:
            # add default translation (unspecified)
            verse = self._verse_to_xml(n, self[n])
            lyrics_elem.append(verse)
            # add translations
            for l in self[n].langs:
                # add default transliteration (unspecified)
                verse = self._verse_to_xml(n, self[n].lang[l], l)
                lyrics_elem.append(verse)
                # Handle transliterations
                for t in self[n].lang[l].translits:
                    lines = self[n].lang[l].translit[t]
                    verse = self._verse_to_xml(n, lines, l, t)
                    lyrics_elem.append(verse)

        if pretty_print:
            self._indent(root)
        
        tree = etree.ElementTree(root)
        return tree

    def _verse_from_xml(self, tree):
        # Parse element 'song/lyrics/verse'
        name = tree.get(u'name', None)
        lang = tree.get(u'lang', None)
        trans = tree.get(u'translit', None) # transliteration name

        lines = []
        for ls_elem in tree.findall(_path(u'lines', self.__ns)):
            part = ls_elem.get(u'part', None)
            for l_elem in ls_elem.findall(_path(u'line', self.__ns)):
                line = Line(l_elem.text, part)
                lines.append(line)

        ## Find right place for text

        # Verse with 'name' does not exits - create one
        if self.get(name) is None: self[name] = Verse()
        position = self[name]

        # Text is translation
        if lang:
            # Verse 'name' does not have 'lang' translation - create one
            if position.lang.get(lang) is None:
                position.lang[lang] = Language()
            position = position.lang[lang]
            # Text is transliteration
            if trans:
                # Translation 'lang' does not have transliteration - create one
                if position.translit.get(trans) is None:
                    position.translit[trans] = [] # empty list
                position = position.translit[trans]
        # Add text to right position
        for l in lines: position.append(l)

    def _verse_to_xml(self, name, lines, lang=None, translit=None):
        'Create the XML element.'
        verse = etree.Element('verse')
        if name: verse.set(u'name', name)
        if lang: verse.set(u'lang', lang)
        if translit: verse.set(u'translit', translit)

        # init <lines> element
        part = lines[0].part
        ls_elem = etree.SubElement(verse, 'lines')
        if part: ls_elem.set('part', part)
        
        for line in lines:
            # start new <lines> section
            if part != line.part:
                part = line.part
                ls_elem = etree.SubElement(verse, 'lines')
                if part: ls_elem.set('part', part)
            l_elem = etree.SubElement(ls_elem, 'line')
            l_elem.text = line.text

        return verse

    # http://infix.se/2007/02/06/gentlemen-indent-your-xml
    def _indent(self, elem, level=0):
        'in-place prettyprint formatter'

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
       

class Properties(object):
    '''
    Stores Song property elements.
    
    titles:         A list of Title (class) objects.
    authors:        A list of Author (class) objects.
    songbooks:      A list of Songbook (class) objects, with a name and entry.
    themes:         A list of Theme (class) objects.
    comments:       A list of string comments
    
    release_date:   The date, in the format of yyyy-mm-ddThh:mm.
    ccli_no:        The CCLI number. Numeric or string value.
    tempo:          Numeric value of speed.
    tempo_type:     Unit of measurement of tempo. Example: "bpm".
    key:            Key of a string. Example: "Eb".
    transposition:  Key adjustment up or down. Integer value.
    variant:        A string describing differentiating it from other songs
                    with a common title.
    keywords:       
    copyright:      A copyright string.
    publisher:      A string value of the song publisher.
    custom_version: 
    '''
    def __init__(self):
        # List types
        self.titles = []
        self.authors = []
        self.songbooks = []
        self.themes = []
        self.comments = []
        
        # String Types
        self.release_date = u''
        self.ccli_no = u''
        self.tempo = u''
        self.tempo_type = u''
        self.key = u''
        self.transposition = u'0'
        self.variant = u''
        self.keywords = u''
        self.copyright = u''
        self.publisher = u''
        self.custom_version = u''

    def titles_by_lang(self, lang, translit=None):
        'Select titles only in one language.'
        return self._items_by_lang(self.titles, lang, translit)
        
    def themes_by_lang(self, lang, translit=None):
        'Select themes only in one language.'
        return self._items_by_lang(self.themes, lang, translit)

    def _items_by_lang(self, items, lang, translit):
        'Select titles or themes in one language.'
        selection = []
        for i in items:
            if i.lang == lang:
                if translit is None:
                    # transliteration doesn't matter
                    selection.append(i)
                elif i.translit == translit:
                    selection.append(i)
        return selection
        
    def _from_xml(self, tree, namespace):
        'Load xml into the properties.'
        self.titles = []
        elem = tree.findall(_path(u'properties/titles/title',namespace))
        for el in elem:
            title = Title(_get_text(el), el.get(u'lang',None),
                    el.get(u'translit',None))
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
            theme = Theme(_get_text(el), el.get(u'id',None),
                    el.get(u'lang',None), el.get(u'translit',None))
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
        
        elem = tree.find(_path(u'properties/releaseDate',namespace))
        if elem != None:
            self.release_date = _get_text(elem)
        
        elem = tree.find(_path(u'properties/tempo',namespace))
        if elem != None:
            self.tempo_type = elem.get(u'type',None)
            self.tempo = _get_text(elem)
        
        elem = tree.find(_path(u'properties/key',namespace))
        if elem != None:
            self.key = _get_text(elem)
        
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
        
        elem = tree.find(_path(u'properties/customVersion',namespace))
        if elem != None:
            self.custom_version = _get_text(elem)
    
    def _to_xml(self):
        'Convert the properties to XML.'
        props = etree.Element(u'properties')
        
        if len(self.titles):
            elem = etree.SubElement(props, u'titles')
            for t in self.titles:
                elem.append(t._to_xml())
        
        if len(self.authors):
            elem = etree.SubElement(props, u'authors')
            for a in self.authors:
                elem.append(a._to_xml())
        
        if len(self.songbooks):
            elem = etree.SubElement(props, u'songbooks')
            for s in self.songbooks:
                elem.append(s._to_xml())
        
        if len(self.themes):
            elem = etree.SubElement(props, u'themes')
            for t in self.themes:
                elem.append(t._to_xml())
        
        if len(self.comments):
            elem1 = etree.SubElement(props, u'comments')
            for c in self.comments:
                elem2 = etree.SubElement(elem1, u'comment')
                elem2.text = str(c)
        
        if self.copyright:
            elem = etree.SubElement(props, u'copyright')
            elem.text = str(self.copyright)
        
        if self.ccli_no:
            elem = etree.SubElement(props, u'ccliNo')
            elem.text = str(self.ccli_no)
        
        if self.release_date:
            elem = etree.SubElement(props, u'releaseDate')
            elem.text = str(self.release_date)
        
        if self.tempo:
            elem = etree.SubElement(props, u'tempo')
            if self.tempo_type:
                elem.set(u'type',self.tempo_type)
            elem.text = self.tempo
        
        if self.key:
            elem = etree.SubElement(props, u'key')
            elem.text = self.key
        
        if self.keywords:
            elem = etree.SubElement(props, u'keywords')
            elem.text = self.keywords
        
        if self.transposition and not self.transposition == u'0':
            elem = etree.SubElement(props, u'transposition')
            elem.text = self.transposition
        
        if self.variant:
            elem = etree.SubElement(props, u'variant')
            elem.text = self.variant
        
        if self.publisher:
            elem = etree.SubElement(props, u'publisher')
            elem.text = self.publisher
        
        if self.custom_version:
            elem = etree.SubElement(props, u'customVersion')
            elem.text = self.custom_version
        
        return props
    

class Title(object):
    '''
    A title for the song.
    
    text:  The title as a string.
    lang:  A language code, in the format of "xx", or "xx-YY".
    translit:  A transliteration language code, in the format of "xx",
                    or "xx-YY".
    '''
    
    def __init__(self, text=u'', lang=None, translit=None):
        'Create the instance.'
        self.text = text
        self.lang = lang
        self.translit = translit
    
    def _to_xml(self):
        'Create the XML element.'
        elem = etree.Element(u'title')
        if self.lang:
            elem.set(u'lang', self.lang)
        if self.translit:
            elem.set(u'translit', self.translit)
        elem.text = self.text
        return elem
    
    def __str__(self):
        'Return a string representation.'
        return unicode(self).encode('UTF-8') 
    
    def __unicode__(self):
        'Return a unicode representation.'
        return self.text


class Author(object):
    '''
    An author of words, music, or a translation.
    
    name:   Author's name as a string.
    type:   One of "words", "music", or "translation". This module will throw
            ValueError if one of these is found to be incorrect.
    lang:   A language code, in the format of "xx", or "xx-YY".
    '''
    
    def __init__(self, name=u'', type_=None, lang=None):
        'Create the instance. May return `ValueError`.'
        self.name = name
        if type_ and type_ not in (u'words',u'music',u'translation'):
            raise ValueError(u'`type` must be one of "words", "music", or' +
                    '"translator".')
        self.type = type_
        self.lang = lang
    
    def _to_xml(self):
        'Convert the XML element.'
        elem = etree.Element(u'author')
        if self.type:
            elem.set(u'type',self.type)
            if self.type == u'translator' and self.lang:
                elem.set(u'lang',self.lang)
        elem.text = self.name
        return elem
    
    def __str__(self):
        'Return a string representation.'
        return unicode(self).encode('UTF-8') 
    
    def __unicode__(self):
        'Return a unicode representation.'
        return self.name


class Songbook(object):
    '''
    A songbook/collection with an entry/number.
    
    name:  The name of the songbook or collection.
    entry: A number or string representing the index in this songbook.
    '''
    
    def __init__(self, name=u'', entry=None):
        'Create the instance.'
        self.name = name
        self.entry = entry
    
    def _to_xml(self):
        'Create the XML element.'
        elem = etree.Element(u'songbook')
        if self.entry:
            elem.set(u'entry',self.entry)
        elem.text = self.name
        return elem
    
    def __str__(self):
        'Return a string representation.'
        return unicode(self).encode('UTF-8') 
    
    def __unicode__(self):
        'Return a unicode representation.'
        return u'%s #%s' % (self.name, self.entry)


class Theme(object):
    '''
    A category for the song.
    
    theme: The name of the song.
    id:    A number from the standardized CCLI list.
                 http://www.ccli.com.au/owners/themes.cfm
    lang:  A language code, in the format of "xx", or "xx-YY".
    translit:  A transliteration language code, in the format of "xx",
                or "xx-YY".
    '''
    
    def __init__(self, name=u'', id=None, lang=None, translit=None):
        'Create the instance.'
        self.name = name
        self.id = id
        self.lang = lang
        self.translit = translit
    
    def _to_xml(self):
        'Create the XML element.'
        elem = etree.Element(u'theme')
        if self.id:
            elem.set(u'id',self.id)
        if self.lang:
            elem.set(u'lang',self.lang)
        if self.translit:
            elem.set(u'translit',self.translit)
        elem.text = self.name
        return elem
    
    def __str__(self):
        'Return a string representation.'
        return unicode(self).encode('UTF-8') 
    
    def __unicode__(self):
        'Return a unicode representation.'
        return self.name

    
# Verse element and subelements

class Verse(list):
    '''
    A verse for a song. A verse is a list of lines and with attribute
    containing translations.
    '''
    def __init__(self, text=[]):
        '''
        Verse can be created from several object types: str, unicode,
        list of str or unicode or list of Line()
        '''
        if type(text) in (str, unicode):
            text = text.splitlines()
        for l in text:
            if type(l) is not Line:
                l = Line(l)
            self.append(l)

        self.lang = LanguageDict()

    @property
    def langs(self):
        'Return available translations of verse.'
        return self.lang.keys()


class LanguageDict(dict):
    '''
    Allows parsing text of language or transliteration from several data types.
    '''
    def __setitem__(self, key, value):
        if type(value) in (str, unicode):
            value = value.splitlines()
        if type(value) is list:
            value = Language(value)
        super(LanguageDict, self).__setitem__(key, value)
  

class Language(list):
    '''
    A translation of a verse including also transliterations
    '''
    def __init__(self, text=[]):
        for l in text:
            if type(l) is not Line:
                l = Line(l)
            self.append(l)

        self.translit = TranslitDict()

    def __str__(self):
        return unicode(self).encode('UTF-8') 

    def __unicode__(self):
        'Return a unicode representation.'
        return u''.join(unicode(l) for l in self)

    @property
    def translits(self):
        '''Return available transliterations of current language.'''
        return self.translit.keys()


class TranslitDict(dict):
    '''
    Allows parsing text of transliteration from several data types.
    '''
    def __setitem__(self, key, value):
        if type(value) in (str, unicode):
            value = value.splitlines()
        lines = []
        for v in value:
            if v is not Line:
                v = Line(v)
            lines.append(v)
        super(TranslitDict, self).__setitem__(key, lines)


# TODO add chords handling - use good internal representation

class Line(object):
    '''
    A single line.
    '''
    def __init__(self, text=u'', part=None):
        '''Text can be string or unicode'''
        self.text = unicode(text)
        self.part = unicode(part) if type(part) is str else part
    
    def __str__(self):
        'Return a string representation.'
        return self.text.encode('UTF-8') 
    
    def __unicode__(self):
        'Return a unicode representation.'
        return self.text


# Various functions private classes



def _path(tag, ns=None):
    '''
    If a namespace is on a document, the XPath requires {ns}tag for every
    tag in the path. This assumes that only one namespace for the document
    exists.
    '''
    if ns:
        return u'/'.join(u'{%s}%s' % (ns, t) for t in tag.split(u'/'))
    else:
        return tag


# FIXME simplify handling mixed content of XML
#def _element_contents_to_string(elem):
    #'''
    #Get a string representation of an XML Element, excluding the tag of the
    #element itself.
    #'''
    #s = u""
    #if elem.text:
        #s += _get_text(elem)
    #if s == None:
        #s = u""
    #for sub in elem.getchildren():
        ## Strip the namespace
        #if sub.tag.partition("}")[2]:
            #tag = sub.tag.partition("}")[2]
        #else:
            #tag = sub.tag
        #subtag = ' '.join((tag,) + tuple('%s="%s"' % i for i in sub.items()))
        #subtext = _element_contents_to_string(sub)
        #if subtext:
            #s += '<%(tag)s>%(text)s</%(tag)s>' % \
                    #{"tag": subtag, 'text': subtext}
        #else:
            #s += "<%(tag)s />" % {'tag': subtag}
        #if sub.tail:
            #s += sub.tail
    #return unicode(s)

def _get_text(elem):
    'Strip whitespace and return the element'
    if not elem.text:
        return ''
    return re.sub('\s+',' ',elem.text.strip())

