**Example 1: 范例**



Input: 

```
tccli wedata RegisterEvent --cli-unfold-argument  \
    --EventSubType DAY \
    --Name aab \
    --EventType TIME_SERIES \
    --DimensionFormat yyyyMMdd \
    --EventBroadcastType SINGLE \
    --ProjectId 1 \
    --Owner TBDS \
    --TimeUnit DAYS \
    --Description aa
```

Output: 
```
{
    "Response": {
        "RequestId": "150c868d-0f20-4c31-b300-12c08be75328",
        "Data": true
    }
}
```

**Example 2: 范例2**



Input: 

```
tccli wedata RegisterEvent --cli-unfold-argument  \
    --EventSubType DAY \
    --Name mytest4 \
    --EventType TIME_SERIES \
    --DimensionFormat yyyyMMdd \
    --EventBroadcastType SINGLE \
    --ProjectId 1 \
    --Owner TBDS \
    --TimeUnit DAYS \
    --Description aa
```

Output: 
```
{
    "Response": {
        "RequestId": "3ba35016-968f-456e-aae9-b31e1e0c8df3",
        "Data": {
            "Result": true,
            "ErrorId": null,
            "ErrorDesc": null
        }
    }
}
```

