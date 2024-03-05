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
        "RequestId": "msgs"
    }
}
```

