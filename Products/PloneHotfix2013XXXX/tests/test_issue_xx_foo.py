from Products.PloneHotfix2013XXXX.tests import FunctionalTestCase
from Products.PloneHotfix2013XXXX.tests import default_user
from Products.PloneHotfix2013XXXX.tests import default_password

class TestAttackVector(FunctionalTestCase):

    def test_foo(self):
        res = self.publish('/plone/foo',
                           basic='%s:%s' % (default_user, default_password))
        
        if res.status == 302:
            self.assertTrue(
                res.headers['location'].startswith('http://nohost/plone/login_form') or
                res.headers['location'].startswith('http://nohost/plone/acl_users/credentials_cookie_auth/require_login') or
                res.headers['location'].startswith('http://nohost/plone/acl_users/credentials_cookie_auth/login_form')
            )
        else:
            self.assertTrue(res.status in (401, 403))
