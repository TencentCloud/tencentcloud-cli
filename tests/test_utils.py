# -*- coding: utf-8 -*-
import os
import shutil
import stat
import tempfile
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

from tccli.utils import Utils


@unittest.skipIf(os.name == "nt", "POSIX permission modes are not supported")
class TestDumpJsonMsgPermissions(unittest.TestCase):

    def setUp(self):
        self.root_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.root_dir)

    def _dump_with_permissive_umask(self, cli_dir):
        credential_path = os.path.join(cli_dir, "default.credential")
        old_umask = os.umask(0)
        try:
            Utils.dump_json_msg(credential_path, {"secretKey": "secret"})
        finally:
            os.umask(old_umask)
        return credential_path

    def test_new_directory_is_private(self):
        cli_dir = os.path.join(self.root_dir, ".tccli")

        self._dump_with_permissive_umask(cli_dir)

        self.assertEqual(stat.S_IMODE(os.stat(cli_dir).st_mode), 0o700)

    def test_existing_directory_is_tightened_on_write(self):
        cli_dir = os.path.join(self.root_dir, ".tccli")
        os.makedirs(cli_dir)
        os.chmod(cli_dir, 0o755)

        self._dump_with_permissive_umask(cli_dir)

        self.assertEqual(stat.S_IMODE(os.stat(cli_dir).st_mode), 0o700)

    def test_existing_private_directory_skips_chmod(self):
        cli_dir = os.path.join(self.root_dir, ".tccli")
        os.makedirs(cli_dir, 0o700)
        os.chmod(cli_dir, 0o700)

        with mock.patch("os.chmod") as chmod:
            self._dump_with_permissive_umask(cli_dir)
            chmod.assert_not_called()
