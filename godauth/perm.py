from trac.core import *
from trac.perm import IPermissionGroupProvider 
from trac.util import TracError

class GodAuthPermissionGroupProvider(Component):

    implements(IPermissionGroupProvider)

    def get_permission_groups(self, username):
        groups = ['anonymous']
        if username == 'Anonymous':
            return groups

        # gah! we don't actually get passed the reqeust, since trac works in an
        # odd way. this is going to require some re-engineering

        #user = req.get_header("godauth-user")
        #roles = req.get_header("godauth-roles")
        user = None
        roles = None

        if user is not None:
            if roles is not None:
                roles = roles.split(',')
                for role in roles:
                    groups.append(role)

        return groups
