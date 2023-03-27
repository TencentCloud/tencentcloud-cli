**Example 1: 成功**



Input: 

```
tccli tiw DescribeTranscodeSearch --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Keyword 拼音
```

Output: 
```
{
    "Response": {
        "TranscodeTaskSet": [
            {
                "CreateTime": "2020-08-21T16:05:36+08:00",
                "Status": "FINISHED",
                "TaskId": "ggdb2vjdnc3lp0k0ovsb",
                "OriginalFilename": "拼音.pptx",
                "SdkAppId": 1400127140,
                "IsStatic": false,
                "Result": {
                    "ResultUrl": "https://whiteboard-cam-test-1257307760.cos.ap-nanjing.myqcloud.com/doc/ggdb2vjdnc3lp0k0ovsb_tiw/h5/index.html",
                    "Resolution": "960x540",
                    "Title": "拼音.pptx",
                    "Pages": 20,
                    "ThumbnailUrl": "",
                    "ThumbnailResolution": "",
                    "CompressFileUrl": "",
                    "ErrorCode": 0,
                    "ErrorMsg": "ppt convert sucess!"
                }
            }
        ],
        "TotalCount": 1340,
        "RequestId": "bc309eaa-6d64-11e8-a7fe-5254000b4175"
    }
}
```

