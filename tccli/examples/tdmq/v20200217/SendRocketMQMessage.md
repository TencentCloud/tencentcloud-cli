**Example 1: 发送消息示例**



Input: 

```
tccli tdmq SendRocketMQMessage --cli-unfold-argument  \
    --ClusterId rocketmq-4k4orqgq \
    --NamespaceId test_namespace \
    --TopicName test_topic \
    --MsgKey test_key \
    --MsgTag test_tag \
    --MsgBody This is a normal message for Apache RocketMQ
```

Output: 
```
{
    "Response": {
        "Result": true,
        "MsgId": "7F0000013AEC18B4AAC278B640D30002",
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

