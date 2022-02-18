**Example 1: 获取回放文件推送云端后的实时视频URL**



Input: 

```
tccli iotvideoindustry DescribeChannelLocalRecordURL --cli-unfold-argument  \
    --DeviceId 34020000001180000036_34020000001180000036 \
    --ChannelId 34020000001180000036_34020000001320000092 \
    --RecordId 1615998219_1616001641 \
    --ExpireTime 1642132687
```

Output: 
```
{
    "Response": {
        "Data": {
            "RtspAddr": "NULL",
            "RtmpAddr": "rtmp://dev-pl.video.tencentcs.com/live/1073160348?txSecret=cbb387785ac54bd84b6838ea3b42ffc0&txTime=60653086",
            "HlsAddr": "https://dev-pl.video.tencentcs.com/live/1073160348.m3u8?txSecret=cbb387785ac54bd84b6838ea3b42ffc0&txTime=60653086",
            "FlvAddr": "https://dev-pl.video.tencentcs.com/live/1073160348.flv?txSecret=cbb387785ac54bd84b6838ea3b42ffc0&txTime=60653086",
            "StreamId": "1073160348"
        },
        "RequestId": "c5afa3fc-a71e-4fc1-b266-3c3ba49bdf41"
    }
}
```

