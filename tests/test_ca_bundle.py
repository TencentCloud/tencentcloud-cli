# -*- coding: utf-8 -*-
"""Tests for the TCCLI_CA_BUNDLE environment variable."""
import os
import shutil
import tempfile
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

from tccli import sso
from tccli.exceptions import ConfigurationError
from tccli.utils import Utils, _CA_BUNDLE_UNRESOLVED
import tccli.utils as utils_module


class CaBundleTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp(prefix="tccli_ca_test_")
        self.ca_path = os.path.join(self.tmp_dir, "ca.crt")
        with open(self.ca_path, "w") as ca_file:
            ca_file.write("-----BEGIN CERTIFICATE-----\nfake\n-----END CERTIFICATE-----\n")
        self.env_patcher = mock.patch.dict(os.environ, {}, clear=False)
        self.env_patcher.start()
        os.environ.pop(Utils.CA_BUNDLE_ENV, None)
        self.reset_cache()

    def tearDown(self):
        self.reset_cache()
        self.env_patcher.stop()
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    @staticmethod
    def reset_cache():
        utils_module._CA_BUNDLE_CACHE = _CA_BUNDLE_UNRESOLVED

    def set_bundle(self, value):
        self.reset_cache()
        if value is None:
            os.environ.pop(Utils.CA_BUNDLE_ENV, None)
        else:
            os.environ[Utils.CA_BUNDLE_ENV] = value


class TestGetCaBundle(CaBundleTestCase):
    def test_unset_empty_and_blank_values_use_default(self):
        for value in (None, "", "   "):
            self.set_bundle(value)
            self.assertIsNone(Utils.get_ca_bundle())

    def test_valid_file_returns_absolute_path(self):
        self.set_bundle(self.ca_path)
        self.assertEqual(os.path.abspath(self.ca_path), Utils.get_ca_bundle())

    def test_missing_file_and_directory_raise_configuration_error(self):
        for value in (os.path.join(self.tmp_dir, "missing.crt"), self.tmp_dir):
            self.set_bundle(value)
            with self.assertRaises(ConfigurationError) as context:
                Utils.get_ca_bundle()
            self.assertIn(Utils.CA_BUNDLE_ENV, str(context.exception))

    def test_unreadable_file_raises_configuration_error(self):
        self.set_bundle(self.ca_path)
        with mock.patch.object(os, "access", return_value=False):
            with self.assertRaises(ConfigurationError) as context:
                Utils.get_ca_bundle()
        self.assertIn("not readable", str(context.exception))

    def test_result_is_cached_for_process_lifetime(self):
        self.set_bundle(self.ca_path)
        expected = Utils.get_ca_bundle()
        os.environ[Utils.CA_BUNDLE_ENV] = os.path.join(self.tmp_dir, "changed.crt")
        self.assertEqual(expected, Utils.get_ca_bundle())


class TestSsoCaBundle(CaBundleTestCase):
    def test_all_sso_requests_pass_bundle_as_verify(self):
        self.set_bundle(self.ca_path)
        expected = os.path.abspath(self.ca_path)
        cases = (
            (sso.verify_login_skey, ("token", "site"), {"Ok": True}),
            (sso.list_accounts_for_access_assignment, ("token", "site"),
             {"Accounts": [], "TotalCounts": 0}),
            (sso.list_role_configurations_for_account, ("10001", "token", "site"),
             {"RoleConfigurationsForAccount": [], "IsTruncated": False}),
            (sso.gen_saml_response, ("token", "RoleSAML", "10001", "", "config", "site"),
             {"Ok": True}),
            (sso.assume_role_with_saml, ("saml", "principal", "role", "session", 7200, "site"),
             {"Ok": True}),
            (sso.check_login_state, ("state",), {"Ok": True}),
        )
        for function, args, response in cases:
            with mock.patch.object(sso.requests, "post") as post:
                post.return_value.json.return_value = response
                function(*args)
                self.assertEqual(expected, post.call_args[1]["verify"])

    def test_sso_uses_default_when_bundle_is_unset(self):
        self.set_bundle(None)
        with mock.patch.object(sso.requests, "post") as post:
            post.return_value.json.return_value = {"Ok": True}
            sso.check_login_state("state")
        self.assertIsNone(post.call_args[1]["verify"])


class TestBundleReachesTlsLayer(CaBundleTestCase):
    def test_bundle_is_passed_as_requests_verify(self):
        from tencentcloud.common.http.request import ApiRequest, RequestInternal

        self.set_bundle(self.ca_path)
        bundle = Utils.get_ca_bundle()
        request = ApiRequest("https://localhost", certification=bundle)
        internal = RequestInternal(host="https://localhost", method="POST", header={}, data="{}")
        with mock.patch.object(request.conn._session, "request") as session_request:
            request.send_request(internal)
        self.assertEqual(bundle, session_request.call_args[1]["verify"])


if __name__ == "__main__":
    unittest.main()
