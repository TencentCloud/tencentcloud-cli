**Example 1: 获取主题详情**



Input: 

```
tccli tdmq DescribeRocketMQTopic --cli-unfold-argument  \
    --ClusterId rocketmq-zpz97455xwap \
    --NamespaceId namespace \
    --TopicName test_topic \
    --ConsumerGroup 
```

Output: 
```
{
    "Response": {
        "RequestId": "121e5b17-7e8b-4849-b168-c02b67ebfbba",
        "Topic": {
            "Name": "test_topic",
            "Type": "Normal",
            "GroupNum": 0,
            "Remark": null,
            "PartitionNum": 3,
            "CreateTime": 1696662165000,
            "UpdateTime": 1696662165000,
            "InstanceId": "rocketmq-zpz97455xwap",
            "Namespace": "namespace",
            "LastUpdateTime": 1696751238307,
            "SubscriptionCount": 1,
            "SubscriptionData": [
                {
                    "Topic": "test_topic",
                    "Type": null,
                    "PartitionNum": null,
                    "ExpressionType": "TAG",
                    "SubString": "msgTag",
                    "Status": null,
                    "ConsumerLag": 0,
                    "ClusterId": "rocketmq-zpz97455xwap",
                    "ConsumerGroup": "test_group",
                    "IsOnline": true,
                    "ConsumeType": 0,
                    "Consistency": 0,
                    "LastUpdateTime": 1696751238307,
                    "MaxRetryTimes": 16
                }
            ]
        }
    }
}
```

