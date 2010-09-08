Trac SSO
========

Single Sign-on (SSO) support for Trac.
This plugin is set up to use <a href="http://github.com/exflickr/GodAuth">GodAuth</a>,
but can easily be modified to use other SSO systems.

This plugin has been tested with Trac 0.12, but should work with 0.11 too.
It will not work with older versions of Trac that use ClearSilver instead of Genshi.


Installation
------------

First you'll need to build the egg.
Once you have python and setuptools installed (which you probably already do, for Trac), you can just:

    python setup.py bdist_egg

That will build an egg in the <code>dist/</code> folder.

Copy the egg file into the <code>plugins/</code> folder of your Trac install.

Next you'll need to enable the new authentication module in your configuration file,
which can be found at <code>conf/trac.ini</code> inside your trac install. Add these lines to the bottom:

    [components]
    trac.web.auth.* = disabled
    godauth.* = enabled

If your config file already has a <code>[components]</code> section, just append those 2 lines to it.

The permissions model is not yet ported over to use SSO roles, so you'll need to set up admins using <code>trac-admin</code>:

    trac-admin /path/to/trac/install  permission add {your-sso-username-here} TRAC_ADMIN

Finally, restart your webserver. That should be it.
