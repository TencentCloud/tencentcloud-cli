# -*- coding: utf-8 -*-
"""doc_process 模块单元测试"""
import os
import unittest
from unittest.mock import patch, MagicMock

from tccli.plugins.ci.doc_process import (
    doc_preview, doc_preview_html,
    doc_job_submit, doc_job_query, doc_job_list,
)

MOCK_INIT = "tccli.plugins.ci.doc_process.init_cos_client"
MOCK_PRINT = "tccli.plugins.ci.doc_process.print_result"
MOCK_HANDLE = "tccli.plugins.ci.doc_process.handle_cos_error"
MOCK_SAVE = "tccli.plugins.ci.doc_process.save_response_to_file"
PG = {"secretId": "AK", "secretKey": "SK", "region": "ap-guangzhou"}


class TestDocPreview(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_SAVE, return_value=4096)
    @patch(MOCK_INIT)
    def test_minimal(self, mock_init, mock_save, mock_print):
        client = MagicMock()
        client.ci_doc_preview_process.return_value = {"Content-Type": "image/png",
                                                        "X-Total-Page": "5", "X-Total-Sheet": "1"}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "doc.pdf"}
        doc_preview(args, PG)
        mock_print.assert_called_once()
        result = mock_print.call_args[0][0]
        self.assertEqual(result["Page"], "1")

    @patch(MOCK_PRINT)
    @patch(MOCK_SAVE, return_value=2048)
    @patch(MOCK_INIT)
    def test_all_params(self, mock_init, mock_save, mock_print):
        client = MagicMock()
        client.ci_doc_preview_process.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "doc.xlsx", "page": "2", "src_type": "xlsx",
                "image_type": "jpg", "dsttype": "jpg", "local_path": "/tmp/out.jpg"}
        doc_preview(args, PG)
        kw = client.ci_doc_preview_process.call_args[1]
        self.assertEqual(kw["Page"], 2)
        self.assertEqual(kw["SrcType"], "xlsx")
        self.assertIn("imageMogr2/format/jpg", kw["ImageParams"])
        self.assertEqual(kw["DstType"], "jpg")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        doc_preview({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestDocPreviewHtml(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_SAVE, return_value=8192)
    @patch(MOCK_INIT)
    def test_with_local_path(self, mock_init, mock_save, mock_print):
        client = MagicMock()
        client.ci_doc_preview_html_process.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "doc.pdf", "local_path": "/tmp/out.html", "src_type": "pdf"}
        doc_preview_html(args, PG)
        result = mock_print.call_args[0][0]
        self.assertEqual(result["Status"], "Success")

    @patch(MOCK_PRINT)
    @patch(MOCK_SAVE, return_value=10240)
    @patch(MOCK_INIT)
    def test_without_local_path(self, mock_init, mock_save, mock_print):
        client = MagicMock()
        resp = {"Content-Type": "text/html"}
        client.ci_doc_preview_html_process.return_value = resp
        mock_init.return_value = client
        args = {"bucket": "b", "key": "ci-test/doc/test.pdf"}
        doc_preview_html(args, PG)
        # 应自动生成文件名 test_preview.html
        save_path = mock_save.call_args[0][1]
        self.assertTrue(save_path.endswith("_preview.html"))
        result = mock_print.call_args[0][0]
        self.assertEqual(result["Status"], "Success")
        self.assertEqual(result["ContentType"], "text/html")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        doc_preview_html({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestDocJobSubmit(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_minimal(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_create_doc_job.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "doc.pdf", "output_key": "out/doc"}
        doc_job_submit(args, PG)
        kw = client.ci_create_doc_job.call_args[1]
        self.assertEqual(kw["TgtType"], "png")
        self.assertEqual(kw["OutputBucket"], "b")

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_all_params(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_create_doc_job.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "doc.xlsx", "output_key": "out/",
                "output_bucket": "ob", "src_type": "xlsx", "tgt_type": "pdf",
                "start_page": "1", "end_page": "10", "sheet_id": "2"}
        doc_job_submit(args, PG)
        kw = client.ci_create_doc_job.call_args[1]
        self.assertEqual(kw["SrcType"], "xlsx")
        self.assertEqual(kw["TgtType"], "pdf")
        self.assertEqual(kw["StartPage"], 1)
        self.assertEqual(kw["EndPage"], 10)
        self.assertEqual(kw["SheetId"], 2)
        self.assertEqual(kw["OutputBucket"], "ob")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        doc_job_submit({"bucket": "b", "key": "k", "output_key": "o"}, PG)
        mock_handle.assert_called_once()


class TestDocJobQuery(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_get_doc_job.return_value = {}
        mock_init.return_value = client
        doc_job_query({"bucket": "b", "job_id": "j"}, PG)
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        doc_job_query({"bucket": "b", "job_id": "j"}, PG)
        mock_handle.assert_called_once()


class TestDocJobList(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_minimal(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_list_doc_jobs.return_value = {}
        mock_init.return_value = client
        doc_job_list({"bucket": "b"}, PG)

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_all_params(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_list_doc_jobs.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "size": "20", "page": "2", "status": "Success"}
        doc_job_list(args, PG)
        kw = client.ci_list_doc_jobs.call_args[1]
        self.assertEqual(kw["Size"], 20)
        self.assertEqual(kw["Page"], 2)
        self.assertEqual(kw["States"], "Success")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        doc_job_list({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


if __name__ == "__main__":
    unittest.main()
