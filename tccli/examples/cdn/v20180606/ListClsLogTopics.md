**Example 1: Displaying a list of log topics**



Input: 

```
tccli cdn ListClsLogTopics --cli-unfold-argument  \
    --Channel cdn
```

Output: 
```
{
    "Response": {
        "RequestId": "2424",
        "Logset": {
            "AppId": 1242424252,
            "Channel": "cdn",
            "LogsetId": "44d5b2d4-092c-4a4a-971e-07d9e536ccc3",
            "LogsetName": "cdn_logset",
            "IsDefault": 1,
            "LogsetSavePeriod": 7
        },
        "Topics": [
            {
                "TopicId": "def811bf-867e-405c-bbc2-2a3aea45be21",
                "TopicName": "cdn_topic",
                "Enabled": 1
            },
            {
                "TopicId": "e0f6809f-026f-4287-b33f-8041a82188cf",
                "TopicName": "cdn_topic2",
                "Enabled": 1
            },
            {
                "TopicId": "fcfb346d-100d-454c-adc6-bdf2a2af0515",
                "TopicName": "cdn_topic1",
                "Enabled": 1
            }
        ]
    }
}
```

