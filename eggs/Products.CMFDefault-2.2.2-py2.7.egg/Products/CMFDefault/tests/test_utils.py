##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Unit tests for utils module.

$Id: test_utils.py 113211 2010-06-06 15:26:29Z hannosch $
"""

import unittest

from Products.CMFCore.tests.base.content import FAUX_HTML_LEADING_TEXT
from Products.CMFCore.tests.base.content import SIMPLE_HTML
from Products.CMFCore.tests.base.content import SIMPLE_STRUCTUREDTEXT
from Products.CMFCore.tests.base.content import SIMPLE_XHTML
from Products.CMFCore.tests.base.content import STX_WITH_HTML


class DefaultUtilsTests(unittest.TestCase):

    COMMON_HEADERS = '''Author: Tres Seaver
Title: Test Products.CMFDefault.utils.parseHeadersBody'''

    MULTILINE_DESCRIPTION = '''Description: this description spans
        multiple lines.'''

    MULTIPARAGRAPH_DESCRIPTION = \
        '''Description: this description spans multiple lines.
        
        It includes a second paragraph'''

    TEST_BODY = '''Body goes here, and can span multiple
lines.  It can even include "headerish" lines, like:

Header: value
'''

    def setUp(self):
        from zope.component.testing import setUp
        setUp()

    def tearDown(self):
        from zope.component.testing import tearDown
        tearDown()

    def test_parseHeadersBody_no_body( self ):
        from Products.CMFDefault.utils import parseHeadersBody

        headers, body = parseHeadersBody( '%s\n\n' % self.COMMON_HEADERS )
        self.assertEqual( len( headers ), 2 )
        self.failUnless( 'Author' in headers.keys() )
        self.assertEqual( headers[ 'Author' ], 'Tres Seaver' )
        self.failUnless( 'Title' in headers.keys() )
        self.assertEqual( len( body ), 0 )

    def test_parseHeadersBody_continuation( self ):
        from Products.CMFDefault.utils import parseHeadersBody

        headers, body = parseHeadersBody( '%s\n%s\n\n'
                                        % ( self.COMMON_HEADERS
                                          , self.MULTILINE_DESCRIPTION
                                          )
                                        )
        self.assertEqual( len( headers ), 3 )
        self.failUnless( 'Description' in headers.keys() )
        desc_len = len( headers[ 'Description' ].split('\n') )
        self.assertEqual( desc_len, 2 )
        self.assertEqual( len( body ), 0 )

    def test_parseHeadersBody_embedded_blank_line( self ):
        from Products.CMFDefault.utils import parseHeadersBody

        headers, body = parseHeadersBody( '%s\n%s\n\n%s'
                                        % ( self.COMMON_HEADERS
                                          , self.MULTIPARAGRAPH_DESCRIPTION
                                          , self.TEST_BODY
                                          )
                                        )
        self.assertEqual( len( headers ), 3 )
        self.failUnless( 'Description' in headers.keys() )
        desc_lines = headers[ 'Description' ].split('\n')
        desc_len = len( desc_lines )
        self.assertEqual( desc_len, 3, desc_lines )
        self.assertEqual( desc_lines[1], ' ' )
        self.assertEqual( body, self.TEST_BODY )

    def test_parseHeadersBody_body( self ):
        from Products.CMFDefault.utils import parseHeadersBody

        headers, body = parseHeadersBody( '%s\n\n%s'
                                        % ( self.COMMON_HEADERS
                                          , self.TEST_BODY
                                          )
                                        )
        self.assertEqual( len( headers ), 2 )
        self.assertEqual( body, self.TEST_BODY )

    def test_parseHeadersBody_body_malformed_terminator( self ):
        from Products.CMFDefault.utils import parseHeadersBody

        headers, body = parseHeadersBody( '%s\n \n%s'
                                        % ( self.COMMON_HEADERS
                                          , self.TEST_BODY
                                          )
                                        )
        self.assertEqual( len( headers ), 2 )
        self.assertEqual( body, self.TEST_BODY )

    def test_parseHeadersBody_preload( self ):
        from Products.CMFDefault.utils import parseHeadersBody

        preloaded = { 'Author' : 'xxx', 'text_format' : 'structured_text' }
        headers, body = parseHeadersBody( '%s\n%s\n\n%s'
                                        % ( self.COMMON_HEADERS
                                          , self.MULTILINE_DESCRIPTION
                                          , self.TEST_BODY
                                          )
                                        , preloaded
                                        )
        self.assertEqual( len( headers ), 4 )
        self.assertNotEqual( preloaded[ 'Author' ], headers[ 'Author' ] )
        self.assertEqual( preloaded[ 'text_format' ], headers[ 'text_format' ] )

    def test_scrubHTML_no_adapter_falls_back(self):
        from Products.CMFDefault.utils import scrubHTML

        self.assertEqual( scrubHTML('<a href="foo.html">bar</a>'),
                          '<a href="foo.html">bar</a>' )
        self.assertEqual( scrubHTML('<b>bar</b>'),
                          '<b>bar</b>' )
        self.assertEqual( scrubHTML('<base href="" /><base>'),
                          '<base href="" /><base />' )
        self.assertEqual( scrubHTML('<blockquote>bar</blockquote>'),
                          '<blockquote>bar</blockquote>' )
        self.assertEqual( scrubHTML('<body bgcolor="#ffffff">bar</body>'),
                          '<body bgcolor="#ffffff">bar</body>' )
        self.assertEqual( scrubHTML('<br /><br>'),
                          '<br /><br />' )
        self.assertEqual( scrubHTML('<hr /><hr>'),
                          '<hr /><hr />' )
        self.assertEqual( scrubHTML('<img src="foo.png" /><img>'),
                          '<img src="foo.png" /><img />' )
        self.assertEqual( scrubHTML('<meta name="title" content="" /><meta>'),
                          '<meta name="title" content="" /><meta />' )

    def test_scrubHTML_with_adapter(self):
        from zope.component.testing import setUp
        from zope.component.testing import tearDown
        from Products.CMFDefault.interfaces import IHTMLScrubber
        from Products.CMFDefault.utils import scrubHTML
        from zope.component import getSiteManager
        from zope.interface import implements

        class _Scrubber:
            implements(IHTMLScrubber)
            def scrub(self, html):
                return html.upper()


        setUp()

        sm = getSiteManager()
        try:
            sm.registerUtility(_Scrubber(), IHTMLScrubber)
            self.assertEqual( scrubHTML('<a href="foo.html">bar</a>'),
                            '<A HREF="FOO.HTML">BAR</A>' )
            self.assertEqual( scrubHTML('<b>bar</b>'),
                            '<B>BAR</B>' )
            self.assertEqual( scrubHTML('<base href="" /><base>'),
                            '<BASE HREF="" /><BASE>' )
            self.assertEqual( scrubHTML('<blockquote>bar</blockquote>'),
                            '<BLOCKQUOTE>BAR</BLOCKQUOTE>' )
            self.assertEqual( scrubHTML('<body bgcolor="#ffffff">bar</body>'),
                            '<BODY BGCOLOR="#FFFFFF">BAR</BODY>' )
            self.assertEqual( scrubHTML('<br /><br>'),
                            '<BR /><BR>' )
            self.assertEqual( scrubHTML('<hr /><hr>'),
                            '<HR /><HR>' )
            self.assertEqual( scrubHTML('<img src="foo.png" /><img>'),
                            '<IMG SRC="FOO.PNG" /><IMG>' )
            self.assertEqual( scrubHTML(
                                '<meta name="title" content="" /><meta>'),
                            '<META NAME="TITLE" CONTENT="" /><META>' )

        finally:
            tearDown()

    def test_bodyfinder(self):
        from Products.CMFDefault.utils import bodyfinder

        self.assertEqual( bodyfinder(FAUX_HTML_LEADING_TEXT),
                          '\n  <h1>Not a lot here</h1>\n ' )
        self.assertEqual( bodyfinder(SIMPLE_HTML),
                          '\n  <h1>Not a lot here</h1>\n ' )
        self.assertEqual( bodyfinder(SIMPLE_STRUCTUREDTEXT),
                          SIMPLE_STRUCTUREDTEXT )
        self.assertEqual( bodyfinder(SIMPLE_XHTML),
                          '\n  <h1>Not a lot here</h1>\n ' )
        self.assertEqual( bodyfinder(STX_WITH_HTML),
                          '<p>Hello world, I am Bruce.</p>' )

    def test_html_headcheck(self):
        from Products.CMFDefault.utils import html_headcheck

        self.assertEqual( html_headcheck(FAUX_HTML_LEADING_TEXT), 0 )
        self.assertEqual( html_headcheck(SIMPLE_HTML), 1 )
        self.assertEqual( html_headcheck(SIMPLE_STRUCTUREDTEXT), 0 )
        self.assertEqual( html_headcheck(SIMPLE_XHTML), 1 )
        self.assertEqual( html_headcheck(STX_WITH_HTML), 0 )

    def test_tuplize(self):
        from Products.CMFDefault.utils import comma_split
        from Products.CMFDefault.utils import tuplize
        wanted = ('one','two','three')

        self.assertEqual( tuplize('string', 'one two three'), wanted )
        self.assertEqual( tuplize('unicode', u'one two three'), wanted )
        self.assertEqual( tuplize('string', 'one,two,three', comma_split),
                          wanted )
        self.assertEqual( tuplize('list', ['one',' two','three ']), wanted )
        self.assertEqual( tuplize('tuple', ('one','two','three')), wanted )

    def test_seq_strip(self):
        from Products.CMFDefault.utils import seq_strip

        self.assertEqual( seq_strip(['one ', ' two', ' three ']),
                          ['one','two','three'] )
        self.assertEqual( seq_strip(('one ', ' two', ' three ')),
                          ('one','two','three') )

    def test_html_marshal(self):
        from Products.CMFDefault.utils import html_marshal

        self.assertEqual( html_marshal(foo=1), ( ('foo:int', 1), ) )
        self.assertEqual( html_marshal(foo=1, bar='baz >&baz'),
                          ( ('foo:int', 1), ('bar', 'baz >&baz') ) )

    def test_toUnicode(self):
        from Products.CMFDefault.utils import toUnicode

        self.assertEqual( toUnicode('foo'), u'foo' )
        self.assertEqual( toUnicode( ('foo', 'bar'), 'ascii' ),
                          (u'foo', u'bar') )
        self.assertEqual( toUnicode( {'foo': 'bar'}, 'iso-8859-1' ),
                          {'foo': u'bar'} )

    def test_checkEmailAddress(self):
        from Products.CMFDefault.exceptions import EmailAddressInvalid
        from Products.CMFDefault.utils import checkEmailAddress

        self.assertEqual(checkEmailAddress('foo@example.com'), None)
        self.assertEqual(checkEmailAddress('foo@1bar.example.com'), None)
        self.assertEqual(checkEmailAddress('foo@123456.com'), None)
        self.assertEqual(checkEmailAddress('$.-@example.com'), None)
        self.assertEqual(checkEmailAddress(u'foo@example.com'), None)
        # CMF Collector issue #322
        self.assertEqual(checkEmailAddress('user+site@example.com'), None)
        # CMF Collector issue #326
        self.assertEqual(checkEmailAddress('username_@example.com'), None)
        # CMF Collector issue #401
        self.assertEqual(checkEmailAddress("user'site@example.com"), None)
        # CMF Collector issue #495
        self.assertEqual(checkEmailAddress("user@a.example.com"), None)
        self.assertRaises(EmailAddressInvalid, checkEmailAddress,
                          'this is not an e-mail address')
        self.assertRaises(EmailAddressInvalid, checkEmailAddress,
                          'foo@example.com, bar@example.com')
        self.assertRaises(EmailAddressInvalid, checkEmailAddress,
                          'foo.@example.com')
        self.assertRaises(EmailAddressInvalid, checkEmailAddress,
                          '.foo@example.com')
        self.assertRaises(EmailAddressInvalid, checkEmailAddress,
                          'foo@-bar.example.com')
        # RFC 2821 local-part: max 64 characters
        self.assertRaises(EmailAddressInvalid, checkEmailAddress,
                          'f'*63+'oo@example.com')
        # RFC 2821 domain: max 255 characters
        self.assertRaises(EmailAddressInvalid, checkEmailAddress,
                          'foo@'+'b'*242+'ar.example.com')

    def test_formatRFC822Headers_simple(self):
        from Products.CMFDefault.utils import formatRFC822Headers

        HEADERS = [ ('Foo', 'foo')
                  , ('Bar', 'bar')
                  ]

        formatted = formatRFC822Headers( HEADERS )

        self.assertEqual( formatted, 'Foo: foo\r\nBar: bar' )

    def test_formatRFC822Headers_empty(self):
        from Products.CMFDefault.utils import formatRFC822Headers

        HEADERS = [ ('Foo', 'foo')
                  , ('Bar', '')
                  ]

        formatted = formatRFC822Headers( HEADERS )

        self.assertEqual( formatted, 'Foo: foo\r\nBar: ' )

    def test_formatRFC822Headers_multiline(self):
        from Products.CMFDefault.utils import formatRFC822Headers

        HEADERS = [ ('Foo', 'foo')
                  , ('Bar', 'bar\nwith multiline')
                  ]

        formatted = formatRFC822Headers( HEADERS )

        self.assertEqual( formatted
                        , 'Foo: foo\r\nBar: bar\r\n  with multiline' )

    def test_formatRFC822Headers_multiline_trailing_blank_line(self):
        from Products.CMFDefault.utils import formatRFC822Headers

        HEADERS = [ ('Foo', 'foo')
                  , ('Bar', 'bar\nwith multiline\n')
                  ]

        formatted = formatRFC822Headers( HEADERS )

        self.assertEqual( formatted
                        , 'Foo: foo\r\nBar: bar\r\n  with multiline' )

    def test_formatRFC822Headers_multiline_intermediate_blank_line(self):
        from Products.CMFDefault.utils import formatRFC822Headers

        HEADERS = [ ('Foo', 'foo')
                  , ('Bar', 'bar\n\nwith multiline')
                  ]

        formatted = formatRFC822Headers( HEADERS )

        self.assertEqual( formatted
                        , 'Foo: foo\r\nBar: bar\r\n  \r\n  with multiline' )


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(DefaultUtilsTests),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
