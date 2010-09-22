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

EMPTY = len([]) # == 0, length of empty list


class ParsingTestCase(unittest.TestCase):

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
        self.assertEqual(EMPTY, len(song.verse_order))
        self.assertEqual(u'v1 v2 v3', ' '.join(song.raw_verse_order))

        # verse count
        self.assertEqual(3, len(song))

        # verse name
        for name in u'v1 v2 v3'.split():
            self.assertNotEqual(None, song.get(name))

        # lines count - default (None - not specified) language
        for ver in song.values():
            self.assertEqual(4, len(ver[None]))

        # verse content
        lines = [u'Have we trials and temptations? Is there trouble anywhere?',
            u'We should never be discouraged, Take it to the Lord in prayer.',
            u'Can we find a friend so faithful? Who will all our sorrows share?',
            u'Jesus knows our every weakness; Take it to the Lord in prayer.',]
        # 'None' - translation for verse was not specified
        for line, l in zip(lines, song['v2'][None]):
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
        self.assertEqual(u'v1 c v2 c v3 c', ' '.join(song.verse_order))
        self.assertEqual(u'v1 c v2 v3', ' '.join(song.raw_verse_order))

        # verse count
        self.assertEqual(4, len(song))

        # verse name
        for name in u'v1 c v2 v3'.split():
            self.assertNotEqual(None, song[name])

        # lines count
        counts = {'v1':6, 'c':4, 'v2':6, 'v3':6}
        for name, count in counts.items():
            self.assertEqual(count, len(song[name][None]))

        # 1st verse content
        lines = [u'Mám zde přítele,',
            u'Pána Ježíše,',
            u'a na rámě jeho spoléhám;',
            u'v něm své stěstí mám,',
            u'pokoj nalézám,',
            u'když na rámě jeho spoléhám!',]
        for line, li in zip(lines, song['v1'][None]):
            self.assertEqual(line, l.text)

        # chorus content
        verse = song[1] # lines from Verse with index 0
        lines = [u'Boží rámě',
            u'je v soužení náš pevný hrad;',
            u'Boží rámě,',
            u'uč se na ně vždycky spoléhat!',]
        for line, li in zip(lines, song['c'][None]):
            self.assertEqual(line, l.text)

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

    def test_english_song_tostring(self):
        song = openlyrics.Song(paths.eng_song)
        text = openlyrics.tostring(song, update_metadata=False)
        self.assertEqual(patterns.eng_song, text)

    def test_english_song_prettyprint(self):
        song = openlyrics.Song(paths.notprettyprint_eng_song)
        text = openlyrics.tostring(song, update_metadata=False)
        self.assertEqual(patterns.prettyprint_eng_song, text)
        text_not_pretty = openlyrics.tostring(song, pretty_print=False, update_metadata=False)
        self.assertNotEqual(patterns.prettyprint_eng_song, text_not_pretty)


class ParsingUtf8TestCase(ParsingTestCase):

    def test_localized_song(self):
        song = openlyrics.Song(paths.l10n_song)
        self.check_localized_song(song)

    def test_localized_song_fromstring(self):
        text = self.readtext(paths.l10n_song)
        song = openlyrics.fromstring(text)
        self.check_localized_song(song)

    def test_localized_song_tostring(self):
        song = openlyrics.Song(paths.l10n_song)
        text = openlyrics.tostring(song, update_metadata=False)
        self.assertEqual(patterns.l10n_song, text)
        
    def test_localized_song_prettyprint(self):
        song = openlyrics.Song(paths.notprettyprint_l10n_song)
        text = openlyrics.tostring(song, update_metadata=False)
        self.assertEqual(patterns.prettyprint_l10n_song, text)
        text_not_pretty = openlyrics.tostring(song, pretty_print=False, update_metadata=False)
        self.assertNotEqual(patterns.prettyprint_l10n_song, text_not_pretty)


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
     
     
class TranslatedSongTestCase(unittest.TestCase):
    'Test parsing of song with translations'
    def test_parsing(self):
        s = openlyrics.Song(paths.translated_song)
        # contains verses v1,c,b in English, Hebrew and transliteration
        # of Hebrew to English
        self.assertEqual(9, len(s))
        # title in EN, HE, and transliteration to EN
        self.assertEqual(3, len(s.props.titles))
        


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ParsingAsciiTestCase, 'test'))
    #suite.addTest(unittest.makeSuite(ParsingUtf8TestCase, 'test'))
    #suite.addTest(unittest.makeSuite(ParsingCp1250TestCase, 'test'))
    #suite.addTest(unittest.makeSuite(UnicodeFilenameTestCase, 'test'))
    #suite.addTest(unittest.makeSuite(WeirdTestCase, 'test'))
    #suite.addTest(unittest.makeSuite(TranslatedSongTestCase, 'test'))

    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')

