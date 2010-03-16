#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# Copyright (c) 2010 The OpenLyrics Authors.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
#

# History:
# 0.3
# - map some opensong themes to ccli counterparts
# - try add theme id if possible
# - detect vertical bar '|' in a line
# - parse chords
#
# 0.2
# - xml schema definition is red from external file
# - script moved to OpenLyrics trunk
#
# 0.1

__version__ = '0.3'

'''
Convert an OpenSong song to OpenLyrics format.

Not Parsed:
    <timesig>
    advanced lyrics formating (like chords for mutiple verses)

Parsed lyrics:
    verse names [V1], ...
    text lines (lines beginning with space)
    text lines containing vertical bar '|'
    themes (separated by ';' and ccli theme id is added)
    chords

Format version:
    OpenSong 1.5.1
    OpenLyrics 0.7

Usage:

    python opensong2openlyrics.py  opensong_file  openlyrics_file.xml
'''

import locale
import os.path
import sys

try:
    from lxml import etree
except ImportError:
    print 'lxml python module required, please install it.'
    print 'http://pypi.python.org/pypi/lxml/'
    exit(1)


NAMESPACE = 'http://openlyrics.info/namespace/2009/song'
OPENLYRICS_VER = '0.7'

SCRIPTPATH = os.path.dirname(unicode(__file__, locale.getpreferredencoding()))
SCHEMAFILE = os.path.join(SCRIPTPATH, '..', 'openlyrics.rng')

CCLITHEMES_FILE = os.path.join(SCRIPTPATH, '..', 'themelist.txt')
CCLITHEMES = []
for item in open(CCLITHEMES_FILE, 'r').readlines():
    CCLITHEMES.append(item.strip())


# try to map OpenSong theme to ccli
def map_to_ccli_themes(name):
    if name == "Christ: Attributes" : 
        map = ['Christ']
    elif name == "Christ: Birth" : 
        map = ['Seasonal / Christmas']
    elif name == "Christ: Death/Atonement" : 
        map = ['Atonement']
    elif name == "Christ: Power/Majesty" : 
        map = ["God's Attributes / Power", "God's Attributes / Majesty"]
    elif name == "Christ: Love/Mercy" : 
        map = ['Love', 'Mercy']
    elif name == "Christ: Resurrection" : 
        map = ['Resurrection']
    elif name == "Christ: Second Coming" : 
        map = ['Second Coming']
    elif name == "Christ: Victory" : 
        map = ['Victory']
    elif name == "Church: Commitment/Obedience" : 
        map = ['Commitment', 'Obedience']
    elif name == "Church: Country" : 
        map = ['Country']
    elif name == "Church: Eternal Life/Heaven" : 
        map = ['Eternal Life', 'Heaven']
    elif name == "Church: Evangelism" : 
        map = ['Evangelism']
    elif name == "Church: Family/Fellowship" : 
        map = ['Family', 'Fellowship']
    elif name == "Church: Fellowship w/ God" : 
        map = ['Fellowship']
    elif name == "Church: Purity/Holiness" : 
        map = ['Cleansing', 'Holiness']
    elif name == "Church: Repentance/Salvation" : 
        map = ['Repentance', 'Salvation']
    elif name == "Church: Renewal" : 
        map = ['Renewal']
    elif name == "Church: Service/Ministry" : 
        map = ['Service ']
    elif name == "Church: Spiritual Hunger" : 
        map = ['Spiritual Hunger']
    elif name == "Fruit: Faith/Hope" : 
        map = ['Faith', 'Hope']
    elif name == "Fruit: Love" : 
        map = ['Love']
    elif name == "Fruit: Joy" : 
        map = ['Joy']
    elif name == "Fruit: Peace/Comfort" : 
        map = ['Peace']
    elif name == "Fruit: Patience/Kindness" : 
        map = ['Patience', 'Kindness']
    elif name == "Fruit: Humility/Meekness" : 
        map = ['Humility']
    elif name == "God: Attributes" : 
        map = ["God's Attributes"]
    elif name == "God: Creator/Creation" : 
        map = ['Creator', 'Creation']
    elif name == "God: Father" : 
        map = ["God's Attributes / Father"]
    elif name == "God: Guidance/Care" : 
        map = ['Guidance', 'Care']
    elif name == "God: Holy Spirit" : 
        map = ['Holy Spirit']
    elif name == "God: Holiness" : 
        map = ['Holiness']
    elif name == "God: Love/Mercy" : 
        map = ["God's Attributes / Love", "God's Attributes / Mercy"]
    elif name == "God: Power/Majesty" : 
        map = ["God's Attributes / Power", "God's Attributes / Majesty"]
    elif name == "God: Promises" : 
        map = ['Promise']
    elif name == "God: Victory" : 
        map = ['Victory']
    elif name == "God: Word" : 
        map = ["God's Word"]
    elif name == "Worship: Assurance/Trust" : 
        map = ['Assurance', 'Trust']
    elif name == "Worship: Call/Opening" : 
        map = ['Call', 'Opening']
    elif name == "Worship: Celebration" : 
        map = ['Celebration']
    elif name == "Worship: Declaration" : 
        map = ['Declaration']
    elif name == "Worship: Intimacy" : 
        map = ['Intimacy']
    elif name == "Worship: Invitation" : 
        map = ['Invitation']
    elif name == "Worship: Praise/Adoration" : 
        map = ['Praise', 'Adoration ']
    elif name == "Worship: Prayer/Devotion" : 
        map = ['Prayer', 'Devotion']
    elif name == "Worship: Provision/Deliverance" : 
        map = ['Provision', 'Deliverance']
    elif name == "Worship: Thankfulness":
        map = ['Thankfulness']
    else:
        map = [name]

    return map



class LyricsParser(object):

    def __init__(self):
        pass

    # public API

    def parse(self, os_lyrics):
        tree = etree.Element('lyrics')
        lines = os_lyrics.splitlines()
        
        # line with chords (line starts with '.'
        linechords = None

        for line in lines:
            if line.startswith('['):
                versename = line.strip().strip('[]')
                self._add_verse(tree, versename)
            elif line.startswith('.'):
                linechords = line.strip().lstrip('.') # remove leading '.'
            elif line.startswith(' '):
                line = line.strip()
                self._add_line(tree, line, linechords)
                # init chord line for another line with text
                linechords = None

        return tree

    # other methods

    def _add_verse(self, tree, versename):
        versename = versename.lower()
        vtag = etree.SubElement(tree, 'verse')
        vtag.set('name', versename)

    def _parse_line(self, text, linechords):
        '''
        Example of a line with chords:
            .D     Bm    A  D   G          D
             Holy, holy, ho_ly, Lord God Almighty,
        OpenLyrics:
            <chord name="D"/>Holy, <chord name="Bm">holy, \
            <chord name="A"/>ho<chord name="G"/>ly, \
            <chord name="G"/>Lord God Al<chord name="D"/>mighty,

        Works even if 'linechords' is an empty string.
        '''
        if not linechords:
            linechords = ''
        # parse chords and remember position of a chord
        chords = {} # empty dict
        i = 0
        prev = ' ' # previous character
        curr = ' ' # current character
        key = None #  position for current chords (when chord consists of more letters)
        while i < len(linechords):
            curr = linechords[i]
            # start a new chord
            if prev == ' ' and curr != ' ':
                key = i
                chords[key] = curr
            # continue with a chord
            elif curr != ' ':
                chords[key] += curr

            prev = curr
            i += 1

        #print(chords)

        # dict type is not sorted
        keys = chords.keys()
        keys.sort()
        #print 'keys', keys

        # construct xml tree with chords
        root = etree.Element('line')
        for key in keys:
            # add chord tags
            elem = etree.SubElement(root, 'chord')
            elem.set('name', chords[key])

        #print(etree.tostring(root))
            
        # split text to snippets
        snippets = []
        id1 = 0
        id2 = 0
        for k in keys:
            id2 = k
            snippets.append(text[id1:id2])
            id1 = id2
        snippets.append(text[id1:]) # last snippet

        #print(snippets)

        # remove underscores '_' - are used in opensong format
        temp = []
        for s in snippets:
            clean = ''
            for char in s:
                if char != '_':
                    clean += char
            temp.append(clean)
        snippets = temp

        #print(snippets)

        # assign text snippets to chords in xml structure
        root.text = snippets.pop(0)
        for chord_elem in root.getchildren():
            chord_elem.tail = snippets.pop(0)

        #print(etree.tostring(root))

        return root

    def _add_line(self, tree, linetext, chords):
        # ignore empty line
        if not linetext.strip():
            return

        # vertical bar '|' means in opensong new line of text for presentation
        texts = linetext.split('|')
        chordlines = [''] * len(texts) # init chordlines to empty strings
        # add chords to line if chords are available
        if chords:
            offset = 0
            for i in range(len(texts)):
                length = len(texts[i])
                chordlines[i] = chords[offset : offset+length]
                offset += length + 1
                #print(chordlines[i])
        
        #print(chordlines)

        # create element <lines> if necessary
        last_verse_tree = tree[-1]
        if len(last_verse_tree) == 0: # no subelement <lines>
            lines_tree = etree.SubElement(last_verse_tree, 'lines')
        else:
            lines_tree = last_verse_tree[-1] # last subelement <lines>
        
        # parse lines and create xml structure
        for i in range(len(texts)):
            line_tree = self._parse_line(texts[i], chordlines[i])
            lines_tree.append(line_tree)


class OpenLyricsConverter(object):

    def __init__(self, opensong_file):
        print('Parsing...')
        parser = etree.XMLParser(remove_blank_text=True)
        self.osong = etree.parse(opensong_file)
        self.olyrics = etree.ElementTree(etree.Element('song'))

    # public API
        
    def convert(self):
        print('Converting...')
        osong = self.osong.getroot()
        olyrics = self.olyrics.getroot()
        olprop = etree.SubElement(olyrics, 'properties')

        # properties
        self._copy_subelement(osong, 'title', olprop, 'titles', 'title')
        self._copy_subelement(osong, 'aka', olprop, 'titles', 'title')
        self._conv_author(osong, olprop)
        self._copy_element(osong, 'copyright', olprop, 'copyright')
        self._copy_element(osong, 'ccli', olprop, 'ccliNo')
        self._copy_element(osong, 'capo', olprop, 'transposition')
        self._conv_tempo(osong, 'tempo', olprop, 'tempo')
        self._copy_element(osong, 'key', olprop, 'key')
        self._copy_element(osong, 'key_line', olprop, 'keywords')
        self._conv_verseorder(osong, 'presentation', olprop, 'verseOrder')
        self._copy_element(osong, 'hymn_number', olprop, 'trackNo')
        self._conv_themes(osong, 'theme', olprop)
        self._conv_themes(osong, 'alttheme', olprop)
        self._copy_subelement(osong, 'user1', olprop, 'comments', 'comment')
        self._copy_subelement(osong, 'user2', olprop, 'comments', 'comment')
        self._copy_subelement(osong, 'user3', olprop, 'comments', 'comment')


        # other 
        self._conv_lyrics(osong, olyrics)
        self._set_metadata(olyrics)

    def save(self, openlyrics_file):
        print('Saving...')
        # write openlyrics
        self.olyrics.write(openlyrics_file, encoding='utf-8', pretty_print=True,
                xml_declaration=True)

    def validate(self, ol_file, relaxng_schema):
        print('Validating...')
        tree = etree.parse(ol_file)
        schema = etree.RelaxNG(relaxng_schema)
        schema.assertValid(tree)

    # other methods

    def _copy_element(self, os_tree, os_elem, ol_tree, ol_elem):
        '''
        Add content from element in one tree into element
        in another tree. Element in another tree are created.
        
        return  tree element with copied content or None when element not
                present or empty content
        '''
        orig_elem = os_tree.find(os_elem)
        # OpenLyrics specification doesn't allow elements with emtpy content.
        if orig_elem is None or not orig_elem.text:
            elem = None
        else:
            elem = etree.SubElement(ol_tree, ol_elem)
            elem.text = orig_elem.text
        return elem

    def _copy_subelement(self, os_tree, os_elem, ol_tree, ol_elem, ol_subelem):
        '''
        Add content from element in one tree into subelement
        in another tree. Element and/or subelement in another
        tree are created.
        
        return  etree element with copied content or None when element not
                present or empty content
        '''
        orig_elem = os_tree.find(os_elem)
        if orig_elem is None or not orig_elem.text:
            elem = None
        else:
            elem = ol_tree.find(ol_elem)
            # no previous subelement
            if elem is None:
                elem = etree.SubElement(ol_tree, ol_elem)
            elem = etree.SubElement(elem, ol_subelem)
            elem.text = orig_elem.text
        return elem

    def _conv_author(self, os_tree, ol_tree):
        text = os_tree.find('author')
        # existing element
        if text is not None:
            return
        # not empty - continue
        text = text.text
        if not text:
            return
        
        text = text.strip()
        authors = []
        # more names are usually separated by ',', ';', '&' or 'and'
        for a in text.split(','):
            for b in a.split(';'):
                for c in b.split('&'):
                    for d in c.split('and'):
                        d = d.strip()
                        if d: authors.append(d)
        # add authors to openlyrics structure
        elem = etree.SubElement(ol_tree, 'authors')
        for author in authors:
            subelem = etree.SubElement(elem, 'author')
            subelem.text = author
        


    def _conv_verseorder(self, os_tree, os_elem, ol_tree, ol_elem):
        elem = self._copy_element(os_tree, os_elem, ol_tree, ol_elem)
        # verseOrder in lowercase
        if elem is not None:
            elem.text = elem.text.lower()

    # TODO implement
    def _conv_tempo(self, os_tree, os_elem, ol_tree, ol_elem):
        orig_elem = os_tree.find(os_elem)
        if orig_elem is None or not orig_elem.text:
            return
        # bpm value
        try:
            int(orig_elem.text.strip())
            type = 'bpm'
        # text value
        except ValueError:
            type = 'text'
        elem = etree.SubElement(ol_tree, ol_elem)
        elem.set('type', type)
        elem.text = orig_elem.text

    # TODO implement
    def _conv_themes(self, os_tree, os_elem, ol_tree):
        os_elem = os_tree.find(os_elem)
        if os_elem is not None and os_elem.text is not None:

            # themes are sometimes separated by semicolon
            theme_list = os_elem.text.split(';')
            # remove white spaces and empty items
            cleaned_list = []
            for theme in theme_list:
                theme = theme.strip()
                if theme:
                    cleaned_list.append(theme)

            ## construct xml tree
            themes_elem = ol_tree.find('themes')
            # no previous element <themes>
            if themes_elem is None:
                themes_elem = etree.SubElement(ol_tree, 'themes')
            for theme in cleaned_list:
                # OpenSong theme could be mapped to more themes
                ths = map_to_ccli_themes(theme)
                for t in ths:
                    t = t.strip()
                    elem = etree.SubElement(themes_elem, 'theme')
                    elem.text = t
                    # if ccli theme - add 'ID' attribute (index ccli theme list)
                    try:
                        id = CCLITHEMES.index(t)
                        elem.set('id', unicode(id + 1)) # indexing beginns with '1'
                    except ValueError:
                        pass
                    

    def _conv_lyrics(self, os_tree, ol_tree):
        text = os_tree.find('lyrics').text
        parser = LyricsParser()
        lyrics_tree = parser.parse(text)
        ol_tree.append(lyrics_tree)

    def _set_metadata(self, ol_root):
        from datetime import datetime
        ol_root.set('xmlns', NAMESPACE)
        ol_root.set('version', OPENLYRICS_VER)
        progname = '%s %s' % (os.path.basename(__file__), __version__)
        ol_root.set('createdIn', progname)
        ol_root.set('modifiedIn', progname)
        ol_root.set('modifiedDate', datetime.utcnow().isoformat())


def main(): 
    
    if len(sys.argv) != 3:
        print('Usage:')
        print('  python %s opensong_file  openlyrics_file.xml' % __file__)
        exit(1)
    
    else:
        opensong_file = sys.argv[1]
        openlyrics_file = sys.argv[2]
        if not os.path.exists(opensong_file):
            print('ERROR: File %s does not exists.' % opensong_file)
            exit(2)
        if os.path.exists(openlyrics_file):
            print('ERROR: File %s already exists.' % openlyrics_file)
            exit(3)

        converter = OpenLyricsConverter(opensong_file)
        converter.convert()
        converter.save(openlyrics_file)
        schema = etree.parse(SCHEMAFILE)
        converter.validate(openlyrics_file, schema.getroot())



if __name__ == '__main__':
    main()

