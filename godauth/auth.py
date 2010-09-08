import os

from trac.core import *
from trac.web.api import IAuthenticator, IRequestFilter
from trac.web.chrome import INavigationContributor
from trac.util import escape, hex_entropy, TracError, Markup


class GodAuthLoginModule(Component):

    implements(IAuthenticator, INavigationContributor, IRequestFilter)

    #
    # IAuthenticator methods
    #

    def authenticate(self, req):
        authname = None

        user = os.getenv("GodAuth_User")
        if user is not None:
            authname = user

        if not authname:
            return None

        if self.config.getbool('trac', 'ignore_auth_case'):
            authname = authname.lower()

        return authname


    #
    # INavigationContributor methods
    #

    def get_active_navigation_item(self, req):
        return 'login'

    def get_navigation_items(self, req):
        if req.authname and req.authname != 'anonymous':
            yield 'fake', 'fake', 'fake'
        else:
            yield 'metanav', 'login', Markup('<span class="tinylogin">Log in above to edit stuff</span>')


    #
    # IRequestFilter methods
    #

    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, content_type):
        req.hdf.removeTree('chrome.nav.metanav.help')
        req.hdf.removeTree('chrome.nav.metanav.about')
        if not req.authname or req.authname == 'anonymous':
            req.hdf.removeTree('chrome.nav.metanav.settings') 
        return template, content_type

