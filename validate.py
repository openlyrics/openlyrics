#!/usr/bin/env python

import sys

from lxml import etree


xmlschema_file = sys.argv[1]
xml_file = sys.argv[2]

xmlschema_doc = etree.parse(xmlschema_file)
xml_doc = etree.parse(xml_file)

xmlschema = etree.XMLSchema(xmlschema_doc)

xmlschema.assertValid(xml_doc)

