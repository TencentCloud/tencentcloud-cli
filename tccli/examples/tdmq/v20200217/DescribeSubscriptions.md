**Example 1: 消费订阅列表**



Input: 

```
tccli tdmq DescribeSubscriptions --cli-unfold-argument  \
    --EnvironmentId devNamespace \
    --TopicName devTopic \
    --Offset 0 \
    --Limit 1 \
    --SubscriptionName devSub \
    --Filters.0.ConsumerHasCount True \
    --Filters.0.ConsumerHasBacklog True \
    --Filters.0.ConsumerHasExpired True \
    --Filters.0.SubscriptionNames devSub \
    --ClusterId pulsar-b843bz38z5mz
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SubscriptionSets": [
            {
                "EnvironmentId": "devNamespace",
                "TopicName": "devTopic",
                "ConnectedSince": "2024-10-08 11:38:48",
                "ConsumerAddr": "127.0.0.1",
                "ConsumerCount": "6",
                "ConsumerName": "devName",
                "MsgBacklog": "1087",
                "MsgRateExpired": "0.0",
                "MsgRateOut": "0.0",
                "SubType": null,
                "MsgThroughputOut": "0.0",
                "SubscriptionName": "devSub",
                "BlockedSubscriptionOnUnackedMsgs": true,
                "MaxUnackedMsgNum": 0,
                "Remark": "devRemark",
                "CreateTime": "2020-09-18 14:32:41",
                "UpdateTime": "2021-01-13 15:23:35",
                "IsOnline": true,
                "ConsumerSets": [
                    {
                        "ConnectedSince": "2021-01-13T15:19:21.03+08:00",
                        "ConsumerAddr": "/9.219.234.200:9056",
                        "ConsumerName": "axjoy",
                        "Partition": 4,
                        "ClientVersion": "2.7.2"
                    },
                    {
                        "ConnectedSince": "2021-01-13T15:22:20.197+08:00",
                        "ConsumerAddr": "/9.219.234.202:6374",
                        "ConsumerName": "dkhtb",
                        "Partition": 4,
                        "ClientVersion": "2.7.2"
                    },
                    {
                        "ConnectedSince": "2021-01-13T15:22:50.282+08:00",
                        "ConsumerAddr": "/9.219.237.139:57322",
                        "ConsumerName": "ejbij",
                        "Partition": 4,
                        "ClientVersion": "2.7.2"
                    },
                    {
                        "ConnectedSince": "2021-01-13T15:18:50.927+08:00",
                        "ConsumerAddr": "/9.219.233.137:62564",
                        "ConsumerName": "hijsf",
                        "Partition": 4,
                        "ClientVersion": "2.7.2"
                    },
                    {
                        "ConnectedSince": "2021-01-13T15:21:50.227+08:00",
                        "ConsumerAddr": "/9.219.234.202:11554",
                        "ConsumerName": "nbcra",
                        "Partition": 4,
                        "ClientVersion": "2.7.2"
                    },
                    {
                        "ConnectedSince": "2021-01-13T15:19:51.032+08:00",
                        "ConsumerAddr": "/9.219.232.202:19345",
                        "ConsumerName": "vjmts",
                        "Partition": 4,
                        "ClientVersion": "2.7.2"
                    }
                ],
                "ConsumersScheduleSets": [
                    {
                        "NumberOfEntries": 4642,
                        "Partitions": 0,
                        "MsgBacklog": 1087,
                        "MsgRateOut": "0.0",
                        "MsgThroughputOut": "0.0",
                        "MsgRateExpired": "0.0"
                    }
                ]
            }
        ],
        "RequestId": "39ab02af-30c8-41d4-9ac4-46cb519ceac0"
    }
}
```

