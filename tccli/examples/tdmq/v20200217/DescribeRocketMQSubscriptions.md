**Example 1: 获取rocketmq消费组订阅关系**



Input: 

```
tccli tdmq DescribeRocketMQSubscriptions --cli-unfold-argument  \
    --ClusterId rocketmq-a5nzx52ab7jb \
    --Namespace test_namespace \
    --Group test_group \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "cde7c1eb-c631-453a-999b-03c9ed38b892",
        "TotalCount": 1,
        "Subscriptions": [
            {
                "Topic": "test_topic",
                "Type": "Normal",
                "PartitionNum": 3,
                "ExpressionType": "TAG",
                "SubString": "test_tag",
                "Status": 0,
                "ConsumerLag": 120
            }
        ]
    }
}
```

