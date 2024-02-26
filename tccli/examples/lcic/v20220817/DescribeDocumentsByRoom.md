**Example 1: 获取指定课堂文档**

获取指定课堂文档

Input: 

```
tccli lcic DescribeDocumentsByRoom --cli-unfold-argument  \
    --RoomId 1 \
    --SdkAppId 1234567
```

Output: 
```
{
    "Response": {
        "Documents": [
            {
                "DocumentId": "Klpwo90M",
                "DocumentUrl": "https://www.klpa.com",
                "DocumentName": "llppqom",
                "Owner": "abc",
                "SdkAppId": 1,
                "Permission": 1,
                "TranscodeResult": "1909",
                "TranscodeType": 1,
                "TranscodeProgress": 1,
                "TranscodeState": 1,
                "TranscodeInfo": "abc",
                "DocumentType": "abc",
                "DocumentSize": 1,
                "UpdateTime": 1,
                "Pages": 1,
                "Width": 1,
                "Height": 1,
                "Cover": "abc",
                "Preview": "abc"
            }
        ],
        "Total": 1,
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

