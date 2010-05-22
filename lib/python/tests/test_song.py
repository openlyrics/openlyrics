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


'''Test the song parsing.'''


import lxml.etree as etree
from nose.tools import raises

from cslib import io

import paths

# FIXME use unittest module
# FIXME python 2.5 compatibility

def test_english_song():
    fname = paths.eng_song
    song = io.song.Song(fname)

    # test properties
    titles = ['What A Friend We Have In Jesus']
    for i in range(0, len(titles)):
        assert song.titles[i] == titles[i]
    authors = ['Joseph M. Scriven', 'Charles C. Convers']
    for i in range(0, len(authors)):
        assert song.authors[i] == authors[i]
                
        #self.assertEqual('Public Domain', self.song.copyright)
        #self.assertEqual('27714', self.song.ccli)
        #self.assertEqual('Christ: Love/Mercy', self.song.theme)
        #self.assertEqual('Fruit: Peace/Comfort', self.song.alttheme)

    # test verse order
    order = song.lyrics.present_order
    assert order == []
    verses = song.lyrics.verses_order()
    assert verses[0].verse_id == 'v1'
    assert verses[1].verse_id == 'v2'
    assert verses[2].verse_id == 'v3'
    verses = song.lyrics.verses_order_normal()
    assert verses[0].verse_id == 'v1'
    assert verses[1].verse_id == 'v2'
    assert verses[2].verse_id == 'v3'

    # test verse count
    assert len(song.lyrics.verses) == 3

    # test lines count
    vrs = song.lyrics.verses
    sizes = [4, 4, 4]
    for i in range(0, len(sizes)):
        assert len(vrs[i].lines) == sizes[i]

    # test verse content
    verse = song.lyrics.verses[1].lines
    lst = [u'Have we trials and temptations? Is there trouble anywhere?',
        u'We should never be discouraged, Take it to the Lord in prayer.',
        u'Can we find a friend so faithful? Who will all our sorrows share?',
        u'Jesus knows our every weakness; Take it to the Lord in prayer.',]
    for i in range(0, len(lst)):
        assert verse[i].text == lst[i]

def test_localized_song():
    fname = paths.l10n_song
    song = io.song.Song(fname)

    # test metadata
    titles = [u'Mám zde přítele']
    for i in range(0, len(titles)):
        assert song.titles[i] == titles[i]
    authors = ['A.J. Showalter', 'E.A. Hoffman']
    for i in range(0, len(authors)):
        print 'song.authors:', song.authors[i]
        assert song.authors[i] == authors[i]

    # test verse order
    order = song.lyrics.present_order
    assert order == ['v1', 'c', 'v2', 'c', 'v3', 'c']

    # test verses order
    verses = song.lyrics.verses_order()
    assert verses[0].verse_id == 'v1'
    assert verses[1].verse_id == 'c'
    assert verses[2].verse_id == 'v2'
    assert verses[3].verse_id == 'c'
    assert verses[4].verse_id == 'v3'
    assert verses[5].verse_id == 'c'

    # test verses order normal
    verses = song.lyrics.verses_order_normal()
    assert verses[0].verse_id == 'v1'
    assert verses[1].verse_id == 'c'
    assert verses[2].verse_id == 'v2'
    assert verses[3].verse_id == 'v3'

    # test verses order presentation
    verses = song.lyrics.verses_order_presentation()
    assert verses[0].verse_id == 'v1'
    assert verses[1].verse_id == 'c'
    assert verses[2].verse_id == 'v2'
    assert verses[3].verse_id == 'c'
    assert verses[4].verse_id == 'v3'
    assert verses[5].verse_id == 'c'

    # test verses order custom
    verses = song.lyrics.verses_order_custom('v3 c c v2')
    assert verses[0].verse_id == 'v3'
    assert verses[1].verse_id == 'c'
    assert verses[2].verse_id == 'c'
    assert verses[3].verse_id == 'v2'

    # test verses count
    # 3 real verses + 1 chorus
    assert len(song.lyrics.verses) == 4

    # test verse lines count
    vrs = song.lyrics.verses
    sizes = [6, 4, 6, 6]
    for i in range(0, len(sizes)):
        assert len(vrs[i].lines) == sizes[i]

    # test 1st verse content
    verse = song.lyrics.verses[0].lines
    lst = [u'Mám zde přítele,',
        u'Pána Ježíše,',
        u'a na rámě jeho spoléhám;',
        u'v něm své stěstí mám,',
        u'pokoj nalézám,',
        u'když na rámě jeho spoléhám!',]
    for i in range(0, len(lst)):
        assert verse[i].text == lst[i]

    # test chorus content
    chorus = song.lyrics.verses[1].lines
    lst = [u'Boží rámě',
        u'je v soužení náš pevný hrad;',
        u'Boží rámě,',
        u'uč se na ně vždycky spoléhat!',]
    for i in range(0, len(lst)):
        assert chorus[i].text == lst[i]

def test_unicode_filename():
    # on win32 lxml (libxml2) is not able handle unicode filenames itself.
    # Python's file object is used
    import patterns
    fname = paths.unicode_filename
    song = io.song.Song(fname)
    assert io.song.tostring(song) == patterns.unicode_filename_song
   
