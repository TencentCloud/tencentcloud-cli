**Example 1: 导出消息详情**



Input: 

```
tccli tdmq ExportRocketMQMessageDetail --cli-unfold-argument  \
    --ClusterId rocketmq-a5nzx52ab7jb \
    --EnvironmentId test_namespace \
    --TopicName test_topic \
    --MsgId 7F0000013AEC18B4AAC278B640D30002 \
    --DeadLetterMsg True \
    --IncludeMsgBody True
```

Output: 
```
{
    "Response": {
        "MsgId": "7F0000013AEC18B4AAC278B640D30002",
        "BornTimestamp": 1729478721,
        "StoreTimestamp": 1729478721,
        "BornHost": "10.2.139.175:8080",
        "MsgTag": "test_tag",
        "MsgKey": "test_key",
        "Properties": "",
        "ReConsumeTimes": 1,
        "MsgBody": "This is a normal message for Apache RocketMQ",
        "MsgBodyCRC": 0,
        "MsgBodySize": 18,
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

