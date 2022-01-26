**Example 1: 防疫健康码识别示例代码**



Input: 

```
tccli ocr RecognizeHealthCodeOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Name": "京XX",
        "Time": "XXXX - XX - XX XX: XX: XX",
        "Color": "绿色",
        "RequestId": "210103d3-db06-4691-abe0-c0853aae606b"
    }
}
```

