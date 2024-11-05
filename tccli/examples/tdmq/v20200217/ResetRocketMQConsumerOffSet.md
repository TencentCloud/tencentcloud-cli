**Example 1: 重置消费位点**



Input: 

```
tccli tdmq ResetRocketMQConsumerOffSet --cli-unfold-argument  \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId test_namespace \
    --GroupId test_group \
    --Topic test_topic \
    --Type 1 \
    --ResetTimestamp 1697945990000
```

Output: 
```
{
    "Response": {
        "RequestId": "def4f676-27fc-4437-b4a3-cf1509726f98"
    }
}
```

