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
  '''
  __ns = ""
  __titles = None
  __authors = None
  __copyright = ""
  __ccli_no = ""
  __release_date = ""
  __transposition = 0
  __tempo = None
  __tempo_type = None
  __key = ""
  __variant = ""
  __publisher = ""
  __custom_version = ""
  __verse_order = None
  # Should keywords be a list?
  __keywords = ""
  __songbooks = None
  __themes = None
  __comments = None
  
  def __init__(self, file_ = None):
    'Create the instance.'
    self.__titles = []
    self.__authors = []
    self.__songbooks = []
    self.__themes = []
    self.__comments = []
    
    if isinstance(file_, str) or isinstance(file_, file):
      self.open_file(file_)
  
  def open_file(self, file_):
    'Open the XML file.'
    tree = etree.parse(file_)
    
    
    roottag = tree.getroot().tag
    if "}" in roottag:
      self.__ns = roottag.split("}")[0].lstrip("{")
    
    # TODO: Titles
    
    # TODO: Authors
    
    el = tree.find(_path('properties/copyright',self.__ns))
    if el != None:
      self.__copyright = el.text
    
    el = tree.find(_path('properties/ccliNo',self.__ns))
    if el != None:
      self.__ccli_no = el.text
    
    el = tree.find(_path('properties/releaseDate',self.__ns))
    if el != None:
      self.__release_date = el.text
    
    el = tree.find(_path('properties/tempo',self.__ns))
    if el != None:
      self.__tempo_type = el.attrib.get("type",None)
      self.__tempo = el.text
    
    el = tree.find(_path('properties/key',self.__ns))
    if el != None:
      self.__key = el.text
    
    el = tree.find(_path('properties/verseOrder',self.__ns))
    if el != None:
      self.__verse_order = el.text
    
    el = tree.find(_path('properties/keywords',self.__ns))
    if el != None:
      self.__keywords = el.text
    
    el = tree.find(_path('properties/transposition',self.__ns))
    if el != None:
      self.__transposition = el.text
    
    el = tree.find(_path('properties/variant',self.__ns))
    if el != None:
      self.__variant = el.text
    
    el = tree.find(_path('properties/publisher',self.__ns))
    if el != None:
      self.__publisher = el.text
    
    el = tree.find(_path('properties/customVersion',self.__ns))
    if el != None:
      self.__custom_version = el.text
    
    #TODO: Songbooks
    
    #TODO: Themes
    
    #TODO: Comments
    
    #TODO: s
    

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
    if type not in ('words','music','translation'):
      raise ValueError('`type` must be one of \"words\", \"music\", or \"translator\".')
    self.type = type
    self.lang = lang


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

