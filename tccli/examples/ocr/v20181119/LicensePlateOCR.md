**Example 1: 车牌识别示例代码**

车牌识别

Input: 

```
tccli ocr LicensePlateOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Color": "蓝",
        "Confidence": 99,
        "LicensePlateInfos": [
            {
                "Color": "蓝",
                "Confidence": 99,
                "Number": "京AF0236",
                "Rect": {
                    "Height": 66,
                    "Width": 135,
                    "X": 426,
                    "Y": 423
                }
            }
        ],
        "Number": "京AF0236",
        "Rect": {
            "Height": 66,
            "Width": 135,
            "X": 426,
            "Y": 423
        },
        "RequestId": "5141467c-0a67-4f7c-b1c5-8147d84681a1"
    }
}
```

