**Example 1: 查询消费者客户端详情**

查询消费者客户端详情

Input: 

```
tccli trocket DescribeConsumerClient --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Offset 0 \
    --Limit 1 \
    --ConsumerGroup group \
    --ClientId 11.139.244.247@75043#6734858812769343
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Client": {
            "ClientAddr": "11.139.244.247:58330",
            "ClientId": "11.139.244.247@75043#6734858812769343",
            "ConsumerLag": 0,
            "Language": "JAVA",
            "Version": "V4_9_3",
            "ChannelProtocol": "remoting"
        },
        "RequestId": "7e3acbab-5b5f-457f-b276-68c2f7e16f5e",
        "TopicList": [
            {
                "ConsumerLag": 0,
                "LastUpdateTime": 1683614607184,
                "QueueNum": 16,
                "SubString": "test_tag",
                "Topic": "topic",
                "TopicType": "NORMAL"
            }
        ]
    }
}
```

