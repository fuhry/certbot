"""Certbot Hurricane Electric authenticator plugin."""
import collections
import logging
import time
import os
import tldextract

import zope.interface
from botocore.exceptions import NoCredentialsError, ClientError

from certbot import errors
from certbot import interfaces
from certbot.plugins import dns_common

from acme.magic_typing import DefaultDict, List, Dict # pylint: disable=unused-import, no-name-in-module

logger = logging.getLogger(__name__)

INSTRUCTIONS = (
    "To use certbot-dns-hurricane, ...")

@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_common.DNSAuthenticator):
    """Hurricane Electric Authenticator

    This authenticator solves a DNS01 challenge by uploading the answer to
    Hurricane Electric's DNS hosting service.
    """

    description = ("Obtain certificates using a DNS TXT record (if you are using AWS Route53 for "
                   "DNS).")
    ttl = 10

    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)
        
    @classmethod
    def add_parser_arguments(cls, add):  # pylint: disable=arguments-differ
        super(Authenticator, cls).add_parser_arguments(add, default_propagation_seconds=30)
        add('credentials', help='Hurricane Electric credentials INI file.')

    def more_info(self):  # pylint: disable=missing-docstring,no-self-use
        return "Solve a DNS01 challenge using Hurricane Electric Hosted DNS"

    def _setup_credentials(self):
        self.credentials = self._configure_credentials(
            'credentials',
            'Hurricane Electric DNS login details',
            {
                'username': 'dns.he.net username',
                'password': 'dns.he.net password'
            }
        )

    def _perform(self, domain, validation_name, validation): # pylint: disable=missing-docstring
        self._change_txt_record("create", domain, validation_name, validation)

    def _cleanup(self, domain, validation_name, validation):
        self._change_txt_record("delete", domain, validation_name, validation)

    def _change_txt_record(self, action, domain, record_name, validation):
        tld = tldextract.extract(domain)
        domain = '%s.%s' % (tld.domain, tld.suffix)
        username = self.credentials.conf('username')
        password = self.credentials.conf('password')
        cmdline = "he-dns -d %s -u %s -p %s -a %s -t TXT -n %s -v %s" % (
            domain, username, password, action, record_name, validation
        )
        result = os.system(cmdline)
        if result > 0:
            raise RuntimeError("he-dns failed with code %d" % (result))

        return

    def _wait_for_change(self, change_id):
        pass
