**Example 1: 获取某个时间段的视频内容关键字**



Input: 

```
tccli iotexplorer InvokeVideosKeywordsAnalyzer --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev20260426 \
    --StartTimeMs 1777211099723 \
    --EndTimeMs 1777212099723
```

Output: 
```
{
    "Response": {
        "Keywords": [
            "人在行走"
        ],
        "RequestId": "e099a05d-0dd9-4253-9d68-b0ed6eaf6bb2"
    }
}
```

**Example 2: 获取某个时间段的视频内容关键字（指定语言）**



Input: 

```
tccli iotexplorer InvokeVideosKeywordsAnalyzer --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev20260428 \
    --StartTimeMs 1777305600000 \
    --EndTimeMs 1777391999000 \
    --KeywordsLang en-US
```

Output: 
```
{
    "Response": {
        "Keywords": [
            "穿浅色衣物的人在行走"
        ],
        "RequestId": "b7509c52-2a5e-44ea-b97d-0e471b77b3f7"
    }
}
```

