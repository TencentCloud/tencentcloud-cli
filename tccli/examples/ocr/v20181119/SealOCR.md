**Example 1: 印章识别示例代码**



Input: 

```
tccli ocr SealOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "SealBody": "上海市宝山区市场监督管理局",
        "Rect": {
            "X": 428,
            "Y": 259,
            "Width": 226,
            "Height": 235
        },
        "OtherTexts": [],
        "RequestId": "98b75826-8ff4-4633-a9bb-9be12043f3f8"
    }
}
```

