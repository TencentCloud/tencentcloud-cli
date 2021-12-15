**Example 1: 创建直播频道**



Input: 

```
tccli iotvideoindustry CreateLiveChannel --cli-unfold-argument  \
    --LiveChannelType 1 \
    --LiveChannelName 直播001
```

Output: 
```
{
    "Response": {
        "LiveChannelId": "72f556500f0311ec806aacde48001122",
        "PushStreamAddress": "rtmp://10.4.56.32:31935/liveFixed/72f556500f0311ec806aacde48001122",
        "RequestId": "1"
    }
}
```

