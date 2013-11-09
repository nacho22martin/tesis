##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
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

# BBB
from zope.security.metadirectives import (IClassDirective,
                                          IImplementsSubdirective,
                                          IRequireSubdirective,
                                          IAllowSubdirective,
                                          IFactorySubdirective)

# BBB
from zope.component.zcml import (IBasicViewInformation,
                                 IBasicResourceInformation,
                                 IViewDirective,
                                 IResourceDirective)