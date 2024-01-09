**Example 1: 获取数据订阅的消费组**

获取数据订阅的消费组

Input: 

```
tccli dts DescribeConsumerGroups --cli-unfold-argument  \
    --SubscribeId subs-9jyki7hniw
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Account": "account-subs-47damshnra-3",
                "ConsumerGroupLag": 464948,
                "ConsumerGroupName": "consumer-grp-subs-47damshnra-3",
                "ConsumerGroupOffset": -1,
                "ConsumerGroupState": "Dead",
                "CreatedAt": "2022-03-25 17:31:31",
                "Description": "sdfjo",
                "Latency": 528268,
                "PartitionAssignment": [],
                "StateOfPartition": [
                    {
                        "ConsumerGroupLag": 464948,
                        "ConsumerGroupOffset": -1,
                        "Latency": 528268,
                        "PartitionNo": 0
                    }
                ],
                "UpdatedAt": "2022-03-25 17:31:31"
            },
            {
                "Account": "account-subs-47damshnra-2",
                "ConsumerGroupLag": 464948,
                "ConsumerGroupName": "consumer-grp-subs-47damshnra-2",
                "ConsumerGroupOffset": -1,
                "ConsumerGroupState": "Dead",
                "CreatedAt": "2022-03-22 17:34:31",
                "Description": "sdfjo",
                "Latency": 528268,
                "PartitionAssignment": [],
                "StateOfPartition": [
                    {
                        "ConsumerGroupLag": 464948,
                        "ConsumerGroupOffset": -1,
                        "Latency": 528268,
                        "PartitionNo": 0
                    }
                ],
                "UpdatedAt": "2022-03-22 17:34:31"
            },
            {
                "Account": "account-subs-47damshnra-1",
                "ConsumerGroupLag": 464948,
                "ConsumerGroupName": "consumer-grp-subs-47damshnra-1",
                "ConsumerGroupOffset": -1,
                "ConsumerGroupState": "Dead",
                "CreatedAt": "2022-03-04 15:14:18",
                "Description": "sdfjo",
                "Latency": 528268,
                "PartitionAssignment": [],
                "StateOfPartition": [
                    {
                        "ConsumerGroupLag": 464948,
                        "ConsumerGroupOffset": -1,
                        "Latency": 528268,
                        "PartitionNo": 0
                    }
                ],
                "UpdatedAt": "2022-03-04 15:14:18"
            }
        ],
        "RequestId": "68c04ba0-b0d8-11ec-98f5-11f9ac4a2e37",
        "TotalCount": 3
    }
}
```

