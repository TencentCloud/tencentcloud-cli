**Example 1: 拉取云存事件及 AI 分析任务列表**



Input: 

```
tccli iotexplorer DescribeCloudStorageEventsWithAITasks --cli-unfold-argument  \
    --ProductId TSLFHRWDSD \
    --DeviceName dev004 \
    --ServiceTypes VideoToText
```

Output: 
```
{
    "Response": {
        "Context": "DnF1ZXJ5VGhlbkZldGNoCAAAAAAFqzhwFjFFY01POHFmVGxDSnJJTHI5elNNU0EAAAAABZbFYRZmd1ZJbURjWFNuR2F5a0JIR0ozU1NBAAAAAAWUnSYWejUwaVhKNWJScE9ZTkNuV3FycTVYUQAAAAAFlsVgFmZ3VkltRGNYU25HYXlrQkhHSjNTU0EAAAAABaXmlhZyRU9EQTRKeFNrV1VGSDVUXzRiVFRnAAAAAAWUnScWejUwaVhKNWJScE9ZTkNuV3FycTVYUQAAAAAFka-jFm5zbVpuZXVZU0VHNWh1czNkcFFDZ2cAAAAABboqiRZySXYzUUhoblN6T0pqSzFQcThDT2p3",
        "Events": [
            {
                "AITasks": [
                    {
                        "ChannelId": 0,
                        "CreateTime": 1736855569,
                        "DeviceName": "dev004",
                        "EndTime": 1736855561,
                        "Files": [],
                        "ProductId": "TSLFHRWDSD",
                        "Result": "{\"DetectedClassifications\": [\"person\"], \"Summary\": \"一个人在雨天街道上行走\"}",
                        "ServiceType": "VideoToText",
                        "StartTime": 1736855553,
                        "Status": 3,
                        "TaskId": "019464a8-c241-7544-a460-e10298e8ea07",
                        "UpdateTime": 1736855581
                    }
                ],
                "Data": "",
                "EndTime": 1736855561,
                "EventId": "_sys_id1_data",
                "StartTime": 1736855553,
                "Thumbnail": "",
                "UploadStatus": "Finished"
            }
        ],
        "Listover": true,
        "RequestId": "3eace4a0-d09c-4dc9-b91c-98c10d48b009",
        "Total": 1,
        "VideoURL": "https://1259367869.vod2.myqcloud.com/timeshift/live/<streamName>/timeshift.m3u8"
    }
}
```

