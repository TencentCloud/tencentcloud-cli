**Example 1: 查询普通消息的轨迹**



Input: 

```
tccli trocket DescribeMessageTrace --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Topic topic \
    --MsgId 1EAE3915000721B8D17C2C5BB31638D1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "Data": "{\"MsgId\":\"1EAE3915000721B8D17C2C5BB31638D1\",\"Status\":0,\"ProduceTime\":\"2023-05-09 14:43:27,127\",\"ProducerAddr\":\"30.174.57.21\",\"MsgKey\":\"testKey\",\"MsgTags\":\"testTag\",\"Duration\":76}",
                "Stage": "produce"
            },
            {
                "Data": "{\"MsgId\":\"1EAE3915000721B8D17C2C5BB31638D1\",\"Status\":0,\"PersistTime\":\"2023-05-09 14:43:27,184\"}",
                "Stage": "persist"
            },
            {
                "Data": "{\"TotalCount\":1,\"RocketMqConsumeLogs\":[{\"MsgId\":\"1EAE3915000721B8D17C2C5BB31638D1\",\"Status\":2,\"PushTime\":\"2023-05-09 14:43:27,205\",\"ConsumerAddr\":\"11.139.244.247\",\"ConsumerGroup\":\"group\",\"RetryTimes\":1}]}",
                "Stage": "consume"
            }
        ],
        "RequestId": "0112153a-8cba-44f1-b7a5-5e412d493940",
        "ShowTopicName": "test_topic"
    }
}
```

**Example 2: 查询延迟消息的轨迹**



Input: 

```
tccli trocket DescribeMessageTrace --cli-unfold-argument  \
    --InstanceId rmq-cdqzmmgz8o \
    --Topic  \
    --MsgId 010242ECB90067325E06F41EFF00000000 \
    --QueryDelayMessage True
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "Data": "{\"MsgId\":\"010242ECB90067325E06F41EFF00000000\",\"Status\":0,\"ProduceTime\":\"2024-09-12 14:06:55,591\",\"ProducerAddr\":\"9.218.232.160:32038\",\"MsgKey\":\"topic1\",\"MsgTags\":\"tag0\",\"Duration\":2}",
                "Stage": "produce"
            },
            {
                "Data": "{\"MsgId\":\"010242ECB90067325E06F41EFF00000000\",\"Status\":0,\"PersistTime\":\"2024-09-12 14:06:55,590\"}",
                "Stage": "persist"
            },
            {
                "Data": "{\"TotalCount\":0,\"RocketMqConsumeLogs\":[]}",
                "Stage": "consume"
            }
        ],
        "RequestId": "2e4374f9-0c98-4d77-af20-2bc414ccaefd",
        "ShowTopicName": "test_topic"
    }
}
```

