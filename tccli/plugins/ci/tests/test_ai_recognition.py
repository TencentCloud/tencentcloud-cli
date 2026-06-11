# -*- coding: utf-8 -*-
"""ai_recognition 模块单元测试

覆盖目标：
- _ci_process_stream: dict 响应(错误) / stream+local_path / stream 无 local_path
- _ci_process_json: 正常
- 20 个 AI 公开函数：key 缺失 / 成功 / 异常 / 可选参数分支
"""
import json
import os
import unittest
from unittest.mock import patch, MagicMock

from tccli.plugins.ci.ai_recognition import (
    _ci_process_stream,
    _ci_process_json,
    ai_image_coloring,
    ai_enhance_image,
    ai_image_crop,
    ai_image_repair,
    ai_detect_face,
    ai_face_effect,
    ai_body_recognition,
    ai_id_card_ocr,
    ai_license_rec,
    ai_game_rec,
    ocr_process,
    detect_label,
    detect_car,
    assess_quality,
    qrcode_detect,
    qrcode_generate,
    super_resolution,
    goods_matting,
    pic_matting,
    portrait_matting,
)

MOCK_INIT = "tccli.plugins.ci.ai_recognition.init_cos_client"
MOCK_PRINT = "tccli.plugins.ci.ai_recognition.print_result"
MOCK_HANDLE = "tccli.plugins.ci.ai_recognition.handle_cos_error"
MOCK_SAVE = "tccli.plugins.ci.ai_recognition.save_response_to_file"

PG = {"secretId": "AK", "secretKey": "SK", "region": "ap-guangzhou"}


class TestCiProcessStream(unittest.TestCase):
    """_ci_process_stream 私有方法测试"""

    def test_dict_response(self):
        """ci_process 返回 dict (错误响应)"""
        client = MagicMock()
        client.ci_process.return_value = ({"h": "v"}, {"Error": "bad"})

        result, headers = _ci_process_stream(client, "b", "k", "AIImageColoring")
        self.assertEqual(result, {"Error": "bad"})

    @patch(MOCK_SAVE, return_value=1024)
    def test_stream_with_local_path(self, mock_save):
        """stream 响应 + 指定 local_path"""
        client = MagicMock()
        stream_body = MagicMock()
        stream_body.__class__ = type("StreamLike", (), {})
        client.ci_process.return_value = ({"h": "v"}, stream_body)

        result, headers = _ci_process_stream(client, "b", "k", "AIImageColoring",
                                              local_path="/tmp/out.jpg")
        self.assertEqual(result["Status"], "Success")
        self.assertEqual(result["ContentLength"], "1024")

    def test_stream_without_local_path(self):
        """stream 响应 + 无 local_path"""
        client = MagicMock()
        stream_body = MagicMock()
        stream_body.__class__ = type("StreamLike", (), {})
        client.ci_process.return_value = ({"h": "v"}, stream_body)

        result, headers = _ci_process_stream(client, "b", "k", "AIImageColoring")
        self.assertEqual(result["Status"], "Success")
        self.assertIn("no local_path", result["Message"])


class TestCiProcessJson(unittest.TestCase):
    """_ci_process_json 私有方法测试"""

    def test_normal(self):
        client = MagicMock()
        client.ci_process.return_value = ({"h": "v"}, {"data": "ok"})
        result, headers = _ci_process_json(client, "b", "k", "DetectFace")
        self.assertEqual(result, {"data": "ok"})
        self.assertEqual(headers, {"h": "v"})

    def test_with_params(self):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"result": 1})
        result, _ = _ci_process_json(client, "b", "k", "OCR", {"lang": "zh"})
        self.assertEqual(result, {"result": 1})
        client.ci_process.assert_called_once_with(
            Bucket="b", Key="k", CiProcess="OCR", Params={"lang": "zh"}, NeedHeader=True)


# ---------------------------------------------------------------------------
# 辅助：构造通用的 stream 测试 + json 测试
# ---------------------------------------------------------------------------

def _make_stream_test(func_name, func, required_args, optional_args=None):
    """为返回 stream 的 AI 函数生成测试方法"""

    class StreamTests(unittest.TestCase):
        @patch(MOCK_PRINT)
        @patch(MOCK_INIT)
        def test_success(self, mock_init, mock_print):
            client = MagicMock()
            client.ci_process.return_value = ({"h": "v"}, {"Error": "bad"})
            mock_init.return_value = client
            args = {**required_args}
            func(args, PG)
            mock_print.assert_called_once()

        @patch(MOCK_HANDLE)
        @patch(MOCK_INIT)
        def test_error(self, mock_init, mock_handle):
            mock_init.side_effect = Exception("err")
            func({**required_args}, PG)
            mock_handle.assert_called_once()

        @patch(MOCK_HANDLE)
        @patch(MOCK_INIT)
        def test_missing_key(self, mock_init, mock_handle):
            mock_init.return_value = MagicMock()
            args = {k: v for k, v in required_args.items() if k != "key"}
            func(args, PG)
            mock_handle.assert_called_once()
            err = mock_handle.call_args[0][0]
            self.assertIsInstance(err, ValueError)

    StreamTests.__name__ = f"Test_{func_name}"
    StreamTests.__qualname__ = f"Test_{func_name}"
    return StreamTests


def _make_json_test(func_name, func, required_args):
    """为返回 JSON 的 AI 函数生成测试方法"""

    class JsonTests(unittest.TestCase):
        @patch(MOCK_PRINT)
        @patch(MOCK_INIT)
        def test_success(self, mock_init, mock_print):
            client = MagicMock()
            client.ci_process.return_value = ({"h": "v"}, {"result": "ok"})
            mock_init.return_value = client
            func({**required_args}, PG)
            mock_print.assert_called_once()

        @patch(MOCK_HANDLE)
        @patch(MOCK_INIT)
        def test_error(self, mock_init, mock_handle):
            mock_init.side_effect = Exception("err")
            func({**required_args}, PG)
            mock_handle.assert_called_once()

        @patch(MOCK_HANDLE)
        @patch(MOCK_INIT)
        def test_missing_key(self, mock_init, mock_handle):
            mock_init.return_value = MagicMock()
            args = {k: v for k, v in required_args.items() if k != "key"}
            func(args, PG)
            mock_handle.assert_called_once()

    JsonTests.__name__ = f"Test_{func_name}"
    JsonTests.__qualname__ = f"Test_{func_name}"
    return JsonTests


# ---------------------------------------------------------------------------
# 具体测试类
# ---------------------------------------------------------------------------

class TestAiImageColoring(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "url": "http://example.com/img.jpg"}
        ai_image_coloring(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertIn("detect-url", params)

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success_with_local_path(self, mock_init, mock_print):
        client = MagicMock()
        stream = MagicMock()
        stream.__class__ = type("S", (), {})
        client.ci_process.return_value = ({}, stream)
        mock_init.return_value = client
        with patch(MOCK_SAVE, return_value=100):
            args = {"bucket": "b", "key": "k", "local_path": "/tmp/out.jpg"}
            ai_image_coloring(args, PG)
            mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        ai_image_coloring({"bucket": "b"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        ai_image_coloring({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestAiEnhanceImage(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_all_params(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "denoise": "3", "sharpen": "5", "url": "http://x.com/i.jpg"}
        ai_enhance_image(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertEqual(params["denoise"], "3")
        self.assertEqual(params["sharpen"], "5")
        self.assertIn("detect-url", params)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        ai_enhance_image({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestAiImageCrop(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_fixed(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "width": "100", "height": "100", "fixed": "1", "url": "http://x.com"}
        ai_image_crop(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertEqual(params["fixed"], "1")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        ai_image_crop({"bucket": "b", "width": "100", "height": "100"}, PG)
        mock_handle.assert_called_once()


class TestAiImageRepair(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_mask_key(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "mask_key": "mask.jpg"}
        ai_image_repair(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertEqual(params["MaskPic"], "mask.jpg")

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_mask_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "mask_url": "http://mask.com/m.jpg"}
        ai_image_repair(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertEqual(params["MaskPic"], "http://mask.com/m.jpg")

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_no_mask(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k"}
        ai_image_repair(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertNotIn("MaskPic", params)


class TestAiDetectFace(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_max_face_num(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"FaceCount": 2})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "max_face_num": "5"}
        ai_detect_face(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertEqual(params["max-face-num"], "5")


class TestAiFaceEffect(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "effect_type": "aging", "url": "http://x.com"}
        ai_face_effect(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertEqual(params["type"], "aging")
        self.assertIn("detect-url", params)


class TestAiBodyRecognition(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Bodies": []})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "url": "http://x.com"}
        ai_body_recognition(args, PG)


class TestAiIdCardOcr(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_card_side(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"IdInfo": {}})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "card_side": "FRONT", "url": "http://x.com"}
        ai_id_card_ocr(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertEqual(params["CardSide"], "FRONT")


class TestAiLicenseRec(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_card_type(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"License": {}})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "card_type": "motor", "url": "http://x.com"}
        ai_license_rec(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertEqual(params["CardType"], "motor")


class TestAiGameRec(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"GameInfo": {}})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k"}
        ai_game_rec(args, PG)
        mock_print.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "url": "http://x.com"}
        ai_game_rec(args, PG)


class TestOcrProcess(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_key(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"TextDetections": []})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k"}
        ocr_process(args, PG)
        mock_print.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url_no_key(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {})
        mock_init.return_value = client
        args = {"bucket": "b", "url": "http://x.com/doc.jpg"}
        ocr_process(args, PG)
        mock_print.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_all_params(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "language_type": "zh-CN",
                "ispdf": "true", "pdf_pagenumber": "1"}
        ocr_process(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertEqual(params["language-type"], "zh-CN")
        self.assertEqual(params["ispdf"], "true")
        self.assertEqual(params["pdf-pagenumber"], "1")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_no_key_no_url(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        args = {"bucket": "b"}
        ocr_process(args, PG)
        mock_handle.assert_called_once()


class TestDetectLabel(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_key(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Labels": []})
        mock_init.return_value = client
        detect_label({"bucket": "b", "key": "k"}, PG)
        mock_print.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {})
        mock_init.return_value = client
        detect_label({"bucket": "b", "url": "http://x.com"}, PG)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_no_key_no_url(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        detect_label({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestDetectCar(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Cars": []})
        mock_init.return_value = client
        detect_car({"bucket": "b", "key": "k"}, PG)
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_no_key_no_url(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        detect_car({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestAssessQuality(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Score": 90})
        mock_init.return_value = client
        assess_quality({"bucket": "b", "key": "k"}, PG)
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_no_key_no_url(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        assess_quality({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestQrcodeDetect(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_cover(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"CodeStatus": 1})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k", "cover": "1"}
        qrcode_detect(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertEqual(params["cover"], "1")

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_no_cover(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {})
        mock_init.return_value = client
        args = {"bucket": "b", "key": "k"}
        qrcode_detect(args, PG)
        params = client.ci_process.call_args[1]["Params"]
        self.assertEqual(params["cover"], "0")

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_no_key_no_url(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        qrcode_detect({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestQrcodeGenerate(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_minimal(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_qrcode_generate.return_value = {"ResultImage": ""}
        mock_init.return_value = client
        args = {"bucket": "b", "text": "hello"}
        qrcode_generate(args, PG)
        mock_print.assert_called_once()

    @patch(MOCK_PRINT)
    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    @patch("os.makedirs")
    @patch(MOCK_INIT)
    def test_with_local_path(self, mock_init, mock_makedirs, mock_open_fn, mock_print):
        """保存二维码图片"""
        import base64
        img_b64 = base64.b64encode(b"fakepng").decode()
        client = MagicMock()
        client.ci_qrcode_generate.return_value = {"ResultImage": img_b64}
        mock_init.return_value = client
        args = {"bucket": "b", "text": "hello", "local_path": "/tmp/qr.png"}
        qrcode_generate(args, PG)
        result = mock_print.call_args[0][0]
        self.assertIn("Output", result)

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_width_mode(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_qrcode_generate.return_value = {}
        mock_init.return_value = client
        args = {"bucket": "b", "text": "t", "width": "200", "mode": "1"}
        qrcode_generate(args, PG)
        call_kwargs = client.ci_qrcode_generate.call_args[1]
        self.assertEqual(call_kwargs["Width"], 200)
        self.assertEqual(call_kwargs["Mode"], 1)

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        qrcode_generate({"bucket": "b", "text": "t"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_local_path_no_result_image(self, mock_init, mock_print):
        """local_path 有但 ResultImage 为空"""
        client = MagicMock()
        client.ci_qrcode_generate.return_value = {"ResultImage": ""}
        mock_init.return_value = client
        args = {"bucket": "b", "text": "t", "local_path": "/tmp/qr.png"}
        qrcode_generate(args, PG)
        # ResultImage 为空，不保存文件
        result = mock_print.call_args[0][0]
        self.assertNotIn("Output", result)


class TestSuperResolution(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        stream = MagicMock()
        stream.__class__ = type("S", (), {})
        client.ci_process.return_value = ({}, stream)
        mock_init.return_value = client
        with patch(MOCK_SAVE, return_value=2048):
            args = {"bucket": "b", "key": "k", "local_path": "/tmp/out.jpg"}
            super_resolution(args, PG)
            mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        super_resolution({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestGoodsMatting(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        goods_matting({"bucket": "b", "key": "k"}, PG)
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        goods_matting({"bucket": "b"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        goods_matting({"bucket": "b", "key": "k", "url": "http://x.com"}, PG)


class TestPicMatting(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        pic_matting({"bucket": "b", "key": "k"}, PG)
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        pic_matting({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestPortraitMatting(unittest.TestCase):
    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_success(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        portrait_matting({"bucket": "b", "key": "k"}, PG)
        mock_print.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        portrait_matting({"bucket": "b"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        portrait_matting({"bucket": "b", "key": "k", "url": "http://x.com"}, PG)


# ---------------------------------------------------------------------------
# 补充：覆盖各函数 error 分支
# ---------------------------------------------------------------------------

class TestAiEnhanceImageError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        ai_enhance_image({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestAiImageCropError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        ai_image_crop({"bucket": "b", "key": "k", "width": "100", "height": "100"}, PG)
        mock_handle.assert_called_once()


class TestAiImageRepairError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        ai_image_repair({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        ai_image_repair({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestAiDetectFaceError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        ai_detect_face({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        ai_detect_face({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestAiFaceEffectError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        ai_face_effect({"bucket": "b", "key": "k", "effect_type": "aging"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        ai_face_effect({"bucket": "b", "effect_type": "aging"}, PG)
        mock_handle.assert_called_once()


class TestAiBodyRecognitionError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        ai_body_recognition({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        ai_body_recognition({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestAiIdCardOcrError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        ai_id_card_ocr({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        ai_id_card_ocr({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestAiLicenseRecError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        ai_license_rec({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        ai_license_rec({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestAiGameRecError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        ai_game_rec({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_missing_key(self, mock_init, mock_handle):
        mock_init.return_value = MagicMock()
        ai_game_rec({"bucket": "b"}, PG)
        mock_handle.assert_called_once()


class TestOcrProcessError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        ocr_process({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestDetectLabelError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        detect_label({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestDetectCarError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        detect_car({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {})
        mock_init.return_value = client
        detect_car({"bucket": "b", "url": "http://x.com"}, PG)


class TestAssessQualityError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        assess_quality({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {})
        mock_init.return_value = client
        assess_quality({"bucket": "b", "url": "http://x.com"}, PG)


class TestQrcodeDetectError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        qrcode_detect({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {})
        mock_init.return_value = client
        qrcode_detect({"bucket": "b", "url": "http://x.com"}, PG)


class TestGoodsMattingError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        goods_matting({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


class TestPicMattingError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        pic_matting({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()

    @patch(MOCK_PRINT)
    @patch(MOCK_INIT)
    def test_with_url(self, mock_init, mock_print):
        client = MagicMock()
        client.ci_process.return_value = ({}, {"Error": "test"})
        mock_init.return_value = client
        pic_matting({"bucket": "b", "key": "k", "url": "http://x.com"}, PG)


class TestPortraitMattingError(unittest.TestCase):
    @patch(MOCK_HANDLE)
    @patch(MOCK_INIT)
    def test_error(self, mock_init, mock_handle):
        mock_init.side_effect = Exception("err")
        portrait_matting({"bucket": "b", "key": "k"}, PG)
        mock_handle.assert_called_once()


if __name__ == "__main__":
    unittest.main()
