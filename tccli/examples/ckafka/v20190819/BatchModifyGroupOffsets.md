**Example 1: 批量设置Groups 消费分组offset**

批量设置Groups 消费分组offset

Input: 

```
tccli ckafka BatchModifyGroupOffsets --cli-unfold-argument  \
    --GroupName group-test \
    --TopicName topic-abc \
    --InstanceId ckafka-test \
    --Partitions.0.Partition 0 \
    --Partitions.0.Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "OK",
            "ReturnMessage": "success",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "abc"
    }
}
```

