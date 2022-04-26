**Example 1: 重置消费位点**



Input: 

```
tccli tdmq ResetRocketMQConsumerOffSet --cli-unfold-argument  \
    --ClusterId ocketmq-2p9vx3ax9jxg \
    --NamespaceId example \
    --GroupId group-example \
    --Topic example-topic \
    --Type 0
```

Output: 
```
{
    "Response": {
        "RequestId": "def4f676-27fc-4437-b4a3-cf1509726f98"
    }
}
```

