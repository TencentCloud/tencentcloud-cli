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
        "TopicSets": [
            {
                "TopicName": "test",
                "EnvironmentId": "default",
                "AverageMsgSize": "0.0",
                "ConsumerCount": "0",
                "LastConfirmedEntry": "",
                "LastLedgerCreatedTimestamp": "",
                "MsgRateIn": "0.0",
                "MsgRateOut": "0.0",
                "MsgThroughputIn": "0.0",
                "MsgThroughputOut": "0.0",
                "NumberOfEntries": "0",
                "Partitions": 1,
                "ProducerCount": "0",
                "TotalSize": "0",
                "TopicType": 0,
                "Remark": "",
                "CreateTime": "2021-01-13 16:39:57",
                "UpdateTime": "2021-01-13 16:39:57",
                "SubTopicSets": [
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "199291:-1",
                        "LastLedgerCreatedTimestamp": "2021-01-13 16:39:57",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 0,
                        "ProducerCount": "0",
                        "TopicType": 0,
                        "TotalSize": "0"
                    }
                ]
            }
        ],
        "RequestId": "dde566ff-ee5d-4ba9-af1c-0481f4220f93"
    }
}
```

