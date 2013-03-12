# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4
#
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


'''Tests for different ways of constructing song'''

import unittest
import openlyrics


constructed_song = u'''<?xml version='1.0' encoding='UTF-8'?>
<song createdIn="OpenLyrics Python Library 0.2" modifiedDate="2011-01-15T12:07:10" modifiedIn="OpenLyrics Python Library 0.2" version="0.8" xmlns="http://openlyrics.info/namespace/2009/song">
  <properties />
  <lyrics>
    <verse name="v1">
      <lines>Text v1 line1<br />Text v1 line2</lines>
    </verse>
    <verse name="v2">
      <lines>Text v2 line1<br />Text v2 line2</lines>
    </verse>
    <verse lang="he" name="v1">
      <lines>Text v1 he line1<br />Text v1 he line2</lines>
    </verse>
    <verse lang="he" name="v2">
      <lines>Text v2 he line1<br />Text v2 he line2</lines>
    </verse>
    <verse lang="he" name="v1" translit="en">
      <lines>Text v1 he_en line1<br />Text v1 he_en line2</lines>
    </verse>
    <verse lang="he" name="v2" translit="en">
      <lines>Text v2 he_en line1<br />Text v2 he_en line2</lines>
    </verse>
  </lyrics>
</song>'''


class CreateSongTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        
        pass

    def test_create(self):
        from openlyrics import Song, Line
        song = Song()
        song.modifiedIn = openlyrics.OLYR_MODIFIED_IN
        song.modifiedDate = '2011-01-15T12:07:10'
        song._version = openlyrics.OLYR_VERSION

        lines = 'Text v1 line1\nText v1 line2'
        lines_he = 'Text v1 he line1\nText v1 he line2'
        lines_he_en = 'Text v1 he_en line1\nText v1 he_en line2'

        # text without language
        song.add_verse('v1', lines)
        song.add_verse('v2', '''Text v2 line1
Text v2 line2''')

        # translation for verse
        song.add_verse('v1', lines_he, lang='he')
        song.add_verse('v2', '''Text v2 he line1
Text v2 he line2''', lang='he')

        # transliteration for translation
        song.add_verse('v1', lines_he_en, lang='he', translit='en')
        song.add_verse('v2', '''Text v2 he_en line1
Text v2 he_en line2''', lang='he', translit='en')
        
        from xml.sax.saxutils import unescape
        text = openlyrics.tostring(song, update_metadata=False)
        self.assertEquals(constructed_song, text)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CreateSongTestCase, 'test'))

    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')

