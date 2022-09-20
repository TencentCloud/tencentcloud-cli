**Example 1: 获取推送任务列表**



Input: 

```
tccli teo DescribeLogTopicTasks --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --ZoneId zone-28569s6od5na
```

Output: 
```
{
    "Response": {
        "RequestId": "40be710a-9706-4b22-865e-c9739111ef1a",
        "TopicList": [
            {
                "Area": "mainland",
                "CreateTime": "2022-08-31 10:41:11",
                "Deleted": "no",
                "Enabled": true,
                "EntityType": "application",
                "LogSetId": "33a900b2-9860-4da0-be91-bcce94c290ce",
                "Period": 10,
                "LogSetRegion": "ap-guangzhou",
                "Target": "cls",
                "TaskName": "test_task",
                "TopicId": "0a396698-d589-42b6-a6a2-701777d3afe0",
                "ZoneName": "hello.club",
                "ZoneId": "zone-28569s6od5na"
            }
        ],
        "TotalCount": 1
    }
}
```

