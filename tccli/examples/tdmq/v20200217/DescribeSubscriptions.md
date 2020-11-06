**Example 1: 获取指定主题的订阅和消费者**



Input: 

```
tccli tdmq DescribeSubscriptions --cli-unfold-argument  \
    --EnvironmentId default \
    --TopicName sun_topic \
    --Offset 0 \
    --Limit 10 \
    --SubscriptionName 
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SubscriptionSets": [
            {
                "EnvironmentId": "default",
                "TopicName": "rc_price_statis_test",
                "ConnectedSince": "",
                "ConsumerAddr": "",
                "ConsumerCount": "1",
                "ConsumerName": "",
                "MsgBacklog": "0",
                "MsgRateExpired": "0.0",
                "MsgRateOut": "0.0",
                "MsgThroughputOut": "0.0",
                "SubscriptionName": "rc_price_statis_test",
                "Remark": "",
                "CreateTime": "2020-06-17 12:00:22",
                "UpdateTime": "2020-06-17 12:00:22",
                "IsOnline": true,
                "ConsumerSets": [
                    {
                        "ConnectedSince": "2020-06-19 12:07:00",
                        "ConsumerAddr": "9.88.10.221:43911",
                        "ConsumerName": "e2796",
                        "ClientVersion": "2.5.0"
                    }
                ],
                "ConsumersScheduleSets": [
                    {
                        "NumberOfEntries": 12,
                        "Partitions": 0,
                        "MsgBacklog": 0,
                        "MsgRateOut": "0.0",
                        "MsgThroughputOut": "0.0",
                        "MsgRateExpired": "0.0"
                    },
                    {
                        "NumberOfEntries": 12,
                        "Partitions": 0,
                        "MsgBacklog": 0,
                        "MsgRateOut": "0.0",
                        "MsgThroughputOut": "0.0",
                        "MsgRateExpired": "0.0"
                    }
                ]
            }
        ],
        "RequestId": "2d937237-7bd9-4bb2-9e78-86d0518e4d74"
    }
}
```

