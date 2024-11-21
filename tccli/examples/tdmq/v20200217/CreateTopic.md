**Example 1: 创建主题**

创建主题

Input: 

```
tccli tdmq CreateTopic --cli-unfold-argument  \
    --EnvironmentId devNs \
    --TopicName devTopic \
    --Partitions 1 \
    --Remark devTest \
    --TopicType 1 \
    --ClusterId pulsar-5r59xd4vnx \
    --PulsarTopicType 0 \
    --MsgTTL 1
```

Output: 
```
{
    "Response": {
        "EnvironmentId": "default",
        "TopicName": "test_topic",
        "Partitions": 2,
        "TopicType": 0,
        "Remark": "2个分区的普通消息队列",
        "RequestId": "d9686bf9-8d7d-4e78-bb44-5140d70a1ffa"
    }
}
```

