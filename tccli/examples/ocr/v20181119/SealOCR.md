**Example 1: 印章识别示例代码**

印章识别示例代码

Input: 

```
tccli ocr SealOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/document/SealOCR/SealOCR1.png
```

Output: 
```
{
    "Response": {
        "Location": {
            "Height": 98,
            "Width": 98,
            "X": 143,
            "Y": 78
        },
        "OtherTexts": [],
        "RequestId": "442c7c51-9893-4411-9ba0-69747e5424d2",
        "SealBody": "上海市宝山区市场监督管理局",
        "SealInfos": [
            {
                "Location": {
                    "Height": 98,
                    "Width": 98,
                    "X": 143,
                    "Y": 78
                },
                "OtherTexts": [],
                "SealBody": "上海市宝山区市场监督管理局",
                "SealShape": "0"
            }
        ],
        "SealShape": "0"
    }
}
```

