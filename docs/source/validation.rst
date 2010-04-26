:tocdepth: 2

.. _validation:

Data Validation
===============

Data validation is a process how to ensure that the data structure conforms
to the defined format. This is useful especially for developers when they
add support for a data format to their application. It makes developers happier when there is formal way how to test the right structure of newly
created data in the new format.

In the world of XML validation means to check names of elements, their nesting, names of attribues and the type of values in 
elements and attributes. There exist several `XML Schema languages
<http://en.wikipedia.org/wiki/XML_schema>`_ for formal definition of XML
structure. For OpenLyrics data format was created XML schema by using
the language `RelaxNG <http://en.wikipedia.org/wiki/RELAX_NG>`_.


Bundled CLI Script
---------------------------

This section describes how to use bundled script ``validate.py`` in command
prompt.

Prerequisites
^^^^^^^^^^^^^

Before using the script for validation please ensure that the following
is available in your system:

* `Python <http://www.python.org/>`_ >= 2.5
* `lxm <http://codespeak.net/lxml/>`_

Usage
^^^^^

To execute the scrit use the following command::

    python validate.py  openlyrics_schema.rng  xmlfile.xml

``xmlfile.xml`` is the file which you need to validate and
``openlyrics_schema.rng`` contains OpenLyrics RelaxNG XML schema.


Tools and Libraries
-------------------------

The OpenLyrics RelaxNG XML schema can be used in any programming language
for which there exist libraries with support for XML schemas. It is also possible to some extend convert RelaxNG schemas to other languages, like
`DTD <http://en.wikipedia.org/wiki/Document_Type_Definition>`_ or
`W3C XML Schema <http://en.wikipedia.org/wiki/XML_Schema_(W3C)>`_.

* `Sun Multi-Schema Validator <https://msv.dev.java.net/>`_: Java technology 
  tool to validate XML documents against several kinds of XML schemata.
* `lxml <http://codespeak.net/lxml/>`_: Pythonic xml library, offers support 
  for XPath, RelaxNG, XML Schema, XSLT, C14N and more.
* `On-line validator <http://validator.nu/>`_:
* `Jing <http://relaxng.org/#software>`_: A RELAX NG validator in Java
* `XSD to Relax NG Converter <http://debeissat.nicolas.free.fr/XSDtoRNG.php>`_: Web-based converter
* `Libxml2 <http://www.xmlsoft.org/>`_: XML C library, with support for 
  RELAX NG validation.

List of other software for RelaxNG: http://relaxng.org/#software


RelaxNG XML schema
------------------

The following RelaxNG XML schema was created:

.. literalinclude:: ../../openlyrics_schema.rng

