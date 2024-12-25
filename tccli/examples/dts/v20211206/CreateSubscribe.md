**Example 1: 购买订阅任务**

购买1个按量计费的mysql订阅任务

Input: 

```
tccli dts CreateSubscribe --cli-unfold-argument  \
    --Product mysql \
    --PayType 1 \
    --Count 1 \
    --Tags.0.TagKey 负责人 \
    --Tags.0.TagValue jason \
    --Name binlog订阅
```

Output: 
```
{
    "Response": {
        "SubscribeIds": [
            "subs-b6x64o31tm"
        ],
        "RequestId": "xxxxxxxxxxxxxxx"
    }
}
```

