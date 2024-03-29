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
""" Unit tests for RegistrationTool module.

$Id: test_RegistrationTool.py 110659 2010-04-08 15:54:42Z tseaver $
"""

import unittest
from Testing import ZopeTestCase

from Acquisition import Implicit
from zope.interface.verify import verifyClass
from zope.testing.cleanup import cleanUp

from Products.CMFCore.tests.base.testcase import RequestTest
from Products.CMFDefault.testing import FunctionalLayer


class FauxMembershipTool(Implicit):

    def getMemberById( self, username ):
        return None


class RegistrationToolTests(RequestTest):

    def _getTargetClass(self):
        from Products.CMFDefault.RegistrationTool import RegistrationTool

        return RegistrationTool

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def tearDown(self):
        cleanUp()
        RequestTest.tearDown(self)

    def test_interfaces(self):
        from Products.CMFCore.interfaces import IRegistrationTool

        verifyClass(IRegistrationTool, self._getTargetClass())

    def test_spamcannon_collector_243( self ):

        INJECTED_HEADERS = """
To:someone@example.com
cc:another_victim@elsewhere.example.com
From:someone@example.com
Subject:Hosed by Spam Cannon!

Spam, spam, spam
"""

        rtool = self._makeOne().__of__(self.app)
        self.app.portal_membership = FauxMembershipTool()

        props = { 'email' : INJECTED_HEADERS
                , 'username' : 'username'
                }

        result = rtool.testPropertiesValidity(props, None)

        self.failIf( result is None, 'Invalid e-mail passed inspection' )


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RegistrationToolTests))
    s = ZopeTestCase.FunctionalDocFileSuite('RegistrationTool.txt')
    s.layer = FunctionalLayer
    suite.addTest(s)
    return suite

if __name__ == '__main__':
    from Products.CMFCore.testing import run
    run(test_suite())
