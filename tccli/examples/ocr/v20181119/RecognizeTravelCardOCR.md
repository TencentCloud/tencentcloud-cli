**Example 1: 通信行程卡识别示例代码**



Input: 

```
tccli ocr RecognizeTravelCardOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "RiskArea": [
            "xx"
        ],
        "ReachedCity": [
            "xx"
        ],
        "Color": "xx",
        "Telephone": "xx",
        "RequestId": "xx",
        "Time": "XXXX - XX - XX XX: XX: XX"
    }
}
```

