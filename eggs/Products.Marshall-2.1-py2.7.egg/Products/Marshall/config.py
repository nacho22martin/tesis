# Marshall: A framework for pluggable marshalling policies
# Copyright (C) 2004-2006 Enfold Systems, LLC
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
"""
$Id: config.py 12346 2010-03-17 15:36:39Z csenger $
"""
import os
import logging
from App.Common import package_home

logger = logging.getLogger('Marshall')

try:
    import libxml2
except ImportError:
    hasLibxml2 = False
    logger.log(logging.DEBUG, \
        'libxml2-python not available.' \
        ' Unable to register libxml2 based marshallers.')
else:
    hasLibxml2 = True


hasElementtree = True
try:
    from xml.etree import cElementTree
except ImportError:
    try:
        import cElementTree
    except ImportError:
        try:
            from elementtree import ElementTree
        except ImportError:
            hasElementtree = False
            logger.log(logging.INFO, \
                       'ElementTree not available. '
                       'Unable to register elementtree based marshallers, '
                       'at least ATXMLMarshaller (atxml).')

PACKAGE_HOME = package_home(globals())
HANDLE_REFS = False

TOOL_ID = 'marshaller_registry'
AT_NS = 'http://plone.org/ns/archetypes/'
CMF_NS = 'http://cmf.zope.org/namespaces/default/'
DC_NS = "http://purl.org/dc/elements/1.1/"
ADOBE_NS = "adobe:ns:meta"

ATXML_SCHEMA = os.path.join(PACKAGE_HOME, 'validation', 'atxml')
