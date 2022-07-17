**Example 1: 车牌识别示例代码**



Input: 

```
tccli ocr LicensePlateOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Number": "京N0L9U8",
        "Confidence": 99,
        "Rect": {
            "X": 217,
            "Y": 233,
            "Width": 170,
            "Height": 21
        },
        "Color": "蓝",
        "LicensePlateInfos": [
            {
                "Color": "xx",
                "Confidence": 0,
                "Number": "xx",
                "Rect": {
                    "Y": 0,
                    "X": 0,
                    "Height": 0,
                    "Width": 0
                }
            }
        ],
        "RequestId": "210103d3-db06-4691-abe0-c0853aae606b"
    }
}
```

