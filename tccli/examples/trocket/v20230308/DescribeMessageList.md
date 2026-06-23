**Example 1: 查询普通消息列表**



Input: 

```
tccli trocket DescribeMessageList --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Topic topic \
    --Offset 0 \
    --Limit 20 \
    --MsgId 1EAE3915000721B8D17C2C5BB31638D1 \
    --StartTime 1683613796174 \
    --EndTime 1683613796174 \
    --TaskRequestId 901a6956-1ab9-7fb7-3bf5-9f02b7aa2a7d
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "DeadLetterResendSuccessTimes": null,
                "DeadLetterResendTimes": null,
                "Keys": "test_key",
                "MsgId": "1EAE3915000721B8D17C2C5BB31638D1",
                "ProduceTime": "2023-05-09 14:43:27",
                "ProducerAddr": "30.174.57.21",
                "Tags": "test_tag"
            }
        ],
        "RequestId": "7426c613-085b-48c4-9257-87a208a8adcc",
        "TaskRequestId": "901a6956-1ab9-7fb7-3bf5-9f02b7aa2a7d",
        "TotalCount": 1
    }
}
```

**Example 2: 查询轻量消息列表**



Input: 

```
tccli trocket DescribeMessageList --cli-unfold-argument  \
    --InstanceId rmq-16jm9787qv \
    --Topic test_topic_parent \
    --StartTime 1774421710000 \
    --EndTime 1774422130842 \
    --TaskRequestId 901a6956-1ab9-7fb7-3bf5-9f02b7aa2a7d \
    --LiteTopic test_lite_topic \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DeadLetterResendSuccessTimes": null,
                "DeadLetterResendTimes": null,
                "Keys": null,
                "MsgId": "0B8D67BE00072D98A3357ED050E50000",
                "ProduceTime": "2026-03-25 14:59:41.416",
                "ProducerAddr": "11.141.103.190",
                "Tags": null
            }
        ],
        "TaskRequestId": "901a6956-1ab9-7fb7-3bf5-9f02b7aa2a7d",
        "TotalCount": 1,
        "RequestId": "588524c3-f6bd-4321-b274-308d632b0e1c"
    }
}
```

