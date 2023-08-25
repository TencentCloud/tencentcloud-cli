**Example 1: 消费订阅列表**



Input: 

```
tccli tdmq DescribeSubscriptions --cli-unfold-argument  \
    --EnvironmentId abc \
    --TopicName abc \
    --Offset 1 \
    --Limit 1 \
    --SubscriptionName abc \
    --Filters.0.ConsumerHasCount True \
    --Filters.0.ConsumerHasBacklog True \
    --Filters.0.ConsumerHasExpired True \
    --Filters.0.SubscriptionNames abc \
    --ClusterId abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SubscriptionSets": [
            {
                "EnvironmentId": "test1",
                "TopicName": "test",
                "ConnectedSince": "",
                "ConsumerAddr": "",
                "ConsumerCount": "6",
                "ConsumerName": "",
                "MsgBacklog": "1087",
                "MsgRateExpired": "0.0",
                "MsgRateOut": "0.0",
                "SubType": "abc",
                "MsgThroughputOut": "0.0",
                "SubscriptionName": "test",
                "BlockedSubscriptionOnUnackedMsgs": true,
                "MaxUnackedMsgNum": 0,
                "Remark": "",
                "CreateTime": "2020-09-18 14:32:41",
                "UpdateTime": "2021-01-13 15:23:35",
                "IsOnline": true,
                "ConsumerSets": [
                    {
                        "ConnectedSince": "2021-01-13T15:19:21.03+08:00",
                        "ConsumerAddr": "/9.219.234.200:9056",
                        "ConsumerName": "axjoy",
                        "ClientVersion": ""
                    },
                    {
                        "ConnectedSince": "2021-01-13T15:22:20.197+08:00",
                        "ConsumerAddr": "/9.219.234.202:6374",
                        "ConsumerName": "dkhtb",
                        "ClientVersion": ""
                    },
                    {
                        "ConnectedSince": "2021-01-13T15:22:50.282+08:00",
                        "ConsumerAddr": "/9.219.237.139:57322",
                        "ConsumerName": "ejbij",
                        "ClientVersion": ""
                    },
                    {
                        "ConnectedSince": "2021-01-13T15:18:50.927+08:00",
                        "ConsumerAddr": "/9.219.233.137:62564",
                        "ConsumerName": "hijsf",
                        "ClientVersion": ""
                    },
                    {
                        "ConnectedSince": "2021-01-13T15:21:50.227+08:00",
                        "ConsumerAddr": "/9.219.234.202:11554",
                        "ConsumerName": "nbcra",
                        "ClientVersion": ""
                    },
                    {
                        "ConnectedSince": "2021-01-13T15:19:51.032+08:00",
                        "ConsumerAddr": "/9.219.232.202:19345",
                        "ConsumerName": "vjmts",
                        "ClientVersion": ""
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

