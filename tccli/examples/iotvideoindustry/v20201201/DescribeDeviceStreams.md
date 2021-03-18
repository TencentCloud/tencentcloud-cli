**Example 1: 获取设备流地址**



Input: 

```
tccli iotvideoindustry DescribeDeviceStreams --cli-unfold-argument  \
    --DeviceId xxx \
    --ExpireTime 1610199034
```

Output: 
```
{
    "Response": {
        "Data": {
            "RtspAddr": "NULL",
            "RtmpAddr": "rtmp://dev-pl.video.tencentcs.com/live/0035752400?txSecret=1a52a468ed68ce343d42bdb1c80ae855&txTime=5FE720C7",
            "HlsAddr": "http://dev-pl.video.tencentcs.com/live/0035752400.m3u8?txSecret=1a52a468ed68ce343d42bdb1c80ae855&txTime=5FE720C7",
            "FlvAddr": "http://dev-pl.video.tencentcs.com/live/0035752400.flv?txSecret=1a52a468ed68ce343d42bdb1c80ae855&txTime=5FE720C7"
        },
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

