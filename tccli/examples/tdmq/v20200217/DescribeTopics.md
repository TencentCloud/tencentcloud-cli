**Example 1: 列出指定环境下主题**



Input: 

```
tccli tdmq DescribeTopics --cli-unfold-argument  \
    --EnvironmentId default \
    --TopicName  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 15,
        "TopicSets": [
            {
                "TopicName": "cloud-dlq",
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
                "Partitions": 5,
                "ProducerCount": "0",
                "TotalSize": "0",
                "TopicType": 4,
                "Remark": "",
                "SubTopicSets": [
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 11:14:32",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 0,
                        "ProducerCount": "0",
                        "TopicType": 4,
                        "TotalSize": "0"
                    },
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 14:39:41",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 1,
                        "ProducerCount": "0",
                        "TopicType": 4,
                        "TotalSize": "0"
                    },
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 14:39:41",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 2,
                        "ProducerCount": "0",
                        "TopicType": 4,
                        "TotalSize": "0"
                    },
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 14:39:41",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 3,
                        "ProducerCount": "0",
                        "TopicType": 4,
                        "TotalSize": "0"
                    },
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 14:39:41",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 4,
                        "ProducerCount": "0",
                        "TopicType": 4,
                        "TotalSize": "0"
                    }
                ]
            },
            {
                "TopicName": "cloud-retry",
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
                "Partitions": 5,
                "ProducerCount": "0",
                "TotalSize": "0",
                "TopicType": 3,
                "Remark": "55555",
                "SubTopicSets": [
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 11:14:32",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 0,
                        "ProducerCount": "0",
                        "TopicType": 3,
                        "TotalSize": "0"
                    },
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 14:41:29",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 1,
                        "ProducerCount": "0",
                        "TopicType": 3,
                        "TotalSize": "0"
                    },
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 14:41:29",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 2,
                        "ProducerCount": "0",
                        "TopicType": 3,
                        "TotalSize": "0"
                    },
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 14:41:29",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 3,
                        "ProducerCount": "0",
                        "TopicType": 3,
                        "TotalSize": "0"
                    },
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 14:41:29",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 4,
                        "ProducerCount": "0",
                        "TopicType": 3,
                        "TotalSize": "0"
                    }
                ]
            },
            {
                "TopicName": "cloud1-dlq",
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
                "TopicType": 4,
                "Remark": "系统创建",
                "SubTopicSets": [
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 11:50:26",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 0,
                        "ProducerCount": "0",
                        "TopicType": 4,
                        "TotalSize": "0"
                    }
                ]
            },
            {
                "TopicName": "cloud1-retry",
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
                "TopicType": 3,
                "Remark": "系统创建",
                "SubTopicSets": [
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 11:50:25",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 0,
                        "ProducerCount": "0",
                        "TopicType": 3,
                        "TotalSize": "0"
                    }
                ]
            },
            {
                "TopicName": "cloud2-dlq",
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
                "TopicType": 4,
                "Remark": "系统创建",
                "SubTopicSets": [
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 11:53:30",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 0,
                        "ProducerCount": "0",
                        "TopicType": 4,
                        "TotalSize": "0"
                    }
                ]
            },
            {
                "TopicName": "cloud2-retry",
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
                "TopicType": 3,
                "Remark": "系统创建",
                "SubTopicSets": [
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 11:53:30",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 0,
                        "ProducerCount": "0",
                        "TopicType": 3,
                        "TotalSize": "0"
                    }
                ]
            },
            {
                "TopicName": "cloud3-dlq",
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
                "TopicType": 4,
                "Remark": "系统创建",
                "SubTopicSets": [
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 11:59:01",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 0,
                        "ProducerCount": "0",
                        "TopicType": 4,
                        "TotalSize": "0"
                    }
                ]
            },
            {
                "TopicName": "cloud3-retry",
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
                "TopicType": 3,
                "Remark": "系统创建",
                "SubTopicSets": [
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 11:59:01",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 0,
                        "ProducerCount": "0",
                        "TopicType": 3,
                        "TotalSize": "0"
                    }
                ]
            },
            {
                "TopicName": "cloud_test",
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
                "Partitions": 2,
                "ProducerCount": "0",
                "TotalSize": "0",
                "TopicType": 0,
                "Remark": "字符串",
                "SubTopicSets": [
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 14:45:15",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 0,
                        "ProducerCount": "0",
                        "TopicType": 0,
                        "TotalSize": "0"
                    },
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 14:45:15",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 1,
                        "ProducerCount": "0",
                        "TopicType": 0,
                        "TotalSize": "0"
                    }
                ]
            },
            {
                "TopicName": "cloud_test_1",
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
                "Partitions": 2,
                "ProducerCount": "0",
                "TotalSize": "0",
                "TopicType": 0,
                "Remark": "",
                "SubTopicSets": [
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 14:45:28",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 0,
                        "ProducerCount": "0",
                        "TopicType": 0,
                        "TotalSize": "0"
                    },
                    {
                        "AverageMsgSize": "0.0",
                        "ConsumerCount": "0",
                        "LastConfirmedEntry": "",
                        "LastLedgerCreatedTimestamp": "2020-05-12 14:45:28",
                        "MsgRateIn": "0.0",
                        "MsgRateOut": "0.0",
                        "MsgThroughputIn": "0.0",
                        "MsgThroughputOut": "0.0",
                        "NumberOfEntries": "0",
                        "Partitions": 1,
                        "ProducerCount": "0",
                        "TopicType": 0,
                        "TotalSize": "0"
                    }
                ]
            }
        ],
        "RequestId": "5b65e66c-93dd-4752-811d-8053b357df5b"
    }
}
```

