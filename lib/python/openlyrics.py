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

try:
  from lxml import etree
except ImportError:
  try:
    # Python 2.5
    from xml.etree import cElementTree as etree
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

def _path(tag, ns = None):
  'If a namespace is on a document, the XPath requires {ns}tag for every tag in the path.\
  This assumes that only one namespace for the document exists.'
  if ns == None or len(ns) == 0:
    return tag
  else:
    return "/".join("{%s}%s" % (ns, t) for t in tag.split("/"))

class Song:
  '''
  Definition of an Opens song.
  
  titles:         A list of Title (class) objects.
  authors:        A list of Author (class) objects.
  release_date:   The date, in the format of yyyy-mm-ddThh:mm.
  copyright:      A copyright string.
  ccli_no:        The CCLI number. Numeric or string value.
  transposition:  Key adjustment up or down. Integer value.
  tempo:          Numeric value of speed.
  tempo_type:     Unit of measurement of tempo. Example: "bpm".
  key:            Key of a string. Example: "Eb".
  variant:        A string describing differentiating it from other songs with a common title.
  publisher:      A string value of the song publisher.
  custom_version: 
  verse_order:    The verse names in a specific order.
  keywords:       
  songbooks:      A list of Songbook (class) objects, with a name and entry.
  themes:         
  comments:       
  '''
  # List Types
  _titles = None
  _authors = None
  _songbooks = None
  _themes = None
  comments = None
  
  # String Types
  _release_date = None
  _ccli_no = None
  _tempo = None
  _tempo_type = None
  _key = ""
  _transposition = 0
  _variant = ""
  _verse_order = None
  keywords = "" # Should keywords be a list?
  themes = None
  copyright = None
  publisher = ""
  custom_version = None
  
  # Private Variables
  __ns = None
  
  def __init__(self, file_ = None):
    'Create the instance.'
    self._titles = []
    self._authors = []
    self._songbooks = []
    self._themes = []
    self.comments = []
    
    if isinstance(file_, str) or isinstance(file_, file):
      self.open_file(file_)
  
  def open_file(self, file_):
    'Open the XML file.'
    tree = etree.parse(file_)
    
    
    roottag = tree.getroot().tag
    if "}" in roottag:
      self.__ns = roottag.split("}")[0].lstrip("{")
    
    elem = tree.findall(_path('properties/titles/title',self.__ns))
    for el in elem:
      title = Title(el.text, el.attrib.get("lang",None))
      self._titles.append(title)
    
    elem = tree.findall(_path('properties/authors/author',self.__ns))
    for el in elem:
      author = Author(el.text, el.attrib.get("type",None), el.attrib.get("lang",None))
      self._authors.append(author)
    
    elem = tree.findall(_path('properties/songbooks/songbook',self.__ns))
    for el in elem:
      songbook = Songbook(el.text, el.attrib.get("entry",None))
      self._songbooks.append(songbook)
    
    elem = tree.findall(_path('properties/themes/theme',self.__ns))
    for el in elem:
      theme = Theme(el.text, el.attrib.get("id",None), el.attrib.get("lang",None))
      self._themes.append(theme)
    
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
      self._release_date = elem.text
    
    elem = tree.find(_path('properties/tempo',self.__ns))
    if elem != None:
      self._tempo_type = elem.attrib.get("type",None)
      self._tempo = elem.text
    
    elem = tree.find(_path('properties/key',self.__ns))
    if elem != None:
      self._key = elem.text
    
    elem = tree.find(_path('properties/verseOrder',self.__ns))
    if elem != None:
      self._verse_order = elem.text
    
    elem = tree.find(_path('properties/keywords',self.__ns))
    if elem != None:
      self.keywords = elem.text
    
    elem = tree.find(_path('properties/transposition',self.__ns))
    if elem != None:
      self._transposition = elem.text
    
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
    

class Title:
  '''
  An instance of a title for Opens.
  
  title:  The title as a string.
  lang:  A language code, in the format of "xx", or "xx-YY".
  '''
  title = None
  lang = None
  
  def __init__(self, title = None, lang = None):
    'Create the instance.'
    self.title = title
    self.lang = lang
  
  def __str__(self):
    return self.title
  def __unicode__(self):
    return self.title


class Author:
  '''
  An instance of an author for Opens.
  
  author:  Author's name as a string.
  type:  One of "words", "music", or "translation". This module will throw ValueError if one
    of these is found to be incorrect.
  lang:  A language code, in the format of "xx", or "xx-YY".
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
    return self.author
  def __unicode__(self):
    return self.author


class Songbook:
  '''
  A songbook for Opens.
  
  name:  The name of the songbook or collection.
  entry:  A number or string representing the index in this songbook.
  '''
  name = None
  entry = None
  
  def __init__(self, name = None, entry = None):
    'Create the instance.'
    self.name = name
    self.entry = entry
  
  def __str__(self):
    return '%s #%s' % (self.name, self.entry)
  def __unicode__(self):
    return '%s #%s' % (self.name, self.entry)


class Theme:
  '''
  A category for the song.
  
  theme:  The name of the song.
  id:  A number from the standardized CCLI list.
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
    return self.theme
  def __unicode__(self):
    return self.theme

