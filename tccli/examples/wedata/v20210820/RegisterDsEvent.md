**Example 1: 注册事件（新建事件）**

新建事件

Input: 

```
tccli wedata RegisterDsEvent --cli-unfold-argument  \
    --ProjectId 1492511691706699776 \
    --Name test_event_1 \
    --EventSubType DAY \
    --TimeToLive 30 \
    --TimeUnit DAYS \
    --Owner micofywang \
    --Description test
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreationTs": null,
            "Description": "test",
            "DimensionFormat": "yyyyMMdd",
            "EventBroadcastType": "BROADCAST",
            "EventSubType": "DAY",
            "EventType": "TIME_SERIES",
            "Listeners": null,
            "Name": "test_event_1",
            "Owner": "micofywang",
            "ProjectId": "1492511691706699776",
            "ProjectName": "",
            "Properties": null,
            "TimeToLive": 30,
            "TimeUnit": "DAYS"
        },
        "RequestId": "7bf51807-efe1-499a-952f-d6b040effaa0"
    }
}
```

