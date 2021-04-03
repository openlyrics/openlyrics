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
  <xsl:param name="empty-chords">true</xsl:param><!-- Specifies "<chord/>text" or "<chord>text</chord>" format. Possible values: true, false -->
  <xsl:param name="chord-notation">english</xsl:param><!-- Specifies input chord notation. Possible values: english, english-b, german, dutch, hungarian, neolatin -->

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

  <!-- Convert chords: Supports documented notations and all variation of https://github.com/openlyrics/openlyrics/blob/v0.8/chords.txt -->
  <xsl:template match="//ol:chord">
    <!-- Tokenize @name to $root, $structure, $bass, TODO: port to regexp if available -->
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
        <xsl:when test="$chord-notation != 'neolation'">
          <xsl:choose>
            <!-- Cisz, Desz ... -->
            <xsl:when test="substring($temp, 2, 3) = 'isz'
                         or substring($temp, 2, 3) = 'esz'"><xsl:value-of select="substring($temp, 1, 4)" /></xsl:when>
            <!-- Cis, Des ... and Esz, Asz-->
            <xsl:when test="substring($temp, 2, 2) = 'is'
                         or substring($temp, 2, 2) = 'es'
                         or substring($temp, 2, 2) = 'sz'"><xsl:value-of select="substring($temp, 1, 3)" /></xsl:when>
            <!-- C#, Db ... -->
            <xsl:when test="substring($temp, 2, 1) = '#'
                         or substring($temp, 2, 1) = '♯'
                         or substring($temp, 2, 1) = 'b'
                         or substring($temp, 2, 1) = '♭'"><xsl:value-of select="substring($temp, 1, 2)" /></xsl:when>
            <!-- Es, As with attention to sus|sus2|sus4 -->
            <xsl:when test="substring($temp, 1, 2) = 'Es'
                         or substring($temp, 1, 2) = 'As'"><xsl:value-of select="substring($temp, 1, 2)" /></xsl:when>
            <!-- C, D ... -->
            <xsl:otherwise><xsl:value-of select="substring($temp, 1, 1)" /></xsl:otherwise>
          </xsl:choose>
        </xsl:when>
        <xsl:otherwise>
          <xsl:choose>
            <!-- Solb, Sol# -->
            <xsl:when test="substring($temp, 4, 1) = '#'
                         or substring($temp, 4, 1) = '♯'
                         or substring($temp, 4, 1) = 'b'
                         or substring($temp, 4, 1) = '♭'"><xsl:value-of select="substring($temp, 1, 4)" /></xsl:when>
            <!-- Do#, Reb, Re#, Mib, Fa#, Sol, Lab, La#, Sib -->
            <xsl:when test="substring($temp, 3, 1) = '#'
                         or substring($temp, 3, 1) = '♯'
                         or substring($temp, 3, 1) = 'b'
                         or substring($temp, 3, 1) = '♭'
                         or substring($temp, 3, 1) = 'l'"><xsl:value-of select="substring($temp, 1, 3)" /></xsl:when>
            <!-- Do, Re, Mi, Fa, La, Si -->
            <xsl:otherwise><xsl:value-of select="substring($temp, 1, 2)" /></xsl:otherwise>
          </xsl:choose>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="structure" select="substring-after($temp, $root )"/>
    <!-- Convert to new attributes -->
    <xsl:element name="{local-name()}" namespace="{namespace-uri(}">
      <xsl:attribute name="root">
        <xsl:call-template name="convertNote">
          <xsl:with-param name="n" select="$root"/>
        </xsl:call-template>
      </xsl:attribute>
      <xsl:if test="$structure != ''">
        <xsl:attribute name="structure">
          <xsl:call-template name="convertStructure">
            <xsl:with-param name="str" select="$structure"/>
          </xsl:call-template>
        </xsl:attribute>
      </xsl:if>
      <xsl:if test="$bass != ''">
        <xsl:attribute name="bass">
          <xsl:call-template name="convertNote">
            <xsl:with-param name="n" select="$bass"/>
          </xsl:call-template>
        </xsl:attribute>
      </xsl:if>
      <xsl:if test="$empty-chords = 'false'
                    and not(following-sibling::node()[1] = following-sibling::*[1])">
        <xsl:value-of select="normalize-space(following-sibling::text()[1])"/>
      </xsl:if>
    </xsl:element>
    <xsl:if test="$empty-chords = 'false'
              and not(following-sibling::node()[1] = following-sibling::*[1])
              and substring(following-sibling::text()[1],
                            string-length(following-sibling::text()[1]),
                            1) = ' '">
      <xsl:text> </xsl:text>
    </xsl:if>
  </xsl:template>

  <!-- Match text after a chord: only effective in "<chords>text</chords>" mode -->
  <xsl:template match="text()[name(preceding-sibling::node()[1]) = 'chord']">
    <xsl:choose>
      <xsl:when test="$empty-chords = 'false'"></xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="."/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template name="convertNote">
    <xsl:param name="n" />
    <xsl:choose>
      <xsl:when test="$n = 'C'
                   or $n = 'Do'">C</xsl:when>
      <xsl:when test="$n = 'C#'
                   or $n = 'Cis'
                   or $n = 'Cisz'
                   or $n = 'Do#'">C#</xsl:when>
      <xsl:when test="$n = 'Db'
                   or $n = 'Des'
                   or $n = 'Desz'
                   or $n = 'Reb'">Db</xsl:when>
      <xsl:when test="$n = 'D'
                   or $n = 'Re'">D</xsl:when>
      <xsl:when test="$n = 'D#'
                   or $n = 'Dis'
                   or $n = 'Disz'
                   or $n = 'Re#'">D#</xsl:when>
      <xsl:when test="$n = 'Eb'
                   or $n = 'Es'
                   or $n = 'Esz'
                   or $n = 'Mib'">Eb</xsl:when>
      <xsl:when test="$n = 'E'
                   or $n = 'Mi'">E</xsl:when>
      <xsl:when test="$n = 'F'
                   or $n = 'Fa'">F</xsl:when>
      <xsl:when test="$n = 'F#'
                   or $n = 'Fis'
                   or $n = 'Fisz'
                   or $n = 'Fa#'">F#</xsl:when>
      <xsl:when test="$n = 'Gb'
                   or $n = 'Ges'
                   or $n = 'Gesz'
                   or $n = 'Solb'">Gb</xsl:when>
      <xsl:when test="$n = 'G'
                   or $n = 'Sol'">G</xsl:when>
      <xsl:when test="$n = 'G#'
                   or $n = 'Gis'
                   or $n = 'Gisz'
                   or $n = 'Sol#'">G#</xsl:when>
      <xsl:when test="$n = 'Ab'
                   or $n = 'As'
                   or $n = 'Asz'
                   or $n = 'Lab'">Ab</xsl:when>
      <xsl:when test="$n = 'A'
                   or $n = 'La'">A</xsl:when>
      <xsl:when test="$n = 'A#'
                   or $n = 'Ais'
                   or $n = 'Aisz'
                   or $n = 'La#'">A#</xsl:when>
      <xsl:when test="$n = 'Bb'
                   or $n = 'Bes'
                   or $n = 'Sib'">Bb</xsl:when>
      <xsl:when test="$n = 'H'
                   or $n = 'Si'">B</xsl:when>
      <xsl:when test="$n = 'B'">
        <xsl:choose>
          <xsl:when test="$chord-notation = 'english-b'
                       or $chord-notation = 'german'
                       or $chord-notation = 'hungarian'">Bb</xsl:when>
          <xsl:otherwise>B</xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <xsl:otherwise>UNKNOWN:<xsl:value-of select="$n"/></xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template name="convertStructure">
    <xsl:param name="str" />
    <xsl:variable name="s">
      <xsl:value-of select="translate($str, '#b○∅', '♯♭ⵔⵁ')" />
    </xsl:variable>
    <xsl:choose>
      <!-- ** 2 note chords -->
      <!-- perfect 5th; power chord -->
      <xsl:when test="$s = '5'
                   or $s = 'omit3'">power</xsl:when>
      <!-- *** 3 note chords -->
      <!-- major -->
      <xsl:when test="$s = 'maj'"></xsl:when>
      <!-- minor -->
      <xsl:when test="$s = 'm'
                   or $s = '-'
                   or $s = 'min'">min</xsl:when>
      <!-- augmented -->
      <xsl:when test="$s = '+'
                   or $s = '5♯'
                   or $s = '(♯5)'">aug</xsl:when>
      <!-- diminished -->
      <xsl:when test="$s = 'dim'
                   or $s = 'm,5♭'
                   or $s = 'm(♭5)'">dim</xsl:when>
      <!-- **** 4 note chords -->
      <!-- dominant 7th -->
      <xsl:when test="$s = '7'">dom7</xsl:when>
      <!-- major 7th -->
      <xsl:when test="$s = 'maj7'
                   or $s = 'Δ'
                   or $s = 'Maj7'
                   or $s = 'M7'
                   or $s = 'Δ7'
                   or $s = '7+'">maj7</xsl:when>
      <!-- minor 7th -->
      <xsl:when test="$s = 'm7'
                   or $s = 'm7'
                   or $s = '-7'
                   or $s = 'min7'">min7</xsl:when>
      <!-- diminished 7th -->
      <xsl:when test="$s = 'ⵔ'
                   or $s = 'dim7'
                   or $s = 'ⵔ7'
                   or $s = 'o'
                   or $s = 'o7'">dim7</xsl:when>
      <!-- half-diminished 7th -->
      <xsl:when test="$s = 'ⵁ'
                   or $s = 'm7,5♭'
                   or $s = 'm7(♭5)'
                   or $s = '-7(♭5)'
                   or $s = 'ⵁ7'
                   or $s = 'halfdim'
                   or $s = '7(♭5)'
                   or $s = 'm7♭5'">halfdim7</xsl:when>
      <!-- minor major 7th -->
      <xsl:when test="$s = 'mΔ'
                   or $s = 'mMaj7'
                   or $s = 'mM7'
                   or $s = '-M7'
                   or $s = '-Δ'
                   or $s = '-Δ7'
                   or $s = 'm♯7'
                   or $s = 'm(♯7)'
                   or $s = 'm(maj7)'
                   or $s = 'mmaj7'">minmaj7</xsl:when>
      <!-- augmented major 7th -->
      <xsl:when test="$s = '+Δ'
                   or $s = 'Maj7(♯5)'
                   or $s = '+Maj7'
                   or $s = '+M7'
                   or $s = '+Δ7'
                   or $s = 'maj7(♯5)'">augmaj7</xsl:when>
      <!-- dominant 7th flat 5 -->
      <xsl:when test="$s = '7,5♭'
                   or $s = '7(♭5)'">3-d5-m7</xsl:when>
      <!-- dominant 7th sharp 5; augmented 7th -->
      <xsl:when test="$s = '+7'
                   or $s = '7,5♯'
                   or $s = '7(♯5)'">aug7</xsl:when>
      <!-- diminished major 7th -->
      <xsl:when test="$s = 'mΔ,5♭'
                   or $s = 'mΔ(5♭)'
                   or $s = 'mMaj7(♭5)'
                   or $s = 'mM7(♭5)'
                   or $s = '-Δ7(♭5)'">m3-d5-7</xsl:when>
      <!-- major 7th flat 5 -->
      <xsl:when test="$s = 'Δ,5♭'
                   or $s = 'Δ7(♭5)'
                   or $s = 'Maj7(♭5)'
                   or $s = 'M7(♭5)'">3-d5-7</xsl:when>
      <!-- major 6th -->
      <xsl:when test="$s = '6'
                   or $s = 'M6'
                   or $s = 'add6'">maj6</xsl:when>
      <!-- (major minor 6th) -->
      <xsl:when test="$s = '6♭'
                   or $s = '(♭6)'">maj6b</xsl:when>
      <!-- minor 6th -->
      <xsl:when test="$s = 'm6'
                   or $s = 'm,add6'">min6</xsl:when>
      <!-- (minor minor 6th) -->
      <xsl:when test="$s = 'm6♭'
                   or $s = 'm(♭6)'">min6b</xsl:when>
      <!-- ***** 5 note chords -->
      <!-- (dominant) 9th -->
      <xsl:when test="$s = '9'
                   or $s = '7,9'">dom9</xsl:when>
      <!-- dominant minor 9th -->
      <xsl:when test="$s = '7,9♭'
                   or $s = '7(♭9)'
                   or $s = '7♭9'
                   or $s = '7b9'">dom9b</xsl:when>
      <!-- major 9th -->
      <xsl:when test="$s = 'Δ9'
                   or $s = 'Maj9'
                   or $s = 'M9'
                   or $s = 'maj9'">maj9</xsl:when>
      <!-- minor (dominant) 9th -->
      <xsl:when test="$s = 'm9'
                   or $s = 'm7,9'
                   or $s = '-9'
                   or $s = 'min9'">min9</xsl:when>
      <!-- minor major 9th -->
      <xsl:when test="$s = 'mΔ9'
                   or $s = 'mMaj9'
                   or $s = 'mM9'
                   or $s = '-M9'
                   or $s = '-Δ9'
                   or $s = 'm9(maj7)'
                   or $s = 'm9maj7'">minmaj9</xsl:when>
      <!-- augmented major 9th -->
      <xsl:when test="$s = '+Δ9'
                   or $s = 'Maj9(♯5)'
                   or $s = '+Maj9'
                   or $s = '+M9'">3-a5-7-9</xsl:when>
      <!-- augmented (dominant) 9th -->
      <xsl:when test="$s = '+9'
                   or $s = '+7,9'
                   or $s = '9,5♯'
                   or $s = '9(♯5)'">aug9</xsl:when>
      <!-- half-diminished 9th -->
      <xsl:when test="$s = 'ⵁ9'
                   or $s = 'm9,5♭'
                   or $s = 'm9(♭5)'
                   or $s = '-9(♭5)'
                   or $s = 'halfdim9'">halfdim9</xsl:when>
      <!-- half-diminished minor 9th -->
      <xsl:when test="$s = 'ⵁ9♭'
                   or $s = 'ⵁ(♭9)'
                   or $s = 'm7,9♭,5♭'
                   or $s = 'm7(♭9,♭5)'
                   or $s = '-7(♭9,♭5)'
                   or $s = 'halfdim(♭9)'">m3-d5-m7-m9</xsl:when>
      <!-- diminished 9th -->
      <xsl:when test="$s = '°9'
                   or $s = 'dim9'">m3-d5-d7-9</xsl:when>
      <!-- diminished minor 9th -->
      <xsl:when test="$s = '°9♭'
                   or $s = '°(♭9)'
                   or $s = 'dim7,9♭'
                   or $s = '°7,9♭'">m3-d5-d7-m9</xsl:when>
      <!-- dominant flat 10 -->
      <xsl:when test="$s = '7,10♭'
                   or $s = '7(♭10)'
                   or $s = '7♯9'
                   or $s = '7(♯9)'">3-5-m7-m10</xsl:when>
      <!-- ****** 6 note chords -->
      <!-- (dominant) 11th -->
      <xsl:when test="$s = '11'
                   or $s = '7(11)'
                   or $s = '9(11)'">3-5-m7-9-11</xsl:when>
      <!-- major 11th -->
      <xsl:when test="$s = 'Δ11'
                   or $s = 'Maj11'
                   or $s = 'M11'">3-5-7-9-11</xsl:when>
      <!-- minor (dominant) 11th -->
      <xsl:when test="$s = 'm11'
                   or $s = '-11'
                   or $s = 'min11'">m3-5-m7-9-11</xsl:when>
      <!-- minor major 11th -->
      <xsl:when test="$s = 'mΔ11'
                   or $s = 'mMaj11'
                   or $s = 'mM11'
                   or $s = '-M11'
                   or $s = '-Δ11'">m3-5-7-9-11</xsl:when>
      <!-- acoustic (dominant) 11th -->
      <xsl:when test="$s = '11♯'">3-5-m7-9-a11</xsl:when>
      <!-- acoustic major 11th -->
      <xsl:when test="$s = 'Δ11♯'
                   or $s = 'Δ(♯11)'
                   or $s = 'Maj(♯11)'
                   or $s = 'M(♯11)'">3-5-7-9-a11</xsl:when>
      <!-- acoustic minor (dominant) 11th -->
      <xsl:when test="$s = 'm11♯'
                   or $s = 'm(♯11)'
                   or $s = '-(♯11)'
                   or $s = 'min(♯11)'">m3-5-m7-9-a11</xsl:when>
      <!-- acoustic minor major 11th -->
      <xsl:when test="$s = 'mΔ11♯'
                   or $s = 'mΔ(♯11)'
                   or $s = 'mMaj(♯11)'
                   or $s = 'mM(♯11)'
                   or $s = '-M(♯11)'
                   or $s = '-Δ(♯11)'">m3-5-7-9-a11</xsl:when>
      <!-- augmented major 11th -->
      <xsl:when test="$s = '+Δ11'
                   or $s = 'Maj11(♯5)'
                   or $s = '+Maj11'
                   or $s = '+M11'">3-a5-7-9-11</xsl:when>
      <!-- augmented (dominant) 11th -->
      <xsl:when test="$s = '+11'
                   or $s = '11,5♯'
                   or $s = '11(♯5)'">3-a5-m7-9-11</xsl:when>
      <!-- half-diminished 11th -->
      <xsl:when test="$s = 'ⵁ11'
                   or $s = 'm11,5♭'
                   or $s = 'm11(♭5)'
                   or $s = '-11(♭5)'
                   or $s = 'halfdim11'">m3-d5-m7-m9-11</xsl:when>
      <!-- diminished 11th -->
      <xsl:when test="$s = '°11'
                   or $s = 'dim11'">m3-d5-d7-m9-d11</xsl:when>
      <!-- 7 note chords -->
      <!-- (dominant) 13th -->
      <xsl:when test="$s = '13'
                   or $s = '9(add6)'
                   or $s = '9add6'">3-5-m7-9-11-13</xsl:when>
      <!-- major 13th -->
      <xsl:when test="$s = 'Δ13'
                   or $s = 'Maj13'
                   or $s = 'M13'">3-5-7-9-11-13</xsl:when>
      <!-- minor (dominant) 13th -->
      <xsl:when test="$s = 'm13'
                   or $s = '-13'
                   or $s = 'min13'">m3-5-m7-9-11-13</xsl:when>
      <!-- minor major 13th -->
      <xsl:when test="$s = 'mΔ13'
                   or $s = 'mMaj13'
                   or $s = 'mM13'
                   or $s = '-M13'
                   or $s = '-Δ13'">m3-5-7-9-11-13</xsl:when>
      <!-- (dominant) 13th -->
      <xsl:when test="$s = '13(♯11)'">3-5-m7-9-a11-13</xsl:when>
      <!-- major 13th -->
      <xsl:when test="$s = 'Δ13(♯11)'
                   or $s = 'Maj13(♯11)'
                   or $s = 'M13(♯11)'">3-5-7-9-a11-13</xsl:when>
      <!-- minor (dominant) 13th -->
      <xsl:when test="$s = 'm13(♯11)'
                   or $s = '-13(♯11)'
                   or $s = 'min13(♯11)'">m3-5-m7-9-a11-13</xsl:when>
      <!-- minor major 13th -->
      <xsl:when test="$s = 'mΔ13(♯11)'
                   or $s = 'mMaj13(♯11)'
                   or $s = 'mM13(♯11)'
                   or $s = '-M13(♯11)'
                   or $s = '-Δ13(♯11)'">m3-5-7-9-a11-13</xsl:when>
      <!-- augmented major 13th -->
      <xsl:when test="$s = '+Δ13'
                   or $s = 'Maj13(♯5)'
                   or $s = '+Maj13'
                   or $s = '+M13'">3-a5-7-9-11-13</xsl:when>
      <!-- augmented (dominant) 13th -->
      <xsl:when test="$s = '+13'
                   or $s = '13,5♯'
                   or $s = '13(♯5)'">3-a5-m7-9-11-13</xsl:when>
      <!-- half-diminished 13th -->
      <xsl:when test="$s = 'ⵁ13'
                   or $s = 'm13,5♭'
                   or $s = 'm13(♭5)'
                   or $s = '-13(♭5)'
                   or $s = 'halfdim13'">m3-d5-m7-m9-11-13</xsl:when>
      <!-- *** Figured 3 note chords -->
      <!-- major/minor suspended 4th -->
      <xsl:when test="$s = '4'
                   or $s = 'sus4'
                   or $s = 'sus'
                   or $s = 'm(sus4)'
                   or $s = 'msus4'">sus4</xsl:when>
      <!-- major/minor suspended 2nd -->
      <xsl:when test="$s = '2'
                   or $s = 'sus2'
                   or $s = 'sus9'
                   or $s = 'm(sus9)'
                   or $s = 'msus9'">sus2</xsl:when>
      <!-- **** Figured 4 note chords -->
      <!-- dominant (7th) major 6th -->
      <xsl:when test="$s = '7,6'
                   or $s = '7(add13)'
                   or $s = '7(add6)'">3-5-m7-13</xsl:when>
      <!-- major 6th 9th -->
      <xsl:when test="$s = '6,9'
                   or $s = '6(add9)'">3-5-6-9</xsl:when>
      <!-- major added 9th -->
      <xsl:when test="$s =  'add9'
                   or $s = '2'
                   or $s = '(add9)'
                   or $s = '(addD)'
                   or $s = 'addD'
                   or $s = 'add2'
                   or $s = 'add9'
                   or $s = 'addG'">add9</xsl:when>
      <!-- minor added 9th -->
      <xsl:when test="$s = 'm(add9)'
                   or $s = 'madd9'">m3-5-9</xsl:when>
      <!-- augmented added 9th -->
      <xsl:when test="$s = '+add9'
                   or $s = '(♯5)add9'">3-a5-9</xsl:when>
      <!-- major 6th suspended 4th -->
      <xsl:when test="$s = '6,4'
                   or $s = '6(sus4)'">4-5-6</xsl:when>
      <!-- major 6th suspended 2nd -->
      <xsl:when test="$s = '6,2'
                   or $s = '6(sus2)'">2-5-6</xsl:when>
      <!-- minor 6th suspended 4th -->
      <xsl:when test="$s = '6♭,4'
                   or $s = '6♭(sus4)'
                   or $s = '(♭6)sus4'">4-5-m6</xsl:when>
      <!-- minor 6th suspended 2nd -->
      <xsl:when test="$s = '6♭,2'
                   or $s = '6♭(sus2)'
                   or $s = '(♭6)sus2'">2-5-m6</xsl:when>
      <!-- dominant/minor 7th suspended 4th -->
      <xsl:when test="$s = '7,4'
                   or $s = '7sus4'
                   or $s = '7(sus4)'
                   or $s = 'm7sus4'">4-5-m7</xsl:when>
      <!-- dominant/minor 7th suspended 2nd -->
      <xsl:when test="$s = '7,2'
                   or $s = '7sus2'">2-5-m7</xsl:when>
      <!-- (minor) major 7th suspended 4th -->
      <xsl:when test="$s = 'Δ,4'
                   or $s = 'Maj7,4'
                   or $s = 'M7,4'
                   or $s = 'Δ7,4'
                   or $s = 'Δsus4'
                   or $s = 'M7sus4'
                   or $s = 'maj7sus4'">4-5-7</xsl:when>
      <!-- (minor) major 7th suspended 2nd -->
      <xsl:when test="$s = 'Δ,2'
                   or $s = 'Maj7,2'
                   or $s = 'M7,2'
                   or $s = 'Δ7,2'
                   or $s = 'Δsus2'
                   or $s = 'M7sus2'">2-5-7</xsl:when>
      <!-- augmented major 7th suspended 4th -->
      <xsl:when test="$s = '+Δ,4'
                   or $s = 'Maj7(♯5)4'
                   or $s = '+Maj7,4'
                   or $s = '+M7,4'
                   or $s = '+Δ7,4'
                   or $s = 'Maj7(♯5)4sus4'
                   or $s = '+Maj7,4sus4'
                   or $s = '+M7,4sus4'
                   or $s = '+Δ7,4sus4'">4-a5-7</xsl:when>
      <!-- augmented major 7th suspended 2nd -->
      <xsl:when test="$s = '+Δ,2'
                   or $s = 'Maj7(♯5)2'
                   or $s = '+Maj7,2'
                   or $s = '+M7,2'
                   or $s = '+Δ7,2'
                   or $s = 'Maj7(♯5)2sus2'
                   or $s = '+Maj7,2sus2'
                   or $s = '+M7,2sus2'
                   or $s = '+Δ7,2sus2'">2-a5-7</xsl:when>
      <!-- half-diminished 7th suspended 4th; dominant 7th flat 5 suspended 4th -->
      <xsl:when test="$s = 'ⵁ,4'
                   or $s = '7,5♭,4'
                   or $s = '7(♭5)4'
                   or $s = 'ⵁ7,4'
                   or $s = 'halfdim,4'
                   or $s = '7,5♭,4sus4'
                   or $s = '7(♭5)4sus4'
                   or $s = 'ⵁ7,4sus4'
                   or $s = 'halfdim,4sus4'">4-d5-m7</xsl:when>
      <!-- half-diminished 7th suspended 2nd; dominant 7th flat 5 suspended 2nd -->
      <xsl:when test="$s = 'ⵁ,2'
                   or $s = '7,5♭,2'
                   or $s = '7(♭5)2'
                   or $s = 'ⵁ7,2'
                   or $s = 'halfdim,2'
                   or $s = '7,5♭,2sus2'
                   or $s = '7(♭5)2sus2'
                   or $s = 'ⵁ7,2sus2'
                   or $s = 'halfdim,2sus2'">2-d5-m7</xsl:when>
      <!-- diminished 7th suspended 4th -->
      <xsl:when test="$s = 'ⵔ,4'
                   or $s = 'dim7,4'
                   or $s = 'ⵔ7,4'
                   or $s = 'ⵔ(sus4)'
                   or $s = 'dim7(sus4)'
                   or $s = 'ⵔ7(sus4)'">4-d5-d7</xsl:when>
      <!-- diminished 7th suspended 2nd -->
      <xsl:when test="$s = 'ⵔ,2'
                   or $s = 'dim7,2'
                   or $s = 'ⵔ7,2'
                   or $s = 'ⵔ(sus2)'
                   or $s = 'dim7(sus2)'
                   or $s = 'ⵔ7(sus2)'">2-d5-d7</xsl:when>
      <!-- diminished major 7th suspended 4th; major 7th flat 5 suspended 4th -->
      <xsl:when test="$s = 'Δ,5♭,4'
                   or $s = 'Δ7(♭5)4'
                   or $s = 'Maj7(♭5)4'
                   or $s = 'M7(♭5)4'
                   or $s = 'Δ7(♭5)4sus4'
                   or $s = 'Maj7(♭5)4sus4'
                   or $s = 'M7(♭5)4sus4'">4-d5-7</xsl:when>
      <!-- diminished major 7th suspended 2nd; major 7th flat 5 suspended 2nd -->
      <xsl:when test="$s = 'Δ,5♭,2'
                   or $s = 'Δ7(♭5)2'
                   or $s = 'Maj7(♭5)2'
                   or $s = 'M7(♭5)2'
                   or $s = 'Δ7(♭5)2sus2'
                   or $s = 'Maj7(♭5)2sus2'
                   or $s = 'M7(♭5)2sus2'">2-d5-7</xsl:when>
      <!-- dominant (7th) major 6th suspended 4th -->
      <xsl:when test="$s = '7,6,4'
                   or $s = '7(add13)4'
                   or $s = '7(add6)4'
                   or $s = '7,6sus4'
                   or $s = '7(add13)sus4'
                   or $s = '7(add6)sus4'
                   or $s = '6sus4'
                   or $s = '6(sus4)'">4-5-m7-13</xsl:when>
      <!-- dominant (7th) major 6th suspended 4th -->
      <xsl:when test="$s = '7,6,2'
                   or $s = '7(add13)2'
                   or $s = '7(add6)2'
                   or $s = '7,6sus2'
                   or $s = '7(add13)sus2'
                   or $s = '7(add6)sus2'">2-5-m7-13</xsl:when>
      <!-- ***** Figured 5 note chords -->
      <!-- (dominant) 9th suspended 4th -->
      <xsl:when test="$s = '9,4'
                   or $s = '9sus4'
                   or $s = '9sus'">4-5-m7-9</xsl:when>
      <!-- dominant minor 9th suspended 4th -->
      <xsl:when test="$s = '7,9♭,4'
                   or $s = '7(♭9)4'
                   or $s = '7,9♭,sus4'
                   or $s = '7(♭9)sus4'">4-5-m7-m9</xsl:when>
      <!-- major 9th suspended 4th -->
      <xsl:when test="$s = 'Δ9,4'
                   or $s = 'Δ9sus4'
                   or $s = 'Maj9,4'
                   or $s = 'M9,4'
                   or $s = 'Maj9sus4'
                   or $s = 'M9sus4'">4-5-7-9</xsl:when>
      <!-- augmented major 9th suspended 4th -->
      <xsl:when test="$s = '+Δ9,4'
                   or $s = '+Δ9sus4'
                   or $s = 'Maj9(♯5)4'
                   or $s = '+M9,4'
                   or $s = '+M9sus4'
                   or $s = '+Maj9,4'">4-a5-7-9</xsl:when>
      <!-- augmented (dominant) 9th suspended 4th -->
      <xsl:when test="$s = '+9,4'
                   or $s = '+9sus4'
                   or $s = '9(♯5)sus4'">4-a5-m7-9</xsl:when>
      <!-- Extra or custom chords -->
      <xsl:when test="$s = 'm♯5'
                   or $s = 'm(♯5)'">SIXTH:<xsl:value-of select="$s"/></xsl:when><!-- the major sixth chord (first inversion) of the chord n3-below the current root, example: Dm(♯5) → Bb/D - Needs to  be updated manually -->
      <xsl:otherwise>UNKNOWN:<xsl:value-of select="$s"/></xsl:otherwise>
    </xsl:choose>
  </xsl:template>

</xsl:stylesheet>
