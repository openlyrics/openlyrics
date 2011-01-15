#!/usr/bin/env python
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


'''This script runs the OpenLyrics test suite.'''


import sys
import os
import unittest
from os import path

from tests import test_core
from tests import test_default_values
from tests import test_creating_song


# use relative paths
# Workaround for placing openlyrics module in a path
# with only ascii characters.
scriptdir = path.join(path.dirname(__file__))
os.chdir(scriptdir)

# add OpenLyric Python library to PYTHON_PATH
sys.path.insert(0, '.')


def suite():

    suite = unittest.TestSuite()
    suite.addTest(test_core.suite())
    suite.addTest(test_default_values.suite())
    suite.addTest(test_creating_song.suite())

    return suite


if __name__ == '__main__':
    print('Running OpenLyrics test suite...')
    unittest.main(defaultTest='suite')
