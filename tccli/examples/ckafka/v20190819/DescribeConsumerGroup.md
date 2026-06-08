**Example 1: 列出消费分组**

 

Input: 

```
tccli ckafka DescribeConsumerGroup --cli-unfold-argument  \
    --InstanceId ckafka-test
```

Output: 
```
{
    "Response": {
        "RequestId": "e59b15f1-8c26-4f28-8d7a-31fdbb5d2e90",
        "Result": {
            "GroupList": [
                {
                    "ConsumerGroupName": "hh",
                    "SubscribedInfo": [
                        {
                            "Partition": [
                                0,
                                1,
                                2
                            ],
                            "PartitionOffset": [
                                {
                                    "Offset": 3395,
                                    "Partition": "0"
                                },
                                {
                                    "Offset": 3269,
                                    "Partition": "1"
                                },
                                {
                                    "Offset": 3336,
                                    "Partition": "2"
                                }
                            ],
                            "TopicId": "topic-brany0f0",
                            "TopicName": "dev"
                        },
                        {
                            "Partition": [
                                0,
                                1,
                                2
                            ],
                            "PartitionOffset": [
                                {
                                    "Offset": 2110,
                                    "Partition": "0"
                                },
                                {
                                    "Offset": 2239,
                                    "Partition": "1"
                                },
                                {
                                    "Offset": 2197,
                                    "Partition": "2"
                                }
                            ],
                            "TopicId": "topic-4f78nggi",
                            "TopicName": "te"
                        }
                    ]
                },
                {
                    "ConsumerGroupName": "tes",
                    "SubscribedInfo": [
                        {
                            "Partition": [
                                0,
                                1,
                                2
                            ],
                            "PartitionOffset": [
                                {
                                    "Offset": 3395,
                                    "Partition": "0"
                                },
                                {
                                    "Offset": 3269,
                                    "Partition": "1"
                                },
                                {
                                    "Offset": 3336,
                                    "Partition": "2"
                                }
                            ],
                            "TopicId": "topic-brany0f0",
                            "TopicName": "dev"
                        },
                        {
                            "Partition": [
                                0,
                                1,
                                2
                            ],
                            "PartitionOffset": [
                                {
                                    "Offset": 1409,
                                    "Partition": "0"
                                },
                                {
                                    "Offset": 1474,
                                    "Partition": "1"
                                },
                                {
                                    "Offset": 1453,
                                    "Partition": "2"
                                }
                            ],
                            "TopicId": "topic-4f78nggi",
                            "TopicName": "te"
                        }
                    ]
                },
                {
                    "ConsumerGroupName": "vv",
                    "SubscribedInfo": [
                        {
                            "Partition": [
                                0,
                                1,
                                2
                            ],
                            "PartitionOffset": [
                                {
                                    "Offset": 3395,
                                    "Partition": "0"
                                },
                                {
                                    "Offset": 3269,
                                    "Partition": "1"
                                },
                                {
                                    "Offset": 3336,
                                    "Partition": "2"
                                }
                            ],
                            "TopicId": "topic-brany0f0",
                            "TopicName": "dev"
                        }
                    ]
                }
            ],
            "GroupListForMonitor": [
                {
                    "GroupName": "hh"
                },
                {
                    "GroupName": "tes"
                },
                {
                    "GroupName": "vv"
                }
            ],
            "PartitionListForMonitor": [],
            "TopicList": [
                {
                    "TopicId": "topic-brany0f0",
                    "TopicName": "dev"
                },
                {
                    "TopicId": "topic-4f78nggi",
                    "TopicName": "te"
                }
            ],
            "TopicListForMonitor": [
                {
                    "TopicId": "topic-brany0f0",
                    "TopicName": "dev"
                },
                {
                    "TopicId": "topic-4f78nggi",
                    "TopicName": "te"
                }
            ],
            "TotalCount": 3,
            "TotalPartition": 0,
            "TotalTopic": 2
        }
    }
}
```

