**Example 1: 注册事件（新建事件）**

新建事件

Input: 

```
tccli wedata RegisterDsEvent --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --Name event_0811_01 \
    --EventSubType DAY \
    --TimeToLive 30 \
    --TimeUnit DAYS \
    --Owner wenjieyao \
    --Description 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreationTs": null,
            "Description": "1",
            "DimensionFormat": "yyyyMMdd",
            "EventBroadcastType": "BROADCAST",
            "EventSubType": "DAY",
            "EventType": "TIME_SERIES",
            "Listeners": null,
            "Name": "event_0811_01",
            "Owner": "wenjieyao",
            "ProjectId": "1470547050521227264",
            "ProjectName": "",
            "Properties": null,
            "TimeToLive": 30,
            "TimeUnit": "DAYS"
        },
        "RequestId": "bd5bbfc6-41e6-4e8f-a64e-f656b236b779"
    }
}
```

