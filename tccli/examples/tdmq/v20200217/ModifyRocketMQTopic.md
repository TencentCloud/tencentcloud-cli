**Example 1: 修改主题**



Input: 

```
tccli tdmq ModifyRocketMQTopic --cli-unfold-argument  \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId test_namespace \
    --Topic test_topic \
    --Remark 测试修改 \
    --PartitionNum 3
```

Output: 
```
{
    "Response": {
        "RequestId": "5d41e0f7-5668-46f9-a549-9a7540a9966c"
    }
}
```

