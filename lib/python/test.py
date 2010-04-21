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



parse_begin = time()
s = openlyrics.Song(os.path.join(os.path.dirname(__file__),"test.xml"))
parse_end = time()

write_begin = time()
s.to_xml('out.xml')
write_end = time()

print "titles: "
for title in s.titles:
  print '  * ', title
print "authors: "
for auth in s.authors:
  print '  * ', auth
print "songbooks: "
for song in s.songbooks:
  print '  * ', song
print "themes: "
for thm in s.themes:
  print '  * ', thm
print "comments: ", s.comments
print "release_date: ", s.release_date
print "ccli_no: ", s.ccli_no
print "tempo: ", s.tempo
print "tempo_type: ", s.tempo_type
print "key: ", s.key
print "transposition: ", s.transposition
print "variant: ", s.variant
print "verse_order: ", s.verse_order
print "keywords: ", s.keywords
print "copyright: ", s.copyright
print "publisher: ", s.publisher
print "custom_version: ", s.custom_version
for verse in s.verses:
  print "Verse: %s" % verse.name
  for lines in verse.lines:
    print "  Lines (Part '%s')" % lines.part
    for line in lines.lines:
      print "    Line: %s" % line.markup

print ''
print 'Time parsing:', parse_end - parse_begin
print 'Time writing:', write_end - write_begin
print 'Time total:', write_end - parse_begin
