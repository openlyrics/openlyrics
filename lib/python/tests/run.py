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

import test_example
import test_basic


# use relative paths
# Workaround for placing openlyrics module in a path
# with only ascii characters.
scriptdir = path.join(path.dirname(__file__))
os.chdir(scriptdir)

# add OpenLyric Python library to PYTHON_PATH
sys.path.insert(0, '.')

# TODO replace Nose test framework with built-in unittest module


def suite():

    suite = unittest.TestSuite()
    suite.addTest(test_basic.suite())
    suite.addTest(test_example.suite())

    return suite


if __name__ == '__main__':
    print('Running OpenLyrics test suite...')
    print(os.getcwd())
    unittest.main(defaultTest='suite')
