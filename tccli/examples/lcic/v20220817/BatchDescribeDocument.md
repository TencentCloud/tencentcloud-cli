**Example 1: 示例**

批量获取文档详情

Input: 

```
tccli lcic BatchDescribeDocument --cli-unfold-argument  \
    --SdkAppId 1 \
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
        "Total": 0,
        "Documents": [
            {
                "DocumentId": "abc",
                "DocumentUrl": "abc",
                "DocumentName": "abc",
                "Owner": "abc",
                "SdkAppId": 1,
                "Permission": 1,
                "TranscodeResult": "abc",
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
        "RequestId": "abc"
    }
}
```

