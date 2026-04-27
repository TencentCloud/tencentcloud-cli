# -*- coding: utf-8 -*-
"""auditing 模块单元测试"""
import unittest
from unittest.mock import patch, MagicMock

from tccli.plugins.ci.auditing import (
    _parse_detect_type,
    auditing_image,
    auditing_video_submit, auditing_video_query,
    auditing_audio_submit, auditing_audio_query,
    auditing_text_submit, auditing_text_query,
    auditing_document_submit, auditing_document_query,
    auditing_webpage_submit, auditing_webpage_query,
    auditing_live_submit, auditing_live_cancel,
    auditing_virus_submit, auditing_virus_query,
    auditing_report_badcase,
)

MOCK_INIT = "tccli.plugins.ci.auditing.init_cos_client"
MOCK_PRINT = "tccli.plugins.ci.auditing.print_result"
MOCK_HANDLE = "tccli.plugins.ci.auditing.handle_cos_error"
PG = {"secretId": "AK", "secretKey": "SK", "region": "ap-guangzhou"}


class TestParseDetectType(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(_parse_detect_type(None))

    def test_empty(self):
        self.assertIsNone(_parse_detect_type(""))

    def test_numeric(self):
        self.assertEqual(_parse_detect_type("15"), 15)

    def test_single_name(self):
        self.assertEqual(_parse_detect_type("porn"), 1)

    def test_multiple_comma(self):
        self.assertEqual(_parse_detect_type("porn,terrorist"), 3)

    def test_multiple_pipe(self):
        self.assertEqual(_parse_detect_type("porn|ads"), 9)

    def test_all_types(self):
        self.assertEqual(_parse_detect_type("porn,terrorist,politics,ads"), 15)

    def test_terrorism_alias(self):
        self.assertEqual(_parse_detect_type("terrorism"), 2)

    def test_unknown_returns_none(self):
        self.assertIsNone(_parse_detect_type("unknown"))

    def test_mixed_case(self):
        self.assertEqual(_parse_detect_type("Porn,ADS"), 9)


class TestAuditingImage(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_keys(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_image_batch.return_value = {"JobsDetail": []}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "a.jpg,b.jpg", "detect_type": "porn,ads", "biz_type": "biz1"}
        auditing_image(args, PG)
        kw = client.ci_auditing_image_batch.call_args[1]
        self.assertEqual(len(kw["Input"]), 2)
        self.assertEqual(kw["DetectType"], 9)
        self.assertEqual(kw["BizType"], "biz1")

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_urls(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_image_batch.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "url": "http://a.com, http://b.com"}
        auditing_image(args, PG)
        kw = client.ci_auditing_image_batch.call_args[1]
        self.assertEqual(len(kw["Input"]), 2)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_no_input(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        auditing_image({"bucket": "b"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        auditing_image({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestAuditingVideoSubmit(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_all_params(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_video_submit.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "v.mp4", "url": "http://x.com", "detect_type": "porn",
                "biz_type": "biz", "snapshot_mode": "Interval", "snapshot_count": "10"}
        auditing_video_submit(args, PG)
        kw = client.ci_auditing_video_submit.call_args[1]
        self.assertEqual(kw["DetectType"], 1)
        self.assertEqual(kw["Count"], 10)

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_minimal(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_video_submit.return_value = {}
        mock_init.return_value = client
        auditing_video_submit({"bucket": "b"}, PG)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        auditing_video_submit({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestAuditingVideoQuery(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_video_query.return_value = {}
        mock_init.return_value = client
        auditing_video_query({"bucket": "b", "job_id": "j1"}, PG)
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        auditing_video_query({"bucket": "b", "job_id": "j1"}, PG)
        mock_handle.assert_called_once()


class TestAuditingAudioSubmit(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_all_params(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_audio_submit.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "a.mp3", "url": "http://x.com",
                "detect_type": "15", "biz_type": "b1"}
        auditing_audio_submit(args, PG)
        kw = client.ci_auditing_audio_submit.call_args[1]
        self.assertEqual(kw["DetectType"], 15)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        auditing_audio_submit({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestAuditingAudioQuery(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_audio_query.return_value = {}
        mock_init.return_value = client
        auditing_audio_query({"bucket": "b", "job_id": "j1"}, PG)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        auditing_audio_query({"bucket": "b", "job_id": "j1"}, PG)
        mock_handle.assert_called_once()


class TestAuditingTextSubmit(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_key(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_text_submit.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "text.txt", "detect_type": "porn"}
        auditing_text_submit(args, PG)

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_content_str(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_text_submit.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "content": "测试文本", "biz_type": "biz1"}
        auditing_text_submit(args, PG)
        kw = client.ci_auditing_text_submit.call_args[1]
        self.assertIsInstance(kw["Content"], bytes)

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_content_bytes(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_text_submit.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "content": b"bytes text"}
        auditing_text_submit(args, PG)

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_text_submit.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "url": "http://x.com/t.txt"}
        auditing_text_submit(args, PG)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_no_input(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        auditing_text_submit({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestAuditingTextQuery(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_text_query.return_value = {}
        mock_init.return_value = client
        auditing_text_query({"bucket": "b", "job_id": "j"}, PG)


class TestAuditingDocumentSubmit(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_all(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_document_submit.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "doc.pdf", "url": "http://x.com",
                "doc_type": "pdf", "detect_type": "porn", "biz_type": "b1"}
        auditing_document_submit(args, PG)
        kw = client.ci_auditing_document_submit.call_args[1]
        self.assertEqual(kw["Type"], "pdf")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_no_input(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        auditing_document_submit({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestAuditingDocumentQuery(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_document_query.return_value = {}
        mock_init.return_value = client
        auditing_document_query({"bucket": "b", "job_id": "j"}, PG)


class TestAuditingWebpageSubmit(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_all(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_html_submit.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "url": "http://x.com", "detect_type": "porn", "biz_type": "b1"}
        auditing_webpage_submit(args, PG)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        auditing_webpage_submit({"bucket": "b", "url": "u"}, PG)
        mock_handle.assert_called_once()


class TestAuditingWebpageQuery(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_html_query.return_value = {}
        mock_init.return_value = client
        auditing_webpage_query({"bucket": "b", "job_id": "j"}, PG)


class TestAuditingLiveSubmit(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_all(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_live_video_submit.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "url": "rtmp://x.com", "biz_type": "b", "callback": "http://cb"}
        auditing_live_submit(args, PG)
        kw = client.ci_auditing_live_video_submit.call_args[1]
        self.assertEqual(kw["Callback"], "http://cb")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        auditing_live_submit({"bucket": "b", "url": "u"}, PG)
        mock_handle.assert_called_once()


class TestAuditingLiveCancel(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_live_video_cancle.return_value = {}
        mock_init.return_value = client
        auditing_live_cancel({"bucket": "b", "job_id": "j"}, PG)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        auditing_live_cancel({"bucket": "b", "job_id": "j"}, PG)
        mock_handle.assert_called_once()


class TestAuditingVirusSubmit(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_key(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_virus_submit.return_value = {}
        mock_init.return_value = client
        auditing_virus_submit({"bucket": "b", "key": "f.exe"}, PG)

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_virus_submit.return_value = {}
        mock_init.return_value = client
        auditing_virus_submit({"bucket": "b", "url": "http://x.com/f"}, PG)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_no_input(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        auditing_virus_submit({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestAuditingVirusQuery(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_virus_query.return_value = {}
        mock_init.return_value = client
        auditing_virus_query({"bucket": "b", "job_id": "j"}, PG)


class TestAuditingReportBadcase(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_all(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_report_badcase.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "content_type": "1", "label": "Porn",
                "suggestion_label": "Normal", "url": "http://x.com", "text": "test"}
        auditing_report_badcase(args, PG)
        kw = client.ci_auditing_report_badcase.call_args[1]
        self.assertEqual(kw["ContentType"], 1)
        self.assertEqual(kw["SuggestedLabel"], "Normal")
        self.assertEqual(kw["Url"], "http://x.com")
        self.assertEqual(kw["Text"], "test")

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_default_suggestion(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_auditing_report_badcase.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "content_type": "2", "label": "Ads"}
        auditing_report_badcase(args, PG)
        kw = client.ci_auditing_report_badcase.call_args[1]
        self.assertEqual(kw["SuggestedLabel"], "Block")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        auditing_report_badcase({"bucket": "b", "content_type": "1", "label": "L"}, PG)
        mock_handle.assert_called_once()


if __name__ == "__main__":
    unittest.main()
