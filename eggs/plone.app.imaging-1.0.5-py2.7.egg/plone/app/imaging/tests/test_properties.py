from unittest import defaultTestLoader
from plone.app.imaging.tests.base import ImagingTestCase
from plone.app.imaging.utils import getAllowedSizes


class PropertiesTests(ImagingTestCase):

    def testAllowedSizes(self):
        # test the defaults
        self.assertEqual(getAllowedSizes(), dict(
            large =   (768, 768),
            preview = (400, 400),
            mini =    (200, 200),
            thumb =   (128, 128),
            tile =    ( 64,  64),
            icon =    ( 32,  32),
            listing = ( 16,  16)))
        # override and test again
        iprops = self.portal.portal_properties.imaging_properties
        iprops.manage_changeProperties(allowed_sizes='foo 23:23')
        self.assertEqual(getAllowedSizes(), dict(foo = (23, 23)))
        # empty lines and white space should be ignored
        iprops.manage_changeProperties(allowed_sizes=['x   23 :23 ', '', ' '])
        self.assertEqual(getAllowedSizes(), dict(x = (23, 23)))
        # however, white space within the name should be fine...
        iprops.manage_changeProperties(allowed_sizes=['foo bar 23:23'])
        self.assertEqual(getAllowedSizes(), dict(foo_bar = (23, 23)))


def test_suite():
    return defaultTestLoader.loadTestsFromName(__name__)
