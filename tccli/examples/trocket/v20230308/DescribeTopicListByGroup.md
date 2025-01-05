**Example 1: 查询消费组订阅的主题列表**



Input: 

```
tccli trocket DescribeTopicListByGroup --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Offset 0 \
    --Limit 10 \
    --ConsumerGroup test_group
```

Output: 
```
{
    "Response": {
        "RequestId": "fcf7340b-b7b8-48fd-afe2-b061df13a290",
        "TotalCount": 1,
        "Data": [
            {
                "InstanceId": "rmq-72mo3a9o",
                "Topic": "test_topic",
                "TopicType": "NORMAL",
                "TopicQueueNum": 3,
                "ConsumerGroup": "test_group",
                "IsOnline": true,
                "ConsumeType": "PUSH",
                "SubString": "test_tag",
                "ExpressionType": "TAG",
                "Consistency": 0,
                "ConsumerLag": 20,
                "LastUpdateTime": 1736935187759,
                "MaxRetryTimes": 16,
                "ConsumeMessageOrderly": false,
                "MessageModel": "CLUSTERING"
            }
        ]
    }
}
```

