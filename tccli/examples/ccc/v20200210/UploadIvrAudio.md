**Example 1: 上传IVR音频文件**



Input: 

```
tccli ccc UploadIvrAudio --cli-unfold-argument  \
    --SdkAppId 140000000 \
    --AudioList.0.CustomFileName 测试文件名 \
    --AudioList.0.AudioUrl http://xxxx.com/a.mp3
```

Output: 
```
{
    "Response": {
        "RequestId": "a",
        "FailedFileList": [],
        "SuccessFileList": [
            {
                "AudioFileName": "business_id_pic5.mp3",
                "CustomFileName": "1231",
                "FileId": 50,
                "Status": 0
            },
            {
                "AudioFileName": "business_id_pic6.mp3",
                "CustomFileName": "4561",
                "FileId": 51,
                "Status": 0
            }
        ]
    }
}
```

