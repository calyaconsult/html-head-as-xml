<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Pages - Titles</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Page</th>
      <th>Title</th>
      <th>Meta content</th>
      <th>Meta name</th>
    </tr>
    <xsl:for-each select="pageset/page">
    <tr>
      <td><xsl:value-of select="@name"/></td>
      <td><xsl:value-of select="title"/></td>
      <td><xsl:value-of select="meta/@content"/></td>
      <td><xsl:value-of select="meta/@name"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>
