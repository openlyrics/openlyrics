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

import openlyrics
import os.path

from time import time

def printSong(s):
    print "titles: "
    for title in s.props.titles:
        print '  * ', title
    print "authors: "
    for auth in s.props.authors:
        print '  * ', auth
    print "songbooks: "
    for song in s.props.songbooks:
        print '  * ', song
    print "themes: "
    for thm in s.props.themes:
        print '  * ', thm
    print "comments: ", s.props.comments
    print "release_date: ", s.props.release_date
    print "ccli_no: ", s.props.ccli_no
    print "tempo: ", s.props.tempo
    print "tempo_type: ", s.props.tempo_type
    print "key: ", s.props.key
    print "transposition: ", s.props.transposition
    print "variant: ", s.props.variant
    print "verse_order: ", s.props.verse_order
    print "keywords: ", s.props.keywords
    print "copyright: ", s.props.copyright
    print "publisher: ", s.props.publisher
    print "custom_version: ", s.props.custom_version
    for verse in s.verses:
      print "Verse: %s" % verse.name
      for lines in verse.lines:
        print "  Lines (Part '%s')" % lines.part
        for line in lines.lines:
          print "    Line: %s" % line.markup

fl = os.path.join(os.path.dirname(__file__),"test.xml")

# Test file access

parse_begin = time()
s = openlyrics.Song(fl)
parse_end = time()
print 'Time parsing:', parse_end - parse_begin

write_begin = time()
s.write('out.xml')
write_end = time()
print 'Time writing:', write_end - write_begin

print 'Time total:', write_end - parse_begin

printSong(s)

print ''

#Test string access

parse_begin = time()
f = open(fl, "r")
lines = f.readlines()
s = openlyrics.fromstring("\n".join(lines))
f.close()
parse_end = time()

print 'Time parsing:', parse_end - parse_begin


write_begin = time()
f = open("out2.xml","w")
xmlstring = openlyrics.tostring(s)
f.write(xmlstring)
f.close()
write_end = time()
print 'Time writing:', write_end - write_begin

print 'Time total:', write_end - parse_begin

