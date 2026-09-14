**Example 1: 查询日志任务示例**



Input: 

```
tccli ga2 DescribeGlobalAcceleratorAccessLog --cli-unfold-argument  \
    --GlobalAcceleratorId ga-rs4cpp5u \
    --Filters.0.Name listener-id \
    --Filters.0.Values lsr-3c7xwnq3 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "GlobalAcceleratorAccessLog": [
            {
                "CloudLogId": "8b82e387-a213-41f7-aaa3-2fd6d02265d8",
                "CloudLogSetId": "b18a3982-b759-4809-9f59-17a0b971f223",
                "CloudRegion": "ap-guangzhou",
                "EndpointGroupId": "epg-pg931p4y",
                "FieldKeys": [],
                "FlowLogDescription": "wick-测试创建日志任务-修改",
                "GlobalAcceleratorId": "ga-rs4cpp5u",
                "ListenerId": "lsr-3c7xwnq3",
                "LogPushTaskId": "galog-8agteyy6",
                "Status": "active"
            }
        ],
        "TotalCount": 1,
        "RequestId": "fb502cae-f49f-4797-b9c9-49bb66046d8c"
    }
}
```

