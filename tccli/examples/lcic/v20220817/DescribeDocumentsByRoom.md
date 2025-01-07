**Example 1: 获取指定课堂文档**

获取指定课堂文档

Input: 

```
tccli lcic DescribeDocumentsByRoom --cli-unfold-argument  \
    --RoomId 2327911 \
    --SdkAppId 342109
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
                "Owner": "Tom",
                "SdkAppId": 36281029,
                "Permission": 1,
                "TranscodeResult": "https://usfhugsjhkdfjhhsjhakjsl.mp4",
                "TranscodeType": 1,
                "TranscodeProgress": 1,
                "TranscodeState": 1,
                "TranscodeInfo": "SUCCESS",
                "DocumentType": "doc",
                "DocumentSize": 1,
                "UpdateTime": 19849018,
                "Pages": 1,
                "Width": 1,
                "Height": 1,
                "Cover": "312",
                "Preview": "1232",
                "Resolution": "",
                "MinScaleResolution": "1280x720"
            }
        ],
        "Total": 1,
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

