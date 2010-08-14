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


'''Unit test creating basic OpenLyrics objects and their initial values.'''

import unittest
import openlyrics

from tests import paths, patterns


def test_props_values(test_case, props):
    test = test_case
    p = props

    # List types
    test.assertEqual([], p.titles)
    test.assertEqual([], p.authors)
    test.assertEqual([], p.songbooks)
    test.assertEqual([], p.themes)
    test.assertEqual([], p.comments)
    test.assertEqual([], p.verse_order)

    # String Types
    test.assertEqual(u'', p.release_date)
    test.assertEqual(u'', p.ccli_no)
    test.assertEqual(u'', p.tempo)
    test.assertEqual(u'', p.tempo_type)
    test.assertEqual(u'', p.key)
    test.assertEqual(u'0', p.transposition)
    test.assertEqual(u'', p.variant)
    test.assertEqual(u'', p.keywords)
    test.assertEqual(u'', p.copyright)
    test.assertEqual(u'', p.publisher)
    test.assertEqual(u'', p.custom_version)


class InitSongClassTestCase(unittest.TestCase):

    def test_Song(self):
        s = openlyrics.Song()

        self.assertEqual(u'0.7', s._version)
        self.assertEqual([], s.verses)
        self.assertEqual(u'OpenLyrics Python Library 0.1', s.createdIn)
        self.assertEqual(u'OpenLyrics Python Library 0.1', s.modifiedIn)
        self.assertEqual(u'', s.modifiedDate)
        self.assertNotEqual(None, s.props)

        test_props_values(self, s.props)

    def test_Song_tostring(self):
        s = openlyrics.Song()
        s.modifiedDate = u'2010-06-04T21:51:57'
        text = openlyrics.tostring(s, update_metadata=False)
        self.assertEqual(patterns.song_with_default_values, text)


class InitPropertiesClassesTestCase(unittest.TestCase):

    def test_Properties(self):
        p = openlyrics.Properties()
        test_props_values(self, p)

    def test_Title(self):
        t = openlyrics.Title()
        self.assertEqual(u'', t.text)
        self.assertEqual(None, t.lang)

    def test_Author(self):
        a = openlyrics.Author()
        self.assertEqual(u'', a.name)
        self.assertEqual(None, a.type)
        self.assertEqual(None, a.lang)

    def test_Songbook(self):
        s = openlyrics.Songbook()
        self.assertEqual(u'', s.name)
        self.assertEqual(None, s.entry)

    def test_Theme(self):
        t = openlyrics.Theme()
        self.assertEqual(u'', t.name)
        self.assertEqual(None, t.id)
        self.assertEqual(None, t.lang)


class InitLyricsClassesTestCase(unittest.TestCase):

    def test_Verse(self):
        v = openlyrics.Verse()
        self.assertEqual(None, v.lang)
        self.assertEqual(None, v.translit)
        self.assertEqual(None, v.name)
        self.assertEqual([], v.lines)

    def test_Lines(self):
        l = openlyrics.Lines()
        self.assertEqual([], l)
        self.assertEqual(u'', l.part)

    # FIXME add tests for initialization of Line class
    def test_Line(self):
        pass


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(InitSongClassTestCase, 'test'))
    suite.addTest(unittest.makeSuite(InitPropertiesClassesTestCase, 'test'))
    suite.addTest(unittest.makeSuite(InitLyricsClassesTestCase, 'test'))

    return suite

