**Example 1: 证照类多图鉴伪识别示例代码**



Input: 

```
tccli ocr VerifyMultiPermit --cli-unfold-argument  \
    --ImageUrlList xx \
    --ImageBase64List xx
```

Output: 
```
{
    "Response": {
        "Confidence": 0.0,
        "Items": [
            {
                "Confidence": 0.0,
                "Name": "xx",
                "Result": "xx"
            }
        ],
        "Image": "xx",
        "Result": "xx",
        "ImagesScore": 0.0,
        "RequestId": "xx"
    }
}
```

