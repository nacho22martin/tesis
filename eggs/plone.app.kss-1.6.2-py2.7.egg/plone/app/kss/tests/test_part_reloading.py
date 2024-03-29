import unittest
from Products.PloneTestCase import PloneTestCase

from plone.app.kss.plonekssview import PloneKSSView
from plone.app.kss.interfaces import IPortalObject
from plone.app.kss.portlets import (
    attributesTriggerNavigationPortletReload, workflowTriggersReviewPortletReload)
from plone.app.kss.portlets import attributesTriggerRecentPortletReload
from plone.app.kss.tests.kss_and_plone_layer import KSSAndPloneTestCase

from zope.lifecycleevent import ObjectModifiedEvent
from zope import lifecycleevent

from Products.Archetypes.event import ObjectEditedEvent

from plone.app.portlets.portlets.navigation import Assignment as NavigationAssignment
from plone.app.portlets.portlets.recent import Assignment as RecentAssignment
from plone.app.portlets.portlets.review import Assignment as ReviewAssignment
from plone.portlets.interfaces import IPortletManager, IPortletAssignmentMapping
from zope.component import getUtility, getMultiAdapter
from Products.CMFCore.WorkflowCore import ActionSucceededEvent

PloneTestCase.setupPloneSite()

class SampleView(PloneKSSView):

    def change_title(self, title):
        # normally you would change the zope database here
        self.handle(ObjectModifiedEvent(self.context))
        return self.render()


class TestPortletReloading(KSSAndPloneTestCase):

    def afterSetUp(self):
        KSSAndPloneTestCase.afterSetUp(self)
        self.setDebugRequest()
        self.loginAsPortalOwner()
        self.setRoles(['Manager',])
        # register the sample view
        self.view = self.portal.restrictedTraverse('@@change_title')

    def test_no_update_of_nav_portlet_when_unhooked(self):
        # nothing should happen
        result = self.view.render()
        self.assertEqual(result, [])

    def test_no_update_of_nav_portlet_when_hooked_with_wrong_event(self):
        # nothing should happen still because we must change the title or the
        # description
        modified_event = ObjectEditedEvent(self.folder)
        attributesTriggerNavigationPortletReload(self.folder, self.view, modified_event)
        result = self.view.render()
        self.assertEqual(result, [])

    def test_update_of_nav_portlet(self):
        self.loginAsPortalOwner()
        self.portal.invokeFactory('Folder', 'testfolder')
        folder = self.portal.testfolder
        self.create_portlet(u'navigation',
            NavigationAssignment(topLevel=0),
            context=folder)
        self.view = folder.restrictedTraverse('@@change_title')
        descriptor = lifecycleevent.Attributes(IPortalObject, 'title')
        modified_event = ObjectEditedEvent(folder, descriptor)
        attributesTriggerNavigationPortletReload(folder, self.view, modified_event)
        result = self.view.render()
        command = result[0]
        self.failUnless(command.has_key('selector'))
        self.failUnless(command['selector'].startswith('portletwrapper'))
        self.failUnless(command.has_key('name'))
        self.assertEqual(command['name'], 'replaceInnerHTML')
        self.failUnless(command.has_key('params'))
        params = result[0]['params']
        self.failUnless(params.has_key('html'))
        html = params['html']
        self.failUnless('portletNavigationTree' in html)
        self.failUnless(command.has_key('selectorType'))
        self.assertEqual(command['selectorType'], 'htmlid')

    def create_portlet(self, name, portlet, context=None):
        if context == None:
            context = self.portal
        leftColumn = getUtility(IPortletManager, name=u'plone.leftcolumn',
                            context=context)
        left = getMultiAdapter((context, leftColumn,), IPortletAssignmentMapping,
                            context=context)
        assert name not in left, 'Portlet is already there, no need to create it - fix me'
        left[name] = portlet

    def test_update_of_recent_portlet(self):
        # there is no recent portlet now at all, so we need to create one
        # in the front page so we can test it.
        self.create_portlet(u'recent', RecentAssignment())
        #
        descriptor = lifecycleevent.Attributes(IPortalObject, 'title')
        modified_event = ObjectEditedEvent(self.folder, descriptor)
        attributesTriggerRecentPortletReload(self.folder, self.view, modified_event)
        result = self.view.render()
        command = result[0]
        self.failUnless(command.has_key('selector'))
        self.failUnless(command['selector'].startswith('portletwrapper'))
        self.failUnless(command.has_key('name'))
        self.assertEqual(command['name'], 'replaceInnerHTML')
        self.failUnless(command.has_key('params'))
        params = result[0]['params']
        self.failUnless(params.has_key('html'))
        html = params['html']
        self.failUnless('portletRecent' in html)
        self.failUnless(command.has_key('selectorType'))
        self.assertEqual(command['selectorType'], 'htmlid')

    def test_update_of_review_portlet(self):
        self.loginAsPortalOwner()
        portal = self.portal
        self.portal.invokeFactory('Document', 'test-page')
        portal.portal_workflow.doActionFor(self.portal['test-page'], 'submit')
        self.create_portlet(u'review', ReviewAssignment())
        event = ActionSucceededEvent(self.folder, None, None, None)
        event.old_state, event.new_state = 'private', 'pending'
        workflowTriggersReviewPortletReload(self.portal, self.view, event)
        result = self.view.render()
        command = result[0]
        self.failUnless(command.has_key('selector'))
        self.failUnless(command['selector'].startswith('portletwrapper'))
        self.failUnless(command.has_key('name'))
        self.assertEqual(command['name'], 'replaceInnerHTML')
        self.failUnless(command.has_key('params'))
        params = result[0]['params']
        self.failUnless(params.has_key('html'))
        html = params['html']
        self.failUnless('portletWorkflowReview' in html)
        self.failUnless(command.has_key('selectorType'))
        self.assertEqual(command['selectorType'], 'htmlid')

    def test_portlet_remove(self):
        self.loginAsPortalOwner()
        portal = self.portal
        self.create_portlet(u'review', ReviewAssignment())

        event = ActionSucceededEvent(self.folder, None, None, None)
        event.old_state, event.new_state = 'pending', 'published'
        workflowTriggersReviewPortletReload(self.portal, self.view, event)
        result = self.view.render()
        command = result[0]
        self.failUnless(command.has_key('selector'))
        self.failUnless(command['selector'].startswith('portletwrapper'))
        self.failUnless(command.has_key('name'))
        self.assertEqual(command['name'], 'deleteNode')


def test_suite():
    suites = []
    suites.append(unittest.makeSuite(TestPortletReloading))
    return unittest.TestSuite(suites)
