**Example 1: 获取环境下主题列表**



Input: 

```
tccli tdmq DescribeTopics --cli-unfold-argument  \
    --EnvironmentId test1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "TopicSets": [
            {
                "PulsarTopicType": 0,
                "TopicType": 1,
                "ProducerCount": "xx",
                "ConsumerLimit": "xx",
                "ConsumerCount": "xx",
                "LastLedgerCreatedTimestamp": "xx",
                "MsgThroughputIn": "xx",
                "UpdateTime": "2020-09-22 00:00:00",
                "AverageMsgSize": "xx",
                "Partitions": 1,
                "Remark": "xx",
                "LastConfirmedEntry": "xx",
                "TotalSize": "xx",
                "NumberOfEntries": "xx",
                "MsgRateOut": "xx",
                "ProducerLimit": "xx",
                "EnvironmentId": "xx",
                "TopicName": "xx",
                "MsgRateIn": "xx",
                "MsgThroughputOut": "xx",
                "SubTopicSets": [
                    {
                        "TopicType": 1,
                        "ProducerCount": "xx",
                        "LastConfirmedEntry": "xx",
                        "TotalSize": "xx",
                        "NumberOfEntries": "xx",
                        "ConsumerCount": "xx",
                        "MsgRateOut": "xx",
                        "AverageMsgSize": "xx",
                        "MsgThroughputIn": "xx",
                        "MsgRateIn": "xx",
                        "Partitions": 0,
                        "LastLedgerCreatedTimestamp": "xx",
                        "MsgThroughputOut": "xx"
                    }
                ],
                "CreateTime": "2020-09-22 00:00:00"
            }
        ]
    }
}
```

