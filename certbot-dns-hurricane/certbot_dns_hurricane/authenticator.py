"""Shim around `~certbot_dns_hurricane.dns_hurricane` for backwards compatibility."""
import warnings

import zope.interface

from certbot import interfaces
from certbot_dns_hurricane import dns_hurricane


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_hurricane.Authenticator):
    """Shim around `~certbot_dns_hurricane.dns_hurricane.Authenticator` for backwards compatibility."""

    hidden = True

    def __init__(self, *args, **kwargs):
        warnings.warn("The 'authenticator' module was renamed 'dns_hurricane'",
                      DeprecationWarning)
        super(Authenticator, self).__init__(*args, **kwargs)
