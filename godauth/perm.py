from trac.core import *
from trac.perm import IPermissionGroupProvider 
from trac.util import TracError

class FlAuthPermissionGroupProvider(Component):

    implements(IPermissionGroupProvider)

    def get_permission_groups(self, username):
        groups = ['anonymous']
        if username == 'Anonymous':
            return groups

        if username == 'cal':
            groups.append('admins')

        return groups

