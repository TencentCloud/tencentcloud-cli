**Example 1: 显示日志主题列表**



Input: 

```
tccli cdn ListClsLogTopics --cli-unfold-argument  \
    --Channel cdn
```

Output: 
```
{
    "Response": {
        "RequestId": "1313131-092c-4a4a-971e-07d9e536ccc3",
        "Logset": {
            "AppId": 1242424252,
            "Channel": "cdn",
            "Region": "ap-shanghai",
            "LogsetId": "44d5b2d4-092c-4a4a-971e-07d9e536ccc3",
            "LogsetName": "cdn_logset",
            "IsDefault": 1,
            "LogsetSavePeriod": 7,
            "CreateTime": "2020-09-22 00:00:00"
        },
        "Topics": [
            {
                "TopicId": "def811bf-867e-405c-bbc2-2a3aea45be21",
                "TopicName": "cdn_topic",
                "Enabled": 1,
                "CreateTime": "2020-09-22 00:00:00"
            },
            {
                "TopicId": "e0f6809f-026f-4287-b33f-8041a82188cf",
                "TopicName": "cdn_topic2",
                "Enabled": 1,
                "CreateTime": "2020-09-22 00:00:00"
            },
            {
                "TopicId": "fcfb346d-100d-454c-adc6-bdf2a2af0515",
                "TopicName": "cdn_topic1",
                "Enabled": 1,
                "CreateTime": "2020-09-22 00:00:00"
            }
        ]
    }
}
```

