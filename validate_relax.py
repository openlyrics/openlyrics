#!/usr/bin/env python

import sys

from lxml import etree


relaxng_file = sys.argv[1]
xml_file = sys.argv[2]

relaxng_doc = etree.parse(relaxng_file)
xml_doc = etree.parse(xml_file)

relaxng = etree.RelaxNG(relaxng_doc)

relaxng.assertValid(xml_doc)

