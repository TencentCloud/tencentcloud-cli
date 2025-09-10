**Example 1: 设置Groups 消费分组offset**



Input: 

```
tccli ckafka ModifyGroupOffsets --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --Group "group" \
    --Strategy 1
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "SUCCESS",
            "Data": {
                "FlowId": 0
            }
        },
        "RequestId": "36713f94-d07d-4b96-babf-42d139276f23"
    }
}
```

