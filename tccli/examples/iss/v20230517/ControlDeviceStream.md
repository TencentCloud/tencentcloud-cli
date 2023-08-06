**Example 1: 成功**

 

Input: 

```
tccli iss ControlDeviceStream --cli-unfold-argument  \
    --ChannelId 12345678-abcd-efgh-ijkl-1234567890abcd
```

Output: 
```
{
    "Response": {
        "Data": {
            "Flv": "https://test.com.cn/live/12345678-abcd-efgh-ijkl-1234567890abcd.live.flv",
            "Hls": "https://test.com.cn/live/12345678-abcd-efgh-ijkl-1234567890abcd/hls.m3u8",
            "Rtmp": "rtmp://test.com.cn/live/12345678-abcd-efgh-ijkl-1234567890abcd"
        },
        "RequestId": "80913db2-a570-4c81-bd55-526ef3932aea"
    }
}
```

