**Example 1: 获取消费进度**



Input: 

```
tccli tdmq DescribeRocketMQConsumeStats --cli-unfold-argument  \
    --ClusterId rocketmq-7j8m97bqpx5d \
    --NamespaceId sla_rop_namespace_504344 \
    --ConsumerGroup group-2023-09-21-824790
```

Output: 
```
{
    "Response": {
        "RequestId": "d97e7c2f-da5f-4f73-b4da-440e0650ed0b",
        "ConsumerStatsList": [
            {
                "TopicName": "%RETRY%group-2023-09-21-824790",
                "BrokerName": "rocketmq-7j8m97bqpx5d-0",
                "QueueId": 0,
                "ConsumerClientId": "9.43.174.90@18834#7187709773375173",
                "ConsumerOffset": 0,
                "BrokerOffset": 0,
                "DiffTotal": 0,
                "LastTimestamp": 0
            }
        ]
    }
}
```

