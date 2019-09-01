"""Tests for certbot_dns_hurricane.dns_hurricane.Authenticator"""

import unittest

import mock
from botocore.exceptions import NoCredentialsError, ClientError

from certbot import errors
from certbot.compat import os
from certbot.plugins import dns_test_common
from certbot.plugins.dns_test_common import DOMAIN


class AuthenticatorTest(unittest.TestCase, dns_test_common.BaseAuthenticatorTest):
    # pylint: disable=protected-access

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_perform(self):
        pass

    def test_perform_no_credentials_error(self):
        pass

    def test_perform_client_error(self):
        pass

    def test_cleanup(self):
        pass

    def test_cleanup_no_credentials_error(self):
        pass

    def test_cleanup_client_error(self):
        pass


class ClientTest(unittest.TestCase):
    # pylint: disable=protected-access

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_zone_id_for_domain(self):
        pass

    def test_find_zone_id_for_domain_pagination(self):
        pass

    def test_find_zone_id_for_domain_no_results(self):
        pass

    def test_find_zone_id_for_domain_no_correct_results(self):
        pass

    def test_change_txt_record(self):
        pass

    def test_change_txt_record_delete(self):
        pass

    def test_change_txt_record_multirecord(self):
        pass

    def test_wait_for_change(self):
        pass


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
