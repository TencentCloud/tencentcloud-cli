**Example 1: 查询消息轨迹**

查询消息轨迹

Input: 

```
tccli tdmq DescribeRocketMQMsgTrace --cli-unfold-argument  \
    --ClusterId rocketmq-4k4orqgq \
    --EnvironmentId test_namespace \
    --TopicName test_topic \
    --MsgId 01963F0B14BAF0B5360728F44800000000 \
    --GroupName test_group \
    --QueryDLQMsg True
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "Stage": "produce",
                "Data": "{\"MsgId\":\"01963F0B14BAF0B5360728F44800000000\",\"Status\":0,\"ProduceTime\":\"2024-10-22 15:54:49,124\",\"ProducerAddr\":\"111.206.94.148:47557\",\"MsgKey\":\"yourMessageKey-1c151062f96e\",\"MsgTags\":\"yourMessageTagA\",\"Duration\":10}"
            },
            {
                "Stage": "persist",
                "Data": "{\"MsgId\":\"01963F0B14BAF0B5360728F44800000000\",\"Status\":0,\"PersistTime\":\"2024-10-22 15:54:49,132\"}"
            },
            {
                "Stage": "consume",
                "Data": "{\"TotalCount\":1,\"RocketMqConsumeLogs\":[{\"MsgId\":\"01963F0B14BAF0B5360728F44800000000\",\"Status\":2,\"PushTime\":\"2024-10-22 15:55:00,122\",\"ConsumerAddr\":\"111.206.94.148:53792\",\"ConsumerGroup\":\"test_group\",\"RetryTimes\":1}]}"
            }
        ],
        "ShowTopicName": "news-topic",
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

