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
attributes. Several `XML Schema languages <http://en.wikipedia.org/wiki/XML_schema>`_
exist for the formal definition of an XML structure. For the OpenLyrics data
format the `RelaxNG <http://en.wikipedia.org/wiki/RELAX_NG>`_ chosen and
used to create the format definition.

Bundled CLI Script
---------------------------

This section describes how to use bundled script ``validate.py`` in command
prompt.

Prerequisites
^^^^^^^^^^^^^

Before using the script for validation please ensure that the following
is available in your system:

* `Python <http://www.python.org/>`_ >= 2.5
* `lxml <http://codespeak.net/lxml/>`_

Usage
^^^^^

To execute the script, use the following command::

    python validate.py  openlyrics_schema.rng  xmlfile.xml

``xmlfile.xml`` is the file which you need to validate and
``openlyrics_schema.rng`` contains OpenLyrics RelaxNG XML schema.


Tools and Libraries
-------------------------

The OpenLyrics RelaxNG XML schema can be used in any programming language
which has libraries with support for XML schemas. It is also possible, to
some extent, to convert RelaxNG schemas to other languages, like
`DTD <http://en.wikipedia.org/wiki/Document_Type_Definition>`_ or
`W3C XML Schema <http://en.wikipedia.org/wiki/XML_Schema_(W3C)>`_.

* `Sun Multi-Schema Validator <https://msv.dev.java.net/>`_: Java technology
  tool to validate XML documents against several kinds of XML schemata.
* `lxml <http://codespeak.net/lxml/>`_: Pythonic xml library, offers support
  for XPath, RelaxNG, XML Schema, XSLT, C14N and more.
* `On-line validator <http://validator.nu/>`_.
* `Jing <http://relaxng.org/#software>`_: A validator written in Java.
* `XSD to Relax NG <http://debeissat.nicolas.free.fr/XSDtoRNG.php>`_: An
  online converter.
* `Libxml2 <http://www.xmlsoft.org/>`_: XML C library, with support for
  RelaxNG validation.

A list of other software for RelaxNG can be found on the
`RelaxNG site <http://relaxng.org/#software>`_.


RelaxNG XML schema
------------------

The following RelaxNG XML schema was created:

.. literalinclude:: ../../openlyrics_schema.rng

