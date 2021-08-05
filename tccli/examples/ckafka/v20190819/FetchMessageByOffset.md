**Example 1: 消息查询**



Input: 

```
tccli ckafka FetchMessageByOffset --cli-unfold-argument  \
    --InstanceId xxx \
    --Topic xxx \
    --Partition 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Result": {
            "Timestamp": 0,
            "Topic": "xxx",
            "Partition": 2,
            "Offset": 2,
            "Key": "xxx",
            "Value": "xxx"
        },
        "RequestId": "62d589e0-53d5-47e0-95ff-237c48b8fb77"
    }
}
```

