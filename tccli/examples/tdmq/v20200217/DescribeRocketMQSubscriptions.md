**Example 1: 获取rocketmq消费组订阅关系**



Input: 

```
tccli tdmq DescribeRocketMQSubscriptions --cli-unfold-argument  \
    --Limit 10 \
    --ClusterId rocketmq-a5nzx52ab7jb \
    --Namespace test \
    --Group consume_group \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "cde7c1eb-c631-453a-999b-03c9ed38b892",
        "TotalCount": 2,
        "Subscriptions": [
            {
                "Topic": "test",
                "Type": "Normal",
                "PartitionNum": 3,
                "ExpressionType": "TAG",
                "SubString": "*",
                "Status": 0
            },
            {
                "Topic": "%RETRY%consume_group",
                "Type": "Retry",
                "PartitionNum": 1,
                "ExpressionType": "TAG",
                "SubString": "*",
                "Status": 0
            }
        ]
    }
}
```

