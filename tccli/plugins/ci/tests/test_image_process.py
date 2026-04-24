# -*- coding: utf-8 -*-
"""image_process 模块单元测试

覆盖 10 个函数的成功路径、错误路径、以及关键分支：
- image_process: local_path 有/无
- image_process_saveas: objects 为 dict / list
- image_upload_process: savekey 有/无, 本地文件不存在, objects 为 dict / list
- image_info: data 为 bytes / dict
- image_exif_info: bytes / tuple
- image_ave_color: bytes / tuple
- image_inspect: bytes / tuple
- image_style_add/get/delete: 正常/异常
- image_style_get: style_name 有/无, tuple 返回/非 tuple
"""
import json
import os
import unittest
from unittest.mock import patch, MagicMock

from tccli.plugins.ci.image_process import (
    image_process,
    image_process_saveas,
    image_upload_process,
    image_info,
    image_exif_info,
    image_ave_color,
    image_inspect,
    image_style_add,
    image_style_get,
    image_style_delete,
)

MOCK_INIT = "tccli.plugins.ci.image_process.init_cos_client"
MOCK_PRINT = "tccli.plugins.ci.image_process.print_result"
MOCK_HANDLE = "tccli.plugins.ci.image_process.handle_cos_error"

PG = {"secretId": "AK", "secretKey": "SK", "region": "ap-guangzhou"}


class TestImageProcess(unittest.TestCase):
    """image_process 函数测试"""

    @patch(MOCK_PRINT)
    @patch("os.path.getsize", return_value=1024)
    @patch("os.path.exists", return_value=True)
    @patch("os.makedirs")
    @patch(MOCK_INIT)
    def test_success_with_local_path(self, mock_init, mock_makedirs, mock_exists, mock_size, mock_print):
        client = MagicMock()
        client.ci_get_object.return_value = {"Content-Type": "image/jpeg", "x-cos-request-id": "req1"}
        mock_init.return_value = client

        args = {"bucket": "b", "key": "dir/test.jpg", "rule": "imageView2/2/w/800", "local_path": "/tmp/out.jpg"}
        image_process(args, PG)
        client.ci_get_object.assert_called_once()
        mock_print.assert_called_once()

    @patch(MOCK_PRINT)
    @patch("os.path.getsize", return_value=512)
    @patch("os.path.exists", return_value=True)
    @patch(MOCK_INIT)
    def test_success_default_local_path(self, mock_init, mock_exists, mock_size, mock_print):
        """local_path 未指定时使用 basename(key)"""
        client = MagicMock()
        client.ci_get_object.return_value = {"Content-Type": "image/png"}
        mock_init.return_value = client

        args = {"bucket": "b", "key": "test.png", "rule": "imageView2/2/w/800"}
        image_process(args, PG)
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error_handling(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("network error")
        args = {"bucket": "b", "key": "test.jpg", "rule": "imageView2/2/w/800"}
        image_process(args, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_PRINT)
    @patch("os.path.getsize", return_value=0)
    @patch("os.path.exists", return_value=False)
    @patch(MOCK_INIT)
    def test_file_not_exists_after_download(self, mock_init, mock_exists, mock_size, mock_print):
        """下载后文件不存在，ContentLength 为 0"""
        client = MagicMock()
        client.ci_get_object.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "key": "test.jpg", "rule": "r"}
        image_process(args, PG)
        result = mock_print.call_args[0][0]
        self.assertEqual(result["ContentLength"], "0")


class TestImageProcessSaveas(unittest.TestCase):
    """image_process_saveas 函数测试"""

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success_objects_list(self, mock_init, mock_print):
        """ProcessResults.Object 为 list"""
        client = MagicMock()
        resp_headers = {"x-cos-request-id": "req1"}
        data = {
            "OriginalInfo": {"ImageInfo": {"Format": "jpeg", "Width": "800", "Height": "600"}},
            "ProcessResults": {"Object": [{"Key": "out.jpg", "ETag": "etag1", "Format": "jpeg",
                                            "Width": "400", "Height": "300", "Size": "1024", "Quality": "80"}]},
        }
        client.ci_image_process.return_value = (resp_headers, data)
        mock_init.return_value = client

        args = {"bucket": "b", "key": "test.jpg", "rule": "r", "savekey": "out.jpg"}
        image_process_saveas(args, PG)
        mock_print.assert_called_once()
        result = mock_print.call_args[0][0]
        self.assertEqual(len(result["ProcessedImages"]), 1)
        self.assertIn("OriginalImage", result)

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success_objects_dict(self, mock_init, mock_print):
        """ProcessResults.Object 为 dict（单个结果）"""
        client = MagicMock()
        resp_headers = {"x-cos-request-id": "req1"}
        data = {
            "OriginalInfo": {"ImageInfo": {}},
            "ProcessResults": {"Object": {"Key": "out.jpg", "ETag": "e", "Format": "png",
                                           "Width": "400", "Height": "300", "Size": "512", "Quality": "90"}},
        }
        client.ci_image_process.return_value = (resp_headers, data)
        mock_init.return_value = client

        args = {"bucket": "b", "key": "test.jpg", "rule": "r", "savekey": "out.jpg"}
        image_process_saveas(args, PG)
        result = mock_print.call_args[0][0]
        self.assertEqual(len(result["ProcessedImages"]), 1)

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_no_original_info(self, mock_init, mock_print):
        """OriginalInfo.ImageInfo 为空"""
        client = MagicMock()
        client.ci_image_process.return_value = (
            {"x-cos-request-id": "r"},
            {"OriginalInfo": {"ImageInfo": {}}, "ProcessResults": {"Object": []}},
        )
        mock_init.return_value = client

        args = {"bucket": "b", "key": "t.jpg", "rule": "r", "savekey": "o.jpg"}
        image_process_saveas(args, PG)
        result = mock_print.call_args[0][0]
        self.assertNotIn("OriginalImage", result)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        image_process_saveas({"bucket": "b", "key": "k", "rule": "r", "savekey": "s"}, PG)
        mock_handle.assert_called_once()


class TestImageUploadProcess(unittest.TestCase):
    """image_upload_process 函数测试"""

    @patch(MOCK_PRINT)
    @patch("os.path.isfile", return_value=True)
    @patch(MOCK_INIT)
    def test_success_with_savekey(self, mock_init, mock_isfile, mock_print):
        """指定 savekey"""
        client = MagicMock()
        client.ci_put_object_from_local_file.return_value = (
            {"x-cos-request-id": "r"},
            {"OriginalInfo": {"ImageInfo": {"Format": "png", "Width": "100", "Height": "100"}},
             "ProcessResults": {"Object": []}},
        )
        mock_init.return_value = client

        args = {"bucket": "b", "local": "/tmp/test.jpg", "key": "test.jpg",
                "rule": "r", "savekey": "out.jpg"}
        image_upload_process(args, PG)
        mock_print.assert_called_once()

    @patch(MOCK_PRINT)
    @patch("os.path.isfile", return_value=True)
    @patch(MOCK_INIT)
    def test_success_default_savekey(self, mock_init, mock_isfile, mock_print):
        """savekey 未指定时使用 key"""
        client = MagicMock()
        client.ci_put_object_from_local_file.return_value = (
            {"x-cos-request-id": "r"},
            {"OriginalInfo": {"ImageInfo": {}}, "ProcessResults": {"Object": []}},
        )
        mock_init.return_value = client

        args = {"bucket": "b", "local": "/tmp/test.jpg", "key": "test.jpg", "rule": "r"}
        image_upload_process(args, PG)
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch("os.path.isfile", return_value=False)
    @patch(MOCK_INIT)
    def test_file_not_found(self, mock_init, mock_isfile, mock_handle):
        """本地文件不存在"""
        mock_init.return_value = MagicMock()
        args = {"bucket": "b", "local": "/nonexist.jpg", "key": "k", "rule": "r"}
        image_upload_process(args, PG)
        mock_handle.assert_called_once()
        err = mock_handle.call_args[0][0]
        self.assertIsInstance(err, FileNotFoundError)

    @patch(MOCK_PRINT)
    @patch("os.path.isfile", return_value=True)
    @patch(MOCK_INIT)
    def test_objects_dict(self, mock_init, mock_isfile, mock_print):
        """Object 为 dict"""
        client = MagicMock()
        client.ci_put_object_from_local_file.return_value = (
            {}, {"OriginalInfo": {"ImageInfo": {}},
                 "ProcessResults": {"Object": {"Key": "k", "ETag": "e", "Format": "f",
                                                "Width": "w", "Height": "h", "Size": "s", "Quality": "q"}}},
        )
        mock_init.return_value = client
        args = {"bucket": "b", "local": "/tmp/t.jpg", "key": "k", "rule": "r", "savekey": "s"}
        image_upload_process(args, PG)
        result = mock_print.call_args[0][0]
        self.assertEqual(len(result["ProcessedImages"]), 1)


class TestImageInfo(unittest.TestCase):
    """image_info 函数测试"""

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success_dict(self, mock_init, mock_print):
        """data 返回为 dict"""
        client = MagicMock()
        client.ci_get_image_info.return_value = ({"x-ci-request-id": "r"}, {"format": "png"})
        mock_init.return_value = client

        image_info({"bucket": "b", "key": "k"}, PG)
        mock_print.assert_called_once_with({"format": "png"}, {"x-ci-request-id": "r"})

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success_bytes(self, mock_init, mock_print):
        """data 返回为 bytes"""
        client = MagicMock()
        client.ci_get_image_info.return_value = (
            {"x-ci-request-id": "r"},
            json.dumps({"format": "jpeg"}).encode(),
        )
        mock_init.return_value = client

        image_info({"bucket": "b", "key": "k"}, PG)
        mock_print.assert_called_once()
        data = mock_print.call_args[0][0]
        self.assertEqual(data["format"], "jpeg")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        image_info({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestImageExifInfo(unittest.TestCase):
    """image_exif_info 函数测试"""

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_bytes_response(self, mock_init, mock_print):
        """SDK 返回 bytes"""
        client = MagicMock()
        client.ci_get_image_exif_info.return_value = json.dumps({"exif": "data"}).encode()
        mock_init.return_value = client

        image_exif_info({"bucket": "b", "key": "k"}, PG)
        mock_print.assert_called_once()
        data = mock_print.call_args[0][0]
        self.assertEqual(data["exif"], "data")

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_tuple_response_bytes_data(self, mock_init, mock_print):
        """SDK 返回 (headers, bytes_data) 元组"""
        client = MagicMock()
        client.ci_get_image_exif_info.return_value = (
            {"x-ci-request-id": "r"},
            json.dumps({"exif": "info"}).encode(),
        )
        mock_init.return_value = client

        image_exif_info({"bucket": "b", "key": "k"}, PG)
        mock_print.assert_called_once()
        data = mock_print.call_args[0][0]
        self.assertEqual(data["exif"], "info")

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_tuple_response_dict_data(self, mock_init, mock_print):
        """SDK 返回 (headers, dict_data) 元组"""
        client = MagicMock()
        client.ci_get_image_exif_info.return_value = (
            {"x-ci-request-id": "r"},
            {"exif": "dict_data"},
        )
        mock_init.return_value = client

        image_exif_info({"bucket": "b", "key": "k"}, PG)
        data = mock_print.call_args[0][0]
        self.assertEqual(data["exif"], "dict_data")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        image_exif_info({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestImageAveColor(unittest.TestCase):
    """image_ave_color 函数测试"""

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_bytes_response(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_get_image_ave_info.return_value = json.dumps({"RGB": "0x123456"}).encode()
        mock_init.return_value = client
        image_ave_color({"bucket": "b", "key": "k"}, PG)
        data = mock_print.call_args[0][0]
        self.assertEqual(data["RGB"], "0x123456")

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_tuple_response(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_get_image_ave_info.return_value = (
            {"x-ci-request-id": "r"},
            json.dumps({"RGB": "0xABCDEF"}).encode(),
        )
        mock_init.return_value = client
        image_ave_color({"bucket": "b", "key": "k"}, PG)
        data = mock_print.call_args[0][0]
        self.assertEqual(data["RGB"], "0xABCDEF")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        image_ave_color({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestImageInspect(unittest.TestCase):
    """image_inspect 异常图片检测函数测试"""

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_bytes_response_normal_image(self, mock_init, mock_print):
        """正常图片 - SDK 返回 bytes"""
        client = MagicMock()
        client.ci_image_inspect.return_value = json.dumps({
            "picSize": 158421,
            "picType": "jpeg",
            "suspicious": False,
        }).encode()
        mock_init.return_value = client
        image_inspect({"bucket": "b", "key": "k"}, PG)
        data = mock_print.call_args[0][0]
        self.assertEqual(data["picSize"], 158421)
        self.assertEqual(data["picType"], "jpeg")
        self.assertFalse(data["suspicious"])

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_tuple_response_suspicious_image(self, mock_init, mock_print):
        """可疑图片 - SDK 返回 (headers, bytes_data) 元组"""
        client = MagicMock()
        client.ci_image_inspect.return_value = (
            {"x-ci-request-id": "r"},
            json.dumps({
                "picSize": 1048576,
                "picType": "png",
                "suspicious": True,
                "suspiciousBeginByte": "524288",
                "suspiciousEndByte": "1048575",
                "suspiciousSize": "524288",
                "suspiciousType": "MPEG-TS",
            }).encode(),
        )
        mock_init.return_value = client
        image_inspect({"bucket": "b", "key": "k"}, PG)
        data = mock_print.call_args[0][0]
        self.assertTrue(data["suspicious"])
        self.assertEqual(data["suspiciousType"], "MPEG-TS")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        image_inspect({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestImageStyleAdd(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_put_image_style.return_value = {"x-cos-request-id": "r"}
        mock_init.return_value = client
        args = {"bucket": "b", "style_name": "thumb", "style_body": "imageView2/2/w/200"}
        image_style_add(args, PG)
        client.ci_put_image_style.assert_called_once_with(
            Bucket="b", Request={"StyleName": "thumb", "StyleBody": "imageView2/2/w/200"})
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        image_style_add({"bucket": "b", "style_name": "s", "style_body": "body"}, PG)
        mock_handle.assert_called_once()


class TestImageStyleGet(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_style_name_tuple(self, mock_init, mock_print):
        """指定 style_name，返回 tuple"""
        client = MagicMock()
        client.ci_get_image_style.return_value = (
            {"x-ci-request-id": "r"},
            {"StyleRule": [{"StyleName": "thumb"}]},
        )
        mock_init.return_value = client
        args = {"bucket": "b", "style_name": "thumb"}
        image_style_get(args, PG)
        mock_print.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_without_style_name_non_tuple(self, mock_init, mock_print):
        """不指定 style_name，返回非 tuple"""
        client = MagicMock()
        client.ci_get_image_style.return_value = {"StyleRule": []}
        mock_init.return_value = client
        args = {"bucket": "b"}
        image_style_get(args, PG)
        mock_print.assert_called_once_with({"StyleRule": []}, None)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        image_style_get({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestImageStyleDelete(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_delete_image_style.return_value = {"x-cos-request-id": "r"}
        mock_init.return_value = client
        args = {"bucket": "b", "style_name": "thumb"}
        image_style_delete(args, PG)
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        image_style_delete({"bucket": "b", "style_name": "s"}, PG)
        mock_handle.assert_called_once()


if __name__ == "__main__":
    unittest.main()
