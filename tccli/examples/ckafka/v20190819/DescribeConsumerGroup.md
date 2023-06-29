**Example 1: 列出消费分组**

 

Input: 

```
tccli ckafka DescribeConsumerGroup --cli-unfold-argument  \
    --InstanceId 10
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 2,
            "TopicList": [
                {
                    "TopicId": "topic-g8ud11it",
                    "TopicName": "connect-offset"
                }
            ],
            "GroupList": [
                {
                    "ConsumerGroupName": "connect-cluster-1",
                    "SubscribedInfo": []
                },
                {
                    "ConsumerGroupName": "qcloud_tocos",
                    "SubscribedInfo": [
                        {
                            "TopicName": "connect-offset",
                            "PartitionOffset": [
                                {
                                    "Partition": "0",
                                    "Offset": 966186803
                                },
                                {
                                    "Partition": "1",
                                    "Offset": 968552882
                                },
                                {
                                    "Partition": "2",
                                    "Offset": 957792934
                                }
                            ]
                        }
                    ]
                }
            ],
            "TotalPartition": 0,
            "PartitionListForMonitor": [],
            "TotalTopic": 1,
            "TopicListForMonitor": [
                {
                    "TopicId": "topic-g8ud11it",
                    "TopicName": "connect-offset"
                }
            ],
            "GroupListForMonitor": [
                {
                    "GroupName": "connect-cluster-1"
                },
                {
                    "GroupName": "qcloud_tocos"
                }
            ]
        },
        "RequestId": "3c8a91a3-5921-4d7f-9fd9-6b4261cca363"
    }
}
```

