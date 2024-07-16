**Example 1: 获取指定消费组下订阅的主题列表**



Input: 

```
tccli tdmq DescribeRocketMQTopicsByGroup --cli-unfold-argument  \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId example \
    --GroupId group-example \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "4668f537-44f3-4aca-bd78-fc26fb8d86ff",
        "TotalCount": 1,
        "Topics": [
            "topic-example"
        ]
    }
}
```

