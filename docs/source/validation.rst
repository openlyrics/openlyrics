:tocdepth: 2

.. _validation:

Data Validation
===============

Data validation is the process of ensuring that the structure of the data
confirms to a defined format. This is especially useful for developers when
they add support for a data format to their application. They are able to
test that the data they produce is correct and conforms to the format.

In the world of XML, validation involves checking the names of elements,
their nesting, names of attribues and the type of values in elements and
attributes. Several `XML Schema languages <https://en.wikipedia.org/wiki/XML_schema>`_
exist for the formal definition of an XML structure. For the OpenLyrics data
format the `RelaxNG <https://en.wikipedia.org/wiki/RELAX_NG>`_ chosen and
used to create the format definition.

Tools and Libraries
-------------------------

The OpenLyrics RelaxNG XML schema can be used in any programming language
which has libraries with support for XML schemas. It is also possible, to
some extent, to convert RelaxNG schemas to other languages, like
`DTD <https://en.wikipedia.org/wiki/Document_type_definition>`_ or
`W3C XML Schema <https://en.wikipedia.org/wiki/XML_Schema_(W3C)>`_.

* `Sun Multi-Schema Validator <https://github.com/xmlark/msv>`_: Java technology
  tool to validate XML documents against several kinds of XML schemata.
* `lxml <https://lxml.de/>`_: Pythonic xml library, offers support
  for XPath, RelaxNG, XML Schema, XSLT, C14N and more.
* `On-line validator <https://validator.nu/>`_.
* `Jing <https://relaxng.org/#software>`_: A validator written in Java.
* `XSD to Relax NG <http://debeissat.nicolas.free.fr/XSDtoRNG.php>`_: An
  online converter.
* `Libxml2 <http://www.xmlsoft.org/>`_: XML C library, with support for
  RelaxNG validation.

A list of other software for RelaxNG can be found on the
`RelaxNG site <https://relaxng.org/#software>`_.

Validation examples
-------------------

CLI validation using Libxml2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To validate an OpenLyrics XML file use the following command::

    xmllint --noout --relaxng openlyrics-0.9.rng xmlfile.xml

``xmlfile.xml`` is the OpenLyrics file which you need to validate and
``openlyrics-0.9.rng`` contains OpenLyrics RelaxNG XML schema.
``xmllint`` is part of the ``libxml2`` library and can be installed on Debian based
system with ``apt-get install libxml2-utils``.


Validating using Python
^^^^^^^^^^^^^^^^^^^^^^^

Example::

    #!/usr/bin/env python3

    from lxml import etree

    xml_validator = etree.RelaxNG(file = "openlyrics-0.9.rng")
    xml_file = etree.parse("xmlfile.xml")
    is_valid = xml_validator.validate(xml_file)

    print(f'xmlfile.xml is{"" if is_valid else " not"} valid')

``xmlfile.xml`` is the OpenLyrics file which you need to validate and
``openlyrics-0.9.rng`` contains OpenLyrics RelaxNG XML schema.

Bundled CLI Script
^^^^^^^^^^^^^^^^^^

To execute the included script, use the following command::

    python3 tools/validate.py openlyrics-0.9.rng xmlfile.xml

``xmlfile.xml`` is the OpenLyrics file which you need to validate and
``openlyrics-0.9.rng`` contains OpenLyrics RelaxNG XML schema.
`Python <https://www.python.org/>`_ >= 3.6 and `lxml <https://lxml.de/>`_ is required.


RelaxNG XML schema
------------------

The following RelaxNG XML schema was created:

.. literalinclude:: ../../openlyrics-0.9.rng

