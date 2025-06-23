**Example 1: 获取某个时间段的视频内容关键字**



Input: 

```
tccli iotexplorer InvokeVideosKeywordsAnalyzer --cli-unfold-argument  \
    --ProductId MVTYMD8YCD \
    --DeviceName dev001 \
    --StartTimeMs 1750158420000 \
    --EndTimeMs 1750169220000
```

Output: 
```
{
    "Response": {
        "RequestId": "a9a9d232-01c0-494a-baa3-57c384463c3f",
        "Keywords": [
            "key1",
            "key2"
        ]
    }
}
```

