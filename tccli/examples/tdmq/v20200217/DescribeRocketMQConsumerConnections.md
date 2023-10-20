**Example 1: 获取指定消费组下当前客户端的连接情况**



Input: 

```
tccli tdmq DescribeRocketMQConsumerConnections --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId example \
    --GroupId group-example
```

Output: 
```
{
    "Response": {
        "RequestId": "11da7a88-c7d0-41e9-96eb-9130257ac16a",
        "TotalCount": 0,
        "Connections": [],
        "GroupDetail": null
    }
}
```

