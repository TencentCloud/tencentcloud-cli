**Example 1: 示例**

批量获取文档详情

Input: 

```
tccli lcic BatchDescribeDocument --cli-unfold-argument  \
    --SdkAppId 1 \
    --Page 0 \
    --Limit 0 \
    --Permission 1 \
    --Owner 2kJJBH6G1dfBFUJqXLh0Mg3ELLk \
    --Keyword hello \
    --DocumentId cdockjkj
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Documents": [
            {
                "DocumentId": "dej45ee21",
                "DocumentUrl": "https://www.baidu.com/1.pdf",
                "DocumentName": "docddabc",
                "Owner": "2kJJBH6G1dfBFUJqXLh0Mg3ELLk",
                "SdkAppId": 1,
                "Permission": 1,
                "TranscodeResult": "success",
                "TranscodeType": 1,
                "TranscodeProgress": 1,
                "TranscodeState": 1,
                "TranscodeInfo": "llkjkjiijk",
                "DocumentType": "pdf",
                "DocumentSize": 1,
                "UpdateTime": 1,
                "Pages": 1,
                "Width": 1,
                "Height": 1,
                "Cover": "https://www.baidu.com/1.jpg",
                "Preview": "https://www.baidu.com/preview.jpg",
                "Resolution": "1280*720",
                "MinScaleResolution": "1280*720"
            }
        ],
        "RequestId": "2a117d109a0c533e5ecd37fc221ba7f7"
    }
}
```

