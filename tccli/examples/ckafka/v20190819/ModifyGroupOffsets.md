**Example 1: 设置Groups 消费分组offset**



Input: 

```
tccli ckafka ModifyGroupOffsets --cli-unfold-argument  \
    --InstanceId 10 \
    --Group "group" \
    --Strategy 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok"
        },
        "RequestId": "ae362db8-81f6-4441-b0cc-1f6ffa31127e"
    }
}
```

