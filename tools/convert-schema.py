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
    replace <collection> with <songbook name>
    replace <trackNo> with <songbook entry>
    replace "xml:lang" with "lang"

From schema 0.7 to 0.8:
    drop <line> element
    use <br/> for line endings
    at the end of <comment> line add <br/>
    replace <customVersion> with <version>
    replace <releaseDate> with <released>

Usage:
    convert-schema.py OLD-OPENLYRICS-FILE.xml NEW-OPENLYRICS-FILE.xml
'''

import locale
import os.path
import sys
from datetime import datetime


#########################################################################
# Utility definitions

def error(s):
    sys.stderr.write(os.path.basename(sys.argv[0]) + ': ' + s + '\n');
    exit(1)


#########################################################################
# LXML module

try:
    from lxml import etree
except ImportError:
    error('lxml python module not found\n\n' +
          'This program requires the lxml python module.  Please install it from\n' +
          'http://pypi.python.org/pypi/lxml/')


#########################################################################
# Constants and global variables

NAMESPACE             = 'http://openlyrics.info/namespace/2009/song'
TARGET_OPENLYRICS_VER = '0.8'
OPENLYRICS_VERSIONS   = ['0.6', '0.7', '0.8']

SCRIPTPATH = os.path.dirname(unicode(__file__, locale.getpreferredencoding()))
SCHEMAFILE = os.path.join(SCRIPTPATH, '..', 'openlyrics-0.8.rng')


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

        parser = etree.XMLParser(ns_clean=True, remove_blank_text=False)
        self.tree = etree.parse(self.old_file, parser)

        self.root = self.tree.getroot()
        if self.root.tag != '{' + NAMESPACE + '}song':
            error('%s: not an OpenLyrics XML file (expected <song>, found <%s>)'
                  % (old_file, self.root.tag))

        self.old_version = self.root.attrib["version"]
        if not self.old_version in OPENLYRICS_VERSIONS:
            error('%s: unsupported OpenLyrics XML version %s'
                  % (self.old_file, self.old_version))


    def save(self, new_file):
        '''
        Save the possibly-modified XML tree to a new stream.
        '''

        if self.modified:
            self.root.attrib["modifiedIn"]   = os.path.basename(sys.argv[0])
            self.root.attrib["modifiedDate"] = datetime.now().isoformat()

        self.tree.write(new_file, pretty_print=True, xml_declaration=True,
                        encoding='UTF-8')


    def convert(self):
        '''
        Convert the parsed XML tree to the latest version of OpenLyrics.
        '''

        if self.old_version != TARGET_OPENLYRICS_VER:
            self.root.attrib["version"] = TARGET_OPENLYRICS_VER
            self.modified = True

        # @@@ To be completed...


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
