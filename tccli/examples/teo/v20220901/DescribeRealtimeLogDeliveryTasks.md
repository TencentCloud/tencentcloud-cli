**Example 1: 查询某个站点下的所有实时日志投递任务信息**

查询指定 zone-id 下的所有实时日志投递任务信息。

Input: 

```
tccli teo DescribeRealtimeLogDeliveryTasks --cli-unfold-argument  \
    --ZoneId zone-2o7b38ba1hvr \
    --Offset 0 \
    --Limit 1000
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RealtimeLogDeliveryTasks": [
            {
                "TaskId": "57f6ebaa-f952-4ebf-8105-8071d1c59dde",
                "TaskName": "test_log_task",
                "DeliveryStatus": "enabled",
                "TaskType": "cls",
                "EntityList": [
                    "domain.example.com"
                ],
                "LogType": "domain",
                "Area": "overseas",
                "Fields": [
                    "RequestID",
                    "ClientIP",
                    "ClientRegion"
                ],
                "CustomFields": [],
                "DeliveryConditions": [],
                "Sample": 1000,
                "CLS": {
                    "LogSetId": "288f187c-c3ef-4479-a086-b9465a1243cb",
                    "LogSetRegion": "ap-guangzhou",
                    "TopicId": "0e23008b-c0ed-4d98-a77c-bdc65dfe3731"
                },
                "CustomEndpoint": null,
                "S3": null,
                "CreateTime": "2023-12-22T15:27:53+00:00",
                "UpdateTime": "2023-12-22T15:30:07+00:00"
            }
        ],
        "RequestId": "f025c1f0-cb83-41b1-bb7d-565af7e28479"
    }
}
```

**Example 2: 根据加速域名查询对应实时日志投递任务信息**

查询指定加速域名对应的实时日志投递任务信息。根据输出返回结果中的 TotalCount 为 0 可以判断此加速域名暂未被添加到任何实时日志投递任务中。

Input: 

```
tccli teo DescribeRealtimeLogDeliveryTasks --cli-unfold-argument  \
    --ZoneId zone-2o7b38ba1hvr \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name entity-list \
    --Filters.0.Values domain.example.com
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RealtimeLogDeliveryTasks": [],
        "RequestId": "f025c1f0-cb83-41b1-bb7d-565af7e28479"
    }
}
```

