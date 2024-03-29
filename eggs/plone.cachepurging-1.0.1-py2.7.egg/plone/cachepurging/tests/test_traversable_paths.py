import unittest

from zope.interface import implements

from plone.cachepurging.paths import TraversablePurgePaths
from OFS.interfaces import ITraversable

class FauxTraversable(object):
    implements(ITraversable)

    def absolute_url_path(self):
        return '/foo'

class TestTraversablePaths(unittest.TestCase):
    
    def test_traversable_paths(self):
        
        context = FauxTraversable()
        paths = TraversablePurgePaths(context)
        
        self.assertEquals(['/foo'], paths.getRelativePaths())
        self.assertEquals([], paths.getAbsolutePaths())
        
def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
