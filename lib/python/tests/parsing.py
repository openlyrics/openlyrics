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


'''General test cases for checking values in parsed/created songs.'''

import unittest
import openlyrics

from tests import paths, patterns

EMPTY = len([]) # == 0, length of empty list


class ParsingCheckerTestCase(unittest.TestCase):

    def check_english_song(self, song):
        # test properties
        titles = [u'What A Friend We Have In Jesus']
        for title, t in zip(titles, song.props.titles):
            self.assertEqual(title, t.text)
        authors = [u'Joseph M. Scriven', u'Charles C. Convers']
        for author, a in zip(authors, song.props.authors):
            self.assertEqual(author, a.name)
        self.assertEqual(u'Public Domain', song.props.copyright)
        self.assertEqual(u'27714', song.props.ccli_no)
        themes = [u'Christ: Love/Mercy', u'Fruit: Peace/Comfort']
        for theme, t in zip(themes, song.props.themes):
            self.assertEqual(theme, t.name)
                    
        # verse order
        self.assertEqual(EMPTY, len(song.props.verse_order))
        self.assertEqual(u'v1 v2 v3', ' '.join(song.props.get_raw_verse_order()))

        # verse count
        self.assertEqual(3, len(song))

        # verse name
        for name in u'v1 v2 v3'.split():
            self.assertNotEqual(None, song.get_verse(name))

        # lines count - default (not specified) language
        for verse in song.verses:
            self.assertEqual(4, len(verse))

        # verse content
        lines = [u'Have we trials and temptations? Is there trouble anywhere?',
            u'We should never be discouraged, Take it to the Lord in prayer.',
            u'Can we find a friend so faithful? Who will all our sorrows share?',
            u'Jesus knows our every weakness; Take it to the Lord in prayer.',]
        # translation for verse was not specified
        
        ##TODO
        for line, l in zip(lines, song.get_verse('v2').lines[0].lines):
            self.assertEqual(line, l.text)

    def check_localized_song(self, song):
        # test properties

        titles = [u'Mám zde přítele']
        for title, t in zip(titles, song.props.titles):
            self.assertEqual(title, t.text)
        authors = [u'A.J. Showalter', u'E.A. Hoffman']
        for author, a in zip(authors, song.props.authors):
            self.assertEqual(author, a.name)

        # verse order
        self.assertEqual(u'v1 c v2 c v3 c', ' '.join(song.props.verse_order))
        self.assertEqual(u'v1 c v2 v3', ' '.join(song.props.get_raw_verse_order()))

        # verse count
        self.assertEqual(4, len(song))

        # verse name
        for name in u'v1 c v2 v3'.split():
            self.assertNotEqual(None, song.get_verse(name))

        # lines count
        counts = {'v1':6, 'c':4, 'v2':6, 'v3':6}
        for name, count in counts.items():
            self.assertEqual(count, len(song.get_verse(name)))

        # 1st verse content
        ##TODO
        lines = [u'Mám zde přítele,',
            u'Pána Ježíše,',
            u'a na rámě jeho spoléhám;',
            u'v něm své stěstí mám,',
            u'pokoj nalézám,',
            u'když na rámě jeho spoléhám!',]
        for line, l in zip(lines, song.get_verse('v1').lines[0].lines):
            self.assertEqual(line, l.text)

        # chorus content
        lines = [u'Boží rámě',
            u'je v soužení náš pevný hrad;',
            u'Boží rámě,',
            u'uč se na ně vždycky spoléhat!',]
        for line, l in zip(lines, song.get_verse('c').lines[0].lines):
            self.assertEqual(line, l.text)

    def readtext(self, filename):
        '''return unicode string'''
        import codecs
        f = codecs.open(filename, 'r', 'UTF-8')
        text = f.read()
        f.close()
        return text


