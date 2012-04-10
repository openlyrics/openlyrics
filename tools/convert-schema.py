#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################################################
#                                                                       #
#           Convert old OpenLyrics files to the latest schema           #
#             Copyright (C) 2010-12, The OpenLyrics Authors             #
#                                                                       #
#########################################################################

# Authors: Martin Zibricky <mzibr.public@gmail.com>
#          John Zaitseff <J.Zaitseff@zap.org.au>

# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

# History:
# 1.0  Initial release: convert from OpenLyrics 0.6 and 0.7 to 0.8

__version__ = '1.0'

'''
Convert old OpenLyrics files to the latest schema.

This script converts files written in old versions of the OpenLyrics
schema to the latest version.  The following changes are made:

From schema 0.6 to 0.7:
    - Replace "xml:lang" attributes with "lang"
    - Replace <collection> with <songbooks><songbook name>
    - Replace <trackNo> with <songbooks><songbook entry>

From schema 0.7 to 0.8:
    - Replace <customVersion> with <version>
    - Replace <releaseDate> with <released>
    - Replace <line> with <br/> in the appropriate places
    - Add <br/> to the end of <comment> lines

Usage:
    convert-schema.py OLD-OPENLYRICS-FILE.xml NEW-OPENLYRICS-FILE.xml
'''

import locale
import os.path
import sys
from datetime import datetime


#########################################################################
# Constants and global variables

NAMESPACE             = 'http://openlyrics.info/namespace/2009/song'
TARGET_OPENLYRICS_VER = '0.8'
OPENLYRICS_VERSIONS   = ['0.6', '0.7', '0.8']
LIBXML2_BUGGY         = True	# Does libxml2 have bugs processing 'xml:lang'?

SCRIPTPATH = os.path.dirname(unicode(__file__, locale.getpreferredencoding()))
SCHEMAFILE = os.path.join(SCRIPTPATH, '..', 'openlyrics-0.8.rng')


#########################################################################
# Utility definitions

def error(s):
    sys.stderr.write(os.path.basename(sys.argv[0]) + ': ' + s + '\n');
    exit(1)


#########################################################################
# LXML, StringIO and RE modules

try:
    from lxml import etree
except ImportError:
    error('lxml python module not found\n\n' +
          'This program requires the lxml python module.  Please install it from\n' +
          'http://pypi.python.org/pypi/lxml/')

if LIBXML2_BUGGY:
    import StringIO
    import re


#########################################################################
# OpenLyrics XML parser and converter

class OpenLyricsTree(object):
    '''
    Parse and convert an OpenLyrics XML stream.
    '''

    def __init__(self, old_file):
        '''
        Read in and parse an OpenLyrics XML stream.
        '''

        self.old_file = old_file
        self.modified = False

        if LIBXML2_BUGGY:
            self._libxml2_bug_triggered = False

        parser = etree.XMLParser(ns_clean=True, remove_blank_text=False)
        self.tree = etree.parse(self.old_file, parser)

        self.root = self.tree.getroot()
        if self.root.tag != '{' + NAMESPACE + '}song':
            error('%s: not an OpenLyrics XML file (expected <song>, found <%s>)'
                  % (old_file, self.root.tag))

        self.old_version = self.root.attrib['version']
        if not self.old_version in OPENLYRICS_VERSIONS:
            error('%s: unsupported OpenLyrics XML version %s'
                  % (self.old_file, self.old_version))


    def save(self, new_file):
        '''
        Save the possibly-modified XML tree to a new stream.
        '''

        if self.modified:
            self.root.attrib['modifiedIn']   = os.path.basename(sys.argv[0])
            self.root.attrib['modifiedDate'] = datetime.now().isoformat()

        if not LIBXML2_BUGGY or not self._libxml2_bug_triggered:
            self.tree.write(new_file, pretty_print=True, xml_declaration=True,
                            encoding='UTF-8')
        else:
            # Work around bugs in libxml2: remove 'xml:lang' attributes
            new_strio = StringIO.StringIO()
            self.tree.write(new_strio, pretty_print=True, xml_declaration=True,
                            encoding='UTF-8')
            new_string = new_strio.getvalue()
            new_strio.close()

            new_string = re.sub(r'\s+xml:lang="[^"]+"', '', new_string)

            new_output = open(new_file, 'w')
            new_output.write(new_string)
            new_output.close()


    def xpath(self, path, elem=None):
        '''
        Return the result of elem.xpath with the namespace "ol"
        '''

        if elem is None:
            elem = self.tree

        return elem.xpath(path, namespaces={ 'ol' : NAMESPACE })


    def convert(self):
        '''
        Convert the parsed XML tree to the latest version of OpenLyrics.
        '''

        if self.old_version in ['0.6']:

            # Replace 'xml:lang' attributes with 'lang'
            for attr in self.xpath('//@xml:lang'):
                elem = attr.getparent()
                if not elem.attrib.has_key('lang'):
                    elem.set('lang', attr)
                    if not LIBXML2_BUGGY:
                        elem.set('xml:lang', None)
                    else:
                        self._libxml2_bug_triggered = True
                    self.modified = True

            # Replace <collection> with <songbooks><songbook name>
            songbooks = None
            songbook_elem = None
            for elem in self.xpath('/ol:song/ol:properties/ol:collection'):
                val = elem.text
                tail = elem.tail
                songbooks = etree.Element('songbooks')
                songbooks.tail = tail
                elem.getparent().replace(elem, songbooks)
                songbook_elem = etree.SubElement(songbooks, 'songbook')
                songbook_elem.set('name', val)
                self.modified = True

            # Replace <trackNo> with <songbooks><songbook entry>
            for elem in self.xpath('/ol:song/ol:properties/ol:trackNo'):
                val = elem.text
                tail = elem.tail
                if songbook_elem != None:
                    elem.getparent().remove(elem)
                else:
                    songbooks = etree.Element('songbooks')
                    songbooks.tail = tail
                    elem.getparent().replace(elem, songbooks)
                    songbook_elem = etree.SubElement(songbooks, 'songbook')
                    songbook_elem.set('name', 'Songbook')
                songbook_elem.set('entry', val)
                self.modified = True


        if self.old_version in ['0.7']:
            # No conversions specific to this version
            None

        if self.old_version in ['0.6', '0.7']:

            # Replace <customVersion> with <version>
            for elem in self.xpath('/ol:song/ol:properties/ol:customVersion'):
                elem.tag = 'version'
                self.modified = True

            # Replace <releaseDate> with <released>
            for elem in self.xpath('/ol:song/ol:properties/ol:releaseDate'):
                elem.tag = 'released'
                self.modified = True

            # Replace <line> with <br/> in the appropriate places
            ''' @@@ to be completed
            for elem in self.xpath('/ol:song/ol:lyrics/ol:verse/ol:lines//ol:line'):
                prev_elem = elem.getprevious()
                if prev_elem == None:
                    if elem.text != None:
                        elem.getparent().text += elem.text
                    if list(elem) == []:
                        elem.getparent().text += elem.tail
                        elem.getparent().remove(elem)
                    else:
                        None
            '''

            # Add <br/> to the end of <comment> lines
            for elem in self.xpath('/ol:song/ol:lyrics/ol:verse/ol:lines//ol:comment'):
                next_elem = elem.getnext()
                if next_elem != None and next_elem.tag != 'br':
                    elem_pos = elem.getparent().index(elem)
                    br_elem = etree.Element('br')
                    br_elem.tail = elem.tail
                    elem.tail = None
                    elem.getparent().insert(elem_pos + 1, br_elem)

        # Update the version number
        if self.old_version != TARGET_OPENLYRICS_VER:
            self.root.attrib['version'] = TARGET_OPENLYRICS_VER
            self.modified = True


#########################################################################
# Main program

def main():
    if len(sys.argv) != 3:
        error('Missing command line arguments.\n\n' +
              'Usage:\n' +
              '    %s OLD-OPENLYRICS-FILE.xml NEW-OPENLYRICS-FILE.xml'
              % __file__)
    else:
        old_file = sys.argv[1]
        new_file = sys.argv[2]

    if not os.path.isfile(old_file):
        error('%s: file not found' % old_file)
    if os.path.exists(new_file):
        error('%s: file exists' % new_file)

    converter = OpenLyricsTree(old_file)
    converter.convert()
    converter.save(new_file)


if __name__ == '__main__':
    main()
