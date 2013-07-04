import os

from AccessControl.SecurityInfo import ModuleSecurityInfo
from AccessControl.SecurityManagement import newSecurityManager
try:
    from Products.PloneTestCase import utils
except ImportError:
    pass
else:
    if getattr(utils, 'makelist', None) is None:
        utils.makelist = list
try:
    from Products.PloneTestCase import PloneTestCase as ptc
    HAVE_PTC = True
except:
    from Testing.ZopeTestCase import PortalTestCase
    from Testing.ZopeTestCase import Functional
    from Testing.ZopeTestCase import user_name
    from Testing.ZopeTestCase import user_password
    HAVE_PTC = False
try:
    from Products.CMFDefault.testing import FunctionalLayer as CMFFunctionalLayer
    HAVE_CMF = True
except ImportError:
    from Testing.ZopeTestCase.testPortalTestCase import DummyPortal as PortalObject
    HAVE_CMF = False


ModuleSecurityInfo('AccessControl').declarePublic('Unauthorized')
portal_name = 'plone'
if not HAVE_PTC:
    portal_owner = 'portal_owner'

    class FunctionalTestCase(Functional, PortalTestCase):

        __implements__ = (getattr(Functional, '__implements__', ()),
                          getattr(PortalTestCase, '__implements__', ()))

        if HAVE_CMF:
            layer = CMFFunctionalLayer

        def getPortal(self):
            if HAVE_CMF and portal_name not in self.app.objectIds():
                from Acquisition import aq_base
                site = self.app._getOb('site')
                self.app._delObject('site', suppress_events=True)
                site = aq_base(site)
                site._setId(portal_name)
                self.app._setObject(portal_name, site, set_owner=0, suppress_events=True)
            elif not HAVE_CMF:
                self.app._setObject(portal_name, PortalObject(portal_name))
            return getattr(self.app, portal_name)

        def _setup(self):
            super(FunctionalTestCase, self)._setup()
            if self._configure_portal:
                uf = self.portal.acl_users
                uf.userFolderAddUser(portal_owner, user_password,
                                     ['Manager'], [])

        def loginAsPortalOwner(self):
            '''Use if - AND ONLY IF - you need to manipulate
               the portal object itself.
            '''
            uf = self.portal.acl_users
            user = uf.getUserById(portal_owner)
            if not hasattr(user, 'aq_base'):
                user = user.__of__(uf)
            newSecurityManager(None, user)

    default_user = user_name
    default_password = user_password
else:
    class FunctionalTestCase(ptc.FunctionalTestCase):
        def afterSetUp(self):
            pass

    portal_owner = ptc.portal_owner
    default_user = ptc.default_user
    default_password = ptc.default_password


# Patch exceptionformatter behavior for new versions of zope.testrunner being
# used with old versions of zope.exceptions.
from zope.exceptions import exceptionformatter
try:
    exceptionformatter.TextExceptionFormatter(limit=None, with_filenames=True)
except TypeError:
    OriginalTextExceptionFormatter = exceptionformatter.TextExceptionFormatter

    class NewStyleTextExceptionFormatter(exceptionformatter.TextExceptionFormatter):

        def __init__(self, with_filenames=True, *args, **kwargs):
            OriginalTextExceptionFormatter.__init__(self, *args, **kwargs)

    exceptionformatter.TextExceptionFormatter = NewStyleTextExceptionFormatter

def get_file(filename):
    return open(os.path.join(os.path.dirname(__file__),
                             'data',
                             filename),
                'r')


def get_data(filename):
    return get_file(filename).read()
