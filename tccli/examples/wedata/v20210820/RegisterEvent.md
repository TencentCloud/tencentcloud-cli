**Example 1: 注册事件**

注册事件

Input: 

```
tccli wedata RegisterEvent --cli-unfold-argument  \
    --ProjectId 1492511691706699776 \
    --Name test_event_11 \
    --EventType TIME_SERIES \
    --EventSubType DAY \
    --EventBroadcastType SINGLE \
    --DimensionFormat yyyyMMdd \
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
            "ErrorDesc": null,
            "ErrorId": null,
            "Result": true
        },
        "RequestId": "d43d2a97-0522-4917-a471-dbc0a8b3c318"
    }
}
```

