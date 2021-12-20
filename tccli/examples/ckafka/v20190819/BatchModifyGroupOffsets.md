**Example 1: 批量设置Groups 消费分组offset**

批量设置Groups 消费分组offset

Input: 

```
tccli ckafka BatchModifyGroupOffsets --cli-unfold-argument  \
    --InstanceId xx \
    --GroupName xx \
    --TopicName xx \
    --Partitions.0.Partition 0 \
    --Partitions.0.Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok",
            "Data": "ok"
        },
        "RequestId": "ae362db8-81f6-4441-b0cc-1f6ffa31127e"
    }
}
```

