**Example 1: 获取消费进度**



Input: 

```
tccli tdmq DescribeRocketMQConsumeStats --cli-unfold-argument  \
    --ClusterId rocketmq-7j8m97bqpx5d \
    --NamespaceId test_namespace \
    --ConsumerGroup test_group
```

Output: 
```
{
    "Response": {
        "RequestId": "d97e7c2f-da5f-4f73-b4da-440e0650ed0b",
        "ConsumerStatsList": [
            {
                "TopicName": "test_topic",
                "BrokerName": "rocketmq-7j8m97bqpx5d-0",
                "QueueId": 10,
                "ConsumerClientId": "9.43.174.90@18834#7187709773375173",
                "ConsumerOffset": 30,
                "BrokerOffset": 100,
                "DiffTotal": 70,
                "LastTimestamp": 1727580008838
            }
        ]
    }
}
```

