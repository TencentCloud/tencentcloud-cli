**Example 1: 查询某个站点下的所有实时日志投递任务信息**

查询指定 zone-id 下的所有实时日志投递任务信息。

Input: 

```
tccli teo DescribeRealtimeLogDeliveryTasks --cli-unfold-argument  \
    --ZoneId zone-2ur49nglp1a2 \
    --Offset 0 \
    --Limit 1000
```

Output: 
```
{
    "Response": {
        "RealtimeLogDeliveryTasks": [
            {
                "Area": "overseas",
                "CLS": {
                    "LogSetId": "980611e5-3eb2-430f-a0cc-e1c4e84a9e40",
                    "LogSetRegion": "ap-guangzhou",
                    "TopicId": "d258c060-dc6e-4586-8b7c-6a951667fa7a"
                },
                "CreateTime": "2024-03-26T03:00:39+08:00",
                "CustomEndpoint": null,
                "CustomFields": [],
                "DeliveryConditions": [],
                "DeliveryStatus": "enabled",
                "EntityList": [
                    "qqqq.loliyu.com"
                ],
                "Fields": [
                    "RequestID",
                    "ClientIP",
                    "ClientRegion",
                    "RequestTime",
                    "RequestHost",
                    "RequestBytes",
                    "RequestMethod",
                    "RequestUrl",
                    "RequestUrlQueryString",
                    "RequestUA",
                    "RequestRange",
                    "RequestReferer",
                    "RequestProtocol",
                    "RemotePort",
                    "EdgeCacheStatus",
                    "EdgeResponseStatusCode",
                    "EdgeResponseBytes",
                    "EdgeResponseTime",
                    "EdgeInternalTime",
                    "ClientState",
                    "ClientISP",
                    "EdgeServerID",
                    "EdgeServerIP"
                ],
                "LogFormat": null,
                "LogType": "domain",
                "S3": null,
                "Sample": 0,
                "TaskId": "f0e1686a-1c4e-4f15-967b-5afb2a0803ea",
                "TaskName": "ccc",
                "TaskType": "cls",
                "UpdateTime": "2024-03-26T03:10:13+08:00"
            }
        ],
        "RequestId": "05205d07-f582-444d-b558-b338a3f68857",
        "TotalCount": 1
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

