#!/usr/bin/env python

import sys

try:
    from lxml import etree
except ImportError:
    print('Python module "lxml" is required')
    exit(1)


if len(sys.argv) != 3:
    print('Usage: python   %s   openlyrics_schema.rng  xmlfile.xml' % __file__)
    exit(1)


relaxng_file = sys.argv[1]
xml_file = sys.argv[2]

relaxng_doc = etree.parse(relaxng_file)
xml_doc = etree.parse(xml_file)

relaxng = etree.RelaxNG(relaxng_doc)

relaxng.assertValid(xml_doc)

