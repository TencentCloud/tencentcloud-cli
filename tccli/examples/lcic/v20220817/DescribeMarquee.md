**Example 1: 查询跑马灯配置**



Input: 

```
tccli lcic DescribeMarquee --cli-unfold-argument  \
    --SdkAppId 34442819 \
    --RoomId 353861
```

Output: 
```
{
    "Response": {
        "BackgroundColor": "",
        "BackgroundOpacity": 0.1,
        "Content": "",
        "DisplayMode": 1,
        "Duration": 9,
        "FontColor": "",
        "FontOpacity": 0.3,
        "FontSize": 11,
        "FontWeight": 1,
        "MarqueeCount": 1,
        "MarqueeType": 1,
        "RequestId": "5872d14e-d7-4122-990e-44a20e7dd6a5"
    }
}
```

