**Example 1: 查询某个订阅任务的消费组**



Input: 

```
tccli dts DescribeConsumerGroups --cli-unfold-argument  \
    --SubscribeId subs-p383pfn0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Account": "account-subs-p383pfn0-order-system-distributer",
                "ConsumerGroupLag": 0,
                "ConsumerGroupName": "consumer-grp-subs-p383pfn0-order-system-distributer",
                "ConsumerGroupOffset": 626960429,
                "ConsumerGroupState": "Stable",
                "CreatedAt": "2026-07-31 11:12:50",
                "Description": "order-system-distributer",
                "Latency": 0,
                "PartitionAssignment": [
                    {
                        "ClientId": "consumer-consumer-grp-subs-p383pfn0-order-system-distributer-2",
                        "PartitionNo": []
                    },
                    {
                        "ClientId": "consumer-consumer-grp-subs-p383pfn0-order-system-distributer-1",
                        "PartitionNo": [
                            0
                        ]
                    }
                ],
                "StateOfPartition": [
                    {
                        "ConsumerGroupLag": 0,
                        "ConsumerGroupOffset": 626960429,
                        "Latency": 0,
                        "PartitionNo": 0
                    }
                ],
                "UpdatedAt": "2026-07-31 11:12:50"
            }
        ],
        "RequestId": "4d0c123d-11a3-4b7b-b4d5-861bd763038e",
        "TotalCount": 1
    }
}
```

