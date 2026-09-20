**Example 1: 查询 TWeSee 人员关联的云存事件**

查询指定 TWeSee 人员所关联的云存事件及 AI 任务。

Input: 

```
tccli iotexplorer DescribeCloudStorageEventsByTWeSeePerson --cli-unfold-argument  \
    --ProductId QDA1PZLBNB \
    --DeviceName dev001 \
    --ChannelId 0 \
    --PersonId person-11111111-2222-3333-4444-555555555555 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Events": [
            {
                "StartTime": 1710487888,
                "EndTime": 1710487898,
                "Thumbnail": "/10000****725/QDA****BNB/dev001/events/1710487888.jpg",
                "EventId": "event-123",
                "UploadStatus": "Finished",
                "Data": "",
                "AITasks": [
                    {
                        "TaskId": "fb066d7a-baac-4706-acda-058f56f82759",
                        "ProductId": "QDA1PZLBNB",
                        "DeviceName": "dev001",
                        "ChannelId": 0,
                        "ServiceType": "VideoToText",
                        "StartTime": 1710487888,
                        "EndTime": 1710487898,
                        "StartTimeMs": 1710487888270,
                        "EndTimeMs": 1710487898990,
                        "Status": 3,
                        "Result": "{\"Summary\":\"一个人在门前经过\"}",
                        "Files": [],
                        "CreateTime": 1711338476,
                        "UpdateTime": 1711338476,
                        "CustomId": "event-123"
                    }
                ]
            }
        ],
        "RequestId": "3eace4a0-d09c-4dc9-b91c-98c10d48b009"
    }
}
```

