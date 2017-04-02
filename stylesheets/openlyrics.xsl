<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
 version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 xmlns:ol="http://openlyrics.info/namespace/2009/song"
 xmlns:str="http://exslt.org/strings"
 xmlns:xhtml="http://www.w3.org/1999/xhtml"
 xmlns="http://www.w3.org/1999/xhtml">
<xsl:output method="html" encoding="utf-8" indent="yes" doctype-system="about:legacy-compat" />

  <!-- Locale-specific content -->
  <xsl:variable name="locale-strings">
    <xsl:text>../stylesheets/xsl/openlyrics.lang.</xsl:text>
    <xsl:value-of select="//@xml:lang"/>
    <xsl:text>.xml</xsl:text>
  </xsl:variable>
  <xsl:variable name="locale" select="document ($locale-strings)/locale"/>

  <!-- Main -->
  <xsl:template match="/">
    <html lang="{//@xml:lang}">
      <head>
        <title><xsl:value-of select="//ol:song/ol:properties/ol:titles/ol:title[1]/text()"/></title>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="../stylesheets/css/html/openlyrics.html.css" />
      </head>
      <body>
        <xsl:apply-templates/>
      </body>
    </html>
  </xsl:template>
  
  <xsl:template match="ol:song">
    <xsl:variable name="rootProperties">
      <xsl:text>OpenLyrics  </xsl:text><xsl:value-of select="@version"/>
      <xsl:if test="@createdIn">
        <xsl:text> • </xsl:text><xsl:value-of select="$locale/properties/creator/text()"/><xsl:text>: </xsl:text><xsl:value-of select="@createdIn"/>
      </xsl:if>
      <xsl:if test="@xml:lang">
        <xsl:text> • </xsl:text><xsl:value-of select="$locale/properties/language/text()"/><xsl:text>: </xsl:text><xsl:value-of select="$locale/languages/*[local-name()=current()/@xml:lang]/text()"/>
      </xsl:if>
    </xsl:variable>

    <div class="song" lang="{@xml:lang}" data-ol-version="{@version}" data-root-properties="{$rootProperties}">
      <xsl:apply-templates/>
        <footer>
          <p class="root-properties">
            <xsl:value-of select="$rootProperties"/>
          </p>
       </footer>
    </div>
  </xsl:template>

  <!-- Header properties -->
  <xsl:template match="ol:properties">
    <header>
      <xsl:apply-templates select="ol:titles"/>
    </header>
    <section class="{local-name()}">
      <p class="properties-authors">
      <xsl:apply-templates select="ol:authors"/>
      </p>
      <p class="properties-other">
        <xsl:apply-templates select="ol:released"/>
        <xsl:apply-templates select="ol:version"/>
        <xsl:apply-templates select="ol:variant"/>
        <xsl:apply-templates select="ol:publisher"/>
        <xsl:apply-templates select="ol:copyright"/>
        <xsl:apply-templates select="ol:comments"/>
        <xsl:apply-templates select="ol:keywords"/>
      </p>
      <p class="properties-main">
        <xsl:apply-templates select="ol:key"/>
        <xsl:apply-templates select="ol:transposition"/>
        <xsl:apply-templates select="ol:tempo"/>
        <xsl:apply-templates select="ol:ccliNo"/>
      </p>
      <p class="properties-themes">
        <xsl:apply-templates select="ol:themes"/>
      </p>
      <p class="properties-songbooks">
        <xsl:apply-templates select="ol:songbooks"/>
      </p>
    </section>
  </xsl:template>
  
  <xsl:template match="ol:title[1]">
    <h1 title="{$locale/properties/title/text()}"><xsl:value-of select="."/></h1>
  </xsl:template>
  <xsl:template match="ol:title[@original]">
    <span class="{local-name()} {name(@original)}" title="{$locale/properties/originalTitle/text()}">
      <em><xsl:value-of select="$locale/properties/originalTitle/text()"/>: </em>
      <xsl:value-of select="."/>
      <xsl:if test="@lang">
        (<xsl:value-of select="$locale/languages/*[local-name()=current()/@lang]/text()"/>)
      </xsl:if>
    </span>
  </xsl:template>
  <xsl:template match="ol:title[position()>1][not(@original)]">
    <span class="{local-name()}" title="{$locale/properties/subtitle/text()}">
      <em><xsl:value-of select="$locale/properties/subtitle/text()"/>: </em>
      <xsl:value-of select="."/>
      <xsl:if test="@lang">
        (<xsl:value-of select="$locale/languages/*[local-name()=current()/@lang]/text()"/>)
      </xsl:if>
    </span>
  </xsl:template>

  <xsl:template match="ol:author[not(@type)]">
    <span class="{local-name()}" title="{$locale/properties/author/text()}">
      <em><xsl:value-of select="$locale/properties/author/text()"/>: </em>
      <xsl:value-of select="."/>
    </span>
  </xsl:template>
  <xsl:template match="ol:author[@type='words']|ol:author[@type='music']">
    <span class="{local-name()} {@type}" title="{$locale/properties/*[local-name()=current()/@type]/text()}">
      <em><xsl:value-of select="$locale/properties/*[local-name()=current()/@type]/text()"/>: </em>
      <xsl:value-of select="."/>
    </span>
  </xsl:template>
  <xsl:template match="ol:author[@type='translation']">
    <span class="{local-name()} {@type}" title="{$locale/properties/*[local-name()=current()/@type]/text()}">
      <em><xsl:value-of select="$locale/properties/*[local-name()=current()/@type]/text()"/>: </em>
      <xsl:value-of select="."/>
      <xsl:if test="@lang">
        (<xsl:value-of select="$locale/languages/*[local-name()=current()/@lang]/text()"/>)
      </xsl:if>
    </span>
  </xsl:template>

  <xsl:template match="ol:released|ol:version|ol:variant|ol:publisher|ol:copyright|ol:comment|ol:keywords|ol:key|ol:transposition|ol:ccliNo">
    <span class="{local-name()}" title="{$locale/properties/*[local-name()=local-name(current())]/text()}">
      <em><xsl:value-of select="$locale/properties/*[local-name()=local-name(current())]/text()"/>: </em>
      <xsl:choose>
        <xsl:when test="local-name()='ccliNo'">
          <a href="https://songselect.ccli.com/songs/{.}"><xsl:value-of select="."/></a>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="."/>
        </xsl:otherwise>
      </xsl:choose>
    </span>
    <xsl:text> </xsl:text>
  </xsl:template>

  <xsl:template match="ol:tempo">
    <span class="{local-name()}" title="{$locale/properties/tempo/text()}">
      <em><xsl:value-of select="$locale/properties/tempo/text()"/>: </em>
      <xsl:value-of select="."/>
      <xsl:if test="string(number(.))!='NaN'">
        <xsl:text> BMP</xsl:text>
      </xsl:if>
    </span>
    <xsl:text> </xsl:text>
  </xsl:template>

  <xsl:template match="ol:themes">
    <span class="{local-name()}" title="{$locale/properties/themes/text()}">
      <em><xsl:value-of select="$locale/properties/themes/text()"/>: </em>
      <xsl:for-each select="ol:theme">
        <xsl:if test="not(@lang)">
          <xsl:value-of select="."/>
          <xsl:if test="position()!=last()">, <xsl:text/></xsl:if>
        </xsl:if>
        <xsl:if test="@lang">
          <xsl:value-of select="."/>
          (<xsl:value-of select="$locale/languages/*[local-name()=current()/@lang]/text()"/>)<xsl:if test="position()!=last()">, <xsl:text/></xsl:if>
        </xsl:if>
      </xsl:for-each>
    </span>
  </xsl:template>

  <xsl:template match="ol:songbook">
    <div class="{local-name()}" title="{$locale/properties/songbook/text()}">
      <span class="songbook_name">
        <xsl:value-of select="@name"/>
      </span>
      <span class="songbook_entry">
        <xsl:text> </xsl:text><xsl:value-of select="@entry"/><xsl:text>.</xsl:text>
      </span>
    </div>
  </xsl:template>

  <!-- Lyrics and chords -->
  <xsl:template match="ol:lyrics">
    <aside class="verse-order">
      <xsl:apply-templates select="../ol:properties/ol:verseOrder"/>
    </aside>
    <section class="{local-name()}">
      <xsl:apply-templates/>
    </section>
  </xsl:template>

  <xsl:template match="ol:verseOrder">
    <span class="{local-name()}" title="{$locale/properties/verseOrder/text()}">
      <em><xsl:value-of select="$locale/properties/verseOrder/text()"/>: </em>
      <div>
        <xsl:for-each select="str:tokenize(.,' ')">
          <xsl:call-template name="displayVerseName">
            <xsl:with-param name="name" select="."/>
          </xsl:call-template>
          <xsl:call-template name="break" />
        </xsl:for-each>
      </div>
    </span>
  </xsl:template>

  <xsl:template name="displayVerseName">
    <xsl:param name="name" />
    <xsl:variable name="verseName" select="substring($name,1,1)" />
    <xsl:variable name="verseNum"  select="substring($name,2,string-length(-1))" />
    <xsl:if test="$verseNum!='' and $locale/lyrics/verseNameFormat[@initial='number']">
      <xsl:value-of select="$verseNum" />
      <xsl:value-of select="$locale/lyrics/verseNameFormat/@separator" />
    </xsl:if>
    <xsl:choose>
      <xsl:when test="$locale/lyrics/verseNameFormat[@initial='number'] and
                      $verseNum!='' and
                      $locale/lyrics/verseNameFormat[@translateFrom] and
                      $locale/lyrics/verseNameFormat[@translateTo]">
        <xsl:value-of select="translate( $locale/lyrics/verseNames/*[local-name()=$verseName]/text(),
                                         $locale/lyrics/verseNameFormat/@translateFrom,
                                         $locale/lyrics/verseNameFormat/@translateTo
                                        )"/>
      </xsl:when>
      <xsl:otherwise>
       <xsl:value-of select="$locale/lyrics/verseNames/*[local-name()=$verseName]/text()"/>
      </xsl:otherwise>
    </xsl:choose>
    <xsl:if test="$verseNum!='' and $locale/lyrics/verseNameFormat[@initial='name']">
      <xsl:value-of select="$locale/lyrics/verseNameFormat/@separator" />
      <xsl:value-of select="$verseNum" />
    </xsl:if>
  </xsl:template>

  <xsl:template match="ol:verse">
    <xsl:variable name="verseId">
      <xsl:if test="@name">
        <xsl:value-of select="@name" />
      </xsl:if>
      <xsl:if test="@lang">
        <xsl:text>-</xsl:text><xsl:value-of select="@lang" />
      </xsl:if>
      <xsl:if test="@translit">
        <xsl:text>-</xsl:text><xsl:value-of select="@translit" />
      </xsl:if>
    </xsl:variable>
    <xsl:element name="article">
      <xsl:attribute name="class"><xsl:value-of select="local-name()" /></xsl:attribute>
      <xsl:if test="@name">
        <xsl:attribute name="id"><xsl:value-of select="$verseId" /></xsl:attribute>
        <xsl:attribute name="data-verse-name"><xsl:value-of select="substring(@name,1,1)" /></xsl:attribute>
        <xsl:attribute name="data-verse-num"><xsl:value-of select="substring(@name,2,string-length(-1))" /></xsl:attribute>
      </xsl:if>
      <xsl:if test="@lang">
        <xsl:attribute name="lang"><xsl:value-of select="@lang" /></xsl:attribute>
      </xsl:if>
      <xsl:if test="@translit">
        <xsl:attribute name="data-verse-translit"><xsl:value-of select="@translit" /></xsl:attribute>
      </xsl:if>
      <xsl:if test="@name">
        <div class="verse-name" title="{$locale/lyrics/name/text()}">
          <em><xsl:value-of select="$locale/lyrics/name/text()"/>: </em>
          <xsl:call-template name="displayVerseName">
            <xsl:with-param name="name" select="@name"/>
          </xsl:call-template>
        </div>
      </xsl:if>
      <xsl:if test="@lang and not(@translit)">
        <div class="verse-lang" title="{$locale/lyrics/lang/text()}">
          <em><xsl:value-of select="$locale/lyrics/lang/text()"/>: </em>
          <xsl:value-of select="$locale/languages/*[local-name()=current()/@lang]/text()"/>
        </div>
      </xsl:if>
      <xsl:if test="@lang and @translit">
        <div class="verse-translit" title="{$locale/lyrics/translit/text()}">
          <em><xsl:value-of select="$locale/lyrics/translit/text()"/>: </em>
          <xsl:value-of select="$locale/languages/*[local-name()=current()/@lang]/text()"/>
          <xsl:text>→</xsl:text>
          <xsl:value-of select="$locale/languages/*[local-name()=current()/@translit]/text()"/>
        </div>
      </xsl:if>
      <xsl:apply-templates/>
    </xsl:element>
  </xsl:template>

  <xsl:template match="ol:lines">
    <xsl:variable name="has-segments">
      <xsl:if test="//ol:chord">
        <xsl:text> has-segments</xsl:text>
      </xsl:if>
    </xsl:variable>
    <p class="{local-name()}{$has-segments}">
      <xsl:if test="@part">
        <span class="line-part" title="{$locale/lyrics/part/text()}">
          <em><xsl:value-of select="$locale/lyrics/part/text()"/>: </em>
          <xsl:value-of select="@part"/>
        </span>
      </xsl:if>
      <xsl:apply-templates/>
    </p>
  </xsl:template>

  <xsl:template match="ol:beat[position() != last()]">
    <xsl:apply-templates/>
    <span class="{local-name()}-sign">|</span>
  </xsl:template>

  <xsl:include href="../stylesheets/xsl/openlyrics.08chords.xsl" />

  <xsl:template match="ol:lyrics//ol:comment">
    <span class="lyrics-{local-name()}" title="{$locale/lyrics/comment/text()}">
      <em><xsl:value-of select="$locale/lyrics/comment/text()"/>: </em>
      <xsl:value-of select="."/>
    </span>
  </xsl:template>

  <xsl:template match="ol:br" name="break">
    <xsl:choose>
      <xsl:when test="system-property('xsl:vendor')='Transformiix'">
        <br/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text disable-output-escaping="yes">&lt;br /&gt;</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  
  <xsl:template match="ol:format"></xsl:template>

</xsl:stylesheet>

