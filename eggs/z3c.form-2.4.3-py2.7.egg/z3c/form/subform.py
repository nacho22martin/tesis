##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Logical Sub-Form Implementation

$Id: subform.py 79464 2007-09-04 18:22:18Z srichter $
"""
__docformat__ = "reStructuredText"
import zope.interface

from z3c.form import action, button, form, interfaces
from z3c.form.i18n import MessageFactory as _


class EditSubForm(form.BaseForm):
    zope.interface.implements(
        interfaces.ISubForm, interfaces.IHandlerForm)

    formErrorsMessage = _('There were some errors.')
    successMessage = _('Data successfully updated.')
    noChangesMessage = _('No changes were applied.')

    def __init__(self, context, request, parentForm):
        self.context = context
        self.request = request
        self.parentForm = self.__parent__ = parentForm

    @button.handler(form.EditForm.buttons['apply'])
    def handleApply(self, action):
        data, errors = self.widgets.extract()
        if errors:
            self.status = self.formErrorsMessage
            return
        content = self.getContent()
        changed = form.applyChanges(self, content, data)
        if changed:
            zope.event.notify(
                zope.lifecycleevent.ObjectModifiedEvent(content))
            self.status = self.successMessage
        else:
            self.status = self.noChangesMessage


    def update(self):
        super(EditSubForm, self).update()
        for action in self.parentForm.actions.executedActions:
            adapter = zope.component.queryMultiAdapter(
                (self, self.request, self.getContent(), action),
                interface=interfaces.IActionHandler)
            if adapter:
                adapter()
