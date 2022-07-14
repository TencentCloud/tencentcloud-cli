**Example 1: RecognizePermanentAccountNumberOCR示例**



Input: 

```
tccli ocr RecognizePermanentAccountNumberOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "WarnInfos": [
            "xx"
        ],
        "Number": "xx",
        "HeadPortrait": "xx",
        "Birthday": "xx",
        "RequestId": "xx",
        "Holder": "xx"
    }
}
```

