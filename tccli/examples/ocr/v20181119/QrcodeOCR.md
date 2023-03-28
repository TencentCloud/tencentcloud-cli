**Example 1: 二维码和条形码识别示例代码  [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=QrcodeOCR)**

二维码和条形码识别

Input: 

```
tccli ocr QrcodeOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "CodeResults": [
            {
                "TypeName": "QR_CODE",
                "Url": "http://baike.baidu.com",
                "Position": {
                    "LeftTop": {
                        "X": 0,
                        "Y": 0
                    },
                    "RightTop": {
                        "X": 380,
                        "Y": 0
                    },
                    "RightBottom": {
                        "X": 380,
                        "Y": 380
                    },
                    "LeftBottom": {
                        "X": 0,
                        "Y": 380
                    }
                }
            }
        ],
        "ImgSize": {
            "Wide": 380,
            "High": 380
        },
        "RequestId": "06c7ba12-ec94-4fd4-be48-239c714f0cf4"
    }
}
```

