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


class PropertiesClassesTestCase(unittest.TestCase):

    def test_Properties(self):

        p = openlyrics.Properties()
        # List types
        self.assertEqual([], p.titles)
        self.assertEqual([], p.authors)
        self.assertEqual([], p.songbooks)
        self.assertEqual([], p.themes)
        self.assertEqual([], p.comments)
        self.assertEqual([], p.verse_order)

        # String Types
        self.assertEqual(u'', p.release_date)
        self.assertEqual(u'', p.ccli_no)
        self.assertEqual(u'', p.tempo)
        self.assertEqual(u'', p.tempo_type)
        self.assertEqual(u'', p.key)
        self.assertEqual(u'0', p.transposition)
        self.assertEqual(u'', p.variant)
        self.assertEqual(u'', p.keywords)
        self.assertEqual(u'', p.copyright)
        self.assertEqual(u'', p.publisher)
        self.assertEqual(u'', p.custom_version)

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


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PropertiesClassesTestCase, 'test'))

    return suite

