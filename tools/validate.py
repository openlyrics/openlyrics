#!/usr/bin/env python3
# Usage: validate.py openlyrics-0.9.rng <XML file to be validated>

import argparse
import sys

from lxml import etree

parser = argparse.ArgumentParser(description = 'Validate an OpenLyrics XML file using a RELAX NG schema.')
parser.add_argument('relaxng', help = 'RELAX NG schema file')
parser.add_argument('openlyrics', help = 'OpenLyrics XML file')

args = parser.parse_args()

xml_validator = etree.RelaxNG(file = args.relaxng)
xml_file = etree.parse(args.openlyrics)
is_valid = xml_validator.validate(xml_file)

print(f'{sys.argv[2]} is{"" if is_valid else " not"} valid')

# set exit code to 0 if the file validates, set it to 1 otherwise
sys.exit(int(not is_valid))
