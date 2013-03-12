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
<song createdIn="opensong2openlyrics.py 0.1" modifiedDate="2013-03-12T09:13:04.212538" modifiedIn="convert-schema.py" version="0.8" xmlns="http://openlyrics.info/namespace/2009/song">
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
        What a friend we have in Jesus, All ours sins and griefs to bear;<br />
        What a privilege to carry, Everything to God in prayer!<br />
        O what peace we often forfeit, O what needless pain we bear;<br />
        All because we do not carry, Everything to God in prayer!
      </lines>
    </verse>
    <verse name="v2">
      <lines>
        Have we trials and temptations? Is there trouble anywhere?<br />
        We should never be discouraged, Take it to the Lord in prayer.<br />
        Can we find a friend so faithful? Who will all our sorrows share?<br />
        Jesus knows our every weakness; Take it to the Lord in prayer.
      </lines>
    </verse>
    <verse name="v3">
      <lines>
        Are we weak and heavy laden, Cumbered with a load of care?<br />
        Precious Saviour still our refuge; Take it to the Lord in prayer.<br />
        Do thy friends despise forsake thee? Take it to the Lord in prayer!<br />
        In His arms He’ll take and shield thee; Thou wilt find a solace there.
      </lines>
    </verse>
  </lyrics>
</song>'''


l10n_song = u'''<?xml version='1.0' encoding='UTF-8'?>
<song createdIn="opensong2openlyrics.py 0.1" modifiedDate="2013-03-12T09:39:58.853358" modifiedIn="convert-schema.py" version="0.8" xmlns="http://openlyrics.info/namespace/2009/song">
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
        Mám zde přítele,<br />
        Pána Ježíše,<br />
        a na rámě jeho spoléhám;<br />
        v něm své stěstí mám,<br />
        pokoj nalézám,<br />
        když na rámě jeho spoléhám!
      </lines>
    </verse>
    <verse name="c">
      <lines>
        Boží rámě<br />
        je v soužení náš pevný hrad;<br />
        Boží rámě,<br />
        uč se na ně vždycky spoléhat!
      </lines>
    </verse>
    <verse name="v2">
      <lines>
        Jak je sladké být,<br />
        v jeho družině,<br />
        když na rámě jeho spoléhám,<br />
        jak se života<br />
        cesta zjasňuje<br />
        když na rámě Boží spoléhám!
      </lines>
    </verse>
    <verse name="v3">
      <lines>
        Čeho bych se bál,<br />
        čeho strachoval,<br />
        když na rámě Boží spoléhám?<br />
        Mír je v duši mé,<br />
        když On blízko je,<br />
        když na rámě jeho spoléhám.
      </lines>
    </verse>
  </lyrics>
</song>'''


prettyprint_eng_song = u'''<?xml version='1.0' encoding='UTF-8'?>
<song createdIn="opensong2openlyrics.py 0.1" modifiedDate="2013-03-12T09:44:49.913345" modifiedIn="convert-schema.py" version="0.8" xmlns="http://openlyrics.info/namespace/2009/song">
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
      <lines>What a friend we have in Jesus, All ours sins and griefs to bear;<br />What a privilege to carry, Everything to God in prayer!</lines>
    </verse>
  </lyrics>
</song>'''


prettyprint_l10n_song = u'''<?xml version='1.0' encoding='UTF-8'?>
<song createdIn="opensong2openlyrics.py 0.1" modifiedDate="2013-03-12T09:42:10.424812" modifiedIn="convert-schema.py" version="0.8" xmlns="http://openlyrics.info/namespace/2009/song">
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
      <lines>Mám zde přítele,<br />Pána Ježíše,<br />a na rámě jeho spoléhám;</lines>
    </verse>
    <verse name="c">
      <lines>Boží rámě<br />je v soužení náš pevný hrad;</lines>
    </verse>
  </lyrics>
</song>'''


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
        What a friend we have in Jesus, All ours sins and griefs to bear;<br />
        What a privilege to carry, Everything to God in prayer!
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
        Mám zde přítele,<br />
        Pána Ježíše,<br />
        a na rámě jeho spoléhám;
      </lines>
    </verse>
    <verse name="c">
      <lines>
        Boží rámě<br />
        je v soužení náš pevný hrad;
      </lines>
    </verse>
  </lyrics>
</song>
'''

unicode_filename_song = \
u'''<?xml version='1.0' encoding='UTF-8'?>
<song createdIn="ChangingSong 0.0.3" modifiedDate="2013-03-12T09:47:32.249946" modifiedIn="convert-schema.py" version="0.8" xmlns="http://openlyrics.info/namespace/2009/song">
  <properties>
    <titles>
      <title>This is Song Title</title>
    </titles>
  </properties>
  <lyrics>
    <verse name="v1">
      <lines>
        This is first verse.
      </lines>
    </verse>
    <verse name="c">
      <lines>
        This is chorus.
      </lines>
    </verse>
  </lyrics>
</song>'''

song_with_default_values = \
u'''<?xml version='1.0' encoding='UTF-8'?>
<song createdIn="OpenLyrics Python Library 0.2" modifiedDate="2010-06-04T21:51:57" modifiedIn="OpenLyrics Python Library 0.2" version="0.8" xmlns="http://openlyrics.info/namespace/2009/song">
  <properties />
  <lyrics />
</song>'''
