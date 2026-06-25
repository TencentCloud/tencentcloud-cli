# -*- coding: utf-8 -*-
"""ci_helpers 模块单元测试

覆盖目标：
- _load_credential_from_profile: 命令行传入 / 文件加载 / 环境变量 / 缺失报错
- init_cos_client: 正常初始化 + 密钥缺失
- handle_cos_error: CosServiceError / 通用 Exception
- _extract_request_id: 正常 / 空头 / None / 非 dict
- print_result: 带 headers / 不带 headers / data 非 dict
- save_response_to_file: StreamBody / dict+Body(StreamBody) / dict+Body(raw) / bytes / 不支持类型
"""
import json
import os
import sys
import unittest
from unittest.mock import patch, MagicMock, mock_open

from tccli.plugins.ci.ci_helpers import (
    _load_credential_from_profile,
    init_cos_client,
    handle_cos_error,
    _extract_request_id,
    print_result,
    save_response_to_file,
)


class TestLoadCredentialFromProfile(unittest.TestCase):
    """测试 _load_credential_from_profile"""

    def test_already_has_credentials(self):
        """命令行已传入 secretId 和 secretKey，直接返回"""
        pg = {"secretId": "AKIDxxx", "secretKey": "SKxxx"}
        result = _load_credential_from_profile(pg)
        self.assertEqual(result["secretId"], "AKIDxxx")
        self.assertEqual(result["secretKey"], "SKxxx")

    @patch("os.path.isfile", return_value=True)
    @patch("builtins.open", mock_open(read_data='{"secretId":"file_id","secretKey":"file_key","token":"file_token"}'))
    def test_load_from_credential_file(self, mock_isfile):
        """从 credential 文件加载密钥"""
        pg = {"secretId": None, "secretKey": None, "profile": "default"}
        result = _load_credential_from_profile(pg)
        self.assertEqual(result["secretId"], "file_id")
        self.assertEqual(result["secretKey"], "file_key")
        self.assertEqual(result["token"], "file_token")

    @patch("os.path.isfile", return_value=False)
    @patch.dict(os.environ, {
        "TENCENTCLOUD_SECRET_ID": "env_id",
        "TENCENTCLOUD_SECRET_KEY": "env_key",
        "TENCENTCLOUD_TOKEN": "env_token",
    })
    def test_load_from_env_vars(self, mock_isfile):
        """从环境变量加载密钥"""
        pg = {"secretId": None, "secretKey": None, "profile": None, "token": None}
        result = _load_credential_from_profile(pg)
        self.assertEqual(result["secretId"], "env_id")
        self.assertEqual(result["secretKey"], "env_key")
        self.assertEqual(result["token"], "env_token")

    @patch("os.path.isfile", return_value=False)
    @patch.dict(os.environ, {}, clear=True)
    def test_missing_credentials_raises(self, mock_isfile):
        """密钥缺失时抛出 ValueError"""
        pg = {"secretId": None, "secretKey": None, "profile": "default", "token": None}
        with self.assertRaises(ValueError) as ctx:
            _load_credential_from_profile(pg)
        self.assertIn("SecretId and SecretKey is Required", str(ctx.exception))

    @patch("os.path.isfile")
    @patch("builtins.open", mock_open(read_data='invalid json'))
    def test_invalid_json_in_credential_file(self, mock_isfile):
        """credential 文件 JSON 解析失败，降级到环境变量"""
        mock_isfile.return_value = True

        with patch.dict(os.environ, {
            "TENCENTCLOUD_SECRET_ID": "env_id",
            "TENCENTCLOUD_SECRET_KEY": "env_key",
        }):
            pg = {"secretId": None, "secretKey": None, "profile": "default", "token": None}
            result = _load_credential_from_profile(pg)
            self.assertEqual(result["secretId"], "env_id")

    @patch("os.path.isfile")
    @patch("builtins.open")
    def test_load_region_from_configure_file(self, mock_open_func, mock_isfile):
        """从 configure 文件加载 region"""
        cred_data = '{"secretId":"id","secretKey":"key"}'
        conf_data = '{"_sys_param":{"region":"ap-beijing"}}'

        def isfile_side_effect(path):
            return True

        mock_isfile.side_effect = isfile_side_effect

        # 第一次 open 返回 cred, 第二次返回 conf
        mock_open_func.side_effect = [
            mock_open(read_data=cred_data)(),
            mock_open(read_data=conf_data)(),
        ]

        pg = {"secretId": None, "secretKey": None, "profile": "default", "token": None, "region": None}
        result = _load_credential_from_profile(pg)
        self.assertEqual(result["region"], "ap-beijing")

    @patch("os.path.isfile")
    @patch("builtins.open")
    def test_configure_file_invalid_json(self, mock_open_func, mock_isfile):
        """configure 文件 JSON 无效时跳过 region 加载"""
        cred_data = '{"secretId":"id","secretKey":"key"}'
        conf_data = 'not json'

        mock_isfile.return_value = True
        mock_open_func.side_effect = [
            mock_open(read_data=cred_data)(),
            mock_open(read_data=conf_data)(),
        ]

        pg = {"secretId": None, "secretKey": None, "profile": "default", "token": None, "region": None}
        result = _load_credential_from_profile(pg)
        # region 未被设置
        self.assertIsNone(result.get("region"))

    @patch("os.path.isfile", return_value=False)
    @patch.dict(os.environ, {
        "TENCENTCLOUD_SECRET_ID": "env_id",
        "TENCENTCLOUD_SECRET_KEY": "env_key",
        "TENCENTCLOUD_REGION": "ap-shanghai",
        "TCCLI_PROFILE": "myprofile",
    })
    def test_env_region_and_profile(self, mock_isfile):
        """使用环境变量的 TCCLI_PROFILE 和 TENCENTCLOUD_REGION"""
        pg = {"secretId": None, "secretKey": None, "profile": None, "token": None, "region": None}
        # configure 文件不存在，走 env fallback
        result = _load_credential_from_profile(pg)
        self.assertEqual(result["secretId"], "env_id")

    def test_partial_credentials_id_only(self):
        """只有 secretId，缺少 secretKey"""
        with patch("os.path.isfile", return_value=False), \
             patch.dict(os.environ, {}, clear=True):
            pg = {"secretId": "AKIDxxx", "secretKey": None, "profile": "default", "token": None}
            with self.assertRaises(ValueError):
                _load_credential_from_profile(pg)


class TestInitCosClient(unittest.TestCase):
    """测试 init_cos_client"""

    @patch("tccli.plugins.ci.ci_helpers.CosS3Client")
    @patch("tccli.plugins.ci.ci_helpers.CosConfig")
    @patch("tccli.plugins.ci.ci_helpers._load_credential_from_profile")
    def test_normal_init(self, mock_load, mock_config, mock_client_cls):
        """正常初始化 COS 客户端"""
        mock_load.return_value = None
        pg = {
            "secretId": "AKIDxxx",
            "secretKey": "SKxxx",
            "region": "ap-guangzhou",
            "token": None,
            "endpoint": None,
        }
        client = init_cos_client(pg)
        mock_config.assert_called_once_with(
            Region="ap-guangzhou",
            SecretId="AKIDxxx",
            SecretKey="SKxxx",
            Token=None,
            Endpoint=None,
        )
        mock_client_cls.assert_called_once()

    @patch("tccli.plugins.ci.ci_helpers.CosS3Client")
    @patch("tccli.plugins.ci.ci_helpers.CosConfig")
    @patch("tccli.plugins.ci.ci_helpers._load_credential_from_profile")
    def test_default_region(self, mock_load, mock_config, mock_client_cls):
        """region 为空时使用默认值 ap-guangzhou"""
        mock_load.return_value = None
        pg = {"secretId": "AKIDxxx", "secretKey": "SKxxx", "region": None, "token": None, "endpoint": None}
        init_cos_client(pg)
        mock_config.assert_called_once_with(
            Region="ap-guangzhou",
            SecretId="AKIDxxx",
            SecretKey="SKxxx",
            Token=None,
            Endpoint=None,
        )


class TestHandleCosError(unittest.TestCase):
    """测试 handle_cos_error"""

    @patch("sys.exit")
    @patch("sys.stderr")
    def test_cos_service_error(self, mock_stderr, mock_exit):
        """CosServiceError 格式化输出"""
        from qcloud_cos import CosServiceError

        err = MagicMock(spec=CosServiceError)
        err.get_error_code.return_value = "NoSuchKey"
        err.get_error_msg.return_value = "The specified key does not exist"
        err.get_request_id.return_value = "req-123"
        err.get_status_code.return_value = 404
        # 让 isinstance 检查通过
        err.__class__ = CosServiceError

        handle_cos_error(err)
        mock_exit.assert_called_once_with(1)

    @patch("sys.exit")
    @patch("sys.stderr")
    def test_generic_error(self, mock_stderr, mock_exit):
        """通用异常格式化输出"""
        err = ValueError("test error")
        handle_cos_error(err)
        mock_exit.assert_called_once_with(1)


class TestExtractRequestId(unittest.TestCase):
    """测试 _extract_request_id"""

    def test_both_ids(self):
        """包含 ci 和 cos 两个 request id"""
        headers = {"x-ci-request-id": "ci-123", "x-cos-request-id": "cos-456"}
        result = _extract_request_id(headers)
        self.assertEqual(result["RequestId"], "ci-123")
        self.assertEqual(result["CosRequestId"], "cos-456")

    def test_only_ci_id(self):
        """只有 ci request id"""
        headers = {"x-ci-request-id": "ci-123"}
        result = _extract_request_id(headers)
        self.assertEqual(result["RequestId"], "ci-123")
        self.assertNotIn("CosRequestId", result)

    def test_only_cos_id(self):
        """只有 cos request id"""
        headers = {"x-cos-request-id": "cos-456"}
        result = _extract_request_id(headers)
        self.assertNotIn("RequestId", result)
        self.assertEqual(result["CosRequestId"], "cos-456")

    def test_no_ids(self):
        """header 中没有 request id"""
        headers = {"Content-Type": "application/json"}
        result = _extract_request_id(headers)
        self.assertEqual(result, {})

    def test_none_headers(self):
        """headers 为 None"""
        result = _extract_request_id(None)
        self.assertEqual(result, {})

    def test_empty_headers(self):
        """headers 为空 dict"""
        result = _extract_request_id({})
        self.assertEqual(result, {})

    def test_non_dict_headers(self):
        """headers 不是 dict"""
        result = _extract_request_id("not a dict")
        self.assertEqual(result, {})


class TestPrintResult(unittest.TestCase):
    """测试 print_result"""

    @patch("builtins.print")
    def test_print_dict_with_headers(self, mock_print):
        """dict 输出时注入 RequestId"""
        data = {"key": "value"}
        headers = {"x-ci-request-id": "ci-123"}
        print_result(data, headers)
        output = mock_print.call_args[0][0]
        parsed = json.loads(output)
        self.assertEqual(parsed["RequestId"], "ci-123")
        self.assertEqual(parsed["key"], "value")

    @patch("builtins.print")
    def test_print_dict_without_headers(self, mock_print):
        """dict 输出不带 headers"""
        data = {"key": "value"}
        print_result(data)
        output = mock_print.call_args[0][0]
        parsed = json.loads(output)
        self.assertEqual(parsed, {"key": "value"})

    @patch("builtins.print")
    def test_print_list_data(self, mock_print):
        """list 输出不注入 RequestId"""
        data = [{"item": 1}]
        headers = {"x-ci-request-id": "ci-123"}
        print_result(data, headers)
        output = mock_print.call_args[0][0]
        parsed = json.loads(output)
        self.assertEqual(parsed, [{"item": 1}])

    @patch("builtins.print")
    def test_print_dict_with_empty_req_ids(self, mock_print):
        """headers 没有 request id 时不注入"""
        data = {"key": "value"}
        headers = {"Content-Type": "application/json"}
        print_result(data, headers)
        output = mock_print.call_args[0][0]
        parsed = json.loads(output)
        self.assertNotIn("RequestId", parsed)


class TestSaveResponseToFile(unittest.TestCase):
    """测试 save_response_to_file"""

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_stream_body_response(self, mopen, mock_makedirs):
        """StreamBody 直接响应"""
        from qcloud_cos.cos_client import StreamBody

        mock_stream_body = MagicMock(spec=StreamBody)
        mock_stream_body.__class__ = StreamBody
        mock_stream_body.get_stream.return_value = [b"chunk1", b"chunk2"]

        total = save_response_to_file(mock_stream_body, "/tmp/test/output.jpg")
        self.assertEqual(total, 12)
        mopen.assert_called_once_with("/tmp/test/output.jpg", "wb")

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_dict_body_stream_body(self, mopen, mock_makedirs):
        """dict 响应中 Body 为 StreamBody"""
        from qcloud_cos.cos_client import StreamBody

        mock_body = MagicMock(spec=StreamBody)
        mock_body.__class__ = StreamBody
        mock_body.get_stream.return_value = [b"data"]

        response = {"Body": mock_body}
        total = save_response_to_file(response, "output.jpg")
        self.assertEqual(total, 4)

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_dict_body_raw_stream(self, mopen, mock_makedirs):
        """dict 响应中 Body 为普通对象（使用 get_raw_stream）"""
        mock_raw = MagicMock()
        mock_raw.stream.return_value = [b"raw_chunk"]

        mock_body = MagicMock()
        mock_body.get_raw_stream.return_value = mock_raw
        # 确保不被识别为 StreamBody
        mock_body.__class__ = type("FakeBody", (), {})

        response = {"Body": mock_body}
        total = save_response_to_file(response, "output.jpg")
        self.assertEqual(total, 9)

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_bytes_response(self, mopen, mock_makedirs):
        """bytes 响应直接写入"""
        response = b"binary_data_here"
        total = save_response_to_file(response, "output.jpg")
        self.assertEqual(total, 16)

    def test_unsupported_response_type(self):
        """不支持的响应类型抛出 ValueError"""
        with self.assertRaises(ValueError) as ctx:
            save_response_to_file(12345, "/tmp/test.txt")
        self.assertIn("Unsupported response type", str(ctx.exception))

    @patch("os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_no_output_dir(self, mopen, mock_makedirs):
        """输出路径没有目录部分"""
        response = b"data"
        save_response_to_file(response, "output.jpg")
        mock_makedirs.assert_not_called()


if __name__ == "__main__":
    unittest.main()
