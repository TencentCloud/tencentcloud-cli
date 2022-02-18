**Example 1: 获取设备通道实时流地址URL**

获取设备指定通道实时流地址URL

Input: 

```
tccli iotvideoindustry DescribeChannelStreamURL --cli-unfold-argument  \
    --DeviceId 34020000001180000036_34020000001180000036 \
    --ChannelId 34020000001180000036_34020000001320000092 \
    --ExpireTime 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "RtspAddr": "NULL",
            "RtmpAddr": "rtmp://dev-pl.video.tencentcs.com/live/1073160348?txSecret=cbb387785ac54bd84b6838ea3b42ffc0&txTime=60653086",
            "HlsAddr": "https://dev-pl.video.tencentcs.com/live/1073160348.m3u8?txSecret=cbb387785ac54bd84b6838ea3b42ffc0&txTime=60653086",
            "FlvAddr": "https://dev-pl.video.tencentcs.com/live/1073160348.flv?txSecret=cbb387785ac54bd84b6838ea3b42ffc0&txTime=60653086"
        },
        "RequestId": "c5afa3fc-a71e-4fc1-b266-3c3ba49bdf41"
    }
}
```

