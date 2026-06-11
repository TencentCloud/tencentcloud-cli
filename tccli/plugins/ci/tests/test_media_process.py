# -*- coding: utf-8 -*-
"""media_process 模块单元测试

覆盖目标：
- video_snapshot: 可选参数全覆盖 (width/height/mode/rotate/format/local_path)
- _xml_to_dict: 叶子节点 / 非叶子 / 同名多节点 / 命名空间
- media_info: 正常
- media_job_submit: operation 有/无, output_key 有/无, queue_id/callback
- media_job_query: 正常
- media_job_list: 可选参数全覆盖
- media_job_cancel: 正常
- 所有函数的异常处理
"""
import json
import os
import unittest
import xml.etree.ElementTree as ET
from unittest.mock import patch, MagicMock

from tccli.plugins.ci.media_process import (
    video_snapshot,
    _xml_to_dict,
    media_info,
    media_job_submit,
    media_job_query,
    media_job_list,
    media_job_cancel,
)

MOCK_INIT = "tccli.plugins.ci.media_process.init_cos_client"
MOCK_PRINT = "tccli.plugins.ci.media_process.print_result"
MOCK_HANDLE = "tccli.plugins.ci.media_process.handle_cos_error"
MOCK_SAVE = "tccli.plugins.ci.media_process.save_response_to_file"

PG = {"secretId": "AK", "secretKey": "SK", "region": "ap-guangzhou"}


class TestXmlToDict(unittest.TestCase):
    """_xml_to_dict 函数测试"""

    def test_simple_leaf(self):
        xml_str = "<Root><Name>test</Name><Size>100</Size></Root>"
        root = ET.fromstring(xml_str)
        result = _xml_to_dict(root)
        self.assertEqual(result, {"Name": "test", "Size": "100"})

    def test_nested(self):
        xml_str = "<Root><Parent><Child>value</Child></Parent></Root>"
        root = ET.fromstring(xml_str)
        result = _xml_to_dict(root)
        self.assertEqual(result, {"Parent": {"Child": "value"}})

    def test_multiple_same_tags(self):
        xml_str = "<Root><Item>a</Item><Item>b</Item><Item>c</Item></Root>"
        root = ET.fromstring(xml_str)
        result = _xml_to_dict(root)
        self.assertEqual(result, {"Item": ["a", "b", "c"]})

    def test_namespace(self):
        xml_str = '<Root xmlns:ns="http://example.com"><ns:Name>test</ns:Name></Root>'
        root = ET.fromstring(xml_str)
        result = _xml_to_dict(root)
        self.assertEqual(result, {"Name": "test"})

    def test_empty_text(self):
        xml_str = "<Root><Empty></Empty></Root>"
        root = ET.fromstring(xml_str)
        result = _xml_to_dict(root)
        self.assertEqual(result, {"Empty": ""})

    def test_empty_root(self):
        xml_str = "<Root></Root>"
        root = ET.fromstring(xml_str)
        result = _xml_to_dict(root)
        self.assertEqual(result, {})

    def test_two_same_then_third(self):
        """第一个元素为值，第二个相同 tag 时转为 list"""
        xml_str = "<Root><Tag>a</Tag><Tag>b</Tag></Root>"
        root = ET.fromstring(xml_str)
        result = _xml_to_dict(root)
        self.assertIsInstance(result["Tag"], list)
        self.assertEqual(result["Tag"], ["a", "b"])


class TestVideoSnapshot(unittest.TestCase):
    """video_snapshot 函数测试"""

    @patch(MOCK_PRINT)
    @patch(MOCK_SAVE, return_value=2048)
    @patch(MOCK_INIT)
    def test_success_minimal(self, mock_init, mock_save, mock_print):
        """最小参数"""
        client = MagicMock()
        client.get_snapshot.return_value = {"Content-Type": "image/jpeg"}
        mock_init.return_value = client

        args = {"bucket": "b", "key": "video.mp4", "snapshot_time": "1.5"}
        video_snapshot(args, PG)
        client.get_snapshot.assert_called_once()
        mock_save.assert_called_once()
        mock_print.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_SAVE, return_value=4096)
    @patch(MOCK_INIT)
    def test_success_all_params(self, mock_init, mock_save, mock_print):
        """全部可选参数"""
        client = MagicMock()
        client.get_snapshot.return_value = {"Content-Type": "image/png"}
        mock_init.return_value = client

        args = {
            "bucket": "b", "key": "dir/video.mp4", "snapshot_time": "3",
            "width": "640", "height": "480", "format": "png",
            "mode": "exactframe", "rotate": "auto",
            "local_path": "/tmp/snap.png",
        }
        video_snapshot(args, PG)
        call_kwargs = client.get_snapshot.call_args[1]
        self.assertEqual(call_kwargs["Width"], 640)
        self.assertEqual(call_kwargs["Height"], 480)
        self.assertEqual(call_kwargs["Mode"], "exactframe")
        self.assertEqual(call_kwargs["Rotate"], "auto")
        self.assertEqual(call_kwargs["Format"], "png")

    @patch(MOCK_PRINT)
    @patch(MOCK_SAVE, return_value=1024)
    @patch(MOCK_INIT)
    def test_empty_optional_params(self, mock_init, mock_save, mock_print):
        """可选参数为空字符串时不传"""
        client = MagicMock()
        client.get_snapshot.return_value = {}
        mock_init.return_value = client

        args = {
            "bucket": "b", "key": "v.mp4", "snapshot_time": "0",
            "width": "", "height": "", "mode": "", "rotate": "",
        }
        video_snapshot(args, PG)
        call_kwargs = client.get_snapshot.call_args[1]
        self.assertNotIn("Width", call_kwargs)
        self.assertNotIn("Height", call_kwargs)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        video_snapshot({"bucket": "b", "key": "v.mp4", "snapshot_time": "1"}, PG)
        mock_handle.assert_called_once()


class TestMediaInfo(unittest.TestCase):
    """media_info 函数测试"""

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.get_media_info.return_value = {"MediaInfo": {"Format": {"Duration": "60"}}}
        mock_init.return_value = client
        media_info({"bucket": "b", "key": "v.mp4"}, PG)
        mock_print.assert_called_once_with({"MediaInfo": {"Format": {"Duration": "60"}}})

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        media_info({"bucket": "b", "key": "v.mp4"}, PG)
        mock_handle.assert_called_once()


class TestMediaJobSubmit(unittest.TestCase):
    """media_job_submit 函数测试"""

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_minimal(self, mock_init, mock_print):
        """最小参数，无 operation"""
        client = MagicMock()
        client.ci_create_media_jobs.return_value = {"JobsDetail": {"JobId": "j1"}}
        mock_init.return_value = client

        args = {"bucket": "b", "key": "v.mp4", "tag": "Transcode"}
        media_job_submit(args, PG)
        mock_print.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_all_params(self, mock_init, mock_print):
        """全部参数"""
        client = MagicMock()
        client.ci_create_media_jobs.return_value = {"JobsDetail": {}}
        mock_init.return_value = client

        args = {
            "bucket": "b", "key": "v.mp4", "tag": "Transcode",
            "operation": '{"Transcode":{"Container":{"Format":"mp4"}}}',
            "output_key": "out.mp4",
            "output_bucket": "ob",
            "output_region": "ap-beijing",
            "queue_id": "q1",
            "callback": "http://cb.example.com",
        }
        media_job_submit(args, PG)
        call_kwargs = client.ci_create_media_jobs.call_args[1]
        jobs = call_kwargs["Jobs"]
        self.assertIn("QueueId", jobs)
        self.assertIn("CallBack", jobs)
        self.assertEqual(jobs["Operation"]["Output"]["Bucket"], "ob")
        self.assertEqual(jobs["Operation"]["Output"]["Region"], "ap-beijing")

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_output_key_default_bucket(self, mock_init, mock_print):
        """output_key 有但 output_bucket 无时用 bucket"""
        client = MagicMock()
        client.ci_create_media_jobs.return_value = {}
        mock_init.return_value = client

        args = {"bucket": "b", "key": "v.mp4", "tag": "Snapshot", "output_key": "snap.jpg"}
        media_job_submit(args, PG)
        jobs = client.ci_create_media_jobs.call_args[1]["Jobs"]
        self.assertEqual(jobs["Operation"]["Output"]["Bucket"], "b")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        media_job_submit({"bucket": "b", "key": "k", "tag": "T"}, PG)
        mock_handle.assert_called_once()


class TestMediaJobQuery(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_get_media_jobs.return_value = {"JobsDetail": {"State": "Success"}}
        mock_init.return_value = client
        media_job_query({"bucket": "b", "job_id": "j1"}, PG)
        client.ci_get_media_jobs.assert_called_once_with(Bucket="b", JobIDs="j1")
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        media_job_query({"bucket": "b", "job_id": "j1"}, PG)
        mock_handle.assert_called_once()


class TestMediaJobList(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_minimal(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_list_media_jobs.return_value = {"JobsDetail": []}
        mock_init.return_value = client
        media_job_list({"bucket": "b", "tag": "Transcode"}, PG)
        mock_print.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_all_optional_params(self, mock_init, mock_print):
        """全部可选参数"""
        client = MagicMock()
        client.ci_list_media_jobs.return_value = {}
        mock_init.return_value = client

        args = {
            "bucket": "b", "tag": "Transcode",
            "queue_id": "q1", "status": "Success",
            "size": "20", "next_token": "abc",
            "order_by_time": "Desc",
        }
        media_job_list(args, PG)
        call_kwargs = client.ci_list_media_jobs.call_args[1]
        self.assertEqual(call_kwargs["QueueId"], "q1")
        self.assertEqual(call_kwargs["States"], "Success")
        self.assertEqual(call_kwargs["Size"], 20)
        self.assertEqual(call_kwargs["NextToken"], "abc")
        self.assertEqual(call_kwargs["OrderByTime"], "Desc")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        media_job_list({"bucket": "b", "tag": "T"}, PG)
        mock_handle.assert_called_once()


class TestMediaJobCancel(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_cancel_jobs.return_value = {}
        mock_init.return_value = client
        media_job_cancel({"bucket": "b", "job_id": "j1"}, PG)
        client.ci_cancel_jobs.assert_called_once_with(Bucket="b", JobID="j1")
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        media_job_cancel({"bucket": "b", "job_id": "j1"}, PG)
        mock_handle.assert_called_once()


if __name__ == "__main__":
    unittest.main()
