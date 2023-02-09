**Example 1: 获取指定课堂文档**

获取指定课堂文档

Input: 

```
tccli lcic DescribeDocumentsByRoom --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Documents": [
            {
                "DocumentId": "xx",
                "DocumentUrl": "xx",
                "DocumentName": "xx",
                "Owner": "xx",
                "SdkAppId": 1,
                "Permission": 1,
                "TranscodeResult": "xx",
                "TranscodeType": 1,
                "TranscodeProgress": 1,
                "TranscodeState": 1,
                "TranscodeInfo": "xx",
                "DocumentType": "xx",
                "DocumentSize": 1,
                "UpdateTime": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

