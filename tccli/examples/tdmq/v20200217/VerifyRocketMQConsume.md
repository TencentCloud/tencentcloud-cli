**Example 1: 示例**



Input: 

```
tccli tdmq VerifyRocketMQConsume --cli-unfold-argument  \
    --NamespaceId test_ns \
    --MsgId abc \
    --ClusterId rocketmq-abc \
    --GroupId test_group \
    --TopicName test_topic \
    --ClientId 1.1.1.1@abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

