**Example 1: 获取Kafka协议消费组详情**



Input: 

```
tccli cls DescribeKafkaConsumerGroupList --cli-unfold-argument  \
    --TopicId 5023192e-1254139626 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Groups": [
            {
                "Group": "same_group_id",
                "ProtocolName": "",
                "State": "Empty"
            }
        ],
        "LogsetId": "a8248746-c989-468e-b931-a9bf6c999c89",
        "RequestId": "53ac1397-336a-4d4b-87ff-a2a16ff97519",
        "TopicName": "1254139626-5023192e",
        "Total": 2
    }
}
```

