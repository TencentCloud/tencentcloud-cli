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
                "EnvironmentId": "xx",
                "Remark": "xx",
                "TopicType": 1,
                "ProducerCount": "xx",
                "LastConfirmedEntry": "xx",
                "TotalSize": "xx",
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
                "NumberOfEntries": "xx",
                "ConsumerCount": "xx",
                "MsgRateOut": "xx",
                "UpdateTime": "2020-09-22 00:00:00",
                "CreateTime": "2020-09-22 00:00:00",
                "ConsumerLimit": "xx",
                "AverageMsgSize": "xx",
                "MsgThroughputIn": "xx",
                "MsgRateIn": "xx",
                "Partitions": 1,
                "ProducerLimit": "xx",
                "LastLedgerCreatedTimestamp": "xx",
                "TopicName": "xx",
                "MsgThroughputOut": "xx"
            }
        ]
    }
}
```

