<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
 version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 xmlns:ol="http://openlyrics.info/namespace/2009/song"
 xmlns:str="http://exslt.org/strings"
 extension-element-prefixes="str"
 xmlns="http://openlyrics.info/namespace/2009/song">
  <xsl:output method="xml" encoding="utf-8" indent="yes"/>

  <!-- config variables -->
  <xsl:param name="empty-chords">true</xsl:param>

  <!-- Main: copy all nodes and attributes -->
  <xsl:template match="node()|@*">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
    </xsl:copy>
  </xsl:template>

  <!-- Set OL version -->
  <xsl:template match="/ol:song/@version">
    <xsl:attribute name="version">0.9</xsl:attribute>
  </xsl:template>

  <!-- Convert chords -->
  <xsl:template match="//ol:chord">
    <!-- Tokenize @name to $root, $structure, $bass
         If regexp:match worked... ^([ABE]b|[ACDFG]#|[ABCDEFG])([\d\w\(\)\+\#]*)?(?:\/([ABE]b|[ACDFG]#|[ABCDEFG]))?$
         Supports all variation of https://github.com/openlyrics/openlyrics/blob/v0.8/chords.txt
         - Root/Bass: C, C#, Db, D, D#, Eb, E, F, F#, Gb, G, G#, Ab, A, A#, Bb, B.
           Any other input will return 'UNKNOWN:' frefix.
         - Structure: 5, maj, m, +, dim, 7, maj7, m7, 7(b5), m7b5, maj7(#5), 6, m6, 9, 7(b9), 7b9, maj9, m9, 11, m11, 13,
           4, sus, sus4, sus2, sus9, (add9), (addD), addD, add2, add9, addG7(sus4), 7sus4, 7sus2, maj7sus4, 9sus
    -->
    <xsl:variable name="temp">
      <xsl:choose>
        <xsl:when test="contains(@name, '/')">
          <xsl:value-of select="substring-before(@name, '/' )" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="@name" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="bass" select="substring-after(@name, concat($temp, '/'))" />
    <xsl:variable name="root">
      <xsl:choose>
        <xsl:when test="substring($temp, 2, 1) = '#' or substring($temp, 2, 1) = 'b'">
          <xsl:value-of select="substring($temp, 1, 2)" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="substring($temp, 1, 1)" />
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="structure" select="substring-after($temp, $root )"/>
    <!-- Convert to new attributes -->
    <xsl:element name="{local-name()}" namespace="{namespace-uri(}">
      <xsl:attribute name="root">
        <xsl:call-template name="convertNote">
          <xsl:with-param name="note" select="$root"/>
        </xsl:call-template>
      </xsl:attribute>
      <xsl:if test="$structure != ''">
        <xsl:attribute name="structure">
          <xsl:choose>
            <xsl:when test="$structure = 'm'">min</xsl:when>
            <xsl:when test="$structure = '5'">power</xsl:when>
            <xsl:when test="$structure = 'maj'"></xsl:when>
            <xsl:when test="$structure = 'm'">min</xsl:when>
            <xsl:when test="$structure = '+'">aug</xsl:when>
            <xsl:when test="$structure = 'dim'">dim</xsl:when>
            <xsl:when test="$structure = '7'">dom7</xsl:when>
            <xsl:when test="$structure = 'maj7'">maj7</xsl:when>
            <xsl:when test="$structure = 'm7'">min7</xsl:when>
            <xsl:when test="$structure = '7(b5)' or $structure = 'm7b5'">halfdim7</xsl:when>
            <xsl:when test="$structure = 'm#7' or $structure = 'm(#7)' or $structure = 'm(maj7)' or $structure = 'mmaj7'">minmaj7</xsl:when>
            <xsl:when test="$structure = 'maj7(#5)'">augmaj7</xsl:when>
            <xsl:when test="$structure = '6'">maj6</xsl:when>
            <xsl:when test="$structure = 'm6'">min6</xsl:when>
            <xsl:when test="$structure = '9'">dom9</xsl:when>
            <xsl:when test="$structure = '7(b9)' or $structure = '7b9'">dom9b</xsl:when>
            <xsl:when test="$structure = 'maj9'">maj9</xsl:when>
            <xsl:when test="$structure = 'm9'">min9</xsl:when>
            <xsl:when test="$structure = 'm9(maj7)' or $structure = 'm9maj7'">minmaj9</xsl:when>
            <xsl:when test="$structure = 'm(add9)' or $structure = 'madd9 '">m3-5-9</xsl:when>
            <xsl:when test="$structure = '7#9' or $structure = '7(#9)'">3-5-m7-m10</xsl:when>
            <xsl:when test="$structure = '11' or $structure = '7(11)' or $structure = '9(11)'">3-5-m7-9-11</xsl:when>
            <xsl:when test="$structure = 'm11'">m3-5-m7-9-11</xsl:when>
            <xsl:when test="$structure = '13' or $structure = '9(add6)' or $structure = '9add6'">3-5-m7-9-11-13</xsl:when>
            <xsl:when test="$structure = '4'or $structure = 'sus' or $structure = 'sus4' or $structure ='m(sus4)' or $structure = 'msus4'">sus4</xsl:when>
            <xsl:when test="$structure = 'sus2' or $structure = 'sus9' or $structure='m(sus9)' or $structure = 'msus9'">sus2</xsl:when>
            <xsl:when test="$structure = '2' or $structure = '(add9)' or $structure = '(addD)' or $structure = 'addD' or $structure = 'add2' or $structure = 'add9' or $structure = 'addG'">add9</xsl:when>
            <xsl:when test="$structure = '7(sus4)' or $structure = '7sus4' or $structure = 'm7sus4'  or $structure = 'addE'">4-5-m7</xsl:when>
            <xsl:when test="$structure = '7sus2'">2-5-m7</xsl:when>
            <xsl:when test="$structure = '6sus4' or $structure = '6(sus4)'">4-5-m7-13</xsl:when>
            <xsl:when test="$structure = 'maj7sus4'">4-5-7</xsl:when>
            <xsl:when test="$structure = '9sus'">4-5-m7-9</xsl:when>
            <xsl:when test="$structure = 'm#5' or $structure = 'm(#5)'">SIXTH:<xsl:value-of select="$structure"/></xsl:when><!-- the major sixth chord (first inversion) of the chord n3-below the current root, example: Dm(#5) → Bb/D-->
            <xsl:otherwise>UNKNOWN:<xsl:value-of select="$structure"/></xsl:otherwise>
          </xsl:choose>
        </xsl:attribute>
      </xsl:if>
      <xsl:if test="$bass != ''">
        <xsl:attribute name="bass">
          <xsl:call-template name="convertNote">
            <xsl:with-param name="note" select="$bass"/>
          </xsl:call-template>
        </xsl:attribute>
      </xsl:if>
      <xsl:if test="$empty-chords = 'false' and
                    name(following-sibling::node()[1]) != 'chord'">
        <xsl:value-of select="normalize-space(following-sibling::text()[1])"/>
      </xsl:if>
    </xsl:element>
    <xsl:if test="$empty-chords = 'false' and
                  name(following-sibling::node()[1]) != 'chord' and
                  substring(following-sibling::text()[1], string-length(following-sibling::text()[1]), 1) = ' '">
      <xsl:text> </xsl:text>
    </xsl:if>
  </xsl:template>

  <xsl:template match="text()[name(preceding-sibling::node()[1]) = 'chord']">
    <xsl:choose>
      <xsl:when test="$empty-chords = 'false'"></xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="."/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template name="convertNote">
    <xsl:param name="note" />
    <xsl:choose>
      <xsl:when test="$note = 'C'  or
                      $note = 'C#' or
                      $note = 'Db' or
                      $note = 'D'  or
                      $note = 'D#' or
                      $note = 'Eb' or
                      $note = 'E'  or
                      $note = 'F'  or
                      $note = 'F#' or
                      $note = 'Gb' or
                      $note = 'G'  or
                      $note = 'G#' or
                      $note = 'Ab' or
                      $note = 'A'  or
                      $note = 'A#' or
                      $note = 'Bb' or
                      $note = 'B'">
        <xsl:value-of select="$note"/>
      </xsl:when>
      <xsl:otherwise>UNKNOWN:<xsl:value-of select="$note"/></xsl:otherwise>
    </xsl:choose>
  </xsl:template>

</xsl:stylesheet>
