**Example 1: 获取环境下主题列表**

获取环境下主题列表

Input: 

```
tccli tdmq DescribeTopics --cli-unfold-argument  \
    --EnvironmentId devNs \
    --TopicName devTopic \
    --Offset 1 \
    --Limit 1 \
    --TopicType 1 \
    --ClusterId pulsar-uahenidn \
    --TopicCreator 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "bee03397-31dd-4688-8fe0-81c691c3c1ae",
        "TopicSets": [
            {
                "PulsarTopicType": 0,
                "TopicType": 1,
                "ProducerCount": "1",
                "ConsumerLimit": "1000",
                "ConsumerCount": "200",
                "LastLedgerCreatedTimestamp": "14578964532",
                "MsgThroughputIn": "24",
                "UpdateTime": "2020-09-22 00:00:00",
                "AverageMsgSize": "20",
                "Partitions": 1,
                "Remark": "devRemark",
                "LastConfirmedEntry": "23",
                "TotalSize": "1",
                "NumberOfEntries": "12",
                "MsgRateOut": "10",
                "ProducerLimit": "10",
                "EnvironmentId": "devNs",
                "TopicName": "devTopic",
                "MsgRateIn": "12",
                "MsgThroughputOut": "100",
                "SubTopicSets": [
                    {
                        "TopicType": 1,
                        "ProducerCount": "1",
                        "LastConfirmedEntry": "100",
                        "TotalSize": "1",
                        "NumberOfEntries": "100",
                        "ConsumerCount": "1",
                        "MsgRateOut": "100",
                        "AverageMsgSize": "1",
                        "MsgThroughputIn": "100",
                        "MsgRateIn": "100",
                        "Partitions": 0,
                        "LastLedgerCreatedTimestamp": "124567885324",
                        "MsgThroughputOut": "100"
                    }
                ],
                "CreateTime": "2020-09-22 00:00:00"
            }
        ]
    }
}
```

