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


'''Unit test example using unittest module.'''

import unittest
import openlyrics

from tests import paths, patterns


class ParsingTestCase(unittest.TestCase):

    def check_english_song(self, song):
        # test properties

        titles = [u'What A Friend We Have In Jesus']
        for i in range(0, len(titles)):
            self.assertEqual(titles[i], song.props.titles[i].text)
        authors = [u'Joseph M. Scriven', u'Charles C. Convers']
        for i in range(0, len(authors)):
            self.assertEqual(authors[i], song.props.authors[i].name)
        self.assertEqual(u'Public Domain', song.props.copyright)
        self.assertEqual(u'27714', song.props.ccli_no)
        self.assertEqual(u'Christ: Love/Mercy', song.props.themes[0].name)
        self.assertEqual(u'Fruit: Peace/Comfort', song.props.themes[1].name)
                    

        # verse order
        order = song.props.verse_order
        self.assertEqual([], order)

        # verses
        verses = song.verses

        # verse count
        self.assertEqual(len(verses), 3)

        # verse name
        self.assertEqual(u'v1', verses[0].name)
        self.assertEqual(u'v2', verses[1].name)
        self.assertEqual(u'v3', verses[2].name)

        # lines count
        for ver in verses:
            self.assertEqual(4, len(ver.lines[0].lines))

        # verse content
        lines = verses[1].lines[0].lines
        lst = [u'Have we trials and temptations? Is there trouble anywhere?',
            u'We should never be discouraged, Take it to the Lord in prayer.',
            u'Can we find a friend so faithful? Who will all our sorrows share?',
            u'Jesus knows our every weakness; Take it to the Lord in prayer.',]
        for i in range(0, len(lst)):
            self.assertEqual(lst[i], lines[i].text)

    def check_localized_song(self, song):
        # test properties

        titles = [u'Mám zde přítele']
        for i in range(0, len(titles)):
            self.assertEqual(titles[i], song.props.titles[i].text)
        authors = [u'A.J. Showalter', u'E.A. Hoffman']
        for i in range(0, len(authors)):
            self.assertEqual(authors[i], song.props.authors[i].name)
                    

        # verse order
        order = song.props.verse_order
        self.assertEqual([u'v1', u'c', u'v2', u'c', u'v3', u'c'], order)

        # verses
        verses = song.verses

        # verse count
        self.assertEqual(len(verses), 4)

        # verse name
        self.assertEqual(u'v1', verses[0].name)
        self.assertEqual(u'c', verses[1].name)
        self.assertEqual(u'v2', verses[2].name)
        self.assertEqual(u'v3', verses[3].name)

        # lines count
        self.assertEqual(6, len(verses[0].lines[0].lines))
        self.assertEqual(4, len(verses[1].lines[0].lines))
        self.assertEqual(6, len(verses[2].lines[0].lines))
        self.assertEqual(6, len(verses[3].lines[0].lines))

        # 1st verse content
        lines = verses[0].lines[0].lines
        lst = [u'Mám zde přítele,',
            u'Pána Ježíše,',
            u'a na rámě jeho spoléhám;',
            u'v něm své stěstí mám,',
            u'pokoj nalézám,',
            u'když na rámě jeho spoléhám!',]
        for i in range(0, len(lst)):
            self.assertEqual(lst[i], lines[i].text)

        # chorus content
        lines = verses[1].lines[0].lines
        lst = [u'Boží rámě',
            u'je v soužení náš pevný hrad;',
            u'Boží rámě,',
            u'uč se na ně vždycky spoléhat!',]
        for i in range(0, len(lst)):
            self.assertEqual(lst[i], lines[i].text)

    def readtext(self, filename):
        '''return unicode string'''
        import codecs
        f = codecs.open(filename, 'r', 'UTF-8')
        text = f.read()
        f.close()
        return text


class ParsingAsciiTestCase(ParsingTestCase):

    def test_english_song(self):
        song = openlyrics.Song(paths.eng_song)
        self.check_english_song(song)

    def test_english_song_fromstring(self):
        text = self.readtext(paths.eng_song)
        song = openlyrics.fromstring(text)
        self.check_english_song(song)


class ParsingUtf8TestCase(ParsingTestCase):

    def test_localized_song(self):
        song = openlyrics.Song(paths.l10n_song)
        self.check_localized_song(song)

    def test_localized_song_fromstring(self):
        text = self.readtext(paths.l10n_song)
        song = openlyrics.fromstring(text)
        self.check_localized_song(song)


class ParsingCp1250TestCase(ParsingTestCase):

    def test_localized_song(self):
        song = openlyrics.Song(paths.l10n_song_cp1250)
        self.check_localized_song(song)

    def test_localized_song_fromstring(self):
        f = open(paths.l10n_song_cp1250)
        byte_string_text = f.read()
        f.close()
        song = openlyrics.fromstring(byte_string_text)
        self.check_localized_song(song)


class UnicodeFilenameTestCase(unittest.TestCase):

    def test_unicode_filename(self):
        # on win32 lxml (libxml2) is not able handle unicode filenames itself.
        # Python's file object should be used
        fname = paths.unicode_filename
        song = openlyrics.Song(fname)

        # modifiedDate is usually updated during conversion to string but
        # we need to be able compare string with another sing.
        text = openlyrics.tostring(song, update_metadata=False)
        self.assertEqual(patterns.unicode_filename_song, text)

        # modifiedDate should be different not equal
        text = openlyrics.tostring(song, update_metadata=True)
        self.assertNotEqual(patterns.unicode_filename_song, text)
        

class WeirdTestCase(unittest.TestCase):

    def test_notexist_file(self):
        fname = 'not existing file.xml'
        self.assertRaises(IOError, openlyrics.Song, fname)

    def test_invalid_xml(self):
        fname = paths.invalid_song
        self.assertRaises(SyntaxError, openlyrics.Song, fname)
     

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ParsingAsciiTestCase, 'test'))
    suite.addTest(unittest.makeSuite(ParsingUtf8TestCase, 'test'))
    suite.addTest(unittest.makeSuite(ParsingCp1250TestCase, 'test'))
    suite.addTest(unittest.makeSuite(UnicodeFilenameTestCase, 'test'))
    suite.addTest(unittest.makeSuite(WeirdTestCase, 'test'))

    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')

