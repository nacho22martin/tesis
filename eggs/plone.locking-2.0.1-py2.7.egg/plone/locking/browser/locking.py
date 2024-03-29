
from Acquisition import aq_inner
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from DateTime import DateTime
from datetime import timedelta

from plone.locking.interfaces import ILockable, IRefreshableLockable
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('plone')


class LockingOperations(BrowserView):
    """Lock acquisition and stealing operations
    """

    def force_unlock(self, redirect=True):
        """Steal the lock.

        If redirect is True, redirect back to the context URL, i.e. reload
        the page.
        """
        lockable = ILockable(self.context)
        lockable.unlock()
        if redirect:
            self.request.RESPONSE.redirect(self.context.absolute_url())

    def safe_unlock(self):
        """Unlock the object if the current user has the lock
        """
        lockable = ILockable(self.context)
        if lockable.can_safely_unlock():
            lockable.unlock()
    
    def refresh_lock(self):
        """Reset the lock start time
        """
        lockable = IRefreshableLockable(self.context, None)
        if lockable is not None:
            lockable.refresh_lock()

class LockingInformation(BrowserView):
    """Lock information
    """

    def is_locked(self):
        lockable = ILockable(aq_inner(self.context))
        return lockable.locked()

    def is_locked_for_current_user(self):
        """True if this object is locked for the current user (i.e. the
        current user is not the lock owner)
        """
        lockable = ILockable(aq_inner(self.context))
        # Faster version - we rely on the fact that can_safely_unlock() is
        # True even if the object is not locked
        return not lockable.can_safely_unlock()
        # return lockable.locked() and not lockable.can_safely_unlock()

    def lock_is_stealable(self):
        """Find out if the lock is stealable
        """
        lockable = ILockable(self.context)
        return lockable.stealable()

    def lock_info(self):
        """Get information about the current lock, a dict containing:

        creator - the id of the user who created the lock
        fullname - the full name of the lock creator
        author_page - a link to the home page of the author
        time - the creation time of the lock
        time_difference - a string representing the time since the lock was
        acquired.
        """

        portal_membership = getToolByName(self.context, 'portal_membership')
        portal_url = getToolByName(self.context, 'portal_url')
        lockable = ILockable(aq_inner(self.context))
        url = portal_url()
        for info in lockable.lock_info():
            creator = info['creator']
            time = info['time']
            token = info['token']
            lock_type = info['type']
            # Get the fullname, but remember that the creator may not
            # be a member, but only Authenticated or even anonymous.
            # Same for the author_page
            fullname = ''
            author_page = ''
            member = portal_membership.getMemberById(creator)
            if member:
                fullname = member.getProperty('fullname', '')
                author_page = "%s/author/%s" % (url, creator)
            if fullname == '':
                fullname = creator or _('label_an_anonymous_user',
                                        u'an anonymous user')
            time_difference = self._getNiceTimeDifference(time)

            return {
                'creator'         : creator,
                'fullname'        : fullname,
                'author_page'     : author_page,
                'time'            : time,
                'time_difference' : time_difference,
                'token'           : token,
                'type'            : lock_type,
            }

    def _getNiceTimeDifference(self, baseTime):
        now = DateTime()
        days = int(round(now - DateTime(baseTime)))
        delta = timedelta(now - DateTime(baseTime))
        days = delta.days
        hours = int(delta.seconds / 3600)
        minutes = (delta.seconds - (hours * 3600)) /60

        dateString = u""
        if days == 0:
            if hours == 0:
                if delta.seconds < 120:
                    dateString = _(u"1 minute")
                else:
                    dateString = _(u"$m minutes", mapping={'m': minutes})
            elif hours == 1:
                dateString = _(u"$h hour and $m minutes", mapping={'h': hours, 'm': minutes})
            else:
                dateString = _(u"$h hours and $m minutes", mapping={'h': hours, 'm': minutes})
        else:
            if days == 1:
                dateString = _(u"$d day and $h hours", mapping={'d': days, 'h': hours})
            else:
                dateString = _(u"$d days and $h hours", mapping={'d': days, 'h': hours})
        return dateString
