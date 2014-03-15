{% load i18n %}<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.1"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:atom="http://www.w3.org/2005/Atom"
>

    <xsl:output method="html" />
    <xsl:variable name="title" select="/rss/channel/title" />

    <xsl:template match="/">
        <html>
            <head>
                <title><xsl:value-of select="$title"/> RSS Feed</title>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <link rel="stylesheet" href="/static/css/simple.css" type="text/css" />
                <link rel="stylesheet" href="/static/news/css/feed.css" type="text/css" />
                <script type="text/javascript">
function select(el) {
    var selection = window.getSelection();     
    var range = document.createRange();
    range.selectNodeContents(el);
    selection.removeAllRanges();
    selection.addRange(range);
}
                </script>
            </head>
            <body>
                <div class="container">
                    <xsl:apply-templates select="rss/channel" />
                </div>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="channel">
        <h1><a href="http://tjrapid.sk">TJ Rapid</a></h1>
        <h2>{% trans "RSS Feed" %}</h2>
        <p><div class="url" onclick="select(this)"><xsl:value-of select="atom:link/@href" /></div></p>
        <p>
            {% blocktrans %}
This is an RSS feed. Your browser does not seem to support RSS
feeds, but you can use one of these popular clients:
            {% endblocktrans %}
        </p>
        <ul class="clients-list">
            <li><a href="https://www.mozilla.org/en-US/firefox">Firefox</a></li>
            <li><a href="https://www.mozilla.org/en-US/thunderbird/">Thunderbird</a></li>
            <li><a href="https://chrome.google.com/webstore/detail/rss-feed-reader/pnjaodmkngahhkoihejjehlcdlnohgmp?hl=en">Chrome RSS Feed Reader</a></li>
        </ul>
        <p>{% blocktrans %}Copy the address above to the client of your choice.{% endblocktrans %}</p>
    </xsl:template>
</xsl:stylesheet>
