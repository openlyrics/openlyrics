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


'''
Provides a module to access OpenLyrics data type.

Usage:
from openlyrics import Song
s = Song('song.xml')
'''

from datetime import datetime

try:
  from lxml import etree
except ImportError:
  try:
    # Python 2.5
    from xml.etree import cElementTree as etree
    print 'cElementTree'
  except ImportError:
    try:
      # Python 2.5
      from xml.etree import ElementTree as etree
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
        except ImportError:
          raise ImportError("No ElementTree Installation.")

class Song:
  '''
  Definition of an Opens song.
  
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
  variant:        A string describing differentiating it from other songs with a common title.
  keywords:       
  copyright:      A copyright string.
  publisher:      A string value of the song publisher.
  custom_version: 
  '''
  # List Types
  titles = None
  authors = None
  songbooks = None
  themes = None
  comments = None
  
  # String Types
  release_date = None
  ccli_no = None
  tempo = None
  tempo_type = None
  key = ""
  transposition = 0
  verse_order = None
  variant = ""
  keywords = "" # Should keywords be a list?
  copyright = None
  publisher = ""
  custom_version = None
  
  # Private Variables
  __ns = None
  _version = 0.7
  createdIn = ""
  modifiedIn = ""
  modifiedDate =""
  
  def __init__(self, file_ = None):
    'Create the instance.'
    self.titles = []
    self.authors = []
    self.songbooks = []
    self.themes = []
    self.comments = []
    
    if isinstance(file_, str) or isinstance(file_, file):
      self.from_xml(file_)
  
  def from_xml(self, file_):
    'Open the XML file.'
    tree = etree.parse(file_)
    
    
    root = tree.getroot()
    if "}" in root.tag:
      self.__ns = root.tag.split("}")[0].lstrip("{")
    self.createdIn = root.attrib.get("createdIn", None)
    self.modifiedIn = root.attrib.get("modifiedIn", None)
    self.modifiedDate = root.attrib.get("modifiedDate", None)
    
    self.titles = []
    elem = tree.findall(_path('properties/titles/title',self.__ns))
    for el in elem:
      title = Title(el.text, el.attrib.get("lang",None))
      self.titles.append(title)
    
    self.authors = []
    elem = tree.findall(_path('properties/authors/author',self.__ns))
    for el in elem:
      author = Author(el.text, el.attrib.get("type",None), el.attrib.get("lang",None))
      self.authors.append(author)
    
    self.songbooks = []
    elem = tree.findall(_path('properties/songbooks/songbook',self.__ns))
    for el in elem:
      songbook = Songbook(el.attrib.get("name",None), el.attrib.get("entry",None))
      self.songbooks.append(songbook)
    
    self.themes = []
    elem = tree.findall(_path('properties/themes/theme',self.__ns))
    for el in elem:
      theme = Theme(el.text, el.attrib.get("id",None), el.attrib.get("lang",None))
      self.themes.append(theme)
    
    self.comments = []
    elem = tree.findall(_path('properties/comments/comment',self.__ns))
    for el in elem:
      self.comments.append(el.text)
    
    elem = tree.find(_path('properties/copyright',self.__ns))
    if elem != None:
      self.copyright = elem.text
    
    elem = tree.find(_path('properties/ccliNo',self.__ns))
    if elem != None:
      self.ccli_no = elem.text
    
    elem = tree.find(_path('properties/releaseDate',self.__ns))
    if elem != None:
      self.release_date = elem.text
    
    elem = tree.find(_path('properties/tempo',self.__ns))
    if elem != None:
      self.tempo_type = elem.attrib.get("type",None)
      self.tempo = elem.text
    
    elem = tree.find(_path('properties/key',self.__ns))
    if elem != None:
      self.key = elem.text
    
    elem = tree.find(_path('properties/verseOrder',self.__ns))
    if elem != None:
      self.verse_order = elem.text
    
    elem = tree.find(_path('properties/keywords',self.__ns))
    if elem != None:
      self.keywords = elem.text
    
    elem = tree.find(_path('properties/transposition',self.__ns))
    if elem != None:
      self.transposition = elem.text
    
    elem = tree.find(_path('properties/variant',self.__ns))
    if elem != None:
      self.variant = elem.text
    
    elem = tree.find(_path('properties/publisher',self.__ns))
    if elem != None:
      self.publisher = elem.text
    
    elem = tree.find(_path('properties/customVersion',self.__ns))
    if elem != None:
      self.custom_version = elem.text
    
    #TODO: Verses
  
  def to_xml(self, file_, modifiedIn_ = modifiedIn):
    'Save to a file.'
    root = etree.Element('song')
    root.attrib['xmlns'] = self.__ns
    root.attrib['version'] = "0.7"
    root.attrib['createdIn'] = self.createdIn
    root.attrib['modifiedIn'] = modifiedIn_
    root.attrib['modifiedDate'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    
    
    props = etree.Element('properties')
    
    if len(self.titles):
      elem1 = etree.Element('titles')
      for t in self.titles:
        elem2 = etree.Element('title')
        if t.lang:
          elem2.attrib['lang'] = t.lang
        elem2.text = t.title
        elem1.append(elem2)
      props.append(elem1)
    
    if len(self.authors):
      elem1 = etree.Element('authors')
      for a in self.authors:
        elem2 = etree.Element('author')
        if a.type:
          elem2.attrib['type'] = a.type
          if a.type == 'translator' and a.lang:
            elem2.attrib['lang'] = a.lang
        elem2.text = a.author
        elem1.append(elem2)
      props.append(elem1)
    
    if len(self.songbooks):
      elem1 = etree.Element('songbooks')
      for s in self.songbooks:
        elem2 = etree.Element('songbook')
        if s.entry:
          elem2.attrib['entry'] = s.entry
        elem2.text = s.name
        elem1.append(elem2)
      props.append(elem1)
    
    if len(self.themes):
      elem1 = etree.Element('themes')
      for t in self.themes:
        elem2 = etree.Element('theme')
        if t.id:
          elem2.attrib['id'] = t.id
        if t.lang:
          elem2.attrib['lang'] = t.lang
        elem2.text = t.theme
        elem1.append(elem2)
      props.append(elem1)
    
    if len(self.comments):
      elem1 = etree.Element('comments')
      for c in self.comments:
        elem2 = etree.Element('comment')
        elem2.text = str(c)
        elem1.append(elem2)
      props.append(elem1)
    
    if self.copyright:
      elem1 = etree.Element('copyright')
      elem1.text = str(self.copyright)
      props.append(elem1)
    
    if self.ccli_no:
      elem1 = etree.Element('ccliNo')
      elem1.text = str(self.ccli_no)
      props.append(elem1)
    
    if self.release_date:
      elem1 = etree.Element('releaseDate')
      elem1.text = str(self.release_date)
      props.append(elem1)
    
    if self.tempo:
      elem1 = etree.Element('tempo')
      if self.tempo_type:
        elem1.attrib['type'] = self.tempo_type
      elem1.text = self.tempo
      props.append(elem1)
    
    if self.key:
      elem1 = etree.Element('key')
      elem1.text = self.key
      props.append(elem1)
    
    if self.verse_order:
      elem1 = etree.Element('verseOrder')
      elem1.text = self.verse_order
      props.append(elem1)
    
    if self.keywords:
      elem1 = etree.Element('keywords')
      elem1.text = self.keywords
      props.append(elem1)
    
    if self.transposition:
      elem1 = etree.Element('transposition')
      elem1.text = self.transposition
      props.append(elem1)
    
    if self.variant:
      elem1 = etree.Element('variant')
      elem1.text = self.variant
      props.append(elem1)
    
    if self.publisher:
      elem1 = etree.Element('publisher')
      elem1.text = self.publisher
      props.append(elem1)
    
    if self.custom_version:
      elem1 = etree.Element('customVersion')
      elem1.text = self.custom_version
      props.append(elem1)
    
    root.append(props)
    
    #TODO: Verses
    
    tree = etree.ElementTree(root)

    # lxml implements pretty printing
    # argument 'encoding' adds xml declaration: <?xml version='1.0' encoding='UTF-8'?>
    try:
      tree.write(file_, encoding='UTF-8', pretty_print=True)
    except TypeError:
      # TODO: implement pretty_print for other ElementTree API implementations
      tree.write(file_, encoding='UTF-8')
  



class Title:
  '''
  A title for the song.
  
  title: The title as a string.
  lang:  A language code, in the format of "xx", or "xx-YY".
  '''
  title = None
  lang = None
  
  def __init__(self, title = None, lang = None):
    'Create the instance.'
    self.title = title
    self.lang = lang
  
  def __str__(self):
    'Return a string representation of this class.'
    return self.title
  
  def __unicode__(self):
    'Return a unicode representation of this class.'
    return self.title


class Author:
  '''
  An author of words, music, or a translation.
  
  author: Author's name as a string.
  type:   One of "words", "music", or "translation". This module will throw ValueError if one
          of these is found to be incorrect.
  lang:   A language code, in the format of "xx", or "xx-YY".
  '''
  author = None
  type = None
  lang = None
  
  def __init__(self, author = None, type = None, lang = None):
    'Create the instance. May return `ValueError` on incorrect `type` argument.'
    self.author = author
    if type not in ('words','music','translation', None):
      raise ValueError('`type` must be one of \"words\", \"music\", or \"translator\".')
    self.type = type
    self.lang = lang
  
  def __str__(self):
    'Return a string representation of this class.'
    return self.author
  
  def __unicode__(self):
    'Return a unicode representation of this class.'
    return self.author


class Songbook:
  '''
  A songbook/collection with an entry/number.
  
  name:  The name of the songbook or collection.
  entry: A number or string representing the index in this songbook.
  '''
  name = None
  entry = None
  
  def __init__(self, name = None, entry = None):
    'Create the instance.'
    self.name = name
    self.entry = entry
  
  def __str__(self):
    'Return a string representation of this class.'
    return '%s #%s' % (self.name, self.entry)
  
  def __unicode__(self):
    'Return a unicode representation of this class.'
    return '%s #%s' % (self.name, self.entry)


class Theme:
  '''
  A category for the song.
  
  theme: The name of the song.
  id:    A number from the standardized CCLI list.
         http://www.ccli.com.au/owners/themes.cfm
  lang:  A language code, in the format of "xx", or "xx-YY".
  '''
  theme = None
  id = None
  lang = None
  
  def __init__(self, theme = None, id = None, lang = None):
    'Create the instance.'
    self.theme = theme
    self.id = id
    self.lang = lang
  
  def __str__(self):
    'Return a string representation of this class.'
    return self.theme
  
  def __unicode__(self):
    'Return a unicode representation of this class.'
    return self.theme



def _path(tag, ns = None):
  'If a namespace is on a document, the XPath requires {ns}tag for every tag in the path.\
  This assumes that only one namespace for the document exists.'
  if ns == None or len(ns) == 0:
    return tag
  else:
    return "/".join("{%s}%s" % (ns, t) for t in tag.split("/"))
