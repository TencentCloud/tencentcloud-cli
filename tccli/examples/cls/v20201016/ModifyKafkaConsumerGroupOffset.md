**Example 1: 修改Kafka协议消费组点位**



Input: 

```
tccli cls ModifyKafkaConsumerGroupOffset --cli-unfold-argument  \
    --TopicId 5023192e-1254139626 \
    --Group same_group_id-1 \
    --ShiftTimestamp -1
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "RequestId": "c3ae291d-8ffd-4a26-b5ae-00b6863cdf44"
    }
}
```

