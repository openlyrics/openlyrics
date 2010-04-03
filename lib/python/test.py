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


s = openlyrics.Song(os.path.join(os.path.dirname(__file__),"test.xml"))

print "_titles: "
for title in s._titles:
  print '         ', title
print "_authors: "
for auth in s._authors:
  print '          ', auth
print "_songbooks: "
for song in s._songbooks:
  print '            ', song
print "_themes: "
for thm in s._themes:
  print '         ', thm
print "comments: ", s.comments
print "_release_date: ", s._release_date
print "_ccli_no: ", s._ccli_no
print "_tempo: ", s._tempo
print "_tempo_type: ", s._tempo_type
print "_key: ", s._key
print "_transposition: ", s._transposition
print "_variant: ", s._variant
print "_verse_order: ", s._verse_order
print "keywords: ", s.keywords
print "themes: ", s.themes
print "copyright: ", s.copyright
print "publisher: ", s.publisher
print "custom_version: ", s.custom_version