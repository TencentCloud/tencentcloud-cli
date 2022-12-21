**Example 1: 健康码识别示例代码**



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
        "Time": "XX - XX XX: XX: XX",
        "Color": "绿色",
        "TestingResult": "48小时阴性",
        "TestingInterval": "xx",
        "TestingTime": "xx",
        "IDNumber": "xx",
        "Vaccination": "xx",
        "SpotName": "xx",
        "VaccinationTime": "xx",
        "RequestId": "210103d3-db06-4691-abe0-c0853aae606b"
    }
}
```

