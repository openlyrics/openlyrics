<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
 version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 xmlns:ol="http://openlyrics.info/namespace/2009/song"
 xmlns="http://openlyrics.info/namespace/2009/song">
  <xsl:output method="xml" encoding="utf-8" indent="yes"/>

  <!-- Current datetime is given by Makefile -->
  <xsl:param name="datetime"/>

  <!-- Chords -->
  <xsl:variable name="chordnotation" select="document('../stylesheets/xsl/openlyrics-0.9-chord.xml')/chordnotation"/>
  <xsl:variable name="notation">
    <xsl:choose>
      <xsl:when test="//ol:song/@chordnotation">
        <xsl:value-of select="//ol:song/@chordnotation"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>english</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>

  <xsl:template name="chordname">
    <xsl:param name="this" />
    <xsl:value-of select="$chordnotation/notation[@id=$notation]/name[@class=$this/@root]/text()"/>
    <xsl:value-of select="$chordnotation/structure[@id=$this/@structure]/text()|$chordnotation/structure[@shorthand=$this/@structure]/text()"/>
    <xsl:if test="string-length($this/@bass)!=0">
      <xsl:text>/</xsl:text>
      <xsl:value-of select="$chordnotation/notation[@id=$notation]/name[@class=$this/@bass]/text()"/>
    </xsl:if>
  </xsl:template>

  <!-- Main: copy all nodes and attributes -->
  <xsl:template match="node()|@*">
    <xsl:copy>
       <xsl:apply-templates select="node()|@*"/>
    </xsl:copy>
  </xsl:template>

  <!-- Create root element, while attributes createdIn, modifiedIn and modifiedDate are optional. Stripping //ol:song/@chordnotation, //ol:song/@xml:lang -->
  <xsl:template match="//ol:song">
    <xsl:element name="{local-name()}" namespace="{namespace-uri(}">
      <xsl:attribute name="version">0.8</xsl:attribute>
      <xsl:attribute name="createdIn">
        <xsl:choose>
          <xsl:when test="//ol:song/@createdIn !=''"><xsl:value-of select="//ol:song/@createdIn" /></xsl:when>
          <xsl:otherwise>Not known</xsl:otherwise>
       </xsl:choose>
      </xsl:attribute>
      <xsl:attribute name="modifiedIn">
        <xsl:choose>
          <xsl:when test="//ol:song/@modifiedIn !=''"><xsl:value-of select="//ol:song/@modifiedIn" /></xsl:when>
          <xsl:otherwise>OpenLyrics 0.9 to 0.8 XSLT converter</xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>
      <xsl:attribute name="modifiedDate">
        <xsl:choose>
          <xsl:when test="//ol:song/@modifiedDate !=''"><xsl:value-of select="//ol:song/@modifiedDate" /></xsl:when>
          <xsl:otherwise><xsl:value-of select="$datetime"/></xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>
      <xsl:apply-templates/>
    </xsl:element>
  </xsl:template>

  <!-- Remove parts not compliant with version 0.8 -->
  <xsl:template match="//ol:song/ol:lyrics/ol:verse/ol:lines/@repeat"/>
  <xsl:template match="//ol:song/ol:lyrics/ol:instrument"/>
  <xsl:template match="//ol:song/ol:properties/ol:verseOrder">
    <xsl:element name="verseOrder">
      <xsl:value-of select="normalize-space(translate(., 'imos', '' ))"/>
      <!-- XXX needs a better implementation to handle "i2" type declarations -->
    </xsl:element>
  </xsl:template>

  <!-- Transform cords and cord's name respecting chordnotation -->
  <xsl:template match="//ol:chord">
    <xsl:element name="chord">
      <xsl:attribute name="name">
        <xsl:call-template name="chordname">
          <xsl:with-param name="this" select="."/>
        </xsl:call-template>
      </xsl:attribute>
    </xsl:element>
    <xsl:apply-templates/>
  </xsl:template>

</xsl:stylesheet>
