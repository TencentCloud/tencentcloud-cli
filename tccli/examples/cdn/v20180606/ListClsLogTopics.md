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
        "RequestId": "44d5b2d4-092c-4a4a-971e-07d9e536ccc1",
        "Logset": {
            "AppId": 1242424252,
            "Channel": "cdn",
            "Region": "ap-shanghai",
            "LogsetId": "44d5b2d4-092c-4a4a-971e-07d9e536ccc3",
            "LogsetName": "cdn_logset",
            "IsDefault": 1,
            "LogsetSavePeriod": 7,
            "CreateTime": "2020-09-22 00:00:00",
            "RegionEn": "ap-shanghai",
            "Deleted": "no"
        },
        "Topics": [
            {
                "TopicId": "def811bf-867e-405c-bbc2-2a3aea45be21",
                "TopicName": "cdn_topic",
                "Enabled": 1,
                "CreateTime": "2020-09-22 00:00:00",
                "Deleted": "no"
            },
            {
                "TopicId": "e0f6809f-026f-4287-b33f-8041a82188cf",
                "TopicName": "cdn_topic2",
                "Enabled": 1,
                "CreateTime": "2020-09-22 00:00:00",
                "Deleted": "no"
            },
            {
                "TopicId": "fcfb346d-100d-454c-adc6-bdf2a2af0515",
                "TopicName": "cdn_topic1",
                "Enabled": 1,
                "CreateTime": "2020-09-22 00:00:00",
                "Deleted": "no"
            }
        ],
        "ExtraLogset": [
            {
                "Logset": {
                    "AppId": 1306270566,
                    "Channel": "cdn",
                    "LogsetId": "de5965b4-b371-4a5e-86ad-f2d2f9988a4d",
                    "LogsetName": "cloud_cdn_logset_oversea",
                    "IsDefault": 0,
                    "LogsetSavePeriod": 7,
                    "CreateTime": "2021-10-20 17:22:21",
                    "Region": "ap-singapore",
                    "RegionEn": "ap-singapore",
                    "Deleted": "no"
                },
                "Topics": [
                    {
                        "TopicId": "a9619e5a-2387-46bd-83c8-89b133f20f4a",
                        "TopicName": "jory-test",
                        "Enabled": 1,
                        "CreateTime": "2021-10-27 15:17:10",
                        "Deleted": "no",
                        "Channel": "cdn"
                    },
                    {
                        "TopicId": "58474924-8b34-4e26-aa03-b23202007ea6",
                        "TopicName": "jory-oversea",
                        "Enabled": 1,
                        "CreateTime": "2021-10-26 21:06:24",
                        "Deleted": "no",
                        "Channel": "cdn"
                    }
                ]
            }
        ]
    }
}
```

