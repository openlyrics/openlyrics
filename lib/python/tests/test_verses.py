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


'''Unit tests for manipulating with verses.'''

import unittest
import openlyrics

from tests import paths, patterns


class VersesByNameTestCase(unittest.TestCase):

    def test_name_given(self):
        s = openlyrics.Song(paths.translated_song)
        verses = s.verses_by_name('v1')
        self.assertEqual(3, len(list(verses)))
        for ver in verses: self.assertEqual(u'v1', ver.name)

    def test_name_lang_given(self):
        s = openlyrics.Song(paths.translated_song)
        verses = s.verses_by_name('v1', lang='he')
        self.assertEqual(2, len(list(verses)))
        for ver in verses:
            self.assertEqual(u'v1', ver.name)
            self.assertEqual(u'he', ver.lang)

    def test_name_lang_translit_given(self):
        s = openlyrics.Song(paths.translated_song)
        verses = s.verses_by_name('v1', lang='he', translit='en')
        self.assertEqual(1, len(list(verses)))
        for ver in verses:
            self.assertEqual(u'v1', ver.name)
            self.assertEqual(u'he', ver.lang)
            self.assertEqual(u'en', ver.translit)


class VersesByOrderTestCase(unittest.TestCase):

    def test_use_order_noarg(self):
        s = openlyrics.Song(paths.translated_song)
        verses_list = list(s.verses_by_order()) # order is: 'v1 c v1 c b'
        self.assertEqual(15, len(verses_list)) # 3 languages * 5 items in order
        # verse 'v1' should be present twice (in EN, HE and transliterated)
        for v in verses_list[0:3] + verses_list[6:9]:
            self.assertEqual(u'v1', v.name)
        # verse 'c' is present twice
        for v in verses_list[3:6] + verses_list[9:12]:
            self.assertEqual(u'c', v.name)
        # verse 'b' is present once
        for v in verses_list[13:len(verses_list)]:
            self.assertEqual(u'b', v.name)

    def test_no_order_noarg(self):
        s = openlyrics.Song(paths.translated_song)
        verses_list = list(s.verses_by_order(use_order=False))
        self.assertEqual(9, len(verses_list))
        for v in verses_list[0:3]:
            self.assertEqual(u'v1', v.name)
        for v in verses_list[3:6] :
            self.assertEqual(u'c', v.name)
        for v in verses_list[6:len(verses_list)]:
            self.assertEqual(u'b', v.name)

    def test_use_order_lang(self):
        s = openlyrics.Song(paths.translated_song)
        verses_list = list(s.verses_by_order('he'))
        self.assertEqual(10, len(verses_list))
        print unicode(verses_list)
        for v in verses_list[0:2] + verses_list[4:6]:
            self.assertEqual(u'v1', v.name)
        for v in verses_list[2:4] + verses_list[6:8]:
            self.assertEqual(u'c', v.name)
        for v in verses_list[8:len(verses_list)]:
            self.assertEqual(u'b', v.name)
       
    def test_no_order_lang(self):
        s = openlyrics.Song(paths.translated_song)
        verses_list = list(s.verses_by_order('he', use_order=False))
        self.assertEqual(6, len(verses_list))

    def test_use_order_lang_translit(self):
        s = openlyrics.Song(paths.translated_song)
        verses_list = list(s.verses_by_order('he', 'en'))
        self.assertEqual(5, len(verses_list))

    def test_no_order_lang_translit(self):
        s = openlyrics.Song(paths.translated_song)
        verses_list = list(s.verses_by_order('he', 'en', use_order=False))
        self.assertEqual(3, len(verses_list))


 
 
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(VersesByNameTestCase, 'test'))
    suite.addTest(unittest.makeSuite(VersesByOrderTestCase, 'test'))

    return suite


#if __name__ == '__main__':
    #unittest.main(defaultTest='suite')


if __name__ == '__main__':
    unittest.main(defaultTest='suite')

