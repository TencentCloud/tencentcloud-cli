**Example 1: 获取消息详情**



Input: 

```
tccli tdmq DescribeMsg --cli-unfold-argument  \
    --EnvironmentId default \
    --TopicName msg_dev \
    --MsgId 16836:8:-1
```

Output: 
```
{
    "Response": {
        "Properties": "{\"publish-time\": \"1597747661679\", \"X-Pulsar-num-batch-message\": \"1\", \"MESSAGE_ID\": \"16836:8:-1\", \"X-Pulsar-producer-name\": \"fisrtProducer\", \"bookies-address\": \"9.139.220.16:3181#9.139.220.8:3181\"}",
        "Body": "i just a10 testing!",
        "BatchId": "1",
        "ProduceTime": "2020-08-18 18:47:41",
        "MsgId": "16836:8:-1",
        "ProducerName": "fisrtProducer",
        "RequestId": "b9c2eff2-e96a-4558-9ffc-d85279cxxxx",
        "Metadata": "{\"X-Pulsar-event-time\":\"1755674979886\",\"X-Pulsar-redelivery-count\":\"0\",\"X-Pulsar-sequence-id\":\"11\",\"X-Pulsar-deliver-at-time\":\"1755686943517\",\"X-Pulsar-replicated-to\":\"[]\",\"X-Pulsar-ordering-key\":\"[116, 101, 115, 116, 50]\"}",
        "Key": "test1"
    }
}
```

