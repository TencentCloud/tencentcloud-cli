**Example 1: 查询IVR音频文件列表示例**



Input: 

```
tccli ccc DescribeIvrAudioList --cli-unfold-argument  \
    --SdkAppId 160000000 \
    --CustomFileName abc \
    --PageSize 1 \
    --PageNumber 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "FileInfo": [
            {
                "FileId": 1,
                "CustomFileName": "abc",
                "AudioFileName": "a.mp3",
                "Status": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

