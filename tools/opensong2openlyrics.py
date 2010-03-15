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
# 0.2
# - xml schema definition is red from external file
# - script moved to OpenLyrics trunk
#
# 0.1

__version__ = '0.2'

'''
Convert an OpenSong song to OpenLyrics format.

Not Parsed:
    <timesig>
    advanced lyrics formating (like chords, etc)

Parsed lyrics:
    verse names [V1], ...
    text lines (lines beginning with space)

Format version:
    OpenSong 1.5.1
    OpenLyrics 0.6

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
OPENLYRICS_VER = '0.6'

SCRIPTPATH = os.path.dirname(unicode(__file__, locale.getpreferredencoding()))
SCHEMAFILE = os.path.join(SCRIPTPATH, '..', 'openlyrics.rng')



class LyricsParser(object):

    def __init__(self):
        pass

    # public API

    def parse(self, os_lyrics):
        tree = etree.Element('lyrics')
        lines = os_lyrics.splitlines()

        for line in lines:
            if line.startswith('['):
                versename = line.strip().strip('[]')
                self._add_verse(tree, versename)
            elif line.startswith(' '):
                line = line.strip()
                self._add_line(tree, line)

        return tree

    # other methods

    def _add_verse(self, tree, versename):
        versename = versename.lower()
        vtag = etree.SubElement(tree, 'verse')
        vtag.set('name', versename)

    def _add_line(self, tree, text):
        text = text.strip()
        # ignore empty lines
        if not text:
            return
        ltag = etree.Element('line')
        ltag.text = text
        # append line to last verse
        lastv = tree[-1]
        if len(lastv) == 0: # no subelem. <lines>
            linestag = etree.SubElement(lastv, 'lines')
        else:
            linestag = lastv[-1]
        linestag.append(ltag)


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
        self._copy_subelement(osong, 'author', olprop, 'authors', 'author')
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
                elem = etree.SubElement(themes_elem, 'theme')
                elem.text = theme

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

