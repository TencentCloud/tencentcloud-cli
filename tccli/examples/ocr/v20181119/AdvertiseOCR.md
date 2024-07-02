**Example 1: 通用印刷体识别示例代码 [ 前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=AdvertiseOCR)**



Input: 

```
tccli ocr AdvertiseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "TextDetections": [
            {
                "DetectedText": "abc",
                "Confidence": 0,
                "Polygon": [
                    {
                        "X": 0,
                        "Y": 0
                    }
                ],
                "AdvancedInfo": "abc"
            }
        ],
        "ImageSize": {
            "Width": 0,
            "Height": 0
        },
        "RequestId": "abc"
    }
}
```

