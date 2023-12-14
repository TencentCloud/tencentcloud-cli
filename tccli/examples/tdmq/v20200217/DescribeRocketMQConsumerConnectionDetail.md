**Example 1: 获取在线消费端详情**



Input: 

```
tccli tdmq DescribeRocketMQConsumerConnectionDetail --cli-unfold-argument  \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId example \
    --GroupId group-example \
    --ClientId xxxx \
    --Offset 0 \
    --Limit 10
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

