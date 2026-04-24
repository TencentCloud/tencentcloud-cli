# -*- coding: utf-8 -*-
"""file_process 模块单元测试"""
import unittest
from unittest.mock import patch, MagicMock

from tccli.plugins.ci.file_process import (
    file_hash, file_hash_job_submit,
    file_uncompress_submit, file_compress_submit,
    file_zip_preview, file_process_jobs_query,
)

MOCK_INIT = "tccli.plugins.ci.file_process.init_cos_client"
MOCK_PRINT = "tccli.plugins.ci.file_process.print_result"
MOCK_HANDLE = "tccli.plugins.ci.file_process.handle_cos_error"
PG = {"secretId": "AK", "secretKey": "SK", "region": "ap-guangzhou"}


class TestFileHash(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_basic(self, mock_init, mock_print):
        client = MagicMock()
        client.file_hash.return_value = {"FileHashCodeResult": {"MD5": "abc"}}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "hash_type": "md5"}
        file_hash(args, PG)
        kw = client.file_hash.call_args[1]
        self.assertFalse(kw["AddToHeader"])

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_add_to_header_true(self, mock_init, mock_print):
        client = MagicMock()
        client.file_hash.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "hash_type": "sha1", "add_to_header": "true"}
        file_hash(args, PG)
        kw = client.file_hash.call_args[1]
        self.assertTrue(kw["AddToHeader"])

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_add_to_header_false(self, mock_init, mock_print):
        client = MagicMock()
        client.file_hash.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "hash_type": "sha1", "add_to_header": "false"}
        file_hash(args, PG)
        kw = client.file_hash.call_args[1]
        self.assertFalse(kw["AddToHeader"])

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        file_hash({"bucket": "b", "key": "k", "hash_type": "md5"}, PG)
        mock_handle.assert_called_once()


class TestFileHashJobSubmit(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_basic(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_create_file_hash_job.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "hash_type": "md5"}
        file_hash_job_submit(args, PG)
        kw = client.ci_create_file_hash_job.call_args[1]
        self.assertEqual(kw["FileHashCodeConfig"]["Type"], "md5")
        self.assertNotIn("AddToHeader", kw["FileHashCodeConfig"])

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_add_to_header(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_create_file_hash_job.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "hash_type": "sha256", "add_to_header": "True"}
        file_hash_job_submit(args, PG)
        kw = client.ci_create_file_hash_job.call_args[1]
        self.assertEqual(kw["FileHashCodeConfig"]["AddToHeader"], "true")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        file_hash_job_submit({"bucket": "b", "key": "k", "hash_type": "md5"}, PG)
        mock_handle.assert_called_once()


class TestFileUncompressSubmit(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_basic(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_create_file_uncompress_job.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "archive.zip"}
        file_uncompress_submit(args, PG)
        kw = client.ci_create_file_uncompress_job.call_args[1]
        self.assertEqual(kw["OutputBucket"], "b")

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_all_params(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_create_file_uncompress_job.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "a.zip", "password": "pwd123",
                "output_prefix": "unzipped/", "output_bucket": "ob"}
        file_uncompress_submit(args, PG)
        kw = client.ci_create_file_uncompress_job.call_args[1]
        self.assertEqual(kw["FileUncompressConfig"]["UnCompressKey"], "pwd123")
        self.assertEqual(kw["FileUncompressConfig"]["Prefix"], "unzipped/")
        self.assertEqual(kw["OutputBucket"], "ob")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        file_uncompress_submit({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestFileCompressSubmit(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_basic(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_create_file_compress_job.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "keys": "a.txt,b.txt", "output_key": "out.zip"}
        file_compress_submit(args, PG)
        kw = client.ci_create_file_compress_job.call_args[1]
        self.assertEqual(kw["FileCompressConfig"]["Key"], ["a.txt", "b.txt"])
        self.assertEqual(kw["FileCompressConfig"]["Format"], "zip")

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_prefix_and_format(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_create_file_compress_job.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "keys": "a.txt", "output_key": "out.tar.gz",
                "compress_format": "tar.gz", "prefix": "dir/"}
        file_compress_submit(args, PG)
        kw = client.ci_create_file_compress_job.call_args[1]
        self.assertEqual(kw["FileCompressConfig"]["Format"], "tar.gz")
        self.assertEqual(kw["FileCompressConfig"]["Prefix"], "dir/")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        file_compress_submit({"bucket": "b", "keys": "k", "output_key": "o"}, PG)
        mock_handle.assert_called_once()


class TestFileZipPreview(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_tuple_response(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_file_zip_preview.return_value = ({"x-ci-request-id": "r"}, {"FileList": []})
        mock_init.return_value = client
        file_zip_preview({"bucket": "b", "key": "a.zip"}, PG)
        mock_print.assert_called_once_with({"FileList": []}, {"x-ci-request-id": "r"})

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_non_tuple_response(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_file_zip_preview.return_value = {"FileList": []}
        mock_init.return_value = client
        file_zip_preview({"bucket": "b", "key": "a.zip"}, PG)
        mock_print.assert_called_once_with({"FileList": []})

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        file_zip_preview({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestFileProcessJobsQuery(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_get_file_process_jobs.return_value = {}
        mock_init.return_value = client
        file_process_jobs_query({"bucket": "b", "job_id": "j"}, PG)
        client.ci_get_file_process_jobs.assert_called_once_with(Bucket="b", JobIDs="j")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        file_process_jobs_query({"bucket": "b", "job_id": "j"}, PG)
        mock_handle.assert_called_once()


if __name__ == "__main__":
    unittest.main()
