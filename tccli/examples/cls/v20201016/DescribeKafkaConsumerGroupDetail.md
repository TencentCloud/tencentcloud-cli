**Example 1: 获取Kafka协议消费组详情**



Input: 

```
tccli cls DescribeKafkaConsumerGroupDetail --cli-unfold-argument  \
    --TopicId 5023192e-1254139626 \
    --Group same_group_id
```

Output: 
```
{
    "Response": {
        "Group": "same_group_id",
        "LogsetId": "a8248746-c989-468e-b931-a9bf6c999c89",
        "PartitionInfos": [
            {
                "CommitTimestamp": 3223609680,
                "Consumer": "",
                "PartitionId": 0
            },
            {
                "CommitTimestamp": 3223609680,
                "Consumer": "",
                "PartitionId": 1
            },
            {
                "CommitTimestamp": 3223609680,
                "Consumer": "",
                "PartitionId": 2
            },
            {
                "CommitTimestamp": 3223609680,
                "Consumer": "",
                "PartitionId": 3
            },
            {
                "CommitTimestamp": 3223609680,
                "Consumer": "",
                "PartitionId": 4
            },
            {
                "CommitTimestamp": 3223609680,
                "Consumer": "",
                "PartitionId": 5
            },
            {
                "CommitTimestamp": 3223609680,
                "Consumer": "",
                "PartitionId": 6
            }
        ],
        "RequestId": "b4a11979-760c-42e2-92b8-5945eb93ee98",
        "State": "Empty"
    }
}
```

