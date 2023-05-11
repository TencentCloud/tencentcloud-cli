**Example 1: 获取环境下主题列表**

获取环境下主题列表

Input: 

```
tccli tdmq DescribeTopics --cli-unfold-argument  \
    --EnvironmentId abc \
    --TopicName abc \
    --Offset 1 \
    --Limit 1 \
    --TopicType 1 \
    --ClusterId abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --TopicCreator 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "abc",
        "TopicSets": [
            {
                "PulsarTopicType": 0,
                "TopicType": 1,
                "ProducerCount": "abc",
                "ConsumerLimit": "abc",
                "ConsumerCount": "abc",
                "LastLedgerCreatedTimestamp": "14578964532",
                "MsgThroughputIn": "abc",
                "UpdateTime": "2020-09-22 00:00:00",
                "AverageMsgSize": "abc",
                "Partitions": 1,
                "Remark": "abc",
                "LastConfirmedEntry": "abc",
                "TotalSize": "1",
                "NumberOfEntries": "abc",
                "MsgRateOut": "abc",
                "ProducerLimit": "abc",
                "EnvironmentId": "abc",
                "TopicName": "abc",
                "MsgRateIn": "abc",
                "MsgThroughputOut": "abc",
                "SubTopicSets": [
                    {
                        "TopicType": 1,
                        "ProducerCount": "1",
                        "LastConfirmedEntry": "abc",
                        "TotalSize": "1",
                        "NumberOfEntries": "abc",
                        "ConsumerCount": "1",
                        "MsgRateOut": "abc",
                        "AverageMsgSize": "1",
                        "MsgThroughputIn": "abc",
                        "MsgRateIn": "abc",
                        "Partitions": 0,
                        "LastLedgerCreatedTimestamp": "124567885324",
                        "MsgThroughputOut": "abc"
                    }
                ],
                "CreateTime": "2020-09-22 00:00:00"
            }
        ]
    }
}
```

