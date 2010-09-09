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
 
 
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(VersesByNameTestCase, 'test'))

    return suite


#if __name__ == '__main__':
    #unittest.main(defaultTest='suite')


if __name__ == '__main__':
    unittest.main(defaultTest='suite')

