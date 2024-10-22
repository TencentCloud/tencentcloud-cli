**Example 1: 获取在线消费端详情**



Input: 

```
tccli tdmq DescribeRocketMQConsumerConnectionDetail --cli-unfold-argument  \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId test_namespace \
    --GroupId test_group \
    --ClientId local@23645@0@30ey5aef8w \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "2cb0df97-581a-4d70-a9e8-4a0b79998e29",
        "TotalCount": 0,
        "Details": []
    }
}
```

