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

        user = req.get_header("godauth-user")
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
            yield 'metanav', 'login', Markup('<span class="tinylogin">Hello %s</span>' % req.authname)
        else:
            yield 'metanav', 'login', Markup('<span class="tinylogin">Not logged in</span>')


    #
    # IRequestFilter methods
    #

    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, data, content_type):

        new_list = []
        for v in req.chrome['nav']['metanav']:
            use = True
            if v['name'] == 'help':
                use = False
            if v['name'] == 'about':
                use = False
            if not req.authname or req.authname == 'anonymous':
                if v['name'] == 'settings':
                    use = False
            if use:
                new_list.append(v)
        req.chrome['nav']['metanav'] = new_list

        return template, data, content_type

