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


'''Assertion patterns for OpenLyrics Python library test suite.'''


eng_song = u'''<?xml version='1.0' encoding='UTF-8'?>
<song createdIn="opensong2openlyrics.py 0.1" modifiedDate="2009-12-31T07:36:52.305167" modifiedIn="opensong2openlyrics.py 0.1" version="0.6" xmlns="http://openlyrics.info/namespace/2009/song">
  <properties>
    <titles>
      <title>What A Friend We Have In Jesus</title>
    </titles>
    <authors>
      <author>Joseph M. Scriven</author>
      <author>Charles C. Convers</author>
    </authors>
    <themes>
      <theme>Christ: Love/Mercy</theme>
      <theme>Fruit: Peace/Comfort</theme>
    </themes>
    <copyright>Public Domain</copyright>
    <ccliNo>27714</ccliNo>
  </properties>
  <lyrics>
    <verse name="v1">
      <lines>
        <line>What a friend we have in Jesus, All ours sins and griefs to bear;</line>
        <line>What a privilege to carry, Everything to God in prayer!</line>
        <line>O what peace we often forfeit, O what needless pain we bear;</line>
        <line>All because we do not carry, Everything to God in prayer!</line>
      </lines>
    </verse>
    <verse name="v2">
      <lines>
        <line>Have we trials and temptations? Is there trouble anywhere?</line>
        <line>We should never be discouraged, Take it to the Lord in prayer.</line>
        <line>Can we find a friend so faithful? Who will all our sorrows share?</line>
        <line>Jesus knows our every weakness; Take it to the Lord in prayer.</line>
      </lines>
    </verse>
    <verse name="v3">
      <lines>
        <line>Are we weak and heavy laden, Cumbered with a load of care?</line>
        <line>Precious Saviour still our refuge; Take it to the Lord in prayer.</line>
        <line>Do thy friends despise forsake thee? Take it to the Lord in prayer!</line>
        <line>In His arms He’ll take and shield thee; Thou wilt find a solace there.</line>
      </lines>
    </verse>
  </lyrics>
</song>'''


l10n_song = u'''<?xml version='1.0' encoding='UTF-8'?>
<song createdIn="opensong2openlyrics.py 0.1" modifiedDate="2009-12-31T07:36:37.405351" modifiedIn="opensong2openlyrics.py 0.1" version="0.6" xmlns="http://openlyrics.info/namespace/2009/song">
  <properties>
    <titles>
      <title>Mám zde přítele</title>
    </titles>
    <authors>
      <author>A.J. Showalter</author>
      <author>E.A. Hoffman</author>
    </authors>
    <verseOrder>v1 c v2 c v3 c</verseOrder>
  </properties>
  <lyrics>
    <verse name="v1">
      <lines>
        <line>Mám zde přítele,</line>
        <line>Pána Ježíše,</line>
        <line>a na rámě jeho spoléhám;</line>
        <line>v něm své stěstí mám,</line>
        <line>pokoj nalézám,</line>
        <line>když na rámě jeho spoléhám!</line>
      </lines>
    </verse>
    <verse name="c">
      <lines>
        <line>Boží rámě</line>
        <line>je v soužení náš pevný hrad;</line>
        <line>Boží rámě,</line>
        <line>uč se na ně vždycky spoléhat!</line>
      </lines>
    </verse>
    <verse name="v2">
      <lines>
        <line>Jak je sladké být,</line>
        <line>v jeho družině,</line>
        <line>když na rámě jeho spoléhám,</line>
        <line>jak se života</line>
        <line>cesta zjasňuje</line>
        <line>když na rámě Boží spoléhám!</line>
      </lines>
    </verse>
    <verse name="v3">
      <lines>
        <line>Čeho bych se bál,</line>
        <line>čeho strachoval,</line>
        <line>když na rámě Boží spoléhám?</line>
        <line>Mír je v duši mé,</line>
        <line>když On blízko je,</line>
        <line>když na rámě jeho spoléhám.</line>
      </lines>
    </verse>
  </lyrics>
</song>'''


prettyprint_eng_song = \
'''<?xml version='1.0' encoding='UTF-8'?>
<song xmlns="http://openlyrics.info/namespace/2009/song" version="0.6" createdIn="opensong2openlyrics.py 0.1" modifiedIn="opensong2openlyrics.py 0.1" modifiedDate="2009-12-31T07:36:52.305167">
  <properties>
    <titles>
      <title>What A Friend We Have In Jesus</title>
    </titles>
    <authors>
      <author>Joseph M. Scriven</author>
      <author>Charles C. Convers</author>
    </authors>
    <copyright>Public Domain</copyright>
    <ccliNo>27714</ccliNo>
    <themes>
      <theme>Christ: Love/Mercy</theme>
      <theme>Fruit: Peace/Comfort</theme>
    </themes>
  </properties>
  <lyrics>
    <verse name="v1">
      <lines>
        <line>What a friend we have in Jesus, All ours sins and griefs to bear;</line>
        <line>What a privilege to carry, Everything to God in prayer!</line>
      </lines>
    </verse>
  </lyrics>
</song>
'''

prettyprint_l10n_song = \
u'''<?xml version='1.0' encoding='UTF-8'?>
<song xmlns="http://openlyrics.info/namespace/2009/song" version="0.6" createdIn="opensong2openlyrics.py 0.1" modifiedIn="opensong2openlyrics.py 0.1" modifiedDate="2009-12-31T07:36:37.405351">
  <properties>
    <titles>
      <title>Mám zde přítele</title>
    </titles>
    <authors>
      <author>A.J. Showalter</author>
      <author>E.A. Hoffman</author>
    </authors>
    <verseOrder>v1 c v2 c v3 c</verseOrder>
  </properties>
  <lyrics>
    <verse name="v1">
      <lines>
        <line>Mám zde přítele,</line>
        <line>Pána Ježíše,</line>
        <line>a na rámě jeho spoléhám;</line>
      </lines>
    </verse>
    <verse name="c">
      <lines>
        <line>Boží rámě</line>
        <line>je v soužení náš pevný hrad;</line>
      </lines>
    </verse>
  </lyrics>
</song>
'''


editing_eng_song = \
'''<?xml version='1.0' encoding='UTF-8'?>
<song xmlns="http://openlyrics.info/namespace/2009/song" version="0.6" createdIn="opensong2openlyrics.py 0.1" modifiedIn="opensong2openlyrics.py 0.1" modifiedDate="2009-12-31T07:36:52.305167">
  <properties>
    <titles>
      <title>What A Friend We Have In Jesus (Title edited)</title>
    </titles>
    <authors>
      <author>Joseph M. Scriven</author>
      <author>Charles C. Convers</author>
    </authors>
    <copyright>Public Domain</copyright>
    <ccliNo>27714</ccliNo>
    <themes>
      <theme>Christ: Love/Mercy</theme>
      <theme>Fruit: Peace/Comfort</theme>
    </themes>
  </properties>
  <lyrics>
    <verse name="v1">
      <lines>
        <line>What a friend we have in Jesus, All ours sins and griefs to bear;</line>
        <line>What a privilege to carry, Everything to God in prayer!</line>
      </lines>
    </verse>
  </lyrics>
</song>
'''

editing_l10n_song = \
u'''<?xml version='1.0' encoding='UTF-8'?>
<song xmlns="http://openlyrics.info/namespace/2009/song" version="0.6" createdIn="opensong2openlyrics.py 0.1" modifiedIn="opensong2openlyrics.py 0.1" modifiedDate="2009-12-31T07:36:37.405351">
  <properties>
    <titles>
      <title>Mám zde přítele (Title edited)</title>
    </titles>
    <authors>
      <author>A.J. Showalter</author>
      <author>E.A. Hoffman</author>
    </authors>
    <verseOrder>v1 c v2 c v3 c</verseOrder>
  </properties>
  <lyrics>
    <verse name="v1">
      <lines>
        <line>Mám zde přítele,</line>
        <line>Pána Ježíše,</line>
        <line>a na rámě jeho spoléhám;</line>
      </lines>
    </verse>
    <verse name="c">
      <lines>
        <line>Boží rámě</line>
        <line>je v soužení náš pevný hrad;</line>
      </lines>
    </verse>
  </lyrics>
</song>
'''

unicode_filename_song = \
u'''<?xml version='1.0' encoding='UTF-8'?>
<song createdIn="ChangingSong 0.0.3" modifiedDate="2008-11-28T13:15:30+01:00" modifiedIn="ChangingSong 0.0.3" version="0.7" xmlns="http://openlyrics.info/namespace/2009/song">
  <properties>
    <titles>
      <title>This is Song Title</title>
    </titles>
  </properties>
  <lyrics>
    <verse name="v1">
      <lines>
        <line>This is first verse.</line>
      </lines>
    </verse>
    <verse name="c">
      <lines>
        <line>This is chorus.</line>
      </lines>
    </verse>
  </lyrics>
</song>'''

song_with_default_values = \
u'''<?xml version='1.0' encoding='UTF-8'?>
<song createdIn="OpenLyrics Python Library 0.1" modifiedDate="2010-06-04T21:51:57" modifiedIn="OpenLyrics Python Library 0.1" version="0.7" xmlns="http://openlyrics.info/namespace/2009/song">
  <properties />
  <lyrics />
</song>'''
