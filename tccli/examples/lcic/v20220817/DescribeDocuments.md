**Example 1: 示例**

批量获取文档信息

Input: 

```
tccli lcic DescribeDocuments --cli-unfold-argument  \
    --SchoolId 1 \
    --Page 0 \
    --Limit 0 \
    --Permission 1 \
    --Owner abc \
    --Keyword abc \
    --DocumentId abc
```

Output: 
```
{
    "Response": {
        "Total": 50,
        "Documents": [
            {
                "DocumentId": "abc",
                "DocumentUrl": "http://www.hfjk.kop.com",
                "DocumentName": "KLOPP",
                "Owner": "abc",
                "SdkAppId": 1,
                "Permission": 1,
                "TranscodeResult": "90920",
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
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

