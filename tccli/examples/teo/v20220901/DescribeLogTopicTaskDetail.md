**Example 1: 获取推送任务详细信息**



Input: 

```
tccli teo DescribeLogTopicTaskDetail --cli-unfold-argument  \
    --TopicId 0a396698-d589-42b6-a6a2-701777d3afe0 \
    --ZoneId zone-28569s6od5na
```

Output: 
```
{
    "Response": {
        "RequestId": "1ceade23-0016-4351-85d0-faf15b1649c6",
        "LogTopicDetailInfo": {
            "Area": "mainland",
            "CreateTime": "2022-08-31 10:41:11",
            "Deleted": "no",
            "Enabled": true,
            "EntityList": [
                "test1"
            ],
            "EntityType": "application",
            "LogSetId": "33a900b2-9860-4da0-be91-bcce94c290ce",
            "LogSetName": "test_log",
            "Period": 10,
            "LogSetRegion": "ap-guangzhou",
            "TaskName": "test_task",
            "TopicId": "0a396698-d589-42b6-a6a2-701777d3afe0",
            "TopicName": "test_topic",
            "ZoneName": "hello.club",
            "ZoneId": "zone-28569s6od5na"
        }
    }
}
```

