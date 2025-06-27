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
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "06a6649b-76ec-4c5d-b4c8-8a48d24be07f",
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
                "ClientSubscriptionInfos": [],
                "ConsumerLag": 0,
                "LastUpdateTime": 1750853702996,
                "MaxRetryTimes": 16,
                "ConsumeMessageOrderly": false,
                "MessageModel": "CLUSTERING"
            }
        ]
    }
}
```

