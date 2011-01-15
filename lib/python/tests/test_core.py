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


'''Core tests'''

import unittest
import openlyrics

from tests import paths, patterns
from parsing import ParsingCheckerTestCase

EMPTY = len([]) # == 0, length of empty list


class ParsingAsciiTestCase(ParsingCheckerTestCase):

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


class ParsingUtf8TestCase(ParsingCheckerTestCase):

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


class ParsingCp1250TestCase(ParsingCheckerTestCase):

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
        # Contains 3 verses v1,c,b, every verse is in English and Hebrew.
        # Hebrew contains also transliteration to English of Hebrew to English
        s = openlyrics.Song(paths.translated_song)

        # verse count
        self.assertEqual(3, len(s))

        line_counts = [3, 3, 5]

        # lines count in EN translation
        for name, count in zip(s.raw_verse_order, line_counts):
            self.assertEqual(count, len(s[name].lang['en']))

        # lines count in HE translation
        for name, count in zip(s.raw_verse_order, line_counts):
            self.assertEqual(count, len(s[name].lang['he']))

        # lines count in EN transliteration of Hebrew
        for name, count in zip(s.raw_verse_order, line_counts):
            self.assertEqual(count, len(s[name].lang['he'].translit['en']))

        # title in EN, HE, and transliteration to EN
        self.assertEqual(3, len(s.props.titles))

        # theme in EN, HE, and transliteration to EN
        self.assertEqual(3, len(s.props.themes))

        # test select titles and themes by lang
        self.assertEqual(0, len(s.props.titles_by_lang('')))
        self.assertEqual(1, len(s.props.titles_by_lang('en')))
        self.assertEqual(2, len(s.props.titles_by_lang('he')))
        self.assertEqual(1, len(s.props.titles_by_lang('he', 'en')))

        self.assertEqual(0, len(s.props.themes_by_lang('')))
        self.assertEqual(1, len(s.props.themes_by_lang('en')))
        self.assertEqual(2, len(s.props.themes_by_lang('he')))
        self.assertEqual(1, len(s.props.themes_by_lang('he', 'en')))
        


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ParsingAsciiTestCase, 'test'))
    suite.addTest(unittest.makeSuite(ParsingUtf8TestCase, 'test'))
    suite.addTest(unittest.makeSuite(ParsingCp1250TestCase, 'test'))
    suite.addTest(unittest.makeSuite(UnicodeFilenameTestCase, 'test'))
    suite.addTest(unittest.makeSuite(WeirdTestCase, 'test'))
    suite.addTest(unittest.makeSuite(TranslatedSongTestCase, 'test'))

    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')

