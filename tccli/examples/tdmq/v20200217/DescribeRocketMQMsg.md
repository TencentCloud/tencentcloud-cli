**Example 1: 查询消息详情**



Input: 

```
tccli tdmq DescribeRocketMQMsg --cli-unfold-argument  \
    --EnvironmentId test_namespace \
    --ClusterId rocketmq-4k4orqgq \
    --TopicName test_topic \
    --PulsarMsgId 092BAE5A1656070DEA4E276DF0760089 \
    --MsgId 092BAE5A1656070DEA4E276DF0760023 \
    --QueryDlqMsg False
```

Output: 
```
{
    "Response": {
        "Body": "order-id-2ksn3b23",
        "MsgId": "092BAE5A1656070DEA4E276DF0760089",
        "ProduceTime": "2021-11-23 21:21:26",
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7",
        "Properties": "",
        "ProducerAddr": "9.43.174.90",
        "ShowTopicName": "test_topic",
        "MessageTracks": [
            {
                "Group": "test_group",
                "ConsumeStatus": "CONSUMED",
                "TrackType": "CONSUMED",
                "ExceptionDesc": ""
            }
        ]
    }
}
```

