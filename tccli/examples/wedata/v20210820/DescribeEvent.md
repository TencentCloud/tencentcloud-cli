**Example 1: 查看事件详情成功返回**

查看事件详情成功返回

Input: 

```
tccli wedata DescribeEvent --cli-unfold-argument  \
    --ProjectId 1 \
    --EventName sample_event
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreationTimestamp": "2023-03-07T07:12:16.807Z",
            "Description": "",
            "DimensionFormat": "yyyyMMdd",
            "EventBroadcastType": null,
            "EventCases": null,
            "EventSubType": "DAY",
            "EventType": "TIME_SERIES",
            "Listeners": null,
            "Name": "sample_event",
            "Owner": "sample_user",
            "Properties": null,
            "TimeToLive": null,
            "TimeUnit": "DAYS"
        },
        "RequestId": "d9c516be-0f02-4902-a619-18942251bb17"
    }
}
```

