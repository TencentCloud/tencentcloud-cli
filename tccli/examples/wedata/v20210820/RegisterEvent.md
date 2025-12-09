**Example 1: 成功示例**

成功示例

Input: 

```
tccli wedata RegisterEvent --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --Name xxxxx2 \
    --EventSubType DAY \
    --EventBroadcastType BROADCAST \
    --TimeUnit DAYS \
    --Owner jaydenjhu \
    --EventType TIME_SERIES \
    --DimensionFormat yyyyMMdd \
    --TimeToLive 30 \
    --Description ffdsafasdf
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
        "RequestId": "ff9b1b3e-bf16-45d0-ac93-ab093dc2db8c"
    }
}
```

