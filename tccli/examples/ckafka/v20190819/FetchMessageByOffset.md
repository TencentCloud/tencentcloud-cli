**Example 1: 消息查询**



Input: 

```
tccli ckafka FetchMessageByOffset --cli-unfold-argument  \
    --InstanceId ckafka \
    --Topic topic-test \
    --Partition 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Result": {
            "Topic": "topic-test",
            "Partition": 0,
            "Offset": 0,
            "Key": "key",
            "Value": "value",
            "Timestamp": 0,
            "Headers": "head"
        },
        "RequestId": "4a88011d-763d-446d-802e-fcbe970a4043"
    }
}
```

