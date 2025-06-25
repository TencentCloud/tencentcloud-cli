**Example 1: 查询普通消息**



Input: 

```
tccli trocket DescribeMessage --cli-unfold-argument  \
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
        "Body": "testBody",
        "MessageId": "1EAE3915000721B8D17C2C5BB31638D1",
        "MessageTracksCount": 1,
        "MessageTracks": [
            {
                "ConsumeStatus": "CONSUMED",
                "ConsumerGroup": "group",
                "ExceptionDesc": null,
                "TrackType": "CONSUMED"
            }
        ],
        "ProduceTime": "2023-05-09 14:43:27",
        "ProducerAddr": "30.174.57.21",
        "Properties": "{\"TRACE_ON\":\"true\",\"MSG_REGION\":\"cd\",\"KEYS\":\"testKey\",\"UNIQ_KEY\":\"1EAE3915000721B8D17C2C5BB31638D1\",\"CLUSTER\":\"rmqbroker-cd-1\",\"WAIT\":\"true\",\"TAGS\":\"testTag\"}",
        "RequestId": "8e97b978-376b-4d94-96cc-db0ead5f2f99",
        "ShowTopicName": "topic"
    }
}
```

