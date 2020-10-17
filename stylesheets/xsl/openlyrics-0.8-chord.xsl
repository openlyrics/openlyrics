<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
 version="1.0"
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 xmlns:ol="http://openlyrics.info/namespace/2009/song"
 xmlns="http://www.w3.org/1999/xhtml">
<xsl:output method="html" encoding="utf-8" indent="yes" doctype-system="about:legacy-compat" />

  <xsl:template match="ol:song[@version='0.8']//ol:lines/ol:chord">
    <span class="chord">
      <code>{</code>
      <xsl:value-of select="@name"/>
      <code>}</code>
    </span>
  </xsl:template>
  <xsl:template match="ol:song[@version='0.8']//ol:lines[ol:chord]/text()">
    <span class="segment">
      <xsl:value-of select="."/>
    </span>
  </xsl:template>

</xsl:stylesheet>

