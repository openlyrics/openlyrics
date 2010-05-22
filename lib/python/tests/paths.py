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


from os.path import normpath, join, dirname, abspath


SONGDIR = join('.', 'songs')
TMPDIR = join('.', 'tmp')

eng_song = join(SONGDIR, 'What A Friend We Have In Jesus.xml')
l10n_song = join(SONGDIR,
        u'Mám zde přítele, Pána Ježíše.xml')
invalid_song = join(SONGDIR, 'InvalidXml.xml')

notprettyprint_eng_song = join(SONGDIR,
        'NotPrettyPrint - What A Friend We Have In Jesus.xml')
notprettyprint_l10n_song = join(SONGDIR, u'NotPrettyPrint - Mám zde přítele.xml')

editing_eng_song = join(SONGDIR,
        'NotPrettyPrint - What A Friend We Have In Jesus.xml')
editing_l10n_song = join(SONGDIR, u'NotPrettyPrint - Mám zde přítele.xml')

# filename contains Czech and Swedish characters
unicode_filename = join(SONGDIR, u'UnicodeFilename - ěščřžýáíé åäö.xml')
