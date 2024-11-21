**Example 1: 查询IVR音频文件列表示例**



Input: 

```
tccli ccc DescribeIvrAudioList --cli-unfold-argument  \
    --SdkAppId 160000000 \
    --CustomFileName 测试文件名 \
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
                "CustomFileName": "测试文件名",
                "AudioFileName": "a.mp3",
                "Status": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

