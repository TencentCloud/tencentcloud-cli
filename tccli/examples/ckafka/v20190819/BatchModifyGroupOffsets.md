**Example 1: 批量设置Groups 消费分组offset**

批量设置Groups 消费分组offset

Input: 

```
tccli ckafka BatchModifyGroupOffsets --cli-unfold-argument  \
    --GroupName abc \
    --TopicName abc \
    --InstanceId abc \
    --Partitions.0.Partition 0 \
    --Partitions.0.Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "abc",
            "ReturnMessage": "abc",
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

