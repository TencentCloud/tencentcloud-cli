**Example 1: 获取回放视频流(NVR录制用)，使用StartTime/EndTime**

使用StartTime/EndTime

Input: 

```
tccli iotvideoindustry DescribeRecordStream --cli-unfold-argument  \
    --DeviceId 34020000001180000036_34020000001320000092 \
    --StartTime 1615998219 \
    --EndTime 1616001641 \
    --ExpireTime 1616914614
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
        "RequestId": "c5afa3fc-a71e-4fc1-b266-3c3ba49bdf40"
    }
}
```

**Example 2: 获取回放视频流(NVR录制用)，使用RecordId**

使用RecordId，当使用RecordId时候，可以使用RecordId 起始时间组成一个新的RecordId（包含在原来RecordId时间范围内），来实现偏移的效果，例如：服务器返回RecordId为 123456_456789   可以使用 153456_456789 来实现起始时间偏移播放

Input: 

```
tccli iotvideoindustry DescribeRecordStream --cli-unfold-argument  \
    --DeviceId 34020000001180000036_34020000001320000092 \
    --RecordId 1615998219_1616001641 \
    --ExpireTime 1616914614
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
        "RequestId": "c5afa3fc-a71e-4fc1-b266-3c3ba49bdf40"
    }
}
```

