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
        "Result": {
            "TotalCount": 1,
            "TopicList": [
                {
                    "TopicId": "topic-test",
                    "TopicName": "topic-test"
                }
            ],
            "GroupList": [
                {
                    "ConsumerGroupName": "group-test",
                    "SubscribedInfo": [
                        {
                            "TopicId": "topic-test",
                            "TopicName": "topic-test",
                            "Partition": [
                                0,
                                1,
                                2
                            ],
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
            "TotalPartition": 3,
            "PartitionListForMonitor": [],
            "TotalTopic": 1,
            "TopicListForMonitor": [
                {
                    "TopicId": "topic-test",
                    "TopicName": "topic-test"
                }
            ],
            "GroupListForMonitor": [
                {
                    "GroupName": "group-test"
                }
            ]
        },
        "RequestId": "d173b4fb-c6d0-4507-a822-b6f277fc4016"
    }
}
```

